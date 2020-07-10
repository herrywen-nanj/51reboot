import pymysql
import configparser
from prettytable import PrettyTable
import logging

my_conf = '51reboot_config'

MSG = """
    1. 增 insert         # add monkey 12 13312341234 monkey@51reboot.com
    2. 删 delete         # delete monkey
    3. 改 update         # update monkey set age = 18
    4. 查 select         # select
    5. 帮助 help         # 'h' or 'help'
    6. 退出 exit         # exit
"""

def log(info):
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                        filename='51reboot.log',
                        filemode='a'
                        )
    return logging.debug(info)

def connect():
    config = configparser.ConfigParser()
    config.read(my_conf,encoding='utf-8')
    if not config.items('db'):
        return "config db is empty"
    else:
        try:
            conn = pymysql.connect(
                host=config.get('db', 'host'),
                port = config.getint('db', 'port'),
                user = config.get('db', 'user'),
                password = config.get('db', 'password'),
                database = config.get('db', 'database')
            )
        except:
            return None
    return conn

def select_user():
    conn = connect()
    cur = conn.cursor()
    sql = "select * from users"
    cur.execute(sql)
    users_list = cur.fetchall()
    table = PrettyTable()
    table.field_names = ['id', 'username', 'age', 'phone', 'email']
    for users in users_list:
        table.add_row([users[0],users[1],users[2],users[3],users[4]])
    print(table)
    conn.commit()
    cur.close()
    conn.close()

def add_user():
    conn = connect()
    username = input('Please input username:')
    age = input('Please input User\'s age:')
    phone = input('Please input User\'s phone:')
    email = input('Please input User\'s email')
    cur = conn.cursor()
    sql = "insert into users(username, age, phone, email) values (%s,%s,%s,%s)"
    print(sql)
    data = (username,age,phone,email)
    cur.execute(sql,(data))
    conn.commit()
    cur.close()
    conn.close()

def del_user():
    conn = connect()
    cur = conn.cursor()
    user_name = input('Please input the username you want to delete:')
    sql_select = f""" select * from users where username='{user_name}'"""
    print(sql_select)
    cur.execute(sql_select)
    user_list = cur.fetchall()
    print(user_list)
    if user_list:
        sql_delete = f""" delete from users where username='{user_name}'"""
        cur.execute(sql_delete)
        conn.commit()
        log('Delete {} user successfully'.format(user_name))
        print(["\033[1;32;40mDelete {} user successfully\033[0m".format(user_name)])
    else:
        print('user is not exists,Please re-input.')
        log('Delete {} failed，user is not exists'.format(user_name))
        print("\033[1;31mDelete {} failed,user is not exists\033[0m".format(user_name))
    conn.close()

def update_user(username):
    conn = connect()
    cur = conn.cursor()
    sql_select = f""" select * from users where username='{username}'"""
    # print(sql_select)
    cur.execute(sql_select)
    user_list = cur.fetchall()
    # print(user_list[0][1])
    # print(user_list[0][2])
    # print(user_list[0][3])
    # print(user_list[0][4])
    if user_list:
        print(["\033[1;32;40musername {} is exists\033[0m".format(username)])
        new_username = input('Please input the new username:')
        new_age = input('Please input the new age:')
        new_phone = input('Please input the new phone:')
        new_email = input('Please input the new email:')
        if new_username is '':
            new_username = user_list[0][1]
        if new_age is '':
            new_age = user_list[0][2]
        if new_phone is '':
            new_phone = user_list[0][3]
        if new_email is '':
            new_email = user_list[0][4]
        sql_update = f""" update users set username = '{new_username}',age='{new_age}',phone='{new_phone}',email='{new_email}' where username = '{username}'"""
        print(sql_update)
        cur.execute(sql_update)
        conn.commit()
    else:
        print(["\033[1;32;40musername {} is not exists\033[0m".format(username)])
    conn.close()

def main():
    while True:
        info = input("Please input your operation:")
        info_list = info.split()
        action = info_list[0]
        if action == "add":
            add_user()
        elif action == "select":
            select_user()
        elif action == "delete":
            del_user()
        elif action == "update":
            username = input('Please input the username you want to update:')
            update_user(username)
        elif action.lower() == "h" or action.lower() == "help":
            print(MSG)
        elif action == "exit" or action == "quit":
            break

if __name__ == '__main__':
    main()