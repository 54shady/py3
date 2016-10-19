#!/usr/bin/env python

import threading, time

print('Start of program.')

def take_nap():
    time.sleep(5)
    print('Child thread wake up :)')

thread_obj = threading.Thread(target = take_nap)
thread_obj.start()
print('Main thread end.')

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
