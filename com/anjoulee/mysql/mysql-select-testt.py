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

rs = cursor.fetchall()
for row in rs:
    print "ZHMC=%s,QC=%s,YHZT=%s,SJHM=%s,ZDMC=%s" % row

cursor.close()
conn.close()
