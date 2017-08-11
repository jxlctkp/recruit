#!/usr/bin/python
import os
fo=open("foo.txt","a")
print "file name is ",fo.name
print "open mode is ",fo.mode
print "file whether closed",fo.closed
print ""
fo.write("insert some words in foo.txt\n")
fo.close()
fo=open("foo.txt",'r')
str=fo.read()
print "file context is \n"+str
fo.close()
print "file whether closed",fo.closed


os.chdir("/Users/luck")
os.getcwd()
