#!/usr/bin/env python

from find_max import return_max_number
from append_items import append_all
from parameter_without_order import describe_feature

if __name__ == "__main__":
    print(return_max_number(1))
    print(return_max_number(1, 2))
    print(return_max_number(1, 200, 2))

    numbers = []
    print(numbers)
    append_all(numbers, 1, 2, 3)
    print(numbers)

    names = []
    print(names)
    append_all(names, "zeroway", "mobz", "shady", "eminem")
    print(names)

    print(describe_feature(name = 'zeroway', age = 28, weight = 120, species = 'mobz'))
    print(describe_feature(age = 18, weight = 100, species = 'eminem', name = 'shady'))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
