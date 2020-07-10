import sys,json,os,csv,logging
from prettytable import PrettyTable

msg = '''
1. 增 add           # add monkey 12 132xxx monkey@51reboot.com
2. 删 delete        # delete monkey
3. 改 update        # update monkey set age = 18
4. 查 list          # list
5. 搜 find          # find monkey
6. 保存 save        # save
7. 加载 load        # load
8. 分页 display     # display page 1 pagesize 5
'''


USERINFO = ("51reboot","123456")
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
RESULT = {}
info_list = []
FILENAME = "51reboot.txt"

def log(info):
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                        filename='51reboot.log',
                        filemode='a'
                        )
    return logging.debug(info)


def add():
    if info_list[1] not in RESULT:
        content = {"name": info_list[1],"age": info_list[2], "tel": info_list[3], "emial": info_list[4]}
        RESULT[info_list[1]] = content
    else:
        print("User {} exists".format(info_list[1]))

def delete():
    if info_list[1] in RESULT:
        RESULT.pop(info_list[1])
        print("Delete user {} succeeded".format(info_list[1]))
        log('del {} succeeded'.format(info_list[1]))
    else:
        print("User {} does not exist".format(info_list[1]))
        log('del {} failure'.format(info_list[1]))
        
def update():
    if info_list[2] == "set" and info_list[-2] == "=":
        RESULT[info_list[1]][info_list[3]] = info_list[-1]
    else:
        print("User {} does not exist".format(info_list[1]))

def list():
    xtb = PrettyTable()
    xtb.field_names = ["username", "age", "tel", "email"]
    for i,x in RESULT.items():
        b = RESULT[i].values()
        xtb.add_row(b)
    print(xtb)

def find():
    xtb = PrettyTable()
    xtb.field_names = ["username", "age", "tel", "email"]
    if info_list[1] in RESULT:
        g = RESULT[info_list[1]].values()
        xtb.add_row(g)
        print(xtb)
    else:
        print("User {} does not exist".format(info_list[1]))

def save_csv():
    head = ["username", "age", "tel", "email"]
    if os.path.exists("test.csv"):
        fd = open("test.csv", 'w', newline='')
        csv_write = csv.writer(fd, dialect='excel')
        for i, x in RESULT.items():
            b = RESULT[i].values()
            csv_write.writerow(b)
    else:
        os.mknod("test.csv")
        fd = open("test.csv", 'w', newline='')
        csv_write = csv.writer(fd, dialect='excel')
        csv_write.writerow(head)
        for i, x in RESULT.items():
            b = RESULT[i].values()
            csv_write.writerow(b)
    fd.close()

def save_txt():
    f_txt = open(FILENAME, 'w')
    f_txt.write(json.dumps(RESULT))
    f_txt.close()

def load():
    try:
        f_num = open('51reboot.txt', 'r', encoding='utf-8')
    except Exception:
        RESULT = {}
        #f_num.close()
    else:
        size = os.path.getsize('51reboot.txt')
        if size == 0:
            RESULT = {}
            f_num.close()
        else:
            RESULT = eval(f_num.read())
            f_num.close()
    return RESULT


def display():
    xtb = PrettyTable()
    xtb.field_names = ["username", "age", "tel", "email"]
    li = []
    for i,x in RESULT.items():
        b = RESULT[i].values()
        li.append(b)
    #print(li)
    
    page = int(info_list[2])
    line = int(info_list[-1])
    start = (page - 1) * line
    end = line * page
    #print(start,end)
    for j in li[start:end]:
        xtb.add_row(j)
    print(xtb)

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    password = input("Please input your password: ")

    if username == USERINFO[0] and password == USERINFO[1]:
        print("Login successful")
        print(msg)
        log('Log in successfully')
        RESULT = load()
        while True:
            try:
                info = input("Please input your operation:")
                info_list = info.split()
                peration = info_list[0]
                if peration == "add":
                    add()
                elif peration == "delete":
                    delete()
                elif peration == "update":
                    update()
                elif peration == "list":
                    list()
                elif peration == "find":
                    find()
                elif peration == "load":
                    RESULT=load()
                elif peration == "save":
                    save_csv()
                    save_txt()
                elif peration == "display":
                    display()
                elif peration == "exit":
                    sys.exit()
                else:
                    print("The input is invalid")
            except Exception as error:
                print(error)
    else:
        INIT_FAIL_CNT += 1
        print("\033[5;31musername or password error.\033[0m\n")
