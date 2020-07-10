import saveUser
import loadUser
import os

FIELDS = ("name", "age", "tel", "email")
USERFILE = os.path.abspath(os.path.dirname(__file__) + '/51reboot.txt')


def addUser(info_list):
    if len(info_list) != 5:
        print("Add info invaild, Please add again.")
        return False
    username = info_list[1]
    RESULT = loadUser.loadUser(USERFILE)
    if username in RESULT:
        print("Username {} already exists.".format(username))
        return False
    else:
        RESULT[username] = dict(zip(FIELDS, info_list[1:]))
        print("Add {} success.".format(username))
        saveUser.saveUser(RESULT, USERFILE)
        return True
