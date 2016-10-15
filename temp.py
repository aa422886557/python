#!usr/bin/env python
#coding=utf8

 
import MySQLdb  
import xlrd  
import time  
import sys
  
reload(sys) 
sys.setdefaultencoding('utf8')
  
# 从users.xls文件获取10000条用户数据  
# 
def get_table():  
    FILE_NAME = 'all.xls'  
    data = xlrd.open_workbook(FILE_NAME)
    table = data.sheets()[0]
    return table  
  
#循环插入execute     
# def insert_by_loop(table):
    # nrows = table.nrows  
    # for i in xrange(1,nrows):
        # param=[]  
        # try:  
            # #sql = "INSERT INTO t_question(title,questiontype,score,kd,content,flag) values(%s,%s,%s,%s,%s,%s)" 
            # sql = "INSERT INTO t_question(content) values(%s)"
            # # 第一列content，第二列flag，第三列title，  
            # #print 'Insert: ',table.cell(i, 0).value, table.cell(i, 2).value,table.cell(i, 1).value, table.cell(i, 3).value,table.cell(i, 4).value,table.cell(i, 5).value
			
            # #param = (table.cell(i, 0).value, table.cell(i, 2).value,table.cell(i, 1).value, table.cell(i, 3).value,table.cell(i, 4).value,table.cell(i, 5).value)
            # # 单条插入
            # param.append([table.cell(i, 0).value+table.cell(i, 4).value+table.cell(i, 6).value])
            # rei = cur.execute(sql, param)
            # conn.commit()
            # print rei
        # except Exception as e:
            # print e
            # conn.rollback()  
   
  
# 批量插入executemany  
def insert_by_many(table):  
    nrows = table.nrows 
    param=[]  
    for i in xrange(1,nrows): 
        # 注意按字段顺序排列，字段内容一一对应！！ 第一列username，第二列salt，第三列pwd  
        param.append([str(table.cell(i, 0).value)+'<br><br/>'+str(table.cell(i, 4).value)+'<br><br/>'+'附件下载地址:<a href='+'/Download'+'>http://ip/dowload/'+str(table.cell(i, 6).value+'</a>'),table.cell(i, 1).value])
    try:  # 注意按字段顺序排列，字段内容一一对应！！
        sql = "INSERT INTO t_question(content,score) values(%s,%s)"
        #print param
        # 批量插入  
        rem = cur.executemany(sql, param)
        conn.commit()
        print rem		
    except Exception as e:  
        print e  
        conn.rollback()   
      
  
  
# 连接本地数据库  设置编码 导入数据库名字
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="ctfdb",charset="utf8")  
cur = conn.cursor()  
  
# 新建数据库  
# cur.execute('DROP TABLE IF EXISTS user')  
# sql = """CREATE TABLE user( 
        # username CHAR(255) NOT NULL, 
        # salt CHAR(255), 
        # pwd CHAR(255) 
        # )"""  
# cur.execute(sql)  
  
# 从excel文件获取数据  
table = get_table() 
  
# 使用循环插入  
# start = time.clock()  
# insert_by_loop(table)  
# end = time.clock()  

  
# 使用批量插入  
start = time.clock()  
insert_by_many(table)  
end = time.clock()  
  
  
# 释放数据连接  
if cur:  
    cur.close()  
if conn:  
    conn.close()  