#!/usr/bin/env python

zeroway = {'name' : 'zeroway', 'age' : 28, '0' : 'secert'}

# iterate values return tuple type
for v in zeroway.values():
    print(v)

# iterate keys return tuple type
for k in zeroway.keys():
    print(k)

# iterate items return tuple type
for i in zeroway.items():
    print(i)

# make return a list
zwl = list(zeroway.keys())
print(zwl)

# list k and v the same time
for k, v in zeroway.items():
    print('Key: ' + k + ' Value: ' + str(v))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
