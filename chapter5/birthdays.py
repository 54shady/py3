#!/usr/bin/env python

birthdays = {'Alice' : 'Apr 1', 'Bob' : 'Dec 12', 'Carol' : 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have the birthday info for ' + name)
        print('what is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database update :)')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4