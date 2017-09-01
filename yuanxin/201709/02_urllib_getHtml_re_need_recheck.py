#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/1-urllib_getHtml.py
@time: 2017/9/1 
"""

import re
import urllib.request                             # 在python2中，用法为 import urllib


def getHtml(url):
    page = urllib.request.urlopen(url)            # python2中， urllib.urlopen
    html = page.read()                            # 这里page，也可以直接使用上面定义的值
    # print("01",html)
    return html                                   # 这里 return 了 html，下面的打印 02 ，才有值；否则为 None


def getImg(html):
    reg = r'src="(.*?\.jpg)"'
    print("01", reg)
    imgre = re.compile(reg)                        #  re.compile()把正则表达式编译成一个正则表达式对象.
    print("02", imgre)
    html = html.decode('utf-8')                      #  python3 中需要添加，否则会报错；
    print("02+", html)
    imglist = re.findall(imgre, html)              # 读取html中包含imgre的数据
    print("03", imglist)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, "%s.jsp" % x)
        # urllib.urlretrieve()方法，直接将远程数据下载到本地。
        # 通过一个for循环对获取的图片连接进行遍历，对其进行重命名，命名规则通过x变量加1
        x += 1

html = getHtml("http://tieba.baidu.com/p/2460150866")
print("04", getImg(html))
