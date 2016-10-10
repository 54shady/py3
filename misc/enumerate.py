#!/usr/bin/env python

seq = ['zero', 'one', 'two', 'three']

print('Old seq: ', end='')
print(seq)
for i, item in enumerate(seq):
    print('seq[' + str(i) + '] = ' + item)
    seq[i] = '%d == %s' % (i, seq[i])

print('New seq: ', end='')
print(seq)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
