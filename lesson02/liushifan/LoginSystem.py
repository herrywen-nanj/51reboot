'''
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
'''
#标准模块
import sys
print("="*50)
print("   名片管理系统 V0.01")
print(" 1. 添加一个新的名片")
print(" 2. 删除一个名片")
print(" 3. 修改一个名片")
print(" 4. 查询一个名片")
print(" 5. 显示所有的名片")
print(" 6. 保存文件")
print(" 7. 加载文件")
print(" 8. 退出系统")
print("提示：用户:liusfgood 密码：123456")
print("="*50)

#定义变量
card_infors = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("liusfgood", "123456")

while INIT_FAIL_CNT < MAX_FAIL_CNT:
	
	username = input("请输入您的用户名: ")
	password = input("请输入您的密码: ")
	if username == USERINFO[0] and password == USERINFO[1]:
		while True:
			#获取用户的输入
			action = int(input("请输入您要执行的操作: "))
	#		info_list = info.split()
	#		action = info_list[0]
			#根据用户的数据执行相应的功能
			if action == 1:
				new_name = input("请输入您的名字：")
				new_qq = input("请输入您的QQ：")
				new_weixin = input("请输入微信：")
				new_addr = input("请输入的地址：")
				#定义一个新的字典，用来存储一个新的名片
				new_infor = {}
				new_infor['name'] = new_name
				new_infor['qq'] = new_qq
				new_infor['weixin'] = new_weixin
				new_infor['addr'] = new_addr
	
				#将一个字典，添加到列表中
				card_infors.append(new_infor)
			#	print(card_infors)
			elif action == 2:
				pass
			elif action == 3:
				pass
			elif action == 4:
				print("姓名\tQQ\t微信\t住址")
				for temp in card_infors:
					print("{}\t{}\t{}\t{}".format(temp['name'],temp['qq'],temp['weixin'],temp['addr']))
			elif action == 5:
				find_name = input("请输入要查找的姓名：")
				find_flag = 0 #默认表示没有找到
				for temp in card_infors:
					if find_name == temp['name']:
						print("姓名\tQQ\t微信\t住址")
						print("{}\t{}\t{}\t{}".format(temp['name'],temp['qq'],temp['weixin'],temp['addr']))
						find_flag = 1 #表示找到了
						break
			elif action == 6:
				f = open("backup.data","w")
				f.write(str(card_infors))
				f.close()
				print("保存成功")
			elif action == 7:
				try:
					f = open("backup.data")
					card_infors = eval(f.read())
					f.close()
					print("已读取。")
				except Exception:
					pass
			elif action == 8:
				sys.exit(0)
			else:
				print("无效的参数.")
	else:
		print("密码错误，请重新输入.")
		INIT_FAIL_CNT += 1
print("\n输入 {} 次,失败 ，退出.".format(MAX_FAIL_CNT))
