import pymysql
import configmgt
import json

FILENAME = '51reboot.ini'
def connect():
    cfg,ok = configmgt.ReadConfig(FILENAME,'rebootdb')
    if not ok:
        return cfg,False
    # print(cfg)
    try:
        # conn = pymysql.connect(
        #     host='192.168.1.1',
        #     user='monkey',
        #     password="123456",
        #     database='ops',
        #     port=3306,
        # )

        conn = pymysql.connect(
            host=cfg['host'],
            user=cfg['username'],
            password=cfg['password'],
            database=cfg['database'],
            port=int(cfg['port']),
        )
    except:
        return None
    return conn
# print(connect())

def insert(sql):
    conn = connect()
    if not conn:
        return 'conn db fail',False
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
        return 'Insert succ',True
    except Exception as e:
        conn.rollback()
        return e,False
    finally:
        cursor.close()
        conn.close()

def update(sql):
    conn = connect()
    if not conn:
        return 'conn db fail',False
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        print('%s行数据受影响' % cursor.rowcount)
        if cursor.rowcount == 0:
            return 'Update fail',False
        conn.commit()
        return 'Update succ',True
    except Exception as e:
        conn.rollback()
        return e,False
    finally:
        cursor.close()
        conn.close()

def select(sql):
    conn = connect()
    if not conn:
        return 'conn db fail',False
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except Exception as e:
        return e,False
    else:
        rows = cursor.fetchall()
        return rows,True
    finally:
        cursor.close()
        conn.close()

def delete(sql):
    conn=connect()
    if not conn:
        return 'conn db fail',False
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        print('%s行数据受影响'%cursor.rowcount)
        if cursor.rowcount == 0:
            return 'Delete fail',False
        conn.commit()
        return 'Delete succ',True
    except Exception as e:
        conn.rollback()
        return e,False
    finally:
        cursor.close()
        conn.close()

def main():
    flag = False
    msg = ''
    # 添加数据
    # for i in range(10,30):
    #     sql = ''' insert into users(username,age,tel,email) \
    #     values('monkey{0}',12,'133xxx','monkey{0}@51reboot.com');'''.format(i)
    #     print('sql:%s'%sql)
    #     insertMsg,ok = insert(sql)
    #     print('insertMsg:%s'%insertMsg)
    #     print('#'*50)

    # 删除
    # sql = ''' delete from users where username = 'monkey10' '''
    # deleteMsg,ok = delete(sql)
    # print('deleteMsg:%s'%deleteMsg)

    # 更新数据
    # sql = ''' update users set age = 22 where username='monkey11'; '''
    # updateMsg,ok = update(sql)
    # print('updateMsg:%s'%updateMsg)

    # 查询数据
    fields = ['id', 'username', 'age', 'tel', 'email']
    sql = ''' select * from users'''
    result,ok = select(sql)
    if not ok:
        msg ='result:%s'%result
    else:
        data_dic = {}
        print(result,type(result))
        for i in result:
            data_dic[i[1]] = dict(zip(fields,i))
            # print(json.dumps(data_dic))
        print(json.dumps(data_dic))
        # redata =[dict(zip(fields,i)) for i in result]
        # import json
        # print(json.dumps(redata,indent=8))



if __name__ == '__main__':
    main()









