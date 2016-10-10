#!/usr/bin/env python

import os

print(os.path.exists('/etc/portage/xxoo.py'))
print(os.path.exists('/etc/portage/make.conf'))

print(os.path.isdir('/etc/portage/xxoo.py'))
print(os.path.isdir('/etc/portage'))

print(os.path.isfile('/etc/portage'))
print(os.path.isfile('/etc/portage/make.conf'))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
