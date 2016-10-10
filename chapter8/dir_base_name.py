#!/usr/bin/env python

import os
full_name = '/home/python/example/test.py'

bn = os.path.basename(full_name)
dn = os.path.dirname(full_name)
print('Full Name: ' + full_name)
print('Base name: ' + bn)
print('Dir name: ' + dn)

bndn = os.path.split(full_name)
print(bndn[0])
print(bndn[1])
print('bndn: ' + bndn[0] + bndn[1])

# fetch each level dir
f = full_name.split(os.path.sep)
print(f)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
