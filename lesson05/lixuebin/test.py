import os, pymysql, configparser
from datetime import datetime



def MyConn(filename = 'mysql.ini'):
    try:
        config = configparser.ConfigParser()
        config.read(filename)
        if os.path.isfile(filename):
            connect=pymysql.connect(
                host = config.get('mysqld', 'host'),
                port = config.getint('mysqld', 'port'),
                user = config.get('mysqld', 'user'),
                password = config.get('mysqld', 'password'),
                database = config.get('mysqld', 'database')
        )
            return connect
        else:
            return '配置文件不存在',False
    except Exception as  e:
        return e, False

def curInsert(sql):
    conn = MyConn()
    if not conn:
        return 'conn is failed.', False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        return  "\n\033[1;32m Add user success.\033[0m", True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def EXfile(info_list,table='users'):
    try:
        dirInfo = info_list[1]
        sql = '''select * from {} into outfile '/tmp/{}.csv' fields terminated by ',' optionally enclosed by '"' lines terminated by '\r\n';'''.format(table, dirInfo)
        msg, ok = curInsert(sql)
        if ok:
            # 用户自定义文件判断成功与否
            if os.path.isfile('/tmp/{}.csv'.format(info_list[1])):
                return 'AA', True
            else:
                return 'BB', False
        else:
            return msg, False
    except Exception as e:
        print(e)
        return 'D', False

def EXDefaultFile(table='users'):
    unixTime = datetime.now().strftime('%s')
    print(unixTime)
    try:
        sql = '''select * from {} into outfile '/tmp/usersInfo_{}.csv' fields terminated by ',' optionally enclosed by '"' lines terminated by '\r\n';'''.format(table, unixTime)
        msg, ok = curInsert(sql)
        if ok:
        # 默认文件存在判断成功
            if os.path.isfile('/tmp/usersInfo_{}.csv'.format(unixTime)):
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(e)
        return False


def Export(info_list):
    dirInfo = info_list[1]
    unixTime = datetime.now().strftime('%s')
    # 如果用户输入两个参数 后面当作文件名字
    if len(info_list) == 2:
        msg, ok = EXfile(info_list)
        if ok:
            # msg = "\033[32m Export csv file succeed! File is '/tmp/{}.csv'".format(dirInfo)
            return msg, True
        else:
            # msg = '\033[31mExport file failed!\033[0m'
            return msg, False
    # 如果用户只输入了export,导出至默认路径默认文件
    elif len(info_list) == 1:
        msg, ok =  EXDefaultFile()
        if ok:
            msg = "\033[32m Export csv file succeed! File is 'tmp/userInfo_{}.csv'\033[0m".format(unixTime)
            return msg, True
        else:
            msg = '\033[31mExport file failed! \033[0m'
            return msg, False
    else:
        msg = '\033[31m输入错误\033[0m'
        return msg, False



msg, ok = Export(['export','wwww'])
print(msg)