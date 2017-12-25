# encoding:utf8
import MySQLdb

conn = MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='test',
    charset='utf8')

cursor = conn.cursor()

sql = "select * from testpy"
cursor.execute(sql)

sql_insert = "insert into testpy (ZHMC,QC,YHZT,SJHM,ZDMC) values ('999','anjoulee','YES','18638518819','李磊')"
sql_update = "update testpy set ZHMC='TEST',QC='TEST',YHZT='NO',SJHM='18600000000',ZDMC='TEST' where SJHM='15737175705'"
sql_delete = "delete from testpy where sjhm1='15737175702'"
try:
    cursor.execute(sql_insert)
    print cursor.rowcount

    cursor.execute(sql_update)
    print cursor.rowcount

    cursor.execute(sql_delete)
    print cursor.rowcount
    conn.commit()
except Exception as e:
    print e
    conn.rollback()

cursor.close()
conn.close()
