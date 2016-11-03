#!usr/bin/env python
#coding=utf8

 
import MySQLdb  
import xlrd  
import time  
import sys
  
reload(sys) 
sys.setdefaultencoding('utf8')
  
# 一、从users.xls文件获取10000条用户数据  

def get_table():  
    FILE_NAME = 'all.xls'  
    data = xlrd.open_workbook(FILE_NAME)
    table = data.sheets()[0]
    return table  
  

  
# 二、批量插入executemany  
def insert_by_many(table):  
    nrows = table.nrows 
    param=[]  
    for i in xrange(1,nrows): 
        # 注意按字段顺序排列，字段内容一一对应！！ 第一列username，第二列salt，第三列pwd
        # 
        content          = str(table.cell(i, 0).value)+'<br><br/>'+str(table.cell(i, 4).value)+'<br><br/>'+'<a href='+'\'/Download/'+str(table.cell(i, 6).value)+'\' target=\'_blank\'>点击下载'+'</a>'
        score            = str(table.cell(i, 2).value)
        attachmentpath   = str(table.cell(i, 6).value)
        answerkey        = str(table.cell(i, 5).value)
        questiontype     = str(table.cell(i, 1).value)


        a =table.cell(i, 6).value # 附件
        

        if (a == '无'):
            a = ''
            content = str(table.cell(i, 0).value)+'<br><br/>'+str(table.cell(i, 4).value)+'<br><br/>'

        if (a == ''):
            a = ''
            content = str(table.cell(i, 0).value)+'<br><br/>'+str(table.cell(i, 4).value)+'<br><br/>'
            
        print str(i)+'-'*10+a

        param.append([
            content,      # 内容
            score,        # 分值
            a,            # 附件
            answerkey,    # flag
            questiontype, # 类型
            ])

        
        # param.append([str(table.cell(i, 0).value)+'<br><br/>'+str(table.cell(i, 4).value)+'<br><br/>'+'<a href='+'\'/Download/'+str(table.cell(i, 6).value)+'\' target=\'_blank\'>点击下载'+'</a>',
        #     str(table.cell(i, 2).value),# 分值
        #     str(table.cell(i, 6).value),# 附件
        #     str(table.cell(i, 5).value),# flag
        #     str(table.cell(i, 1).value),# 类型
        #     ])
    
    try:  
        # 注意按字段顺序排列，字段内容一一对应！！
        sql = "INSERT INTO t_question(content,score,attachmentpath,answerkey,questiontype) values(%s,%s,%s,%s,%s)"
        #print table.cell(i, 6).value
        #exit(0)
        # 批量插入  
        rem = cur.executemany(sql, param)
        conn.commit()
        print rem		
    except Exception as e:  
        print e  
        conn.rollback()   
      
  
  
################### 数据库配置#########################
#
# db_server = "192.168.146.129"
# db_port = "3306"
# db_user = "root"
# db_passwd = "ichunqiu"
# db_name = "test"
# db_charset = "utf8"


conn = MySQLdb.connect(host="192.168.146.129", port=3306, user="root", passwd="ichunqiu", db="test01",charset="utf8") 
#################### 连接数据库#########################
#conn = MySQLdb.connect(db_server, db_port, db_user, db_passwd, db_name,db_charset)  
cur = conn.cursor()  
  
# 新建数据库  
# cur.execute('DROP TABLE IF EXISTS user')  
# sql = """CREATE TABLE user( 
        # username CHAR(255) NOT NULL, 
        # salt CHAR(255), 
        # pwd CHAR(255) 
        # )"""  
# cur.execute(sql)  
  
# 一 、从excel文件获取sheet0数据  
table = get_table() 
  
# 二、使用批量插入  
start = time.clock()  
insert_by_many(table)  
end = time.clock()  
  
  
# 释放数据连接  
if cur:  
    cur.close()  
if conn:  
    conn.close()  