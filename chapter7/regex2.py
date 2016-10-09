#!/usr/bin/env python

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
