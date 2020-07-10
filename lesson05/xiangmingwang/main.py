# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Maxwell'


import pymysql, datetime, sys
import load_config
from prettytable import PrettyTable


CONFIG_FILE = 'sys.conf'
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
banner = 'Welcome to login the user info table'
try_times = 1
max_times = 4
operation_menu = ('add', 'delete', 'update', 'list', 'find', 'display', 'quit')
display_title = ['ID', 'name', 'age', 'tel', 'email']
warning_info = '''
[Error] You input wrong arguments for %s operation
[Error] Please check the instructions above and try again\n
'''


'''Function for user auth'''
def user_auth(user, password):
    user_return, Flag = load_config.LoadConfig(CONFIG_FILE, 'login_token')
    if not Flag:
        return user_return, False
    else:
        system_user_token = user_return
        if user == system_user_token['username'] and password == system_user_token['password']:
            auth_msg = '%s [INFO] Auth OK. Welcome to login in the user manage system' % timestamp
            auth_Flag =True
        else:
            auth_msg = '%s [Error] You input wrong username or password, please check and try again' % timestamp
            auth_Flag = False
        return  auth_msg, auth_Flag


'''Function for connect database'''
def db_connect():
    db_return, Flag = load_config.LoadConfig(CONFIG_FILE, 'db')
    if not Flag:
        return db_return
    try:
        db_config = db_return
        # print(db_config)
        conn = pymysql.connect(
            host = db_config['host'],
            user = db_config['user'],
            password = db_config['password'],
            database = db_config['database'],
            port = int(db_config['port'])
        )
        db_connect_flag = True
        return conn, db_connect_flag
    except Exception as e:
        db_connect_message = e
        db_connect_flag = False
        return  db_connect_message, db_connect_flag


# '''Function for load user info from db to memory'''
# def load_user_info():
#     db_connect_return, Flag = db_connect()
#     if not Flag:
#         return db_connect_return, Flag
#     else:
#         db_conn = db_connect_return
#         cursor = db_conn.cursor()
#         select_sql = 'select * from users;'
#         cursor.execute(select_sql)
#         db_conn.commit()
#         user_info = cursor.fetchall()  #return tuple type
#         cursor.close()
#         db_conn.close()
#         return  user_info, Flag


'''Function for select user info from db'''
def select_user(sql):
    db_connect_return, Flag = db_connect()
    if not Flag:
        return db_connect_return, Flag
    else:
        db_conn = db_connect_return
        cursor = db_conn.cursor()
        try:
            cursor.execute(sql)
            db_conn.commit()
            user_info = cursor.fetchall()  #return tuple type
            select_msg = user_info
            Flag = True

        except Exception as e:
            select_msg = e
            Flag = False
        finally:
            cursor.close()
            db_conn.close()
        return  select_msg, Flag


'''Function for add new user'''
def add_user(input_info):
    if len(input_info) == 5:
        username = input_info[1]
        age = input_info[2]
        tel = input_info[3]
        email = input_info[4]

        '''check if the user to be added existed or not'''
        sql = "select * from  users where username='%s';" % username
        select_return, Flag = select_user(sql)
        if not Flag:
            return select_return
        else:
            '''The user has existed already if the return is not Null'''
            if len(select_return):
                add_user_msg = '%s [Error] Sorry, the user [%s] you input existed already, please check and try input another as the user should be unique.' % (timestamp, username)
                add_user_flag = False
                return  add_user_msg, add_user_flag
            db_connect_return, Flag = db_connect()
            if not Flag:
                return db_connect_return, Flag
            else:
                db_conn = db_connect_return
                cursor = db_conn.cursor()
                insert_sql = "insert into users(username, age, tel, email) values('%s', %s, '%s', '%s');" % (username, age, tel, email)
                try:
                    cursor.execute(insert_sql)
                    db_conn.commit()
                    add_user_msg = '%s [INFO] Add user [%s] OK.' % (timestamp, username)
                    add_user_flag = True
                except Exception as e:
                    add_user_msg = e
                    add_user_flag = False
                finally:
                    cursor.close()
                    db_conn.close()
    else:
        add_user_msg = warning_info % 'add'
        add_user_flag = False
    return add_user_msg, add_user_flag


