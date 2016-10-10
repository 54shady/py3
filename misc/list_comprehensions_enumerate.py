#!/usr/bin/env python

def __treatmen(pos, item):
    return '%d + %s' % (pos, item)

seq = ['zero', 'one', 'two', 'three']

new_seq = [__treatmen(p, i) for p, i in enumerate(seq)]
print(new_seq)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
