# task02模拟登陆-数据库实现方式
"""
Created on May 21th 20:20:52 2019
Modify1 on May 22th 16:49:30 2019
@author: Owen.Niu
"""
import sys
import pymysql.cursors

class Auth:
    connect = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123',
        db='loginsys',
        charset='utf8'
    )
    cursor = connect.cursor()
    def insert(self,table,username,password):
        sql = "INSERT INTO %s (username,password ) VALUES ('%s','%s')"
        data = (table,username,password)
        self.cursor.execute(sql%data)
        self.connect.commit()
    def delete(self,table,username):
        sql = "DELETE FROM  %s WHERE username = '%s'"
        data = (table,username)
        self.cursor.execute(sql%data)
        self.connect.commit()
    def modify(self,table,username,password):
        sql = "UPDATE %s set password='%s' where username='%s'"
        data = (table,password,username)
        self.cursor.execute(sql%data)
        self.connect.commit()
    def all_list(self,table):
        res = []
        sql = "SELECT * FROM  %s"
        data = (table)
        self.cursor.execute(sql%data)
        for row in self.cursor.fetchall():
            res.append({'username':row[1],'password':row[2]})
        return res
    def one_list(self,table,username):
        user=[]
        sql = "SELECT password FROM  %s where username='%s'"
        data = (table,username)
        try:
            self.cursor.execute(sql%data)
            rows=self.cursor.fetchall()
            if rows:
                for row in rows:
                    return row[0]
            else:
                return 0
        except:
            return 0
if __name__ == '__main__':
    db = Auth()
    #print(db.one_list('user','owen'))
    # 定义变量
    INIT_FAIL_CNT = 1
    MAX_FAIL_CNT = 6
    
    username=str(input("请输入用户名："))
    res=db.one_list('user',username)
    if res != 0:
        password=str(input("请输入密码："))
        count=1
        while INIT_FAIL_CNT < MAX_FAIL_CNT:
            if res == password:
                print("%s Login Successfully"%(username))
                while True:
                    # 业务逻辑
                    info = input("Please input userinfo: ")
                    info_list = info.split()
                    # 输入过滤器
                    if len(info_list) == 3:
                        action = info_list[0]
                        username = info_list[1]
                        password = info_list[2]
                    elif len(info_list) == 2:
                        action = info_list[0]
                        username = info_list[1]
                    else:
                        action = info_list[0]
                    # 增删该查逻辑
                    if action == "add" :
                        db.insert('user',username,password)
                    elif action == "delete" :
                        db.delete('user',username)
                    elif action == "update" :
                        db.modify('user',username,password)
                    elif action == "list" :
                        print(db.all_list('user'))
                    elif action == "exit":
                        sys.exit(0)
                    else:
                        print("invalid action")
            else:
                print("%s Login Failed,Password Error, %d times"%(username,INIT_FAIL_CNT))
                INIT_FAIL_CNT += 1
            password=str(input())
        else:
            print("%s Password Error,times is exhaust"%(username))
    else:
        print("%s Not Exist"%(username))
