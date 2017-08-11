#!/usr/bin/python
# _*_ coding:UTF-8 _*_

'''如果目录存在，则不创建目录，不存在，则创建目录
   created:libiao 2017-08-11'''

import os
import sys

message="文件已经存在"
directory=sys.argv[1]
try:
    home=os.getcwd()
    print home
    if not os.path.exists(os.path.join(home,directory)):
        os.mkdir(os.path.join(home,directory))
except Exception as e:
    print e

