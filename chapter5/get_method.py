#!/usr/bin/env python

picnicItems = {'apples': 5, 'cups': 2}

# use get method to get item value if exists, or use default value in the get(key, default_value)
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
