#!/usr/bin/env python

def return_max_number(*values):
    if not values:
        return None

    max_value = values[0]
    for v in values:
        if v > max_value:
            max_value = v
    return max_value

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
