#!/usr/bin/env python

catNames = []
while True:
    print('Enter the name of cat' + str(len(catNames) + 1) + ' blank to quit')
    name = input()
    if name == '':
        break

    catNames = catNames + [name] # list concatenation

print('Cat names are: ')

for name in catNames:
    print(' ' + name)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
