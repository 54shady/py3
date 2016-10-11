#!/usr/bin/env python

import random
import time

while True:
    messages = ['It is certain',
             'It is decidedly so',
             'Yes definitely',
             'Reply hazy try again',
             'Ask again later',
             'Concentrate and ask again',
             'My reply is no',
             'Outlook not so good',
             'Very doubtful']

    print(str(time.ctime()) + ' ' + messages[random.randint(0, len(messages) - 1)])
    time.sleep(2)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
