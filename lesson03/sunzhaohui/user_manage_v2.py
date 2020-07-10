import time
import csv
import sys
import json
from prettytable import PrettyTable


# 定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("51reboot", "123456")
USER_DATA_FILE = 'user_data.txt'
FIELD_NAMES = ['id','username', 'age', 'tel', 'email']
help_info = '''
        帮助信息:
        有效字段依次顺序: 'username', 'age', 'tel', 'email'
        增加:  add monkey 12 13200000001 monkey@51reboot.com
        删除: 
           - delete monkey 
           - delete 1 
        修改: 
           - update monkey set age = 18
           - update monkey set tel = 13200000002
           - update monkey set email = xxx@51reboot.com
        列出: list
        查找: find monkey (用户名模糊查询)
        保存: save
        加载: load
        分页： 
            - display page 2 pagesize 5
            - display page 2
        导出: export
        退出: exit
        '''


while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ").strip()
    password = input("Please input your password: ").strip()
    if username == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        print('\033[0;32;0m 登录成功!\033[0m')
        print(help_info)
        try:
            f = open(USER_DATA_FILE,'r')
            data = f.read()
            user_data_dict = json.loads(data)
        except:
            user_data_dict = {}
        finally:
            f.close()
        while True:
            # 业务逻辑
            info = input("Please input your operation: ")
            #如果输入为空，跳入下次循环
            if info == '':
                continue
            # string -> list
            info_list = info.split()

            # print(info)
            # print(info_list)
            action = info_list[0]

            if action == "add":
                #判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
                username = info_list[1]
                #判断用户是否在字典里 add monkey 12 132xxx monkey@51reboot.com

                if username in user_data_dict:
                    print('\033[0;35;0m用户已存在,不可以添加\033[0m')
                    continue
                else:
                    username_info_dict = {}
                    username_info_dict['age'] = info_list[2]
                    username_info_dict['tel'] = info_list[3]
                    username_info_dict['email'] = info_list[4]
                    user_data_dict[username] = username_info_dict
                    # 打印结果信息
                    print("\033[0;32;0m Add {} succ.\033[0m".format(info_list[1]))

                    #添加后自动保存
                    try:
                        f = open(USER_DATA_FILE,'w')
                        data = json.dumps(user_data_dict)
                        f.write(data)
                    except:
                        print('{} 不可写，保存失败'.format(USER_DATA_FILE))
                    finally:
                        f.close()
            elif action == "delete":
                #获取输入的可能是用户或id
                username_or_id = info_list[1]
                #我觉得有必要先读取用户数据
                try:
                    f = open(USER_DATA_FILE, 'r')
                    data = f.read()
                    user_data_dict = json.loads(data)
                except:
                    user_data_dict = {}
                finally:
                    f.close()
                # 尝试输入的是不是整数，则认为根据id删除
                if username_or_id.isdigit():
                    id = int(username_or_id)
                    #临时得到用户列表
                    username_list = []
                    for username in user_data_dict:
                        username_list.append(username)
                    try:
                        username = username_list[id - 1]

                        del user_data_dict[username]
                        print('\033[0;32;0m id 为{} 的用户 {} 已删除\033[0m'.format(id,username))
                    except:
                        print('没有id 为 {} 的用户'.format(id))
                else:
                    #否则认为是根据用户名删除
                    username = username_or_id

                    #判断输入的用户名是否在列表里
                    if username not in user_data_dict:
                        print('没有这个用户\033[0;35;0m{}\033[0m'.format(username))
                        continue
                    else:
                        del user_data_dict[username]
                        print('\033[0;32;0m已删除{}\033[0m'.format(username))
                        #删除后自动保存
                try:
                    f = open(USER_DATA_FILE,'w')
                    data = json.dumps(user_data_dict)
                    f.write(data)
                except:
                    print('{} 不可写，保存失败'.format(USER_DATA_FILE))
                finally:
                    f.close()


            elif action == "update":
                # update monkey set age = 18

                #重新分割输入的信息，最大分割3个

                info_list = info.split(maxsplit=3)
                try:
                    username = info_list[1]
                except:
                    print('提供信息不足，请重新输入')
                    print('例如: update monkey set age = 18')
                    continue
                #判断是否有关键字
                if 'set' not in info_list:
                    print('语法错误缺少关键字 set')
                    print('例如: update monkey set age = 18')
                    continue
                #把输入的key 和 value 单独赋值
                try:
                    user_filed_value = info_list[3].strip()
                    if user_filed_value.startswith('='):
                        print('= 等号左边缺少键')
                        print('例如: update monkey set age = 18')
                        continue
                    elif user_filed_value.endswith('='):
                        print('= 等号右边缺少值')
                        print('例如: update monkey set age = 18')
                        continue

                except:
                    print('提供信息不足，请重新输入')
                    print('例如: update monkey set age = 18')

                if '=' not in user_filed_value:
                    print('语法错误缺少关键字 =')
                    print('例如: update monkey set age = 18')
                    continue


                #再把输入的key 和 value 分割提取

                user_filed = user_filed_value.split('=')[0].strip()

                new_value = user_filed_value.split('=')[1].strip()
                if user_filed == 'id' or user_filed == 'username':
                    print('用户字段{} 不能修改'.format(user_filed))
                    continue
                elif user_filed == 'age':
                    if new_value.isdigit():
                        pass
                    else:
                        print('字段{} 必须是整数'.format(user_filed))
                        continue
                elif user_filed == 'tel':
                    if new_value.isdigit():
                        pass
                    else:
                        print('字段{} 必须是整数'.format(user_filed))
                        continue
                elif user_filed == 'email':
                    if '@' in new_value and new_value.endswith('.com') and not new_value.startswith('@'):
                        pass
                    else:
                        print('邮箱格式不合法')
                        continue
                else:
                    print('没有该字段 {}'.format(user_filed))
                    continue

                #我觉得有必要先读取用户数据
                try:
                    f = open(USER_DATA_FILE, 'r')
                    data = f.read()
                    user_data_dict = json.loads(data)
                except:
                    user_data_dict = {}
                finally:
                    f.close()

                #判断用户是否存在
                if username in user_data_dict:
                    old_value = user_data_dict[username][user_filed]
                    user_data_dict[username][user_filed] = new_value
                    print('用户 {} 的字段 {} 值 已由 \033[0;32;0m{}\033[0m 改为 \033[0;35;0m{}\33[0m'.format(username, user_filed,old_value,new_value))

                    #修改后自动保存
                    try:
                        f = open(USER_DATA_FILE,'w')
                        data = json.dumps(user_data_dict)
                        f.write(data)
                    except:
                        print('{} 不可写，保存失败'.format(USER_DATA_FILE))
                    finally:
                        f.close()

                else:
                    print('用户 {} 不存在'.format(username))

            elif action == "list":
                #读取文件数据
                try:
                    f = open(USER_DATA_FILE, 'r')
                    data = f.read()
                    user_data_dict = json.loads(data)

                except:
                    user_data_dict = {}
                finally:
                    f.close()
                x = PrettyTable()
                x.field_names = FIELD_NAMES

                id = 1
                for username in user_data_dict:
                    try:
                        #以用户名的 value 格式字典
                        username_dict = user_data_dict[username]
                        user_row = [id,username,username_dict['age'],username_dict['tel'],username_dict['email']]
                        x.add_row(user_row)
                        id = id + 1
                    except:
                        pass

                print(x)



            elif action == "find":


                #获取要查找的用户名
                if len(info_list) == 2:
                    pass
                else:
                    print('输入信息格式不正确')
                    print('例如:find monkey')
                    continue
                #我觉得有必要先读取用户数据
                try:
                    f = open(USER_DATA_FILE, 'r')
                    data = f.read()
                    user_data_dict = json.loads(data)
                except:
                    user_data_dict = {}
                finally:
                    f.close()

                username_list = []
                #找出所有用户的加入临时列表
                for username_tmp in user_data_dict:
                    username_list.append(username_tmp)
                x = PrettyTable()
                x.field_names = FIELD_NAMES
                username = info_list[1].strip()

                for user_name in username_list:
                    if username in user_name:
                        id = username_list.index(user_name) + 1
                        age = user_data_dict[user_name]['age']
                        tel = user_data_dict[user_name]['tel']
                        email = user_data_dict[user_name]['email']
                        x.add_row([id,user_name,age,tel,email])

                print(x)
            elif action == 'save':
                try:
                    f = open(USER_DATA_FILE, 'w')
                    data = json.dumps(user_data_dict)
                    f.write(data)
                    print('\033[0;32;0m用户信息已保存\033[0m')

                except:
                    print('{} 不可写，保存失败'.format(USER_DATA_FILE))
                finally:
                    f.close()

            elif action == 'load':
                try:
                    f = open(USER_DATA_FILE, 'r')
                    data = f.read()
                    user_data_dict = json.loads(data)
                    print('\033[0;32;0m用户信息已读取\033[0m')
                except:
                    user_data_dict = {}
                finally:
                    f.close()
            elif action == 'display':
                #dispaly page 2 pagesize 5
                info_list = info.split()
                if 'page' not in info_list:
                    print('缺少关键字 page')
                    continue
                try:
                    page = int(info_list[2])
                except:
                    page = 1
                try:
                    pagesize = int(info_list[4])
                except:
                    pagesize = 5
                #读取用户信息
                try:
                    f = open(USER_DATA_FILE, 'r')
                    data = f.read()
                    user_data_dict = json.loads(data)

                except:
                    user_data_dict = {}
                finally:
                    f.close()

                username_list = []
                #找出所有用户的加入临时列表
                for username_tmp in user_data_dict:
                    username_list.append(username_tmp)
                x = PrettyTable()
                user_list = []
                x.field_names = FIELD_NAMES
                #username_number = len(username_list)

                for user_name in username_list:
                    id = username_list.index(user_name)+1
                    age = user_data_dict[user_name]['age']
                    tel = user_data_dict[user_name]['tel']
                    email = user_data_dict[user_name]['email']
                    user_single_list = [id,user_name,age,tel,email]
                    user_list.append(user_single_list)

                all_page_list = []
                i = 1
                #遍历所有用户单条信息，如果整除pagesize 那么就加入到下一页，如果最后没整除且已到最后一条，加入单独一页
                user_page_list = []
                for user_single_list in user_list:
                    user_page_list.append(user_single_list)
                    if i % pagesize == 0:
                        all_page_list.append(user_page_list)
                        user_page_list = []
                    elif i == len(user_list):
                        all_page_list.append(user_page_list)
                    i += 1
                if page > len(all_page_list) or page < 1:
                    print('没有 {} 页,共{}页'.format(page,len(all_page_list)))
                    continue
                display_page_list = all_page_list[page-1]

                for user in display_page_list:
                    x.add_row(user)
                print('第\033[0;32;0m{}\033[0m页，共\033[0;32;0m{}\033[0m页'.format(page,len(all_page_list)))

                print(x)
            elif action == 'export':
                #读取用户信息
                try:
                    f = open(USER_DATA_FILE, 'r')
                    data = f.read()
                    user_data_dict = json.loads(data)

                except:
                    user_data_dict = {}
                finally:
                    f.close()

                username_list = []
                #找出所有用户的加入临时列表
                for username_tmp in user_data_dict:
                    username_list.append(username_tmp)
                x = PrettyTable()
                user_list = []
                x.field_names = FIELD_NAMES
                #username_number = len(username_list)

                for user_name in username_list:
                    id = username_list.index(user_name)+1
                    age = user_data_dict[user_name]['age']
                    tel = user_data_dict[user_name]['tel']
                    email = user_data_dict[user_name]['email']
                    user_single_list = [id,user_name,age,tel,email]
                    user_list.append(user_single_list)
                time_str = time.strftime('%Y%m%d%H%M%S')
                csv_filename = USER_DATA_FILE.split('.')[0]+'_'+time_str+'.csv'
                try:
                    f = open(csv_filename,"w")
                    writer = csv.writer(f)
                    writer.writerow(FIELD_NAMES)
                    for row in user_list:
                        writer.writerow(row)
                    print('已生成csv文件: \033[0;32;0m{}\033[0m'.format(csv_filename))

                except:
                    print('生成csv文件失败')
                finally:
                    f.close()

            elif action == "exit":
                sys.exit(0)
            elif action == 'help':
                print(help_info)
            else:
                print('invalid action: you can input \033[0;32;1m help \033[0m')
    else:
        # 带红颜色
        #print("username or password error.")
        print('\033[0;31;0m username or password error. \033[0m')
        INIT_FAIL_CNT += 1
        if INIT_FAIL_CNT < MAX_FAIL_CNT:
            print('还有\033[0;31;0m {} \033[0m 次机会，否则程序将会退出'.format(MAX_FAIL_CNT - INIT_FAIL_CNT))


#次数带颜色
print("\nInput \033[0;31;0m {}\033[0m failed, Terminal will exit.".format(MAX_FAIL_CNT))





