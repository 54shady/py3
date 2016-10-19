#!/usr/bin/env python

import threading

#print('Cats', 'Dogs', 'Frogs', sep=' & ')
threadObj = threading.Thread(target = print, args = ['Cats', 'Dogs', 'Frogs'], kwargs = {'sep': ' & '})
threadObj.start()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
