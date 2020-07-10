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


def Load_Data(filename=USER_DATA_FILE):
    try:
        f = open(filename, 'r')
        data = f.read()
        user_data_dict = json.loads(data)
        return user_data_dict,True
    except:
        user_data_dict = {}
        return user_data_dict,False
    finally:
        f.close()




def Save_Data(filename=USER_DATA_FILE):
    try:
        f = open(filename, 'w')
        data = json.dumps(user_data_dict)
        f.write(data)
        info = '已保存'
        info = Green_Print('已保存')
        return info,True
    except:
        info = '{} 不可写，保存失败'.format(USER_DATA_FILE)
        info = Red_print(info)
        return info,False
    finally:
        f.close()

def Green_Print(str):
    str = '\033[0;32;0m {}\033[0m'.format(str)
    return str


def Red_print(str):
    str = '\033[0;31;0m {}\033[0m'.format(str)
    return str

def Yellow_print(str):
    str = '\033[0;33;0m {}\033[0m'.format(str)
    return str

def Login_Authentication(username,password):
    if username == USERINFO[0] and password == USERINFO[1]:
        return True
    else:
        return False

def Check_User_Exist(username:str):
    if username in user_data_dict:
        # print('\033[0;35;0m用户已存在,不可以添加\033[0m')
        return True
    else:
        return False



def Add_User(info_list:list):
    username_info_dict = {}
    try:
        username = info_list[1]
        username_info_dict['age'] = info_list[2]
        username_info_dict['tel'] = info_list[3]
        username_info_dict['email'] = info_list[4]
    except:
        info = Red_print('格式不正确')
        return info,False
    if Check_User_Exist(username):
        #Yellow_print('用户已存在,不可以添加')
        info = Yellow_print('用户已存在,不可以添加')
        return info,False
    else:
        user_data_dict[username] = username_info_dict

        info = 'Add {} succes'.format(info_list[1])
        info = Green_Print(info)
        # 添加后自动保存
        Save_Data()
        return info,True

def Delete_User(info_list:list):
    # 获取输入的可能是用户或id
    user_info = info_list[1]
    # 尝试输入的是不是整数，则认为根据id删除
    if user_info.isdigit():
        id = int(user_info)
        # 临时得到用户列表
        username_list = []
        for username in user_data_dict:
            username_list.append(username)
        try:
            username = username_list[id - 1]

            del user_data_dict[username]
            info = 'id 为{} 的用户 {} 已删除'.format(id, username)
            info = Green_Print(info)
            return info,True
        except:
            info = '没有id 为 {} 的用户'.format(id)
            info = Yellow_print(info)
            return info,False
    else:
        # 否则认为是根据用户名删除
        username = user_info

        # 判断输入的用户名是否存在
        if not Check_User_Exist(username):
            info = '没有这个用户: {}'.format(username)
            info = Yellow_print(info)
            return info,False
        else:
            del user_data_dict[username]
            info = '已删除用户: {}'.format(username)
            info = Green_Print(info)
            Save_Data()
            return info,True

def Update_User(info:str):
    # 重新分割输入的信息，最大分割3个

    info_list = info.split(maxsplit=3)
    try:
        username = info_list[1]
    except:
        info = Red_print('提供信息不足，请重新输入')
        return info,False
    # 判断是否有关键字
    if 'set' not in info_list:
        info = Red_print('语法错误缺少关键字 set')
        return info, False
    # 把输入的key 和 value 单独赋值
    try:
        user_filed_value = info_list[3].strip()
        if user_filed_value.startswith('='):
            info = Red_print('= 等号左边缺少键')
            return info,False

        elif user_filed_value.endswith('='):
            info = Red_print('= 等号右边缺少值')
            return info,False

    except:
        info = Red_print('提供信息不足，请重新输入')
        return info,False

    if '=' not in user_filed_value:
        info = Red_print('语法错误缺少关键字 =')
        return info,False
    # 再把输入的key 和 value 分割提取

    user_filed = user_filed_value.split('=')[0].strip()

    new_value = user_filed_value.split('=')[1].strip()
    if user_filed == 'id' or user_filed == 'username':
        info = '用户字段{} 不能修改'.format(user_filed)
        info = Yellow_print(info)
        return info,False
    elif user_filed == 'age':
        if new_value.isdigit():
            pass
        else:
            info = '字段{} 必须是整数'.format(user_filed)
            info = Yellow_print(info)
            return info,False
    elif user_filed == 'tel':
        if new_value.isdigit():
            pass
        else:
            info = '字段{} 必须是整数'.format(user_filed)
            info = Yellow_print(info)
            return info,False
    elif user_filed == 'email':
        if '@' in new_value and new_value.endswith('.com') and not new_value.startswith('@'):
            pass
        else:
            info = Yellow_print('邮箱格式不合法')
            return info,False

    else:
        info = '没有该字段 {}'.format(user_filed)
        info = Yellow_print(info)
        return info,False

    # 判断用户是否存在
    if Check_User_Exist(username):
        old_value = user_data_dict[username][user_filed]
        user_data_dict[username][user_filed] = new_value
        info = '用户 {} 的字段 {} 值 已由 {}改为 {}'.format(username, user_filed, old_value, new_value)
        info = Green_Print(info)
        # 自动保存
        Save_Data()
        return info,True


    else:
        info = '用户 {} 不存在'.format(username)
        info = Yellow_print(info)
        return info,False

