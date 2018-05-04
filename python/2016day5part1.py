# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 18:27:13 2017

@author: James Jiang
"""

from hashlib import md5

input = 'ojvtpuvg'

password = ''
counter = 0

while len(password) < 8:
    md5_hash = md5((input + str(counter)).encode('utf-8')).hexdigest()
    if md5_hash[:5] == '00000':
        password += md5_hash[5]
    counter += 1
        
print(password)
