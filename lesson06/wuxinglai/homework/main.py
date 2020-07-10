# 标准模块
import sys,json,logging,pymysql
import configmgt,dbutils


# 第三方模块
from prettytable import PrettyTable

msg = '''
       1. 增 add           # add monkey 12 132xxx monkey@51reboot.com
       2. 删 delete        # delete monkey
       3. 改 update        # update monkey set age = 18
       4. 查 list          # list
       5. 搜 find          # find monkey
       6. 保存 save        # save
       7. 加载 load        # load
       8. 分页 display     # display page 1 pagesize 5
       9. 退出 logout      #logout
'''

# 全局变量
FIELDS = ['username', 'age', 'tel', 'email']
RESULT = {}

#fields = [ 'username', 'age', 'tel', 'email']
class DB(object):
        def insert(self):
            for i, x in RESULT.items():
                b = list(RESULT[i].values())
                sql_insert = '''insert into users(username,age,tel,email)  values('{}', {},'{}','{}');'''.format(b[0],
                                                                                                                 b[1],
                                                                                                                 b[2],
                                                                                                                 b[3])
                dbutils.insert(sql_insert)
        def load(self):
            # sql_select = '''select username,age,tel,email from users;'''
            sql_select = "select {} from users".format(','.join(FIELDS))
           # print(sql_select)
            rows, ok = dbutils.select(sql_select)
            #print(rows)
            if ok:
                global RESULT
                RESULT = {x[0]: {FIELDS[0]: x[0], FIELDS[1]: x[1], FIELDS[2]: x[2], FIELDS[3]: x[3]} for x in rows}
                return RESULT
        def truncate(self):
            truncate_sql = '''truncate  users'''
            dbutils.truncate(truncate_sql)

            



class User(object):
    def deleteUser(self, args):
        '''
        delete monkey1
        args = monkey1
        :param args:
        :return:
        '''
        #print(RESULT)
        userinfolist = args.split(" ")
        if len(userinfolist) != 1:
            return "deleteUser failed, args length != 1"

        username = args
        if username in RESULT:
            RESULT.pop(username, None)
            print("delete user {} secc.".format(username))
        else:
            print("Username: {} not found.".format(username))

    def updateUser(self, args):
        '''
        update monkey1 set age = 20
        :param args: monkey1 set age = 20
        :return:
        '''
        print(RESULT)
        userinfolist = args.split()
        if len(userinfolist) != 5:
            return "updateUser failed, args length != 5"

        where = userinfolist[1]
        wherefuhao = userinfolist[-2]

        if where != 'set' or wherefuhao != '=':
            return 'syntax error.'
        else:
            username = userinfolist[0]
            where_field = userinfolist[2]
            update_value = userinfolist[-1]
            RESULT[username][where_field] = update_value

    def listUser(self, args):
        '''
        打印所有用户信息
        :return:
        '''
        if len(RESULT) ==0:
            print("no user in system")
        else:
            xtb = PrettyTable()
            xtb.field_names = FIELDS
            for k, v in RESULT.items():
              xtb.add_row(v.values())
            print(xtb)

    def findUser(self, args):
        '''
        find monkey1
        :param args: = monkey1
        :return:
        '''
        username = args
        if username in RESULT:
            userinfo = RESULT[username]  # userinfo是字典
            xtb = PrettyTable()
            xtb.field_names = FIELDS
            xtb.add_row(list(userinfo.values()))
            print(xtb)
        else:
            print("Username: {} not found.".format(username))

    def displayUser(self, args):
        '''
        display page 2 pagesize 5
        :param args: page 2 pagesize 5 ;default pagesize = 5
        page 1 -> 0-4
        切片
        slice
        '''
        userinfolist = args.split()
        if len(userinfolist) == 2:
            if userinfolist[0] != 'page':
                return "syntax error."

            values = [ list(v.values()) for k, v in RESULT.items() ]
            # print(values)

            page_value = int(userinfolist[1]) - 1  # 1
            pagesize = 5
            start = page_value * pagesize
            end = start + pagesize
            # 0:5
            # 5:10

            xtb = PrettyTable()
            xtb.field_names = FIELDS
            for t_user_info in values[start:end]:
                xtb.add_row(t_user_info)
            print(xtb)

        elif len(userinfolist) == 4:
            if userinfolist[0] != 'page' and userinfolist[-2] != 'pagesize':
                return "syntax error."

            values = [list(v.values()) for k, v in RESULT.items()]
            # print(values)

            page_value = int(userinfolist[1]) - 1  # 1
            pagesize = int(userinfolist[-1])
            start = page_value * pagesize
            end = start + pagesize
            # 0:5
            # 5:10

            xtb = PrettyTable()
            xtb.field_names = FIELDS
            for t_user_info in values[start:end]:
                xtb.add_row(t_user_info)
            print(xtb)
        else:
            return "syntax error."

    def addUser(self,args):
        '''
        add monkey1 12 132xxx monkey1@qq.com

        args = "monkey1 12 132xxx monkey1@qq.com"
        :return:
        '''
        userinfolist = args.split(" ")
        if len(userinfolist) != 4:
            return "addUser failed, args length != 4"

        username = userinfolist[0]
        if username in RESULT:
            print("Username: {} already exists.".format(username))
        else:
            RESULT[username] = {
                'name'  : username,
                'age'   : userinfolist[1],
                'tel'   : userinfolist[2],
                'email' : userinfolist[3],
            }
            print("add user {} secc.".format(username))