def List_User():

    x = PrettyTable()
    x.field_names = FIELD_NAMES

    id = 1
    for username in user_data_dict:
        try:
            # 以用户名的 value 格式字典
            username_dict = user_data_dict[username]
            user_row = [id, username, username_dict['age'], username_dict['tel'], username_dict['email']]
            x.add_row(user_row)
            id = id + 1
        except:
            pass
    return x,True

def Find_User(info_list:list):
    # 获取要查找的用户名
    if len(info_list) == 2:
        pass
    else:
        info = Red_print('输入信息格式不正确')
        return info,False

    username_list = []
    # 找出所有用户的加入临时列表
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
            x.add_row([id, user_name, age, tel, email])

    return x,True

def Display_User(info_list:list):
    # dispaly page 2 pagesize 5
    #info_list = info.split()
    if 'page' not in info_list:
        info = Red_print('缺少关键字 page')
        return info,False

    try:
        page = int(info_list[2])
    except:
        page = 1
    try:
        pagesize = int(info_list[4])
    except:
        pagesize = 5

    username_list = []
    # 找出所有用户的加入临时列表
    for username_tmp in user_data_dict:
        username_list.append(username_tmp)
    x = PrettyTable()
    user_list = []
    x.field_names = FIELD_NAMES
    # username_number = len(username_list)

    for user_name in username_list:
        id = username_list.index(user_name) + 1
        age = user_data_dict[user_name]['age']
        tel = user_data_dict[user_name]['tel']
        email = user_data_dict[user_name]['email']
        user_single_list = [id, user_name, age, tel, email]
        user_list.append(user_single_list)

    all_page_list = []
    i = 1
    # 遍历所有用户单条信息，如果整除pagesize 那么就加入到下一页，如果最后没整除且已到最后一条，加入单独一页
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
        info = '没有 {} 页,共{}页'.format(page, len(all_page_list))
        info = Yellow_print(info)
        return info,False
    display_page_list = all_page_list[page - 1]

    for user in display_page_list:
        x.add_row(user)
    info = '第 {} 页，共 {} 页'.format(page, len(all_page_list))
    info = Green_Print(info)
    print(info)

    return x,True

def Export():
    username_list = []
    # 找出所有用户的加入临时列表
    for username_tmp in user_data_dict:
        username_list.append(username_tmp)
    x = PrettyTable()
    user_list = []
    x.field_names = FIELD_NAMES
    # username_number = len(username_list)

    for user_name in username_list:
        id = username_list.index(user_name) + 1
        age = user_data_dict[user_name]['age']
        tel = user_data_dict[user_name]['tel']
        email = user_data_dict[user_name]['email']
        user_single_list = [id, user_name, age, tel, email]
        user_list.append(user_single_list)
    time_str = time.strftime('%Y%m%d%H%M%S')
    csv_filename = USER_DATA_FILE.split('.')[0] + '_' + time_str + '.csv'
    try:
        f = open(csv_filename, "w")
        writer = csv.writer(f)
        writer.writerow(FIELD_NAMES)
        for row in user_list:
            writer.writerow(row)
        info = '已生成csv文件: {} '.format(csv_filename)
        info = Green_Print(info)
        return info,True
    except:
        info = Red_print('生成csv文件失败')
        return info,False
    finally:
        f.close()


while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ").strip()
    password = input("Please input your password: ").strip()
    if Login_Authentication(username,password):
        Green_Print('登录成功!')
        print(help_info)

        while True:
            user_data_dict,ok = Load_Data()


            # 业务逻辑
            cmd_info = input("Please input your operation: ")
            #如果输入为空，跳入下次循环
            if cmd_info == '':
                continue

            info_list = cmd_info.split()


            action = info_list[0]

            if action == "add":
                info,ok = Add_User(info_list)
                print(info)

            elif action == "delete":
                #获取输入的可能是用户或id
                info,ok = Delete_User(info_list)
                print(info)

            elif action == "update":
                info,ok = Update_User(cmd_info)
                print(info)

            elif action == "list":
                info,ok = List_User()
                print(info)

            elif action == "find":
                info,ok = Find_User(info_list)
                print(info)
            elif action == 'save':
                info,ok=Save_Data()
                print(info)


            elif action == 'load':
                user_data_dict,ok = Load_Data()
                if ok:
                    info = Green_Print('已加载')
                    print(info)
                else:
                    info = Red_print('加载失败')
                    print(info)

            elif action == 'display':
                info,ok = Display_User(info_list)
                print(info)

            elif action == 'export':
                info,ok = Export()
                print(info)

            elif action == "exit":
                sys.exit(0)
            elif action == 'help':
                print(help_info)
            else:
                info = Red_print('invalid action: you can input: help ')
                print(info)
    else:

        info = Red_print('账号或密码错误')
        print(info)
        INIT_FAIL_CNT += 1
        if INIT_FAIL_CNT < MAX_FAIL_CNT:
            info = Yellow_print('还有 {} 次机会，否则程序将会退出'.format(MAX_FAIL_CNT - INIT_FAIL_CNT))
            print(info)
#次数带颜色
info = "\nInput {} times failed, Terminal will exit.".format(MAX_FAIL_CNT)
info = Red_print(info)
print(info)




