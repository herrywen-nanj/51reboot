import sys
import addUser
import deleteUser
import updateUser
import listUser
import findUser
import displayUser
import loginAuth

helpDoc = '''{}
add         : add monkey 12 132xxx monkey@51reboot.com
delete      : delete monkey
update      : update monkey set age = 20
list        : list
find        : find monkey
display     : display page 2 page_size 3
doc         : enable/disable docstring
exit        : quit
save        : save 51reboot.txt
load        : load 51reboot.txt
{}
'''.format('-' * 70, '-' * 70)


def main():
    ENABLE_DOC = True
    min_fail_cnt = 1
    max_fail_cnt = 6
    while min_fail_cnt <= max_fail_cnt:
        username = input("Please input your username: ")
        password = input("Please input your password：")
        msg, ok = loginAuth.loginAuth(username, password)
        if ok:
            print(msg)
            while True:
                if ENABLE_DOC:
                    print(helpDoc)
                info = input("\033[0;31;1mPlease input your operation：\033[0m")
                info_list = info.strip().split()
                if len(info) == 0:
                    print("\033[0;31;1mInput info invaild, Please input again.\033[0m")
                    continue
                action = info_list[0]
                if action == "add":
                    addUser.addUser(info_list)
                elif action == "delete":
                    deleteUser.deleteUser(info_list)
                elif action == "update":
                    updateUser.updateUser(info_list)
                elif action == "list":
                    listUser.listUser()
                elif action == "find":
                    findUser.findUser(info_list)
                elif action == "display":
                    displayUser.displayUser(info_list)
                elif action == "doc":
                    doc_action = 'disable' if ENABLE_DOC else 'enable'
                    if ENABLE_DOC:
                        input("You are {} docString,Please Enter：".format(doc_action))
                        ENABLE_DOC = False
                    else:
                        input("You are {} docString,Please Enter：".format(doc_action))
                        ENABLE_DOC = True
                elif action == "exit":
                    sys.exit(0)
                else:
                    print("\033[0;31;1minvalid operation.\033[0m")
        else:
            print("\033[0;31;1musername or password error.\033[0m")
            min_fail_cnt += 1
    print("Input {} times failed,Terminal will exit.".format(max_fail_cnt))
    sys.exit(0)


if __name__ == '__main__':
    main()
