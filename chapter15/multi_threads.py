#!/usr/bin/env python

import threading
import time
import random

def downloadXkcd(arg_one, arg_two):
    time.sleep(random.randint(1, 9))
    print('Thread ' + str(arg_one) + ' End get value ' + str(arg_two))

# Create and start the Thread objects.
downloadThreads = [] # a list of all the Thread objects
for i in range(0, 10): # loops 10 times, creates 10 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i * i))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
