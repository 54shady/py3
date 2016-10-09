#!/usr/bin/env python

import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('this will be store to the file')
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
