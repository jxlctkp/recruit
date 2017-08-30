#!/usr/bin/python
import yaml
yaml_file="./test.yaml"
with open(yaml_file,'r') as application_yml_file:
	x=yaml.load(application_yml_file)
        print x
applist=x.get("name",[])
age=x.get("age",[])
print applist
print age

with open("test_01.yaml",'w') as dump_file:
	yaml.dump(x,dump_file)

