#!/usr/bin/python
import os

confdir=os.getenv("my_config")
print confdir
'''conffile='env_check.conf'
conffilename=os.path.join(confdir,conffile)

for env_check in open(conffilename):
    print env_check
'''
