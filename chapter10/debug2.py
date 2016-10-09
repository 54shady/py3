#!/usr/bin/env python

import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
