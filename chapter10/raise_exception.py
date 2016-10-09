#!/usr/bin/env python

import traceback
try:
    raise Exception('This is the error message.')
except Exception as myerr:
    print('An exception happend: ' + str(myerr))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
