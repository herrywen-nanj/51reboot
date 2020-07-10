# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Maxwell'

import pymysql, datetime, sys
import configmgt
from prettytable import PrettyTable

'''
global variables
'''

CONFIG_FILE = 'sysctl.conf'
system_token = ('51reboot', '123456')
FIELDS = ['name', 'age', 'tel', 'email']
RESULT = {}
operation_menu = ('add', 'delete', 'update', 'list', 'find', 'display', 'quit')
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

banner = 'Welcome to login the user info table'
warning_info = '''
[Error] You input wrong arguments for %s operation
[Error] Please check the instructions above and try again\n
'''
welcome_message = """
     1. add      -- e.g: add Tom 18 132xxxxx tom@tom.com
     2. delete   -- e.g: delete Tom 
     3. update   -- e.g: update Tom set age = 18
     4. list     -- e.g: list
     5. find     -- e.g: find Tom
     6. display  -- e.g: display page 1 pagesize 5 
                 -- e.g: display page 1（with default pagesize 5）
     7. quit
     """

'''
Class for auth
'''


class Auth(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if self.username == system_token[0] and self.password == system_token[1]:
            login_Flag = 1
        else:
            login_Flag = 0
        return login_Flag

    def logout(self):
        sys.exit(0)


'''
class for DB
'''


class DB(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database


    def connect_db(self):
        db_return, Flag = configmgt.LoadConfig(CONFIG_FILE, 'db')
        if not Flag:
            print(db_return)
            return db_return
        try:
            db_config = db_return
            # print(db_config)
            conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=int(self.port)
            )
            db_connect_flag = True
            return conn, db_connect_flag
        except Exception as e:
            conn = e
            db_connect_flag = False
        return conn, db_connect_flag


    def insert(self, sql):
        db_connect_return, Flag = self.connect_db()
        if not Flag:
            return db_connect_return, Flag
        else:
            db_conn = db_connect_return
            cursor = db_conn.cursor()
            try:
                cursor.execute(sql)
                db_conn.commit()
                # insert should affect one row at the least if success
                if cursor.rowcount >= 1:
                    insert_message = '%s [INFO] Inserted [%s] rows into the database [%s].' % (
                    timestamp, cursor.rowcount, self.database)
                    insert_flag = True
            except Exception as e:
                insert_message = e
                insert_flag = False
            finally:
                cursor.close()
                db_conn.close()
            return insert_message, insert_flag


    def select(self, sql):
        db_connect_return, Flag = self.connect_db()
        if not Flag:
            print(db_connect_return)
            return db_connect_return, Flag
        else:
            db_conn = db_connect_return
            cursor = db_conn.cursor()
            try:
                cursor.execute(sql)
                db_conn.commit()
                user_info = cursor.fetchall()  # return tuple type
                select_msg = user_info
                Flag = True
                '''mark a flag if no result return when select'''
                if len(select_msg):
                    Row_Flag = True
                else:
                    Row_Flag = False

            except Exception as e:
                select_msg = e
                Flag = False
                Row_Flag = False
            finally:
                cursor.close()
                db_conn.close()
            return select_msg, Flag, Row_Flag

# method for truncate table in database
# for any operation to modify data, truncate the table and then insert all the entry
    def truncate(self, sql):
        if sql.split()[0] == 'truncate':
            db_connect_return, Flag = self.connect_db()
            if not Flag:
                print(db_connect_return)
                return db_connect_return, Flag
            else:
                db_conn = db_connect_return
                cursor = db_conn.cursor()
                try:
                    cursor.execute(sql)
                    db_conn.commit()
                    truncate_message = '[%s] [INFO] Reset db OK'
                    truncate_flag = True
                except Exception as e:
                    truncate_message = e
                    truncate_flag = False
                finally:
                    cursor.close()
                    db_conn.close()
        else:
            truncate_message = '%s [ERROR] Wrong input sql for truncate database, please check andtry again.' % (timestamp)
            truncate_flag = False
        return truncate_message, truncate_flag


'''
class for save data to database or load data from database
'''


class Persistence(object):
    table_name = '51reboot_users'
    def new_database_obj(self):
        db_config_return, Flag = configmgt.LoadConfig(CONFIG_FILE, 'db')
        if not Flag:
            print(db_config_return)
            return db_config_return, False
        db_config = db_config_return
        db_obj = DB(db_config['host'], db_config['port'], db_config['user'], db_config['password'], db_config['database'])
        return db_obj, True


    '''Save data means to truncate table in the database, and then insert the newest info into database from memory'''
    def save_data(self):
        db_obj_return, Flag = self.new_database_obj()
        if not Flag:
            print(db_obj_return)
            return db_obj_return, False
        else:
            # get the object for class DB
            db_obj = db_obj_return
            truncate_sql = "truncate %s;" % (self.table_name)
            #revoke method select for database object
            truncate_return, Flag = db_obj.truncate(truncate_sql)
            if not Flag:
                print(truncate_return)
                return truncate_return, False
            #insert into database  one entry by one from memory
            print(RESULT)
            for username, info in RESULT.items():
                field_string = ', '.join(FIELDS)
                value_string = "'%s', '%s', '%s', '%s'" % (info['name'], info['age'], info['tel'], info['email'] )
                insert_sql = '''insert into %s (%s) values (%s);''' % (self.table_name, field_string, value_string)
                print(insert_sql)
                insert_return, Flag = db_obj.insert(insert_sql)
                if not Flag:
                    print(insert_return)
                    return insert_return, False
                else:
                    save_data_msg = '%s [INFO] Save the current info to database OK' % timestamp
            return  save_data_msg, True


    def load_data(self):
        db_obj_return, Flag = self.new_database_obj()
        if not Flag:
            return db_obj_return, False
        else:
            # get the object for class DB
            db_obj = db_obj_return
            sql = "select %s from 51reboot_users;" % ', '.join(FIELDS)
            select_return, Flag, Row_Flag = db_obj.select(sql)
            if not Flag:
                return select_return, False
            # no result return when select
            elif not Row_Flag:
                load_data_msg = '%s [INFO] Sorry, thers is no any user info to load from the database.' % timestamp
                return load_data_msg, False
            else:
                global RESULT
                RESULT = { column[0]:{FIELDS[0]:column[0], FIELDS[1]:column[1], FIELDS[2]:column[2], FIELDS[3]:column[3]}
                           for column in select_return }
                return RESULT, True



'''
Class for user
'''


class User(object):
    '''
    add monkey1 12 132xxx monkey1@qq.com
    args = "monkey1 12 132xxx monkey1@qq.com"
    :return:
    '''
    def add(self, args):
        if len(args) == 4:
            username = args[0]
            if username in RESULT:
                add_msg = '%s [ERROR] The user [%s] exists in the system already, please check and try again due to it should be unique' % (timestamp, username)
                return  add_msg, False
            else:
                RESULT[username] = {
                    FIELDS[0]:args[0],
                    FIELDS[1]:args[1],
                    FIELDS[2]:args[2],
                    FIELDS[3]:args[3],
                }
                add_msg = '%s [INFO] Add user [%s] OK.' % (timestamp, username)
                return add_msg, True
        else:
            add_msg = warning_info % 'add'
            return add_msg, False


    '''
    delete monkey1 
    args = "monkey1"
    :return:
    '''
    def delete(self, args):
        if len(args) == 1:
            username = args[0]
            if RESULT.pop(username, None):
                delete_msg = '%s [INFO] Delete user [%s] OK.' % (timestamp, username)
                return  delete_msg, True
            else:
                delete_msg = '%s [ERROR] The user [%s] cant not be found in the system, please check and try again due to it should be unique' % (
                timestamp, username)
                return delete_msg, False
        else:
            delete_msg = warning_info % 'delete'
            return delete_msg, False


    '''
    update monkey1 set age = 20
    :param args: monkey1 set age = 20
    :return:
    '''
    def update(self, args):
        if len(args) == 5:
            set = args[1]
            set_flag = args[-2]
            if set != 'set' or set_flag != '=':
                update_msg = warning_info % 'update'
                return update_msg, False
            username = args[0]
            update_field = args[2]
            if update_field in FIELDS:
                if username in RESULT:
                    update_value = args[-1]
                    RESULT[username][update_field] = update_value
                    update_msg = '%s [INFO] Update the info [%s] to new value [%s] OK for user [%s].' % (
                        timestamp, update_field, update_value, username)
                    return  update_msg, True
                else:
                    update_msg = '[ERROR] The user [%s] you input can not be find in the system.' % (username)
                    return update_msg, False
            else:
                update_msg = '[ERROR] You can only update filed in %s, please check and try again!' % FIELDS
                return update_msg, False
        else:
            update_msg = warning_info % 'update'
            return update_msg, False


    '''
    find monkey1
    :param args: = monkey1
    :return:
    '''
    def find(self, args):
        if len(args) == 1:
            username = args[0]
            if username in RESULT:
                user_info = RESULT[username]
                xtb = PrettyTable()
                xtb.field_names = FIELDS
                xtb.add_row([user_info[x] for x in FIELDS])
                return xtb, True
            else:
                find_msg = '[ERROR] The user [%s] you input can not be find in the system.' % (username)
                return find_msg, False
        else:
            find_msg = warning_info % 'find'
            return find_msg, False

    '''
    list
    :param args: no args
    :return:
    '''
    def list(self, args):
        if len(args):
            list_msg = warning_info % 'list'
            return list_msg, False
        if len(RESULT):
            xtb = PrettyTable()
            xtb.field_names = FIELDS
            for k, v in RESULT.items():
                xtb.add_row(v.values())
            return xtb, True
        else:
            list_msg = '%s [ERROR] Sorry, there is no any user in the system now, you need to add one first.' % timestamp
            return list_msg, False



    '''
    display page 2 pagesize 5
    display page 2 
    :param args: page 2 pagesize 5 ;default pagesize = 5
    '''
    def display(self, args):
        default_pagesize = 5
        default_pagesize_flag = False
        if len(args) == 4 and args[0] == 'page' and args[2] == 'pagesize':
            pagesize_input = args[3]
            dict_pagesize = {'pagesize': pagesize_input}
            default_pagesize_flag = False
        elif len(args) == 2 and args[0] == 'page':
            default_pagesize_flag = True
            dict_pagesize = {}
            default_pagesize_flag = True
        else:
            display_msg = warning_info % 'display'
            return display_msg, False
        if len(RESULT):
            try:
                page = int(args[1])
                pagesize = int(dict_pagesize.get('pagesize', default_pagesize))
                userinfo_list = [ list(v.values()) for k, v in RESULT.items() ]
                if pagesize * (page - 1) < len(userinfo_list):
                    xtb = PrettyTable()
                    xtb.field_names = FIELDS
                    if page * pagesize < len(userinfo_list):
                        start_index = (page - 1) * pagesize
                        end_index = page * pagesize
                    # check if the length of user_database is smaller than pagesize * page
                    else:
                        start_index = (page - 1) * pagesize
                        end_index = len(userinfo_list)
                    display_list_page = userinfo_list[start_index:end_index]
                    for rows in display_list_page:
                        xtb.add_row(rows)
                    print('\tPage: [%s]\t\t\tPagesize: [%s]' % (page, pagesize))
                    if default_pagesize_flag:
                        print('\t\tPagesize:%s by default\t' % (default_pagesize))
                    display_message = xtb
                    return display_message, True
                else:
                    display_message = '[Error] There are only %s entries in the table in total, but the page [%s]  and pagesize [%s] you input are out of range!\n\n' % (
                    len(userinfo_list), page, pagesize)
                    return display_message, False
            except Exception as e:
                print(e)
                display_message = '[Error] You input the wrong arguments for display operation, both page and pagesize should be integer, please check and try again as below:'
                return display_message, False
        else:
            display_message = '%s [ERROR] Sorry, there is no any user in the system now, you need to add one first.' % timestamp
            return display_message, False





'''
main function
'''


def main():
    try_times = 1
    max_times = 4
    print(banner.center(40, '='))
    print()
    while try_times < max_times:
        user_input = input('Please input your login user:\t\t')
        password_input = input('Please input your password:\t\t')
        auth_obj = Auth(user_input, password_input)
        if auth_obj.login():
            print('\nWelcome to login in the system, now you can input your command as below:\n')
            print(welcome_message)
            # load db info into memory
            persistence_obj = Persistence()
            load_data_return, Flag = persistence_obj.load_data()
            # print('before : %s' % RESULT)
            # print return info when failed to load
            if not Flag:
                print(load_data_return)
            while True:
                command_input = input('Please input your operation now:\t\t').split()
                print('\n')
                if len(command_input) >= 1:
                    operation_input = command_input[0]
                    userinfo_string = command_input[1:]
                else:
                    print('%s [Error] Wrong input for your operation, please check and try again' % timestamp)

                if operation_input not in operation_menu:
                    print(
                        '%s [ERROR] Sorry, you input wrong command, please check the instructions above and try again\n\n' % timestamp)
                elif operation_input == 'quit':
                    print('%s [INFO] You choose to quit, the system is exiting...' % timestamp)
                    Auth(user_input, password_input).logout()
                else:
                    if operation_input == 'add':
                        addUser_return, Flag = User().add(userinfo_string)
                        if Flag:
                            # save to db
                            save_db_return, Flag = Persistence().save_data()
                            if not Flag:
                                print(save_db_return)
                        print(addUser_return)

                    if operation_input == 'delete':
                        deleteUser_return, Flag = User().delete(userinfo_string)
                        if Flag:
                            # save to db
                            save_db_return, Flag = Persistence().save_data()
                            if not Flag:
                                print(save_db_return)
                        print(deleteUser_return)

                    if operation_input == 'update':
                        update_return, Flag = User().update(userinfo_string)
                        if Flag:
                            # save to db
                            save_db_return, Flag = Persistence().save_data()
                            if not Flag:
                                print(save_db_return)
                        print(update_return)

                    if operation_input == 'find':
                        find_return, Flag = User().find(userinfo_string)
                        if Flag:
                            print("\nThe user [%s] was found now, and the info of it is shown below:\n" % userinfo_string[0])
                        print(find_return)

                    if operation_input == 'list':
                        list_return, Flag = User().list(userinfo_string)
                        print(list_return)
                        print('\n\n')

                    if operation_input == 'display':
                        display_return, Flag = User().display(userinfo_string)
                        print(display_return)
                        print('\n\n')

        else:
            print('[Error] You input wrong username of password, please check and try again!')
            try_times += 1
            print('\n')


if __name__ == '__main__':
    main()