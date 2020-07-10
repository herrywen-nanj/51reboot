#用户管理系统 V2 数据结构修改为字典,增加持久化存储

'''
登录认证； yuanyuan abc123
增删改查和搜索
 增 add    add username age tel email
 删 delete
 改 update  #update username set age = ''
 查 list
 搜 find
 add yy 24 133504XXX yy@126.com
格式化输出
''' 

#导入模块
import sys
import json
import prettytable as pt

#定义参数
RESULT = {}
USERINFO = ("yuanyuan","abc123")   #定义认证信息-元组，用圆括号，不能修改。
ini_fail_times = 0
Max_fail_times = 6
FIELDS = {}
 
while ini_fail_times < Max_fail_times:  
    username = input("please input username: ")
    password = input("plese input password: ")
    if USERINFO[0] == username and USERINFO[1] == password:
        while True:
            print('_____________________\nadd: add username age tel mail\ndelete: delete username\nupdate: update username set age = x\nlist: list\nfind: find username')
            info = input("please input your operation:")
            info_list = info.split()
            #print(info)
            #print(info_list)
            action = info_list[0]
            
            #业务操作
            if action == "add":
            #判断用户是否存在, 如果用户存在，提示用户已经存在， 不再添加
                for x in RESULT.keys():
                    if x == info_list[1]:
                            print("username have exist, please try again")
                            break
                else:       
                    RESULT[info_list[1]] = info_list[2:]
                    fd = open("51reboot.txt",'w')
                    fd.write(json.dumps(RESULT))
                    fd.close()
                    print("add success {}".format(info_list[1]))
                print(RESULT)
                           
            elif action == "delete":
                fd = open("51reboot.txt",'r+')
                list = fd.read()
                dict = json.loads(list)
                dict.pop(info_list[1])
                fd.seek(0)
                fd.truncate()
                fd.write(json.dumps(dict))
                fd.close()
                print("delete success {}".format(info_list[1]))
                
            elif action == "update":  
            #update username set age = 28
                fd = open("51reboot.txt",'r+')
                list = fd.read()
                dict = json.loads(list)
                
                username1 = info_list[1]
                where = info_list[2]
                fuhao = info_list[4]

                if where != "set" or fuhao != "=":
                    print("Update method error. ")
                    break
                
                NAMES = dict.get(info_list[1])
               
                if info_list[3] == "age":
                    NAMES[0] = info_list[-1]
                elif info_list[3] == "tel":
                    NAMES[1] = info_list[-1]
                elif info_list[3] == "email":
                    NAMES[2] = info_list[-1]
                else:
                    print("User {} not found.".format(username1)) 
                
                dict.pop(info_list[1])
                fd.seek(0)
                fd.truncate()
                dict[username1] = NAMES
                fd.write(json.dumps(dict))
                fd.close()
                
                print("update success {}".format(info_list[1]))

            elif action == "list":  
            #list
                fd = open("51reboot.txt",'r')
                list1 = fd.read()
                dict = json.loads(list1)
                fd.close()
                tb = pt.PrettyTable()
                for k,v in dict.items():
                    v.insert(0,k)                    
                    tb.add_row(v)
                tb.field_names = ["USERNAME","AGE","TEL","EMAIL"]
                print(tb)
                print()

            elif action == "find":  
            #find
                #print("{} :{}".format(info_list[1],''.join(RESULT[info_list[1]])))
                fd = open("51reboot.txt",'r')
                list = fd.read()
                dict = json.loads(list)
                fd.close()
                tb = pt.PrettyTable()
                f = dict.get(info_list[1])
                f.insert(0,info_list[1])                 
                tb.add_row(f)
                tb.field_names = ["USERNAME","AGE","TEL","EMAIL"]
                print(tb)


            elif action == "exit":  
            #Exit
                    sys.exit(0)

            else:
                    print("invalid action")
    
    else:
            print('\033[7;31musername or password error.\033[1;31;40m')
            ini_fail_times += 1

print("\nInput {} failed, Terminal will exit.".format(Max_fail_times))
