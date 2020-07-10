# git pull --rebase origin master
# git push -u origin master

import sys

flag = 0
user_info = ["51reboot","123456"]
user_list = ["lesson01","lesson02"]

def add_user():
    user_add = input("Please enter the user to join:")
    if user_add in user_list:
        print("The user is exist")
    else:
        user_list.append(user_add)
        print("The list after add user:",user_list)
        exit

def del_user():
    user_del = input("Please enter the user you want to delete:")
    if user_del in user_list:
        print("user: {user} will be delete.".format(user=user_del))
        user_list.remove(user_del)
        print("The list after delete user:",user_list)
    else:
        print("User does not exist")
        exit

def update_user():
    user_update = input("Please enter the user you want to update:")
    user_after_update = input("Please enter the user after update:")
    if user_update in user_list:
        print("user: {user} will be update.".format(user=user_update))
        ind = user_list.index(user_update)
        user_list[ind] = user_after_update
        print("The list after upate user:",user_list)
    else:
        print("User does not exist")
        exit

def find_user():
    user_find = input("Please enter the user to find:")
    if user_find in user_list:
        print("The user is exist")
    else:
        print("The user is not exist")
        exit

def list_user():
    print(user_list)

while 1:
    try:
        username = input("please input username: ")
        password = input("plese input password: ")
        if username == user_info[0] and password == user_info[1]:
            flag = 1
            print('Welcome back：',username)
            cmd = input("\033[32;1mPlease input will run command: \033[0m")
            if flag == 1 and cmd == "add":
                print(cmd)
                add_user()
                break
            elif flag == 1 and cmd == "delete":
                print("Original list",user_list)
                print(cmd)
                del_user()
                break
            elif flag == 1 and cmd == "update":
                print(cmd)
                update_user()
                break
            elif flag == 1 and cmd == "list":
                print(cmd)
                list_user()
                break
            elif flag == 1 and cmd == "find":
                print(cmd)
                find_user()
                break
            elif flag == 1 and cmd == "exit":
                break
            else:
                break
        else:
            print('username or password is wrong')
            break
    except KeyboardInterrupt:
        print("\n\033[31;1mbye bye!\033[0m")
        break
