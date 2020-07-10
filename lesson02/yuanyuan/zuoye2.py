#用户管理系统

'''
登录认证； yuanyuan abc123
增删改查和搜索
 增 add    add username age tel email
 删 delete
 改 update  #update username set age = ''
 查 list
 搜 find
格式化输出
''' 

#导入模块
import sys

#定义参数
RESULT = []
USERINFO = ("yuanyuan","abc123")   #定义认证信息-元组，用圆括号，不能修改。
ini_fail_times = 0
Max_fail_times = 6
FIELDS = ['username', 'age', 'tel', 'email']
RESULT.append(FIELDS)
RESULT.remove(FIELDS)

 
while ini_fail_times < Max_fail_times:  
    username = input("please input username: ")
    password = input("plese input password: ")
    if USERINFO[0] == username and USERINFO[1] == password:
        while True:
            info = input("please input your operation: ")
            info_list = info.split()
            #print(info)
            #print(info_list)
            action = info_list[0]
            
            #业务操作
            if action == "add":
            #判断用户是否存在, 如果用户存在，提示用户已经存在， 不再添加
                for x in RESULT:
                    if x[0] == info_list[1]:
                            print("username have exist, please try again")
                            break
                else:       
                    RESULT.append(info_list[1:])
                    print("add success {}".format(info_list[1]))                            
                

            
            elif action == "delete":
                for x in RESULT:
                        if x[0] == info_list[1]:
                                RESULT.remove(x)
                print("delete success {}".format(info_list[1]))
                
            elif action == "update":
                for x in RESULT:
                        if x[0] == info_list[1]:
                                RESULT.remove(x)        
                RESULT.append(info_list[1:])
                print("update success {}".format(info_list[1]))
                
            elif action == "list":
                #print(RESULT)
                for x in RESULT:
                        print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                        print()
                        print("-" * 50)

            elif action == "find":
                for x in RESULT:
                        if x[0] == info_list[1]:
                                print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                                print()
                                print("-" * 50)

            elif action == "exit":
                    sys.exit(0)

            else:
                    print("invalid action")
    
    else:
            print('\033[7;31musername or password error.\033[1;31;40m')
            ini_fail_times += 1

print("\nInput {} failed, Terminal will exit.".format(Max_fail_times))
        
        
     
 
