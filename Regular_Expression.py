#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__="Limin Liu"

'''
Using regular expression to verify  Email address
re_email_1() return email like: someone@gmail.com, bill.gates@microsoft.com
re_email_2() return email with name: <Tom Paris> tom@voyager.org
'''

import re

re_email_1=re.compile(r'^([0-9a-zA-Z.]+)@([0-9a-zA-Z.]+)$')
re_email_1.match('bill.gates@microsoft.com').groups()

re_email_2=re.compile(r'^<([a-zA-Z\s]+)>\s*([0-9a-zA-Z.]+)@([0-9a-zA-Z.]+)$')
re_email_2.match('<Tom Paris> tom@gmail.com').groups()