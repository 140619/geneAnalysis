#python 3.6
# -*- coding:utf-8 -*-
__author__ = 'BH8ANK'

import json
import pymysql


conn = pymysql.connect(
        host = 'localhost',#mysql服务器地址
        port = 3306,#端口号
        user = 'root',#用户名
        passwd = 'xxxxxx',#密码
        db = 'xdb',#数据库名称
        charset = 'utf8',#连接编码，根据需要填写
    )
cur = conn.cursor()#创建并返回游标

#创建表头
sql = "CREATE TABLE daxue (code  VARCHAR(32),charge  VARCHAR(100),level VARCHAR(100),name VARCHAR(100),remark VARCHAR(100),prov VARCHAR(100));"

cur.execute(sql)#执行上述sql命令
a = open(r"D:\alldata.json", "r",encoding='UTF-8')
out = a.read()
tmp = json.dumps(out)
tmp = json.loads(out)
num = len(tmp)
i = 0
while i < num:
    code = tmp[i]['code']
    charge = tmp[i]['charge']
    level = tmp[i]['level']
    name = tmp[i]['name']
    remark = tmp[i]['remark']
    prov = tmp[i]['prov']
    value = [code,charge,level,name,remark,prov]
    sql_insert = "insert into daxue (code,charge,level,name,remark,prov) values (" + "'"+code+"'" +","+ "'"+charge+"'" + ","+"'"+level+"'" + ","+"'"+name+"'" + ","+"'"+remark+"'" + ","+"'"+prov+"'" + ");"
    # sql_insert =("insert into daxue (code,charge,level,name,remark,prov) values (%s,%s,%s,%s,%s,%s);",value)
    # sql_insert = sql_insert.encode("utf8")
    print(sql_insert)

    cur.execute(sql_insert)  # 执行上述sql命令
    i = i+1

# print(num)
conn.commit()
conn.close()