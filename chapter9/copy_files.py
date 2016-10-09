#!/usr/bin/env python

import shutil, os
os.chdir('/etc/portage/')

shutil.copy('/etc/portage/make.conf', '/home/zeroway/github/py3/chapter9/make.conf')

shutil.copy('make.conf.catalyst', '/home/zeroway/github/py3/chapter9/make.conf.catalyst')

shutil.copytree('/usr/portage/app-editors/vim', '/home/zeroway/github/py3/chapter9/vim_ebuild_files')

os.chdir('/home/zeroway/github/py3/chapter9/')
shutil.move('make.conf', 'make.conf_bak')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
