#!/usr/bin/env python

import socket, select

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response  = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(1)

# Since sockets are blocking by default, this is necessary
serversocket.setblocking(0)

# Create an epoll object
epoll = select.epoll()

# Tell the epoll object to monitor specific events on specific sockets
epoll.register(serversocket.fileno(), select.EPOLLIN)

try:
   connections = {}; requests = {}; responses = {}
   while True:
      events = epoll.poll(1)
      for fileno, event in events:
         # If a read event occurred on the socket server
         if fileno == serversocket.fileno():
            print('A New client conneced :)')
            connection, address = serversocket.accept()

            # Set new socket to non-blocking mode
            connection.setblocking(0)

            # Register interest in read (EPOLLIN) events for the new socket.
            epoll.register(connection.fileno(), select.EPOLLIN)
            connections[connection.fileno()] = connection
            requests[connection.fileno()] = b''
            responses[connection.fileno()] = response
         # Perform some action on those sockets
         # If a read event occurred then read new data sent from the client
         elif event & select.EPOLLIN:
            print('Get request from client<<<')
            requests[fileno] += connections[fileno].recv(1024)
            if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
               # Tell the epoll object to modify the list of sockets and/or events to monitor
               # unregister interest in read events and register interest in write (EPOLLOUT) events
               # Write events will occur when it is possible to send response data back to the client
               epoll.modify(fileno, select.EPOLLOUT)
               print('-'*40 + '\n' + requests[fileno].decode()[:-2])
         elif event & select.EPOLLOUT:
            print('Reply to client>>>')
            byteswritten = connections[fileno].send(responses[fileno])
            responses[fileno] = responses[fileno][byteswritten:]
            if len(responses[fileno]) == 0:
               epoll.modify(fileno, 0)
               connections[fileno].shutdown(socket.SHUT_RDWR)
               print('shutdown connection!!!')
         elif event & select.EPOLLHUP:
            epoll.unregister(fileno)
            connections[fileno].close()
            print('close connection!!!')
            del connections[fileno]
finally:
   # Destroy the epoll object
   epoll.unregister(serversocket.fileno())
   epoll.close()
   serversocket.close()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
