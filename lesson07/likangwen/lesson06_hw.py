from prettytable import PrettyTable
import sys
import pandas
import logging
from utils.dbutils import DBOperation



# 日志
class LogAndHelp():
    def userlog(self, msg):
        logging.basicConfig(level=logging.DEBUG,
                            filename='./log.txt',
                            filemode='a',
                            format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        logging.debug(msg)

    def help(self):
        FORMAT = """
        ====================================================================
           2.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
            2.2 删 delete        # delete monkey
            2.3 改 update        # update monkey set age = 18
            2.4 查 list          # list
            2.5 搜 find          # find monkey
            2.6 分页  display    # display page 1 pagesize 5
            2.7 保存csv格式，可跟上名称，否则默认     # export csvname  
            2.8 帮助文档         # 'h' or 'help'    
        ===================================================================
        """
        return FORMAT



# 用户操作
class UserOprate():
    def __init__(self):
        self.FIELDS = ('id', 'username', 'age', 'tel', 'email')
        self.dbopt = DBOperation()

    def userAdd(self, info_list):
        if len(info_list) == 4:
            # 先确认用户是否存在，不存在则添加，存在返回已存在提示
            find_sql = "select * from user where username='{}'".format(info_list[0])
            msg, ok = self.dbopt.sqlOperation(find_sql)
            if not ok:
                age = int(info_list[1])
                info_list[1] = age

                sql = "insert into users{} values{}".format(str(self.FIELDS[1:]).replace("'", ""), tuple(info_list))
                return self.dbopt.sqlOperation(sql)

            else:
                return "User already exists", False
        else:
            return "请输入正确参数", False

    # 删除用户操作
    def userDelete(self, info_list):
        username = info_list[0]
        # 先确认用户是否存在，存在则删除，不存在返回不存在提示
        find_sql = "select * from users where username='{}'".format(username)
        msg, ok = self.dbopt.sqlOperation(find_sql)
        if ok:
            sql = "delete from users where username='{}'".format(username)
            return self.dbopt.sqlOperation(sql)
        else:
            return "用户不存在", False

    def userUpdate(self, info_list):
        # print(info_list)
        # 查找用户是否存在
        find_sql = "select * from users where username='{}'".format(info_list[0])
        # print(find_sql)
        msg, ok = self.dbopt.sqlOperation(find_sql)
        if ok:
            location_index = info_list.index("=")  # 获取 = 在哪个位置
            k = info_list[location_index - 1]  # 获取要修改的参数，如age，username等
            if k in self.FIELDS:
                print(k)
                v = info_list[location_index + 1]

                sql = "update users set {}={} where username='{}'".format(k, v, info_list[0])
                return self.dbopt.sqlOperation(sql)

            else:
                return "请输入正确的参数", False
        else:
            return "用户不存在", False

    # 返回数据库所有数据
    def allData(self):
        sql = "select * from users"
        return self.dbopt.sqlOperation(sql, seek=True)

    # 打印成表格的函数
    def pretable(self, data):
        x = PrettyTable()
        x.field_names = self.FIELDS
        for user_list in data:
            x.add_row(user_list)
        print(x)

    def userList(self, info_list):
        return self.allData()

    def userDisplay(self, info_list):
        pagesize = 5
        if 'page' in info_list and 'pagesize' in info_list and len(info_list) == 4:
            page = int(info_list[1])
            pagesize = int(info_list[-1])

        elif 'page' in info_list and len(info_list) == 2:
            page = int(info_list[-1])

        else:
            return "请输入正确参数", False

        end = page * pagesize
        msg, ok = self.allData()
        if ok:
            return msg[end - pagesize: end], True
        else:
            return msg, ok

    def userFind(self, info_list):
        sql = "select * from users where username='{}'".format(info_list[0])
        return self.dbopt.sqlOperation(sql, seek=True)

    def saveCSV(self, info_list):
        file_name = "kw"
        if len(info_list):
            file_name = info_list.pop(0)
        pd = pandas.DataFrame(columns=self.FIELDS, data=list(self.allData()[0]))
        pd.to_csv('{}.csv'.format(file_name), encoding='utf_8_sig')  # 防止中文乱码

def userOpertion():

    uo = UserOprate()
    logger = LogAndHelp()
    help = LogAndHelp().help()
    # dboprate = DBOperation().sqlOperation()

    print("输入'h'或者 'help'查看帮助文档")
    while True:
        info = input("Please input your operation: ").lower()
        if not info:  # 当直接回车时不会报错
            continue
        info_list = info.split()

        try:  # 异常处理
            action = info_list.pop(0)
        except:
            pass

        if action == "add":
            msg, ok = uo.userAdd(info_list)
            if ok:
                log = "add user {}, status:{}".format(info_list[0], ok)
                logger.userlog(log)

            print(msg)

        elif action == "delete":
            msg, ok = uo.userDelete(info_list)
            # logger.userlog("delete user {}, {}".format(info_list[0], ok))
            log = "delete user {}, status:{}".format(info_list[0], ok)
            logger.userlog(log)
            print(msg)

        elif action == "update":
            msg, ok = uo.userUpdate(info_list)
            print(msg)

        elif action == "list":
            msg, ok = uo.userList(info_list)
            if ok:
                uo.pretable(msg)
            else:
                print(msg)

        elif action == "find":
            msg, ok = uo.userFind(info_list)
            if ok:
                uo.pretable(msg)
            else:
                print("用户不存在")

        elif action == "display":
            msg, ok = uo.userDisplay(info_list)
            if ok:
                uo.pretable(msg)
            else:
                print(msg)

        elif action == "export":
            uo.saveCSV(info_list)

        elif action.lower() == "h" or action.lower() == "help":
            print(help)

        elif action.lower() == "h" or action.lower() == "help":
            print(help)

        elif action == "exit":
            sys.exit(1)

        else:
            print("Syntax error")
            print(help)

class UserLogin():
    def __init__(self):
        self.INIT_FAIL_CNT = 0
        self.MAX_FAIL_CNT = 6
        self.USERNAME = 'a'
        self.PASSWD = 'a'

    def userlogin(self):
        while self.INIT_FAIL_CNT < self.MAX_FAIL_CNT:

            print("******此为直接操作数据库版本******")
            username = input("Please input your username: ")
            password = input("Please input your password: ")
            # password = getpass.getpass("Please input your password: ")
            if username == self.USERNAME and password == self.PASSWD:
                # if True:
                userOpertion()
            else:
                print("账号或密码错误")
                self.INIT_FAIL_CNT += 1

        print("密码错误次数超过6次, 系统退出")


if __name__ == '__main__':
    UserLogin().userlogin()
    # msg, ok = DBOperation().sqlOperation("select * from users", seek=True)
    # print(msg)
