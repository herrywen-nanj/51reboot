from prettytable import PrettyTable
import loadUser
import os

USERFILE = os.path.abspath(os.path.dirname(__file__) + '/51reboot.txt')


def findUser(user_info):
    try:
        username = user_info[1]
        result = loadUser.loadUser(USERFILE)
        usernames = result.keys()
        xtb = PrettyTable()
        xtb.field_names = ["name", "age", "tel", "email"]
        if username in usernames:
            name = result[username]["name"]
            age = result[username]["age"]
            tel = result[username]["tel"]
            email = result[username]["email"]
            xtb.add_row([name, age, tel, email])
            print(xtb)
        else:
            print("\033[0;31;1muser {} not found.\033[0m".format(username))
    except Exception as e:
        print(e)
