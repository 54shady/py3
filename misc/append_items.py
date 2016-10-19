#!/usr/bin/env python

def append_all(old, *new):
    for n in new:
        old.append(n)
    return old

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
