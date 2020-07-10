from prettytable import PrettyTable
import loadUser
import os

USERFILE = os.path.abspath(os.path.dirname(__file__) + '/51reboot.txt')
FIELDS = ("name", "age", "tel", "email")


def displayUser(user_info):
    # dispaly page 2 pagesize 5
    # default = 5
    try:
        if len(user_info[1:]) >= 2 and len(user_info[1:]) <= 4:
            pagesize = 5
            if len(user_info[1:]) == 2:
                if user_info[1] == "page":
                    pagesize = 5
                else:
                    print("Display info invaild,Please input agein.")
                    # continue
            else:
                if user_info[1] == "page" and user_info[3] == "pagesize":
                    pagesize = int(user_info[-1])
                else:
                    print("Display info invaild,Please input agein.")
                    # continue
            page = int(user_info[2]) - 1
            RESULT = loadUser.loadUser(USERFILE)
            data = []
            for k, v in RESULT.items():
                data.append(v.values())
            start = page * pagesize
            end = start + pagesize
            print("Start: {},End: {}".format(start, end))
            xtb = PrettyTable()
            xtb.field_names = FIELDS
            for userinfo in data[start:end]:
                xtb.add_row(userinfo)
            print(xtb)
        else:
            print("Input info invaid,Please input again.")
            # continue
    except Exception as e:
        print(e)
