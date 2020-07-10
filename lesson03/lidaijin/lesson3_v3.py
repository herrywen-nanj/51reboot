"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
    3.6 保存 save        # save
    3.7.查看csv内容       # load
    3.8 分页             # display page 1 pagesize 5
3. 格式化输出
"""

import sys,json,os,csv,time
from prettytable import PrettyTable

msg = '''
1. 增 add           # add monkey 12 132xxx monkey@51reboot.com
2. 删 delete        # delete monkey
3. 改 update        # update monkey set age = 18
4. 查 list          # list
5. 搜 find          # find monkey
6. 保存 save        # save
7. 查看csv内容       # load
8. 分页             # display page 1 pagesize 5
'''

print(msg)

USERINFO = ("test","123456")
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
#RESULT = {}
FILENAME = "51reboot.txt"
LOG_FILE = "51reboot.log"

try:
    try:
        if os.path.exists("51reboot.txt"):
            f_num = open('51reboot.txt', 'r', encoding='utf-8')
        else:
            f_num = open('51reboot.txt', 'w', encoding='utf-8')
    #FileNotFoundError
    except :
        RESULT = {}
        f_num.close()
    else:
        size = os.path.getsize('51reboot.txt')
        if  size == 0 :
            RESULT = {}
            f_num.close()
        else:
            RESULT = eval(f_num.read())
            f_num.close()

    try:
        log = open("51reboot.log","a",encoding="utf-8")
    except :
        os.mknod("51reboot.log")

    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        username = input("Please input your username: ")
        password = input("Please input your password: ")
        if username == USERINFO[0] and password == USERINFO[1]:
            try:
                while True:
                    info = input("Please input your operation:")
                    info_list = info.split()
                    tm = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    lg = "{}  {}".format(tm,info)
                    log.write(lg)
                    log.write("\n")
                    log.flush()
                    #log.close()
                    try:
                        peration = info_list[0]
                    except:
                        print("Input is wrong")
                    else:
                        if peration == "add":
                            if len(info_list) == 5:
                                if info_list[1] not in RESULT:
                                    content = {"age":info_list[2],"tel":info_list[3],"emial":info_list[4]}
                                    #print(info_list[1])
                                    #print(content)
                                    #print(RESULT)
                                    RESULT[info_list[1]] = content
                                    #print(RESULT)
                                    print("Added {} user successfully".format(info_list[1]))
                                    lg = "{}  Added {} user successfully".format(tm, info_list[1])
                                    log.write(lg)
                                    log.write("\n")
                                    log.flush()
                                else:
                                    print("User {} exists".format(info_list[1]))
                            else:
                                print("Grammar mistakes")

                        elif peration == "delete":
                            if len(info_list) == 2:
                                if info_list[1] in RESULT:
                                    RESULT.pop(info_list[1])
                                    print("Delete user {} succeeded".format(info_list[1]))
                                    lg = "{}  Delete user {} succeeded".format(tm, info_list[1])
                                    log.write(lg)
                                    log.write("\n")
                                    log.flush()
                                else:
                                    print("User {} does not exist".format(info_list[1]))
                            else:
                                print("Grammar mistakes")

                        elif peration == "update":

                            if len(info_list) == 6:
                                if info_list[1] in RESULT:
                                    if  info_list[2] == "set" and info_list[-2] == "=":
                                        old = RESULT[info_list[1]][info_list[3]]
                                        RESULT[info_list[1]][info_list[3]] = info_list[-1]
                                        lg = "{}  {} has been modified to {}".format(tm,old,info_list[-1] )
                                        log.write(lg)
                                        log.write("\n")
                                        log.flush()
                                    else:
                                        print("Grammar mistakes")
                                else:
                                    print("User {} does not exist".format(info_list[1]))
                            else:
                                print("Grammar mistakes")

                        elif peration == "list":
                            li,t2 = [],[]
                            xtb = PrettyTable()
                            xtb.field_names = ["username", "age", "tel", "email"]
                            for x,i in RESULT.items():
                                b = i.values()
                                t = list(b)
                                if x not in t2:
                                    t.insert(0, x)
                                    t2 = t
                                    li.append(t)
                            for g in li:
                                xtb.add_row(g)
                            print(xtb)

                        elif peration == "find":
                            if len(info_list) == 2:
                                xtb = PrettyTable()
                                xtb.field_names = ["username", "age", "tel", "email"]
                                if info_list[1] in RESULT:
                                    test = list(RESULT[info_list[1]].values())
                                    #print(test)
                                    test.insert(0,info_list[1])
                                    xtb.add_row(test)
                                    print(xtb)
                                #print(RESULT[info_list[1]])
                                else:
                                    print("User {} does not exist".format(info_list[1]))
                            else:
                                print("Grammar mistakes")

                        elif peration == "save":
                            if len(info_list) == 1:
                                li, t2 = [], []
                                a = ["username", "age", "tel", "email"]
                                if os.path.exists("test.csv"):
                                    #os.mknod("test.csv")
                                    fd = open("test.csv", 'w',newline='')
                                    #fd.write(json.dumps(RESULT))
                                    csv_write = csv.writer(fd, dialect='excel')
                                    for x, i in RESULT.items():
                                        b = i.values()
                                        t = list(b)
                                        if x not in t2:
                                            t.insert(0, x)
                                            t2 = t
                                            li.append(t)
                                    csv_write.writerow(a)
                                    for i in  li:
                                        csv_write.writerow(i)
                                else:
                                    os.mknod("test.csv")
                                    fd = open("test.csv", 'a', newline='')
                                    # fd.write(json.dumps(RESULT))
                                    csv_write = csv.writer(fd, dialect='excel')
                                    for x, i in RESULT.items():
                                        b = i.values()
                                        t = list(b)
                                        if x not in t2:
                                            t.insert(0, x)
                                            t2 = t
                                            li.append(t)
                                    csv_write.writerow(a)
                                    for i in li:
                                        csv_write.writerow(i)

                                fd.close()

                                f_txt = open(FILENAME, 'w')
                                f_txt.write(json.dumps(RESULT))
                                f_txt.close()

                                #print("Save file:{} succ.".format(FILENAME))

                                print("Save file:{} succ.".format(FILENAME))
                            else:
                                print("Grammar mistakes")

                        elif peration == "load":
                            if len(info_list) == 1:
                                try:
                                    fd = open("test.csv", 'r')
                                    data = fd.read()
                                    #RESULT = json.loads(data)
                                    #print(RESULT)
                                    #print(data)
                                    #fd.close()
                                except:
                                    print("No data")
                                else:
                                    print(data)
                                    fd.close()
                            else:
                                print("Grammar mistakes")

                        elif peration == "display":
                            if len(info_list) == 5:
                                xtb = PrettyTable()
                                xtb.field_names = ["username", "age", "tel", "email"]
                                li,t2 = [],[]
                                for x, i in RESULT.items():
                                    b = i.values()
                                    t = list(b)
                                    if x not in t2:
                                        t.insert(0, x)
                                        t2 = t
                                        li.append(t)
                                try:
                                    page = int(info_list[2])
                                    line = int(info_list[-1])
                                    start = (page - 1) * line
                                    end = line * page
                                except ValueError:
                                    print("Input no number,Please re-enter.")

                                else:
                                    for j in li[start:end]:
                                        xtb.add_row(j)
                                    print(xtb)
                            else:
                                print("Grammar mistakes")

                        elif peration == "exit":
                            if len(info_list) == 1:
                                sys.exit()
                            else:
                                print("Grammar mistakes")
                        else:
                            print("The input is invalid")
            except:
                if peration == "exit":
                    sys.exit()
    else:
        INIT_FAIL_CNT += 1
        print("\033[5;31musername or password error.\033[0m\n")
except:
    print("Abnormal exit")