class Auth(object):
    def login(username,password):
        userpassinfo = ('admin', '1')
        if username == userpassinfo[0] and password == userpassinfo[1]:
            return True
        else:
            return False
    def logout(self):
        sys.exit(0)

class Show(object):
    def showmenu(self):
        print('\033[1;32;40m')
        print('*' * 50)
        print('''\n\t\033[1;32;40m欢迎登陆用户管理系统\033[1;32;40m\n''')
        print('*' * 50)
        print('\033[0m')
        print('''\033[1;34;40m\n\t系统功能菜单\n\033[0m''')
        print('''\033[1;36;40m增加用户:add username age tel mail''')
        print('''删除用户:del username''')
        print('''更改用户:update username set age|tel|mail = args''')
        print('''查找用户:find username''')
        print('''列出所有用户:list''')
        print('''分页查找:display page 2 pagesize 5''')
        print('\033[0m')

def logic():
    while True:
        userinfo = input("Please inpur user info: ") # add monkey 12 132xx monkey!@qq.com
        if len(userinfo) == 0:
            print("invalid input.")
        else:
            userinfo_list = userinfo.split()
            action = userinfo_list[0]
            userinfo_string = ' '.join(userinfo_list[1:])
            if action == 'add':
                User().addUser(userinfo_string)
            elif action == 'delete':
                User().deleteUser(userinfo_string)
            elif action == 'update':
                User().updateUser(userinfo_string)
            elif action == 'find':
                User().findUser(userinfo_string)
            elif action == 'display':
                User().displayUser(userinfo_string)
            elif action == 'list':
                User().listUser(userinfo_string)
            elif action == 'save':
                DB().truncate()
                DB().insert()
            elif action == 'load':
                DB().load()
            elif action == 'logout'  or action == 'exit' or action == 'quit':
                Auth().logout()


def main():
    '''
    入口函数
    '''
    DB().load()
    init_fail_count = 0
    max_fail_count = 6
    while init_fail_count < max_fail_count:
        username = input("Please input your login username: ")
        password = input("Please input your login password: ")
        if Auth.login(username,password):
            Show().showmenu()
            logic()
        else:
            print("username or password valid failed.")
            init_fail_count += 1

    print("Game Over.")

if __name__ == '__main__':
    main()
