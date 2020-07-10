### 日志模块，可以方便供后期使用的封装
```
#!/usr/bin/python
#coding:UTF-8
import logging,logging.handlers
def WriteLog(filename):
    logger = logging.getLogger()
    # 防止日志重复
    if not logger.handlers:
        log_filename = filename

        log_level = logging.DEBUG
        # 定义日志格式
        format = logging.Formatter('%(asctime)s | %(filename)s | %(funcName)s | %(levelname)s | %(message)s')

        handler = logging.handlers.RotatingFileHandler(log_filename, mode='a')
        handler.setFormatter(format)

        logger.addHandler(handler)
        logger.setLevel(log_level)
    return logger

```

###### 调用方法
```
mylog.WriteLog('oper.log').info('Hello World')
```

### configparser模块，可以方便供后期使用的封装
```
#!/usr/bin/python
# coding:UTF-8
#import ConfigParser # py2
import configparser as ConfigParser #py3

def getconfig(filename, section=''):
    cf = ConfigParser.ConfigParser()
    cf.read(filename)
    cf_items = dict(cf.items(section)) if cf.has_section(section) else {}
    return cf_items


def setconfig(filename, section='', key='', value=''):
    cf = ConfigParser.ConfigParser()
    cf.read(filename)
    if not cf.has_section(section):
        cf.add_section(section)
    cf.set(section, key, value)
    cf.write(open(filename, 'w'))


def delconfig(filename, *pa):
    cf = ConfigParser.ConfigParser()
    cf.read(filename)
    if len(pa) > 2:
        print
        "paragram is too much"
    elif len(pa) == 2 and cf.remove_option(pa[0], pa[1]):
        cf.write(open(filename, 'w'))
    elif len(pa) == 1 and cf.remove_section(pa[0]):
        cf.write(open(filename, 'w'))
    else:
        print
        'section or option is not exist'
```

###### 配置文件实例
```
[dbconfig]
host = 127.0.0.1
port = 3306
username = monkey
password = 123456
database = ops
```
###### 调用方法
```
conf = getconfig('../Config.ini', 'dbconfig')
#setconfig('im.conf', 'imlog2', 'port', '1090')
#delconfig('im.conf', 'imlog2')
```

### 数据库操作，可以方便供后期使用的封装
```
import pymysql
from .myparse import getconfig

DBHOST = getconfig('Config.ini', 'dbconfig')


def connnet():
# 连接函数中增加异常捕获
    try:

        conn = pymysql.connect(
            host = DBHOST['host'],
            user = DBHOST['username'],
            password= DBHOST['password'],
            database = DBHOST['database'],
            port = int(DBHOST['port']),
            )
    except:
        return None

    return conn

def insert(sql):
    conn = connnet()
    # 数据库增删改查函数中首先要判断连接是否成功
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        conn.commit()
        return 'Insert succ.', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def update():
    conn = connnet()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        print(cur.rowcount)
        if cur.rowcount == 0:
            return 'Update fail', False

        conn.commit()
        return 'Update succ.', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()


def select(sql):
    conn = connnet()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
    except Exception as e:
        return e, False
    else:
        rows = cur.fetchall()
        return rows, True
    finally:
        cur.close()
        conn.close()

def exist(sql):
    conn = connnet()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()
    try:
        cur.execute(sql)
    except Exception as e:
        return e, False
    else:
        rows = cur.fetchall()
        return rows, True
    finally:
        cur.close()
        conn.close()

def delete(sql):
    conn = connnet()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        if cur.rowcount == 0:
            return 'Delete fail', False
        conn.commit()
        return 'Delete succ.', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

```

### pymysql操作练习
![image](https://raw.githubusercontent.com/niushaoshuai/stand_file/master/youdao-pic/pymysql-insert.png)
![image](https://github.com/niushaoshuai/stand_file/blob/master/youdao-pic/pymysql-delete.png?raw=True)
![image](https://github.com/niushaoshuai/stand_file/blob/master/youdao-pic/pymysql-select.png?raw=True)

### 读取文件时对文件描述符的异常判断 locals 。推荐用with不会出现异常
![image](https://github.com/niushaoshuai/stand_file/blob/master/youdao-pic/fd-except-locals-1.jpg?raw=true)
![image](https://raw.githubusercontent.com/niushaoshuai/stand_file/master/youdao-pic/fd-except-locals-2.png)

### pymysql环境部署
```
# 部署mysql
rpm -ivh mysql-community-release-el6-5.noarch.rpm
yum -y install mysql-community-server
# 安装pymysql
pip install pymysql

# 创建数据库和表
create database ops  DEFAULT CHARSET utf8 COLLATE utf8_general_ci;grant all privileges on ops.* to monkey@'%' identified by '123456';flush privileges;

CREATE TABLE users
(
id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
username varchar(32),
age int,
tel varchar(11),
email varchar(50)
);

```

### 模块 os,subprocess
![image](https://raw.githubusercontent.com/niushaoshuai/stand_file/master/youdao-pic/models-os-system.png)
![image](https://raw.githubusercontent.com/niushaoshuai/stand_file/master/youdao-pic/models-os-subprocess.png)