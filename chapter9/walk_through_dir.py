#!/usr/bin/env python

import os

for folderName, subfolders, filenames in os.walk('/usr/portage/games-util/xqf/'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
