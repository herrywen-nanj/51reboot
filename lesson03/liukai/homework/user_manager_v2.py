import json
import sys
from prettytable import PrettyTable

"""
username:51reboot
password:123456
>增: add monkey 12 132xxx monkey@51reboot.com
>删: delete monkey
>改: update monkey set age = 18
>查: list
>搜: find monkey
>退出: logout

"""

message = {
    "0001": "login success, welcome {}",
    "0002": "login fail,your username or password is error",
    "0003": "logout success !!!",
    "0004": "bye {}",
    "0005": "Please input add messages:",
    "0006": "Your input messages invalid！",
    "0007": "Username is already ！！！",
    "0008": "add username {} success",
    "0009": "Please input delete username:",
    "0010": "Operation error ,Please input delete username:",
    "0011": "delete error ,no username",
    "0012": "delete {} success ",
    "0013": "Please input find username:",
    "0014": "Operation error ,Please input find username:",
    "0015": "no username",
    "0016": "Please input your name:",
    "0017": "Please input your password:",
    "0018": "Please input your operation:",
    "0019": "your operation is error !!!!",
    "0020": '''---------------------------------------------
命令：
>增: add monkey 12 132xxx monkey@51reboot.com
>删: delete monkey
>改: update monkey set age = 18
>查: list
>搜: find monkey
>退出: logout
>分页: display page 1 pageSize 5
---------------------------------------------
                            ''',
    "0021": "find {} success",
    "0022": "update error ,no username",
    "0023": "update error ,no args",
    "0024": "update error ,Please  args=xxx ",
    "0025": "write file success",
    "0026": "read file success",
    "0027": "read file error",
    "0028": "page or pageSize args is error ,args must number",

}


class Crm(object):
    """
    用户管理系统
    """

    def __init__(self):
        self.result = {}
        self.init_fail_cnt = 1
        self.max_fail_cnt = 6
        self.user_info = {"name": "51reboot", "password": "123456"}
        self.login_status = False
        self.quit = False
        self.field_names = ["Username", "Age", "Phone", "Email"]
        self.info = ["age", "phone", "email"]
        self.help_info = message.get("0020")
        self.args = []
        self.file_name = "user_info.csv"
        self._read_file()

    def print_table(self, args):
        """
        格式化输出table
        :param args:
        :return:
        """
        x = PrettyTable(self.field_names)
        for i in args:
            x.add_row([i["name"], i["info"]["age"], i["info"]["phone"], i["info"]["email"]])
        print(x)

    def login(self, name, password):
        """
        登陆
        :param name:  用户名
        :param password:  密码
        :return: None
        """
        if name == self.user_info["name"] and password == self.user_info["password"]:
            self.login_status = True
            print(message.get("0001").format(self.user_info["name"]))
        else:
            print(message.get("0002"))

    def logout(self):
        """
        登出
        :return:
        """
        self.login_status = False
        self._write_file()
        print(message.get("0003"))
        print(message.get("0004").format(self.user_info["name"]))
        sys.exit()

    def add(self):
        """
        add
        :return:
        """
        # args = input(message.get("0005"))
        # args = args.split()
        if len(self.args) < 2:
            print(message.get("0006"))
            return
        if self.result.get(self.args[1], None):
            print(message.get("0007"))
        else:
            info = {}
            if len(self.args) >= 3:
                info["age"] = self.args[2]
            else:
                info["age"] = ""
            if len(self.args) >= 4:
                info["phone"] = self.args[3]
            else:
                info["phone"] = ""
            if len(self.args) >= 5:
                info["email"] = self.args[4]
            else:
                info["email"] = ""
            self.result[self.args[1]] = info
            print(message.get("0008").format(self.args[1]))
            self._write_file()

    def delete(self):
        """
        delete
        :return:
        """
        if len(self.args) < 2:
            print(message.get("0006"))
            return
        if not self.result.get(self.args[1], None):
            print(message.get("0011"))
            return
        else:
            self.result.pop(self.args[1])
            print(message.get("0012").format(self.args[1]))
            self._write_file()

    def update(self):
        """
        update
        :return:
        """
        if len(self.args) < 6:
            print(message.get("0006"))
            return
        if not self.result.get(self.args[1], None):
            print(message.get("0022"))
            return
        if self.args[3] not in self.info:
            print(message.get("0023"))
            return
        if self.args[4] != "=":
            print(message.get("0024"))
            return
        self.result[self.args[1]][self.args[3]] = self.args[5]
        kw = {}
        kw["name"] = self.args[1]
        kw["info"] = self.result[self.args[1]]
        self.print_table([kw])
        self._write_file()

    def find(self):
        """
        detail
        :return:
        """
        if len(self.args) < 2:
            print(message.get("0006"))
            return
        if not self.result.get(self.args[1], None):
            print(message.get("0015"))
            return
        else:
            kwargs_new = {}
            kwargs_new["name"] = self.args[1]
            kwargs_new["info"] = self.result.get(self.args[1], None)
            print(message.get("0021").format(self.args[1]))
            self.print_table([kwargs_new])

    def list(self):
        """
        list
        :return:
        """
        data = []
        for k, v in self.result.items():
            kw = {}
            kw["name"] = k
            kw["info"] = v
            data.append(kw)
        self.print_table(data)

    def display(self):
        if len(self.args) < 3:
            print(message.get("0006"))
            return
        if self.args[1] != "page":
            print(message.get("0006"))
            return
        pageSize = 5
        if len(self.args) >= 5 and self.args[3] == "pageSize":
            if str(self.args[4]).isdigit():
                pageSize = int(self.args[4])

        if not str(self.args[2]).isdigit():
            print(message.get("0028"))
            return
        data = []
        for k, v in self.result.items():
            kw = {}
            kw["name"] = k
            kw["info"] = v
            data.append(kw)
        try:
            data = data[(int(self.args[2]) - 1) * pageSize: int(self.args[2]) * pageSize]
        except Exception as e:
            data = []
        self.print_table(data)
        pass

    def _write_file(self):
        f = open(file=self.file_name, mode="w")
        data = json.dumps(self.result)
        f.write(data)
        f.close()
        print(message.get("0025"))

    def _read_file(self):
        try:
            f = open(file=self.file_name, mode="r")
            data = f.read()
            self.result = json.loads(data)
            f.close()
            print(message.get("0026"))
        except Exception as e:
            print(message.get("0027"), e)
            pass

    def main(self):
        """
        主入口
        :return:
        """
        while True:
            if not self.login_status:
                name = input(message.get("0016"))
                password = input(message.get("0017"))
                self.login(name, password)
            else:
                print(self.help_info)
                action_input = input(message.get("0018"))
                action_list = action_input.split()
                if len(action_list) <= 0:
                    print(message.get("0019"))
                else:
                    if hasattr(self, action_list[0]):
                        action = getattr(self, action_list[0])
                        self.args = action_list
                        action()
                    else:
                        print(message.get("0019"))


if __name__ == "__main__":
    # 用户管理系统
    crm = Crm()
    crm.main()
