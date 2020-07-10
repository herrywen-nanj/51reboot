from . import configmgt
from . import uops,auth

def logic():
    while True:
        cmd_str = input("Please input commond: ")
        if len(cmd_str) == 0:
            print("command invalid.")
        cmd_str = cmd_str.split()
        action = cmd_str[0]
        args = cmd_str[1:]
        if action == 'add':
            uops.addUser(args)
        elif action == 'delete':
            uops.deleteUser(args)
        elif action == 'update':
            uops.updateUser(args)
        elif action == 'find':
            uops.findUser(args)
        elif action == 'list':
            uops.listUser()
        elif action == 'save':
            uops.mysql2csv()
        elif action == 'load':
            uops.csv2mysql()
        elif action == 'exit' or action == 'quit':
            uops.logout()
        else:
            print("input invalid.")

def main():
    init_fail_count = 0
    max_fail_count = 3
    while init_fail_count < max_fail_count:
        username = input("Please input username: ")
        password = input("Please input password: ")
        if auth.Auth(username, password):
            print("{}\nWelcome to User Management System\n{}".format('-'*40,'-'*40))
            logic()
        else:
            print("Username or password error.")
            init_fail_count += 1
    print("Game Over.")