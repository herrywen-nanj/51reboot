import page
import logs
import csv

class user():

    def delete_user(user):
        if user in page.admins.keys():
            print(" 查看所有用户 ".center(len(page.h), "*"))
            for i in page.users.keys():
                out = "userName: {}".format(i).ljust(10)
                print(out.center(len(page.h)))
        input_info = input("请输入您需要删除的用户：")
        if input_info not in page.users.keys():
            logs.error("该用户不存在！")
            return
        page.users.pop(input_info)
        logs.info("删除成功！")

    def update_user(user):
        if user in page.admins.keys():
            print(" 查看所有用户 ".center(len(page.h), "*"))
            for i in page.users.keys():
                out = "userName: {}".format(i).ljust(10)
                print(out.center(len(page.h)))
            input_info = input("请输入您需要修改的用户名：")
            if input_info not in page.users.keys():
                logs.error("该用户不存在！")
                return
        else:
            input_info = user

        page.users[input_info] = input("请输入新的密码：")
        logs.info("修改成功！")

    def list_user(user):
        if user in page.admins.keys():
            print(" 查看所有用户 ".center(len(page.h), "*"))
            for i in page.users.keys():
                out = "userName: {:<12}".format(i)
                print(out.center(len(page.h)))
        else:
            logs.error("非管理员不能查看所有用户信息")

    def search_user(user):
        input_info = input("请输入您需要搜索的用户名：")
        if input_info not in page.users.keys():
            logs.error("您输入的用户不存在！")
            return

        print(" 搜索用户 ".center(len(page.h), "*"))
        if user in page.admins.keys():
            out = "userName: {:<6} password: {:<6}".format(input_info, page.users[input_info])
        else:
            out = "userName: {:<6}".format(input_info)
        print(out.center(len(page.h)))

    # 导出csv格式用户信息
    def export_csv(user):
        if user in page.admins.keys():
            logs.info('正在导出csv文件...')
            title = ['用户名', '密码']
            with open('users.csv', 'w', newline='') as users_csv:
                writer = csv.writer(users_csv)
                writer.writerow(title)
                for i in page.users:
                    u = [i, page.users[i]]
                    writer.writerow(u)
            logs.info('csv文件导出成功！请移步查看...')
        else:
            logs.error("非管理员不能导出用户信息")

    # 持久化数据到文件
    def save_file():
        fd = None
        try:
            fd = open("homework01_user_manager.txt", 'w')
            # 覆盖之前的存档，需要该步骤
            fd.write(json.dumps(page.users))
            logs.info("成功保存持久化数据：" + json.dumps(page.users))
        except Exception as e:
            logs.error(str(e))
        finally:
            if fd is not None:
                fd.close()