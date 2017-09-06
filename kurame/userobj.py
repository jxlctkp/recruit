import DB
class userobj():
    sql = 'select usercode,usercname,companycode from pub_user where usercode = :codes and rownum <= 1'
    pars = {'codes':'0100000091'}
    col = {'codes':'', 'names':'', 'company':''}
    tab = {}

class dbobj():
    #,atc.DATA_LENGTH
    _sql = 'select atc.COLUMN_NAME from all_tab_cols atc where atc.table_name = upper(:tabname)'
    _pars = {'tabname':'PUB_USER'}
    _colname = {}
    def _settablename(name):
        dbobj._pars['tabname'] = name
    def _gettablename():
        return dbobj._pars
    def _getsql():
        return dbobj._sql
    def _setcolname(name):
        dbobj.colname = name
    def _getcolname():
        return dbobj._colname
    def table(tbname):
        dbobj._settablename(tbname)
        a = dbobj._getsql()
        b = dbobj._gettablename()
        c = dbobj._getcolname()
        d = DB.queryrow(a,b,c)
        e = []
        for row in d:
            e.append(row[0])
        return e

class queryobj():
    _sql = ''
    _pars = {}

    def grantsql(trager,tb,dirts):
        sql = 'select '
        m = 0
        for i in trager:
            if m > 0:
                sql = sql + ',' + i
            else:
                sql = sql + i
                m+=1
        m = 0
        for t in tb:
            if m > 0:
                sql = sql + ',' + t
            else:
                print(t)
                sql = sql + ' from ' + t
                m+=1
        sql = sql + ' where 1=1'
        for ii in dirts:
            print(dirts)
            print('key = ' + ii + ', value = ' + dirts[ii])
            if ii != '':
                #不要用字段当kye，有坑，暂时丢掉
                sql = sql + ' and ' + ii + ' = :' + ii
        #queryobj.sql = sql
        return sql

    
    def _setsql(a):
        queryobj._sql = a
    def _setpars(b):
        queryobj._pars = b
    def query(a,b,c):
        queryobj._setsql(a)
        queryobj._setpars(b)
        date = DB.queryrow(_sql,_pars,c)
        return date
