#!/usr/bin/env python

def mydiv(divby):
        return 32 / divby

try:
    print(mydiv(2))
    print(mydiv(12))
    print(mydiv(8))
    print(mydiv(0))
except ZeroDivisionError:
    print('Error Invalid argumen.')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
