import saveUser
import loadUser
import os

USERFILE = os.path.abspath(os.path.dirname(__file__) + '/51reboot.txt')


def updateUser(user_info):
    username = user_info[1]
    try:
        keyword = user_info[2]
        field = user_info[3]
        new_value = user_info[-1]
        mark = user_info[-2]
        if keyword != "set" or mark != "=":
            print("\033[0;31;1mupdate method error.\033[0m")
        else:
            result = loadUser.loadUser(USERFILE)
            usernames = result.keys()
            if username in usernames:
                if field == "age":
                    result[username]["age"] = new_value
                    saveUser.saveUser(result, USERFILE)
                    print("\033[0;31;1mupdate {} age success.\033[0m".format(username))
                elif field == "tel":
                    result[username]["tel"] = new_value
                    saveUser.saveUser(result, USERFILE)
                    print("\033[0;31;1mupdate {} tel success.\033[0m".format(username))
                elif field == "email":
                    result[username]["email"] = new_value
                    saveUser.saveUser(result, USERFILE)
                    print("\033[0;31;1mupdate {} email success.\033[0m".format(username))
                else:
                    print("\033[0;31;1mfield {} not found.\033[0m".format(field))
            else:
                print("\033[0;31;1muser {} not found.\033[0m".format(username))
    except Exception as e:
        print(e)
