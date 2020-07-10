class Crm(object):
    """
    用户管理系统
    """

    def __init__(self):
        self.result = []
        self.init_fail_cnt = 1
        self.max_fail_cnt = 6
        self.user_info = ("51reboot", "123456")
        self.login_status = False
        self.quit = False

    def login(self):
        while self.init_fail_cnt < self.max_fail_cnt:
            username = input("输入你的用户名:")
            password = input("输入你的密码:")
            if (username == self.user_info[0] and password == self.user_info[1]):
                self.login_status = True
                print("登陆成功! 欢迎%s", self.user_info[0])
                while True:
                    action = input("输入你需要的操作/增/删/改/查/搜/退出")
                    if action == "退出":
                        self.quit = True
                        break
                    self.action(action)
            else:
                print("用户名或密码错误，请重新输入，还有%s次用户好讲锁定" % (self.max_fail_cnt - self.init_fail_cnt - 1))
            self.init_fail_cnt += 1
            if self.quit:
                print("用户退出")
                break

    def action(self, args):
        if not self.login_status:
            print("未登陆，请登陆")
            return

        if args == "增":
            arg = input("输入你要增的数据：")
            self.result.append(arg)
            print("增加成功")

        elif args == "删":
            arg = input("输入你要删除的数据：")
            self.result.remove(arg)
            print("删除成功")

        elif args == "查":
            if len(self.result) == 0:
                print("当前没有数据")
            else:
                for i in range(len(self.result)):
                    print(i, ":", self.result[i])

        elif args == "改":
            while True:
                index = input("输入你要修改的数据位置：")
                if not index.isdigit():
                    print("请输入数字")
                elif int(index) > len(self.result) - 1:
                    print("输入数字越界")
                else:
                    arg = input("输入你要修改的数据:")
                    self.result[int(index)] = arg
                    print("修改成功")
                    break

        elif args == "搜":
            arg = input("输入你要搜索的数据：")
            count = self.result.count(arg)
            if count == 0:
                print("没有你要搜索的数据")
            else:
                for i in range(len(self.result)):
                    if self.result[i] == arg:
                        print("数据位置index:%s，%s" % (i, arg))
        else:
            print("输入错误，请重新输入")


def sort(args):
    """
    冒泡排序
    :return: list
    """
    if type(args) != list:
        print("输入列表")
        return
    for i in range(len(args)):
        for j in range(len(args) - i-1):
            if args[j] > args[j+1]:
                args[j], args[j+1] = args[j+1], args[j]
    print(args)
    return


if __name__ == "__main__":
    # 用户管理系统
    crm = Crm()
    crm.login()

    # 冒泡排序
    data = [4, 6, 8, 0, 9]
    sort(data)
