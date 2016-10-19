#!/usr/bin/env python

import threading, time

print('Start of program.')

def print_names(*value):
    time.sleep(3)
    print(value)

names = ['zeroway', 'mobz', 'shady']
thread_obj = threading.Thread(target = print_names, args = names)
thread_obj.start()
print('Main thread end.')

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
