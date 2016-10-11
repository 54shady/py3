#!/usr/bin/env python

import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
print(cheese)

names = ['zeroway', 'jordan', ['a', 'b', 'c'], 'eminem', 'mobz']
names_undeep_copy = copy.copy(names)
names_deep_copy = copy.deepcopy(names)

print(names_undeep_copy)
print(names_deep_copy)

print(names_undeep_copy == names)
print(names_undeep_copy == names_deep_copy)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
