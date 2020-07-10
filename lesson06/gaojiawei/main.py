#定义全局变量
FIELDS = ['name', 'age', 'tel', 'email']
RESULT = {}
USERINFO = ('51reboot', '123456')


# 标准模块
import sys

# 第三方模块
from prettytable import PrettyTable

#自定义模块
import dbutils

class DB(object):
    '''数据库操作'''

    def select(self):
        sql = '''select username,age,tel,email from users;'''
        user_info, ok = dbutils.Select(sql)
        fields = ['username', 'age', 'tel', 'email']
        for i in user_info:
            info = dict(zip(fields, i))
            RESULT[i[0]] = info
        return RESULT

    def insert(self):
        for k, v in RESULT.items():
            username, age, tel, emai = v.values()
            sql = '''insert into users(username,age,tel,email)  values('{}',{},'{}','{}');'''.format(username, age, tel,
                                                                                                     emai)
            info, ok = dbutils.Insert(sql)
            if ok is True:
                print(info)

    def clear(self):
        sql = '''truncate table users;'''
        dbutils.Cleartab(sql)


class Persistence(DB):
    '''存储操作，实际调用db方法'''
    def save(self):
        DB.clear(self)
        DB.insert(self)

    def load(self):
        RESULT = DB.select(self)
        return  RESULT


class User():
    '''用户增删改查'''
    def add(self, args):
        userinfolist = args.split(" ")
        if len(userinfolist) != 4:
            return "addUser failed, args length != 4"

        username = userinfolist[0]
        if username in RESULT:
            print("Username: {} already exists.".format(username))
        else:
            RESULT[username] = {
                'name': username,
                'age': userinfolist[1],
                'tel': userinfolist[2],
                'email': userinfolist[3],
            }
            print("add user {} secc.".format(username))

    def delete(self, args):
        userinfolist = args.split(" ")
        if len(userinfolist) != 1:
            return "deleteUser failed, args length != 1"

        username = args
        if username in RESULT:
            RESULT.pop(username, None)
            print("delete user {} secc.".format(username))
        else:
            print("Username: {} not found.".format(username))

    def update(self, args):
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


    def find(self, args):
        username = args
        if username in RESULT:
            userinfo = RESULT[username]  # userinfo是字典
            xtb = PrettyTable()
            xtb.field_names = FIELDS
            xtb.add_row(list(userinfo.values()))
            print(xtb)
        else:
            print("Username: {} not found.".format(username))

    def mylist(self):
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for k, v in RESULT.items():
            xtb.add_row(v.values())
        print(xtb)

    def display(self, args):
        userinfolist = args.split()
        if len(userinfolist) == 2:
            if userinfolist[0] != 'page':
                return "syntax error."

            values = [list(v.values()) for k, v in RESULT.items()]
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


class Auth(User):

    @staticmethod
    def login(username, password):
        if username == USERINFO[0] and password == USERINFO[1]:
            return True
        else:
            return False


def main():
    user = Auth()
    count = 0
    db = Persistence()
    try:
        while count < 3:
            username = input('Please input your login username: ').strip().lower()
            passwd = input('Please input your login passwd: ').strip().lower()
            flg = user.login(username,passwd)
            if flg:
                print("\n\tWelcome to user magage system.\n")
                db.load()
                while True:
                    userinfo = input("Please inpur user info: ")  # add monkey 12 132xx monkey!@qq.com
                    if len(userinfo) == 0:
                        print("invalid input.")
                        continue
                    userinfo_list = userinfo.split()
                    action = userinfo_list[0]
                    userinfo_string = ' '.join(userinfo_list[1:])
                    if hasattr(user,action):
                        cmd = getattr(user,action)
                        cmd(userinfo_string)
                    elif action == 'list':
                        user.mylist()
                    elif action == 'save':
                        db.save()
                    elif action == 'logout' or action == 'exit':
                        sys.exit('exit ...')
                    elif action == 'load':
                        db.load()
                    else:
                        print("invalid input.")

            else:
                print('print("username or password valid failed.")')
                count += 1
        print("Game Over.")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
