#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/17-get-img-update.py
@time: 2017/8/17
"""

import requests
import re
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
r = requests.get(url='https://www.baidu.com')
res = r.text

pattern = r"www.baidu.com.*logo.*(png|jnp)"
m = re.search(pattern, res ) 

imgurl = 'http://'+m.group(0)
response = requests.get(imgurl)
resurl = requests.get(imgurl)
file = open(imgurl.split('/')[-1],'wb')
file.write(resurl.content)
file.close()