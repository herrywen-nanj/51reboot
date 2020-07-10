# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Maxwell'


from prettytable import PrettyTable
from datetime import datetime
import sys,json,os,datetime

#系统全局变量
user_auth_info = ('51reboot', '123456')
try_times = 1
max_times = 4
# 定义的可以操作的菜单选项类型
operation_menu = ('add', 'delete', 'update', 'list', 'find', 'display', 'quit')

# 用户信息完整字典，持久化保存的对象
user_database = {}
# 用户信息子字典，key是age, tel, email
user_info = {}
#properties for user
# 用户的信息属性
user_arg = ['age', 'tel', 'email']
# 定义格式化输出的title
display_title = ['name', 'age', 'tel', 'email']
#获取pagesize的字典，便于用get方法取pagesize的值或赋值默认值
dict_pagesize = {}
#标记是否用默认的pagesize
# default_pagesize_flag = 0
#默认分页显示条目数
default_pagesize = 5

# 持久化保存的文件和日志
db_file = 'db.txt'
log_file = 'user_info.log'

#登陆系统欢迎信息
banner = 'Welcome to login the user info table'
#为每种操作输入错误之后打印的统一提示信息, %s替换成对应的操作类型即可
warning_info = '''
[Error] You input wrong arguments for %s operation
[Error] Please check the instructions above and try again\n
'''
#时间戳，精确到毫秒
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]



#function
##
def load_data(file, database):
    if os.path.exists(file) and os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as f:
            database = json.loads(f.read())
        return  database


def save_data(file, database):
    with open(file, 'w', encoding='utf-8') as f:  # save new user info
        f.write(json.dumps(database))


def user_auth(user, password):
    if user == user_auth_info[0] and password == user_auth_info[1]:
        return True
    else:
        return False


'''function for add operation'''
def add_user(input_info):
    if len(input_info) == 5:
        user = input_info[1]
        if user not in user_database:
            user_info['age'] = input_info[2]
            user_info['tel'] = input_info[3]
            user_info['email'] = input_info[4]
            user_database[user] = user_info
            add_message = "%s [Info] Add user [%s] successfully\n" % (timestamp, user)
            add_flag = True
        else:
            add_message = "[Error] The user [%s] you want to add exists already, you can not to add it for 2 times\n" % user
            add_flag = False
    else:
        add_message = warning_info % 'add'
        add_flag = False
    return add_message, add_flag


'''function for delete operation'''
def delete_user(input_info):
    if len(input_info) == 2:
        user = input_info[1]
        if user in user_database.keys():
            user_database.pop(user)
            del_message = "%s [Info] Delete user [%s] successfully\n" % (timestamp, user)
            del_flag = True
        else:
            del_message = "[Error] The user [%s] can not be found in the system\n\n'" % user
            del_flag = False
    else:
        del_message =warning_info % 'delete'
        del_flag = False
    return  del_message, del_flag


'''function for update operation'''
def update_user(input_info):
    if len(input_info) == 6:
        user = input_info[1]
        if user in user_database.keys():
            # 判断update的字段是否在'age', 'phone_no', 'email'中
            if input_info[3] in user_arg:
                update_filed = input_info[3]
                updated_value = input_info[5]
                user_database[user][update_filed] = updated_value
                update_message = "%s [Info] Update user [%s] for column [%s]  to new value [%s]\n" % (timestamp, user, update_filed, updated_value)
                update_flag = True
            else:
                update_message = "[Error] You can only update field in %s \n\n" % user_arg
                update_flag = False
        else:
            update_message = "[Error] The user [%s] can not be found in the system\n\n'" % user
            update_flag = False
    else:
        update_message = warning_info % 'update'
        update_flag = False
    return  update_message, update_flag


'''function for find operation'''
def find_user(input_info):
    if len(input_info) == 2:
        user = input_info[1]
        if user in user_database.keys():
            print('%s [Info] The user [%s] you find exists in the system, and the info of it is as shown below:\n' % (
            timestamp, user))
            x = PrettyTable()
            x.field_names = display_title
            display_list = []
            display_list.append(user)
            display_list.append(user_database[user]['age'])
            display_list.append(user_database[user]['tel'])
            display_list.append(user_database[user]['email'])
            x.add_row(display_list)
            find_message = x
            find_flag = True
            return  find_message, find_flag
        else:
            find_message = "[Info] Sorry, the user [%s] you find can not be found in the system.\n\n" % user
            find_flag = False
    else:
        find_message = warning_info % 'find'
        find_flag = False
    return find_message, find_flag


'''function for list operation'''
def list_user(input_info):
    if len(input_info) == 1:
        if len(user_database):
            x = PrettyTable()
            x.field_names = display_title
            for username in user_database.keys():
                display_list = []
                display_list.append(username)
                display_list.append(user_database[username]['age'])
                display_list.append(user_database[username]['tel'])
                display_list.append(user_database[username]['email'])
                x.add_row(display_list)
            list_message = x
            list_flag = True
        else:
            list_message = ""
            list_flag = Flase
    else:
        list_message = warning_info % 'list'
        list_flag = False
    return  list_message, list_flag


