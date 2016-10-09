#!/usr/bin/env python

import zipfile, os
os.chdir('/home/zeroway/github/py3/chapter9')# move to the folder with example.zip

# list the files in the example.zip
exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())

exampleZip.close()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
