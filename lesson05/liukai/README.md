## Lesson5

### 包和模块介绍

#### 模版
 一个.py 文件就是一个模块，可以import导入
 
 一个模块可以写多个函数
 
 功能复用
 
 
 #### 包
 
 目录下有__init__.py 文件
 
 import os as linuxos 起别名
 
 linuxos.system('df -h')
 
 from os import system
 
 循环导入，文件1导入文件2 ，文件2导入文件1 会报错
 
 
#### 数据库
 
 MysqlDB 2.7   C写的

 PyMySQL  python 3 Django 1.11
 
 SQLALchemy 支持原生sql ，支持orm， Flask
 
 
  pip install PyMySQL
  
  create database ops default charset uft8 collate utf8_general_ci;
  
  grant all privileges on ops.* to root@'%' identified by '123456';
  
  flush privileges;
  
  
 create table users(id int unsigend not null primary key auto_increment,username varchar(32),age int,tel varchar(11),email varchar(50))
  
  ```python

import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    databse='ops',
    port=3306
)

# 创建游标
cur=conn.cursor()

sql="insert into users( username,age,tel,email) values('mobkey',18,'135xxxx','ss@qq.com')"

cur.execute(sql)

conn.commit()

# 查询all
data=cur.fechall()


#关闭
cur.close()
conn.close()

```

```python
import pymsql
from  . import configmgt

FILENAME="config.ini"

def connect():
    cfg,ok=configmgt.ReadConfig(FILENAME,'rebootdb')
    if not  ok:
        return cfg,False
    try:
        conn = pymysql.connect(
        #host='localhost',
        #user='root',
        #password='123456',
        #databse='ops',
        #port=3306)
        host=cfg['host'],
        user=cfg['user'],
        password=cfg['password'],
        databse=cfg['db'],
        port=cfg['port']
        )
    except:
        return None
    return conn
    
    
def insert(sql):
    conn=connect()
    if not conn:
        return "conn is none",   False
    cur=conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        return 'insert success',True
    except Exception as e:
        conn.rollback()
        return e,False
    finally:
        cur.close()
        conn.close()
        
def update():
    pass

def select():
    pass

def delete(sql):
    conn=connect()
    if not conn:
        return "conn is none",   False
    cur=conn.cursor()
    try:
        cur.execute(sql)
        if cur.rowcount!=1:
            return  'delete fail',False
        conn.commit()
        return 'delete success',True
    except Exception as e:
        conn.rollback()
        return e,False
    finally:
        cur.close()
        conn.close()
        
def main():
    pass


```
  
  ### configparser
  
  ```python
import  configparser

config =configparser.ConfigParser()

config.read('config.ini')
print(config.sections())

print(dict(config['msyqld']))



def ReadConfig(filename,section,key):
    config =configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return 'config init is empty',False
    if key:
        if section in config.sections():
            return dict(config[section])[key],True
        else:
            return '',False
    else:
        return dict(config[section]),True
    
    

```
  
  创建ini文件
  
  [ msyqld]
  
  key=value
  
  
  ### os
  
  os.system('df -h')
  
  cmd='df -h'
  
  p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.STDOUT,shell=True) #建议不用shell
  
  print(p.communicate())
  stdin，stdout=p.communicate()
  
  
  shlex
  
  cmd1= shlex.split(cmd)
  
  
  ### 作业
  修改上次作业使用mysql存储数据
  
  
  
  
  
 
 

 
 