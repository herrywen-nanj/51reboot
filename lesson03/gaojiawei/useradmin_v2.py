

"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
"""


# 标准模块
import sys
import json
import datetime
import csv
import  logging
from prettytable import PrettyTable


# 定义变量
RESULT = {}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("51reboot", "123456")
FILENAME = "51reboot.txt"


class Useradmin(object):
    '''用户管理类，主要功能增删改查，保存加载，存储为txt文本，字典格式'''
    def __init__(self):
        '''初始化方法，定义None为login模块使用做铺垫'''
        self.info = None
        self.info_list = None


    def up_info(self,info,info_list):
        '''传入处理数据信息，login方法使用以后，调用此方法'''
        self.info = info
        self.info_list =info_list


    def login(self):
        '''登陆模块，6次退出，'''
        INIT_FAIL_CNT = 0
        MAX_FAIL_CNT = 6
        while INIT_FAIL_CNT < MAX_FAIL_CNT:
            username = input("Please input your username: ")
            password = input("Please input your password: ")
            if username == USERINFO[0] and password == USERINFO[1]:
                print('Log in successfully.')
                return True
            else:
                print("musername or password error.")
                INIT_FAIL_CNT += 1


    def help_info(self):
        '''帮助 '''
        info = {
            '增': 'add monkey 12 132xxx monkey@51reboot.com',
            '删': 'delete monkey',
            '改': 'update monkey set age = 18',
            '查': 'list',
            '搜': 'find monkey',
            '存': 'save',
            '读': 'load',
            '分': 'display page 1 pagesize 5',
            '退': 'exit',
            '帮': 'help_info'
        }
        for k, v in info.items():
            print(k, v)


    def display(self):
        '''分页'''
        global RESULT
        xtb = PrettyTable()
        xtb.field_names = ["username", "age", "tel", "email"]
        #空列表，字典列表之间数据转换，格式化输出，定义循环索引
        info = []
        for k, v in RESULT.items():
            tmp_info = RESULT[k].values()
            tmp_info = list(tmp_info)
            info.append(tmp_info)
        page = int(self.info_list[2])

        line = int(self.info_list[-1])
        start = (page - 1) * line
        end = line * page
        print(page, line, start, end)

        for x in info[start:end]:
            xtb.add_row(x)
        print(xtb)


    def add(self):
        '''添加方法，判断用户名是否存在RESULT字典中，不存在直接添加，存在报错'''
        global RESULT
        username = self.info_list[1]
        #自定义了一个字典，完成需求格式
        dic_info = {"name": self.info_list[1], "age": self.info_list[2], 'tel': self.info_list[3], 'email': self.info_list[4]}

        if username not in RESULT:
            RESULT[username] = dic_info
            print("Add {} succ.".format(self.info_list[1]))

        else:
            print("Add {} failure .{} existing .".format(self.info_list[1], self.info_list[1]))


    def delete(self):
        '''删除方法，判断用户是否存在字典中，存在直接del 删除该条数据'''
        global RESULT
        cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        username = self.info_list[1]
        if username not in RESULT:
            print("User {} not found.".format(username))
        else:
            del RESULT[username]
            print("[DEBUG] {} {}".format(cur_time, self.info))


    def update(self):
        '''修改方法，把用户传入信息，以列表切片方式将关键信息存储为变量，通过字典修改方式直接赋值'''
        global RESULT
        #用户名，旧的值，新的值变量定义
        username = self.info_list[1]
        upinfo = self.info_list[3]
        nupinfo = self.info_list[-1]
        try:
            if username not in RESULT:
                print(' A null value.')
            else:
                #字典修改嵌套格式所以，[][] = []
                RESULT[username][upinfo] = nupinfo
                print('update {} succ.'.format(username))
        except Exception as e:
            print(e)


    def mylist(slef):
        '''查找方法，显示全部，判断字典长度，如果小于1表示没数据'''
        global RESULT
        if len(RESULT) < 1:
            print('A null value.')
        else:
            xtb = PrettyTable()
            xtb.field_names = ["username", "age", "tel", "email"]
            #定义空列表存储转换后的字典
            info = []
            #遍历字典，values 为全部需要信息，因为for循环传值PrettyTable方法的使用嵌套列表格式
            for k, v in RESULT.items():
                tmp_info = RESULT[k].values()
                #得到所有的信息以后变为列表格式
                tmp = list(tmp_info)
                #临时定义空列表追加
                info.append(tmp)
            #格式化输出
            for x in info:
                xtb.add_row(x)
            print(xtb)


    def find(self):
        '''搜索方法，判断用户是否存在，不存在反回提示空值'''
        global RESULT
        username = self.info_list[1]
        if username not in RESULT:
            print(' A null value.')
        else:
            #重复性代码，数据转换，考虑单独提取为一个方法
            xtb = PrettyTable()
            xtb.field_names = ["username", "age", "tel", "email"]
            info = []
            tmp_info = RESULT[username].values()
            tmp_info = list(tmp_info)
            info.append(tmp_info)
            for x in info:
                xtb.add_row(x)
            print(xtb)


    def save(self):
        '''保存'''
        # save
        # 1. 打开文件 file describe
        global RESULT
        fd = open(FILENAME, 'w')

        # 2. 操作文件 read / write
        fd.write(json.dumps(RESULT))

        # 3. 关闭文件
        fd.close()

        print("Save file:{} succ.".format(FILENAME))


    def load(self):
        '''加载保存文件'''
        global RESULT
        try:
            fd = open(FILENAME, 'r')

            # 2. 操作文件 read / write
            data = fd.read()
            RESULT = json.loads(data)

            # 3. 关闭文件
            fd.close()

        except Exception as e:
            print(e)


def main():
    '''
    主逻辑，实例化对象，调用login方法后，如果登陆成功，会返回True，
    if判断会正确，使用提前定义的up_info方法，传入需要信息，开始进行操作
    使用反射，hasattr，判断是否有该方法，有直接调用getattr
    增加if list 类中mylist方法 实际主方法list，类中如果定义list方法，关键字冲突
    '''
    u = Useradmin()
    res = u.login()
    if res:
        u.help_info()
        while True:
            try:
                info = input("Please input your operation: ")
                info_list = info.split()
                action = info_list[0]
                u.up_info(info, info_list)
                if hasattr(u, action):
                    cmd = getattr(u, action)
                    cmd()
                elif action == 'list':
                    cmd = getattr(u,'mylist')
                    cmd()
                elif action == 'exit':
                    sys.exit('exit...  ')
                else:
                    print('action not fond.')
            except Exception as e:
                print(e)
        else:
            print("login error")



if __name__ == '__main__':
    main()
