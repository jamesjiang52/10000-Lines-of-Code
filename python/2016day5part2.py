# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 18:27:13 2017

@author: James Jiang
"""

from hashlib import md5

input = 'ojvtpuvg'

password_list = [i for i in '00000000']
check_list = [i for i in '01234567']
counter = 0
positions_seen = []

while len(positions_seen) < 8:
    md5_hash = md5((input + str(counter)).encode('utf-8')).hexdigest()
    if md5_hash[:5] == '00000':
        if md5_hash[5] in check_list:
            if md5_hash[5] not in positions_seen:
                positions_seen.append(md5_hash[5])
                password_list[int(md5_hash[5])] = md5_hash[6]
    counter += 1
        
print(''.join(password_list))
