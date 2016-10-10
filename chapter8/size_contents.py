#!/usr/bin/env python

import os

# get file size
sz = os.path.getsize('/etc/portage/make.conf')
print(sz)

# list directory
ld = os.listdir('/etc/portage/')
print(ld)

# absoulte path(/etc/portage/xxoo.txt)
apath = os.path.join('/etc/portage/', 'xxoo.txt')
print(apath)

# list dir and print out the absoulte dir
for file in os.listdir('/etc/portage/'):
    apath = os.path.join('/etc/portage', file)
    print(apath)

# caculate all file size
totalsize = 0
for file in os.listdir('/etc/portage/'):
    apath = os.path.join('/etc/portage', file)
    totalsize = totalsize + os.path.getsize(apath)

print('totalsize: ' + str(totalsize))
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
