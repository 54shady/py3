#!/usr/bin/env python

from find_max import return_max_number
from append_items import append_all

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

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
