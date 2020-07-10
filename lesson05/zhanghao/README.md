'''
用户管理系统 v4
1. 支持配置文件管理方式
- ConfigParser
2. 存储方式 由文件 改成 数据库
- PyMySQL
'''

'''
增加
删除
修改
列出
搜索
分页
退出


日志
'''

# ReadConfig(filename, section, key=None)
读取mysql连接信息

# connect()
连接mysql

# addUser(args)
添加用户到mysql

# deleteUser(agrs)
从mysql删除指定用户

# updateUser(agrs)
更新mysql中用户信息

# listUser()
列出mysql中数据

# findUser(agrs)
从mysql中搜索指定用户

# displayUser(args)
分页功能

# logout()
退出脚本

# opLog()
记录登录和删除日志

# loginAuth(username, password)
登录

# logic()
动作判断

# main()
脚本入口
