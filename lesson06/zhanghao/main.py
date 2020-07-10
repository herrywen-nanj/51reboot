import user
import show
import auth
import log

op = user.User()
sh = show.Output()
au = auth.Auth()
log = log.Log()


def logic():
    while True:
        userinfo = input("Please input your action: ")
        info = userinfo.split()
        if len(info) == 0:
            print("input action invalid.")
        else:
            action = info[0]
            if action == "add":
                # add monkey 12 188*** monkey@qq.com
                op.add(info[1], info[2], info[3], info[4])
            elif action == "delete":
                # delete monkey
                op.delete(info[1])
            elif action == "update":
                # update monkey set age = 20
                op.update(info[1], info[3], info[-1])
            elif action == "list":
                # list
                result = op.list()
                sh.table(result)
            elif action == "find":
                # find monkey
                result = op.find(info[1])
                sh.table(result)
            elif action == "display":
                # display page 1 pagesize 5
                if len(info[1:]) == 2:
                    data = op.display(info[2])
                    sh.table(data)
                elif len(info[1:]) == 4:
                    data = op.display(info[2], info[-1])
                    sh.table(data)
            elif action == "logout":
                au.logout()


def main():
    min_fail_cnt = 0
    max_fail_cnt = 3
    while min_fail_cnt < max_fail_cnt:
        username = input("Please input your login username: ")
        password = input("Please input your login password: ")
        msg, ok = au.login(username, password)
        if ok:
            print("\n\tWelcome to user magage system.\n")
            log.opLog().info(msg)
            logic()
        else:
            min_fail_cnt += 1
            print("username or password valid failed.")
            log.opLog().info(msg)
    print("Input {} times failed,Terminal will exit.".format(max_fail_cnt))


if __name__ == "__main__":
    main()
