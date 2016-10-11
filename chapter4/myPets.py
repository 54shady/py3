#!/usr/bin/env python

myPets = ['Zophie', 'Pooka', 'Fat-tail']

while True:
    print('Enter a pet name(blank to quit):')
    name = input()
    if name == '':
        break

    if name not in myPets:
        print('I do not have a pet name ' + name)
    else:
        print(name + ' is my pet.')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
