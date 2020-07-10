
import page
import user
import logs


class auth():

    def login():
        input_info = input("请输入用户名/密码：")
        info = input_info.split("/")
        if len(info) != 2:
            logs.error("您的输入格式错误，请按照：用户名/密码")
            return
        if info[0] not in page.users or info[1] != page.users[info[0]]:
            logs.error("您输入的用户名或密码错误!")
            return

        if info[0] in page.admins:
            page.model_level01[1] = "删除用户"
            page.model_level01[3] = "查询所有用户"
            page.model_level01[5] = "导出用户信息csv格式"
        else:
            if 3 in page.model_level01.keys():
                page.model_level01.pop(1)
                page.model_level01.pop(3)
                page.model_level01.pop(5)

        logs.info(info[0] + "登录成功")
        while True:
            in2 = page.page.home01(page.model_level01)
            op = page.page.print_model(in2, page.model_level01, info[0])
            if op == "exit":
                return


    def register():
        input_info = input("请输入您注册的用户名/密码：")
        info = input_info.split("/")
        if len(info) != 2:
            logs.error("您的输入格式错误，请按照：用户名/密码")
            retry = input("重试(y), 回到主页面(other)")
            if retry == "y":
                return user.user.register()
            return
        if info[0] in page.users.keys():
            logs.error("您注册的用户已经存在！")
            return
        page.users[info[0]] = info[1]
        logs.info(info[0] + "注册成功！")