'''
function for display
'''
def display_user(input_info):
    default_pagesize = 5
    default_pagesize_flag = 0
    input_valid_flag = 0
    if len(input_info) == 5 and input_info[1] == 'page' and input_info[3] == 'pagesize':
        # 区分pagesize的值
        input_valid_flag = 1
        pagesize_input = input_info[4]
        dict_pagesize = {'pagesize': pagesize_input}
    # 省略输入pagesize的情况，如display page 2
    elif len(input_info) == 3 and input_info[1] == 'page':
        input_valid_flag = 1
        dict_pagesize = {}
        default_pagesize_flag = 1
    else:
        display_message = warning_info % 'display'
        display_flag = False
    # 输入有效情况下的逻辑
    if input_valid_flag:
        if len(user_database):
            # 确认page和pagesize的输入值是否为有效整数，异常处理
            try:
                page = int(input_info[2])
                # 如果有显式输入pagesize，则套用输入值，否则用默认值5
                pagesize = int(dict_pagesize.get('pagesize', default_pagesize))
                # 判断要输出显示的范围是否越界，如只有12条记录，要求每页输出7条，显示第3页
                if pagesize * (page - 1) < len(user_database):
                    x = PrettyTable()
                    x.field_names = display_title
                    display_list = []
                    # 把当前字典信息中的元素，追加到列表中，便于PrettyTable格式化输出
                    for username in user_database.keys():
                        display_list_entry = []
                        display_list_entry.append(username)
                        display_list_entry.append(user_database[username]['age'])
                        display_list_entry.append(user_database[username]['tel'])
                        display_list_entry.append(user_database[username]['email'])
                        display_list.append(display_list_entry)
                    # 处理当前分页实际可显示的条目数为pagesize的情况
                    if page * pagesize < len(user_database):
                        start_index = (page - 1) * pagesize
                        end_index = page * pagesize
                    # 处理当前分页中实际可以显示的条目数小于pagesize的情况，如12条记录，page=3， pagesize=5的情况
                    else:
                        start_index = (page - 1) * pagesize
                        end_index = len(display_list)
                    # 最终版分页显示列表开始切片
                    display_list_page = display_list[start_index:end_index]
                    for rows in display_list_page:
                        x.add_row(rows)
                    print('\tPage: [%s]\t\t\tPagesize: [%s]' % (page, pagesize))
                    if default_pagesize_flag:
                        print('\t\tPagesize:%s by default\t' % (default_pagesize))
                    display_message = x
                    display_flag = True
                else:
                    display_message = '[Error] There are only %s entries in the table in total, but the page [%s]  and pagesize [%s] you input are out of range!\n\n' % (len(user_database), page, pagesize)
                    display_flag = False
            except Exception as e:
                print(e)
                display_message = '[Error] You input the wrong arguments for display operation, both page and pagesize\n should be integer, please check and try again as below:'
                display_flag = False
        else:
            display_message = '[Info] Sorry, no user can not be found in the system, you need to add one...\n\n'
            display_flag = False
    return display_message, display_flag

'''
main function
'''
print(banner.center(40, '='))
print()
while try_times < max_times:
    user_input = input('Please input your login user:\t\t')
    password_input = input('Please input your password:\t\t')
    if user_auth(user_input, password_input):
        print('Welcome to login in the system, now you can input your command as below:\n')
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
                print('[Error] Wrong input for your operation, please check and try again')

            if operation_input not in operation_menu:
                print('[Error] Sorry, you input wrong command, please check the instructions above and try again\n\n')
            elif operation_input == 'quit':
                print('[Info] You choose to quit, the system is exiting...')
                sys.exit(0)
            else:
                user_database = load_data(db_file, user_database)

                if operation_input == 'add':
                    result_message, Flag = add_user(command_input)
                    print(result_message)
                    # 处理成功则持久化保存
                    if Flag:
                        save_data(db_file, user_database)

                if operation_input == 'delete':
                    result_message, Flag = delete_user(command_input)
                    print(result_message)
                    # 处理成功则持久化保存
                    if Flag:
                        save_data(db_file, user_database)

                if operation_input == 'update':
                    result_message, Flag = update_user(command_input)
                    print(result_message)
                    # 处理成功则持久化保存
                    if Flag:
                        save_data(db_file, user_database)

                if operation_input == 'list':
                    result_message, Flag = list_user(command_input)
                    print(result_message)
                    if Flag:
                            print('\n%s rows in total\n' % len(user_database))

                if operation_input == 'find':
                    result_message, Flag = find_user(command_input)
                    print(result_message)
                    if Flag:
                        print('\n')

                if operation_input == 'display':
                    result_message, Flag = display_user(command_input)
                    print(result_message)
                    if Flag:
                        print('\n\n')

    else:
        print('[Error] You input wrong username of password, please check and try again!')
        try_times += 1
        print('\n')

print('\n\n[Error]You input wrong username or password for three times, the system is exiting for secure...')