'''Function for delete user'''
def delete_user(input_info):
    if len(input_info) == 2:
        username = input_info[1]
        db_connect_return, Flag = db_connect()
        if not Flag:
            return db_connect_return, Flag
        else:
            db_conn = db_connect_return
            cursor = db_conn.cursor()
            delete_sql = "delete from users where username='%s';" % username
            try:
                cursor.execute(delete_sql)
                # print(cursor.rowcount)
                if cursor.rowcount == 0:
                    delete_user_msg = '%s [ERROR] Delete the user [%s] failed due to can not find it. Please check and try again.' % (timestamp, username)
                    delete_flag = False
                else:
                    db_conn.commit()
                    delete_user_msg = '%s [INFO] Delete the user [%s] OK.' % (timestamp, username)
                    delete_flag = True
            except Exception as e:
                db_conn.rollback()
                delete_user_msg = e
                delete_flag = False
                # return e, False
            finally:
                cursor.close()
                db_conn.close()
                return delete_user_msg, delete_flag
    else:
        delete_user_msg = warning_info % 'delete'
        delete_flag = False
    return delete_user_msg, delete_flag


'''Function for update user info'''
def update_user(input_info):
    if len(input_info) == 6:
        db_connect_return, Flag = db_connect()
        if not Flag:
            return db_connect_return, Flag
        else:
            username = input_info[1]
            update_filed = input_info[3]
            updated_value = input_info[5]
            db_conn = db_connect_return
            cursor = db_conn.cursor()
            update_sql = "update users set %s='%s' where username='%s';" % (update_filed, updated_value, username)
            try:
                cursor.execute(update_sql)
                if cursor.rowcount == 0:
                    update_user_msg = '%s [ERROR] Update the user [%s] to set the value of column [%s] to value [%s] failed.' % (timestamp, username, update_filed, updated_value)
                    update_flag = False
                db_conn.commit()
                update_user_msg = '%s [ERROR] Update the user [%s] to set the value of column [%s] to value [%s] OK.' % (timestamp, username, update_filed, updated_value)
                update_flag = True
            except Exception as e:
                update_user_msg = e
                update_flag = False
            finally:
                cursor.close()
                db_conn.close()
    else:
        update_user_msg = warning_info % 'update'
        update_flag = False
    return update_user_msg, update_flag


'''Function for list all the users'''
def list_user(input_info):
    if len(input_info) == 1:
        list_sql = "select * from users;"
        list_user_msg, Flag = select_user(list_sql)
        if not Flag:
            return list_user_msg
        list_user_info = sorted(list_user_msg)
        if not len(list_user_info):
            list_user_msg = '%s [ERROR] Sorry, there is no any user in the system now, you need to add one first.' % timestamp
            list_flag = False
        else:
            xt = PrettyTable()
            xt.field_names = display_title
            for entry in list_user_info:
                xt.add_row(entry)
            list_user_msg = xt
            list_flag = True
    else:
        list_user_msg = warning_info % 'list'
        list_flag = False
    return list_user_msg, list_flag


'''Function for find user'''
def find_user(input_info):
    if len(input_info) == 2:
        username = input_info[1]
        find_user_sql = "select * from users where username='%s';" % username
        find_user_msg, Flag = select_user(find_user_sql)
        if not Flag:
            return find_user_msg
        find_user_info = find_user_msg
        if not len(find_user_info):
            find_user_message = '%s [ERROR] The user [%s] you input can not be found in the system.' % (timestamp, username)
            find_flag = False
        else:
            xt = PrettyTable()
            xt.field_names = display_title
            xt.add_row(find_user_info[0])
            find_user_message = xt
            find_flag = True
    else:
        find_user_message = warning_info % 'find'
        find_flag = False
    return find_user_message, find_flag


