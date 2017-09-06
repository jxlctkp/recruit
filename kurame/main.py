import DB
import userobj

#返回pub_company表的字段名列表
tbname = 'pub_company'
companylist = userobj.dbobj.table(tbname)
s = {companylist[2]:'0101010101'}
t = [tbname]
sql = userobj.queryobj.grantsql(companylist,t,s)

print(sql)


#DB.query类实现单挑sql执行
#DB.query.setsql(sql)         设置sql
#DB.query.setvar(key,value)  设置参数
#DB.query.exec()              执行并返回游标

sql = 'select usercname,createtime from pub_user where 1=1 and usercode in (:y,:z) and rownum <= :x'
exec = DB.query
exec.setsql(sql)
exec.setvar('x','3')
exec.setvar('y','0103000010')
exec.setvar('z','0100000001')
for i in exec.exec():
    print(i)