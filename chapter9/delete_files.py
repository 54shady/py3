#!/usr/bin/env python

import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        print('delete ' + filename)
        os.unlink(filename)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
