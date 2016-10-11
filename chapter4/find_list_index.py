#!/usr/bin/env python

names = ['jordan', 'kobe', 'eminem', 'shady']

while True:
    print('Enter the name(blank to quit)')
    name = input()
    if name == '':
        break

    if name in names:
        print('Index of ' + name + ' is ' + str(names.index(name)))
    else:
        print(name + ' is not in the name list')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
