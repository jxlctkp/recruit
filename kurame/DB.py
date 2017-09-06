# -*- coding: utf-8 -*-
#import sys
#sys.path.append(".")
#print(sys.path)
import cx_Oracle
import os
#import userobj
#设置字符集
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8' 
#db1 = cx_Oracle.connect('wodm_datatest/dmwo02test@10.1.108.10:1521/coretestdb')
#DB连接
_ip = '10.1.108.42'
_port = 1521
_datebase = 'tmpdev'
_user = ''
_pw = ''
_dsn_tns = cx_Oracle.makedsn(_ip, _port, _datebase)
_opsdb = cx_Oracle.connect(_user, _pw, _dsn_tns)
version = _opsdb.version
dsn = _opsdb.dsn
_cursor = _opsdb.cursor()


#测试参数
sql = 'select usercode,usercname,companycode from pub_user where usercode = :codes and rownum <= 1'
pars = {'codes':'0100000091'}
dirts = {'codes':'', 'names':'', 'company':''}
#先定义词典再查询单行
def querybyobj(sql,named_params,dirts):
    s = _cursor.execute(sql,named_params)
    for row in s:
        i = len(dirts)
        n = 0
        for ii in dirts:
            dirts[ii]=row[n]
            print(n)
            n=n+1
        return dirts

def querybytable(sql,named_params,dirts):
    s = _cursor.execute(sql,named_params)
    n = 0
    for row in s:
        print(row)
        dirts[n]=row
        n+=1
    return dirts

def queryrow(sql,named_params,dirts):
    dirts = _cursor.execute(sql,named_params)
    return dirts

class query():
    _sql = ''
    _vars = {}

    def setsql(sql):
        query._vars = {}
        query._sql = sql
    def setvar(var1,value1):
        a = {var1:value1}
        query._vars.update(a)
    def exec():
        a = query._sql
        b = query._vars
        results = _cursor.execute(a,b)
        return results