'''Function for display'''
# display page 1 pagesize 5 
# display page 1（with default pagesize 5）
def display_user(input_info):
    default_pagesize = 5
    default_pagesize_flag = 0
    input_valid_flag = False
    if len(input_info) == 5 and input_info[1] == 'page' and input_info[3] == 'pagesize':
        # get the value of pagesize 
        input_valid_flag = True
        pagesize_input = input_info[4]
        dict_pagesize = {'pagesize': pagesize_input}
    # in case the user input 'display page 2'
    elif len(input_info) == 3 and input_info[1] == 'page':
        input_valid_flag = True
        dict_pagesize = {}
        default_pagesize_flag = True
    else:
        display_message = warning_info % 'display'
        display_flag = False
    if input_valid_flag:
        select_sql = 'select * from users;'
        display_user_msg, Flag = select_user(select_sql)
        if not Flag:
            return  display_user_msg
        # get user info as type tuple
        user_database = sorted(display_user_msg)
        if not len(user_database):
            display_message = '%s [ERROR] Sorry, there is no any user in the system now, you need to add one first.' % timestamp
            display_flag = False
        else:
            try:
                page = int(input_info[2])
                # reset pagesize if input it 
                pagesize = int(dict_pagesize.get('pagesize', default_pagesize))
                # check it the page will be out of index or not
                if pagesize * (page - 1) < len(user_database):
                    xt = PrettyTable()
                    xt.field_names = display_title
                    if page * pagesize < len(user_database):
                        start_index = (page - 1) * pagesize
                        end_index = page * pagesize
                    # check if the length of user_database is smaller than pagesize * page
                    else:
                        start_index = (page - 1) * pagesize
                        end_index = len(user_database)
                    display_list_page = user_database[start_index:end_index]
                    for rows in display_list_page:
                        xt.add_row(rows)
                    print('\tPage: [%s]\t\t\tPagesize: [%s]' % (page, pagesize))
                    if default_pagesize_flag:
                        print('\t\tPagesize:%s by default\t' % (default_pagesize))
                    display_message = xt
                    display_flag = True
                else:
                    display_message = '[Error] There are only %s entries in the table in total, but the page [%s]  and pagesize [%s] you input are out of range!\n\n' % (len(user_database), page, pagesize)
                    display_flag = False
            except Exception as e:
                print(e)
                display_message = '[Error] You input the wrong arguments for display operation, both page and pagesize should be integer, please check and try again as below:'
                display_flag = False
    return display_message, display_flag


'''man function'''
def main():
    print(banner.center(40, '='))
    print()
    while try_times < max_times:
        user_input = input('Please input your login user:\t\t')
        password_input = input('Please input your password:\t\t')
        if user_auth(user_input, password_input):
            print('\nWelcome to login in the system, now you can input your command as below:\n')
            print("""
                  1. add      -- e.g: add Tom 18 132xxxxx tom@tom.com
                  2. delete   -- e.g: delete Tom 
                  3. update   -- e.g: update Tom set age = 18
                  4. list     -- e.g: list
                  5. find     -- e.g: find Tom
                  6. display  -- e.g: display page 1 pagesize 5 
                              -- e.g: display page 1（with default pagesize 5）
                  7. quit
            """)

            while True:
                command_input = input('Please input your operation now:\t\t').split()
                print('\n')
                if len(command_input) > 1 or len(command_input) == 1:
                    operation_input = command_input[0]
                else:
                    print('%s [Error] Wrong input for your operation, please check and try again' % timestamp)

                if operation_input not in operation_menu:
                    print('%s [ERROR] Sorry, you input wrong command, please check the instructions above and try again\n\n' % timestamp)
                elif operation_input == 'quit':
                    print('%s [INFO] You choose to quit, the system is exiting...' % timestamp)
                    sys.exit(0)
                else:
                    if operation_input == 'add':
                        result_message, Flag = add_user(command_input)
                        print(result_message)
                        print('\n\n')

                    if operation_input == 'delete':
                        result_message, Flag = delete_user(command_input)
                        print(result_message)
                        print('\n\n')

                    if operation_input == 'update':
                        result_message, Flag = update_user(command_input)
                        print(result_message)
                        print('\n\n')

                    if operation_input == 'list':
                        result_message, Flag = list_user(command_input)
                        print(result_message)
                        print('\n\n')

                    if operation_input == 'find':
                        result_message, Flag = find_user(command_input)
                        if Flag:
                            print("\nThe user [%s] was found now, and the info of it is shown below:\n" % command_input[1])
                        print(result_message)
                        print('\n\n')

                    if operation_input == 'display':
                        result_message, Flag = display_user(command_input)
                        print(result_message)
                        if Flag:
                            print('\n\n')
        else:
            print('[Error] You input wrong username of password, please check and try again!')
            try_times += 1
            print('\n')

'''begin'''
if __name__ == main():
    main()









