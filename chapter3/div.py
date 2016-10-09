#!/usr/bin/env python

def mydiv(divby):
    try:
        return 32 / divby
    except ZeroDivisionError:
        print('Error Invalid argumen.')

print(mydiv(2))
print(mydiv(12))
print(mydiv(0))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
