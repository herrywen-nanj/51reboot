import configmgt
import pymysql

FILENAME = '51reboot.ini'

def connnet():

    cfg, ok = configmgt.ReadConfig(FILENAME, 'rebootdb')
    if not ok:
        return cfg, False
    # print(cfg)
    try:
        # conn = pymysql.connect(
        #     host = "10.0.2.15",
        #     user = "monkey",
        #     password= "123456",
        #     database = "ops",
        #     port = 3306,
        #     )
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


'''1 展示用户信息 '''
def ShowDb():
    conn = connnet()
    if not conn:
        return "conn db fial", False
    print('ID', '\t\t', '姓名''\t\t', '年龄''\t\t', '电话''\t\t', '邮箱')
    print('---' * 20)
    cur = conn.cursor()
    cur.execute("""
            SELECT * FROM users;
        """)
    users_list = cur.fetchall()
    for index, users in enumerate(users_list):
        print(f'{index + 1}\t\t{users[1]}\t\t{users[2]}\t\t{users[3]}\t\t{users[4]}')
    conn.commit()
    cur.close()
    conn.close()

'''2 增加用户信息 '''
def AddDb():
    conn = connnet()
    if not conn:
        return "conn db fial", False
    username = input('用户姓名：')
    age = input('用户年龄：')
    tel = input('用户电话：')
    email = input('用户邮箱')
    cur = conn.cursor()
    sql = 'insert into users(username, age, tel, email) values (%s,%s,%s,%s)'
    print(sql)
    # data = f"""
    #     #     INSERT INTO users (username, age, age, phone)  VALUES ("{name}","{sex}",{age},"{phone}")
    #     # """
    data = (username,age,tel,email)
    cur.execute(sql,(data))
    conn.commit()
    cur.close()
    conn.close()

'''3 修改用户信息 '''
def UpdataDb():
    ShowDb()
    conn = connnet()
    if not conn:
        return "conn db fial", False
    cur = conn.cursor()
    new_id = input("请输入你想要修改的编号:")
    new_name = input('请输入修改后的姓名:')
    new_age = input('请输入新的年龄：')
    new_tel = input('请输入新电话：')
    new_email = input('请输入新邮箱')
    # 先查询输入的学生id是否存在，存在的话更新，不存在的给出用户提示
    sql = f"""
            SELECT * FROM users WHERE id= "{new_id}";
        """
    print(sql)
    cur.execute(sql)
    user_list = cur.fetchall()
    print(user_list)
    if user_list:
        sql2 = f"""
                    UPDATE users SET username = "{new_name}",age="{new_age}",tel="{new_tel}",email="{new_email}"  WHERE id="{new_id}";
                """
        cur.execute(sql2)
        conn.commit()
    else:
        print('用户不存在，请重新操作。')
    conn.close()
    print('用户信息修改成功')
    # 下面的方法也行 看你用哪种
    # cursor.execute("""UPDATE students SET name=?, sex= ?,age=?,phone=? WHERE id="""+new_id,(new_name, new_sex, new_age, new_phone))
    # connect.commit()
    # connect.close()

'''4 删除用户信息 '''
def DeleteDb():
    ShowDb()
    conn = connnet()
    if not conn:
        return "conn db fial", False
    cur = conn.cursor()
    print(""" 删除> 请输入子操作编号：
                     1）按用户编号删除
                     2）删除全部用户（clear） 
           """)
    sub_select = int(input('请选择子操作：'))

    if sub_select == 1:
        ShowDb()
        user_name = input('要删除的学生姓名：')
        delete_name = f""" delete from users where username='{user_name}'"""
        cur.execute(delete_name)
        conn.commit()
        conn.close()
        print('删除成功')
    elif sub_select == 2:
        conn = connnet()
        if not conn:
            return "conn db fial", False
        cur = conn.cursor()
        confirm = input('要删除全部用户？( Y/y):')
        if confirm == 'y':
            clear_as = f"""DELETE FROM users;"""
            cur.execute(clear_as)
            conn.commit()
            conn.close()
            print('删除全部成功')

'''5 插入数据库字段'''
def InsertDb():
    conn = connnet()
    if not conn:
        return "conn db fial" , False
    cur = conn.cursor()
    cur.execute(
        '''
        CREATE TABLE users
        (
        id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
        username varchar(32),
        age int,
        tel varchar(11),
        email varchar(50)
        );
        ''')
    conn.commit()
    cur.close()
    conn.close()
def main():
    # 主函数，程序入口
    while True:
        print("""
              用户管理系统
            1-展示用户信息
            2-增加用户信息
            3-修改用户信息
            4-删除用户信息
            5-插入数据库字段
            0-退出程序
            """)

        num = int(input('请输入操作编号：'))

        if num == 1:
            ShowDb()
        elif num == 2:
            AddDb()
        elif num == 3:
            UpdataDb()
        elif num == 4:
            DeleteDb()
        elif num == 5:
            InsertDb()
        elif num == 0:
            break


if __name__ == '__main__':
    main()