# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 10:24:09 2018

@author: James Jiang
"""

from hashlib import md5

input = 'ckczppom'

counter = 1
while True:
    md5_hash = md5((input + str(counter)).encode('utf-8')).hexdigest()
    if md5_hash[:6] == '000000':
        print(counter)
        break
    counter += 1
