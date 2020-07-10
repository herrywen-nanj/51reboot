from prettytable import PrettyTable
import loadUser
import os

USERFILE = os.path.abspath(os.path.dirname(__file__) + '/51reboot.txt')


def listUser():
    try:
        result = loadUser.loadUser(USERFILE)
        xtb = PrettyTable()
        xtb.field_names = ["name", "age", "tel", "email"]
        for v in result.values():
            name = v["name"]
            age = v["age"]
            tel = v["tel"]
            email = v["email"]
            xtb.add_row([name, age, tel, email])
        print(xtb)
    except Exception as e:
        print(e)
