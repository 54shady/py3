#!/usr/bin/env python

import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242, ths')
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
print(mo.groups())
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
