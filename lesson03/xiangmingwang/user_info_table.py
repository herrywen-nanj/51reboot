# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Maxwell'


from prettytable import PrettyTable
from datetime import datetime
import sys,json,os,datetime

#系统全局变量
user_auth = ('51reboot', '123456')
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
default_pagesize_flag = 0
#默认分页显示条目数
default_pagesize = 5
#区分pagesize的情况，输入有效就重置它的值进入正常逻辑
page_size_flag = 2

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


print(banner.center(40, '='))
print()
while try_times < max_times:
    user_input = input('Please input your login user:\t\t')
    password_input = input('Please input your password:\t\t')
    if user_input == user_auth[0] and password_input == user_auth[1]:
        print('You can input your command as below:\n')
        print("""
              1. add  
                 -- description: to add a new user
                 -- command: add [user_name] [age] [tel] [email] 
                 -- e.g: add Tom 18 132xxxxx tom@tom.com
                 
              2. delete
                 -- description: to delete a user
                 -- command: delete [user_name] e.g: delete Tom
                 -- e.g: delete Tom 
                 
              3. update
                 -- description: to update field in age, tel or email for a specific user
                 -- command: update [user_name] [set]  [age|tel|email] = [new_value]
                 -- e.g: update Tom set age = 18
                 
              4. list
                 -- description: to list all the current users
                 -- command: list
                 
              5. find
                 -- description: to verify a certain user exists or not
                 -- command: find [user_name]  
                 -- e.g: find Tom
                 
              6. display
                 -- description: to display all the users one page with specific rows at a time
                 -- command: display page [page_number] pagesize [pagesize]  
                 -- e.g: display page 1 pagesize 5 
                 -- e.g: display page 1（with default pagesize 5）
              
              7. quit
                 -- description: to quit the system
                 -- command: quit 
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
                if os.path.exists(db_file) and os.path.isfile(db_file): #load db file if exists already
                    with open(db_file, 'r', encoding='utf-8') as f:
                        user_database = json.loads(f.read())  #load user_info saved before

                else:
                    pass

                if operation_input == 'add':
                    if len(command_input) == 5:
                        user = command_input[1]
                        if user not in user_database:
                            user_info['age'] = command_input[2]
                            user_info['tel'] = command_input[3]
                            user_info['email'] = command_input[4]
                            user_database[user] = user_info
                            with open(db_file, 'w', encoding='utf-8') as f: #save new user info
                                f.write(json.dumps(user_database))
                            # 记录修改日志
                            log_info = '%s [Info] Delete user [%s] successfully.\n' % (timestamp, user)
                            with open(log_file, 'a', encoding='utf-8') as f:
                                f.write(log_info)
                            print('%s [Info] Add user [%s] successfully\n' % (timestamp, user))
                        else:
                            print('[Error] The user [%s] you want to add exists already, you can not to add it for 2 times\n' % user)
                    else:
                        print(warning_info % operation_input)

                if operation_input == 'delete':
                    if len(command_input) == 2:
                        user = command_input[1]
                        if user in user_database.keys():
                            user_database.pop(user)
                            with open(db_file, 'w', encoding='utf-8') as f:  # save deleted user info
                                f.write(json.dumps(user_database))
                            #记录修改日志
                            log_info = '%s [Info] Delete user [%s] successfully.\n' % (timestamp, user)
                            with open(log_file, 'a', encoding='utf-8') as f:
                                f.write(log_info)
                            print('%s [Info] Delete user [%s] successfully\n' % (timestamp, command_input[1]))

                        else:
                            print('[Error] The user [%s] can not be found in the system\n\n' % user)
                    else:
                        print(warning_info % operation_input)

                if operation_input == 'update':
                    if len(command_input) == 6:
                        user = command_input[1]
                        if user in user_database.keys():
                            # 判断update的字段是否在'age', 'phone_no', 'email'中
                            if command_input[3] in user_arg:
                                update_filed = command_input[3]
                                updated_value = command_input[5]
                                user_database[user][update_filed] = updated_value
                                with open(db_file, 'w', encoding='utf-8') as f:  # save new user info
                                    f.write(json.dumps(user_database))
                                # 记录修改日志
                                log_info = '%s [Info] Update user [%s] for column [%s]  to new value [%s] successfully.\n' % (timestamp, user, update_filed, updated_value)
                                with open(log_file, 'a', encoding='utf-8') as f:
                                    f.write(log_info)
                                print('%s [Info] Update user [%s] successfully\n\n' % (timestamp,command_input[1]))
                            else:
                                print('[Error] You can only update field in %s \n\n' % user_arg)
                        else:
                            print('[Error] The user [%s] can not be found in the system\n\n' % user)

                    else:
                        print(warning_info % operation_input)

                if operation_input == 'list':
                    if len(command_input) == 1:
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
                            print(x)
                            print('\n%s rows in total\n' % len(user_database))
                        else:
                            print('[Info] Sorry, no user can not be found in the system, you need to add one...\n\n')
                    else:
                        print(warning_info % operation_input)

                if operation_input == 'find':
                    if len(command_input) == 2:
                        user = command_input[1]
                        if user in user_database.keys():
                            print('%s [Info] The user [%s] you find exists in the system, and the info of it is as shown below:\n' % (timestamp, user))
                            x = PrettyTable()
                            x.field_names = display_title
                            display_list = []
                            display_list.append(user)
                            display_list.append(user_database[user]['age'])
                            display_list.append(user_database[user]['tel'])
                            display_list.append(user_database[user]['email'])
                            x.add_row(display_list)
                            print(x)
                            print('\n\n')
                        else:
                            print('[Info] Sorry, the user [%s] you find can not be found in the system.\n\n' % user)
                    else:
                        print(warning_info % operation_input)

                if operation_input == 'display':
                    if len(command_input) == 5 and command_input[1] == 'page' and command_input[3] == 'pagesize':
                        #区分pagesize的值
                        page_size_flag = 1
                        pagesize_input = command_input[4]
                        dict_pagesize = {'pagesize' : pagesize_input}
                    #省略输入pagesize的情况，如display page 2
                    elif len(command_input) == 3 and command_input[1] == 'page':
                        page_size_flag = 0
                        dict_pagesize = {}
                        default_pagesize_flag = 1
                        # # # 默认分页后每页显示5条
                        # default_pagesize = 5
                    else:
                        print(warning_info % operation_input)
                    #输入有效情况下的逻辑
                    if page_size_flag == 1 or page_size_flag == 0:
                        if len(user_database):
                            #确认page和pagesize的输入值是否为有效整数，异常处理
                            try:
                                page = int(command_input[2])
                                #如果有显式输入pagesize，则套用输入值，否则用默认值5
                                pagesize = int(dict_pagesize.get('pagesize', default_pagesize))
                                #判断要输出显示的范围是否越界，如只有12条记录，要求每页输出7条，显示第3页
                                if  pagesize * (page - 1)  < len(user_database):
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
                                    print('\tPage: [%s]\t\t\tPagesize: [%s]' %(page, pagesize))
                                    if default_pagesize_flag:
                                        print('\t\tPagesize:%s by default\t' %(default_pagesize))
                                    print(x)
                                    print('\n\n')
                                else:
                                    print('[Error] There are only %s entries in the table in total, but the page [%s]  and  pagesize [%s] you input are out of range!\n\n' %(len(user_database), page, pagesize))
                            except Exception as e:
                                print(e)
                                print('[Error] You input the wrong arguments for display operation, both page and pagesize should be integer, please check and try again as below:')
                        else:
                            print('[Info] Sorry, no user can not be found in the system, you need to add one...\n\n')
    else:
        try_times += 1

print('\n\n[Error]You input wrong username or password for three times, the system is exiting for secure...')