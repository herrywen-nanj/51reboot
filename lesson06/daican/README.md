"""
用户管理系统
=================V1===================

1、登录认证；
2、增删改查和搜索
    2.1 增 add      # add monkey 12 132xxx monkey@51reboot.com
    2.2 删 delete   # delete mobkey
    2.3 改 update   # update monkey set age = 18
    2.4 查 list     # list
    2.5 搜 find     # find monkey
3、格式化输出
===================V2=================
1. 数据结构：列表 -> 字典；
2. 分页 display page 1 pagesize 5
3. 文件持久化
4. 异常处理
5. PrettyTable 优雅的格式化输出
6. 扩展：导出csv(可写可不写)
===================V3================
1. 函数:
将用户管理系统v2面向过程 升级为 函数式
2. 导出csv:
将用户列表导出csv文件
3. 日志审计:
通过logging模块，记录用户登录和删除操作即可，其它操作不需要记录。
日志级别为debug
====================V4================

1. 支持配置文件管理方式
- ConfigParser
2. 存储方式 由文件 改成 数据库
- PyMySQL
===================V5=================

优化， 改成面向对象的方式。

1.  增   add         : add monkey 12 132xxx monkey@51reboot.com
2.  删   delete      : delete monkey
3.  改   update      : update monkey set age = 20
4.  查   list        : list
5.  搜   find        : find monkey
6.  分页 display     : display page 2 pagesize 3 
7.  帮助 doc         : show help
8.  退出 exit        : exit
9.  保存 save        : save as 51reboot.txt
10. 加载 load        : load 51reboot.txt
11. 导出CSV saveCsv  : save as users.csv
12. 加载CSV loadCsv  : load from users.csv
13. 存到DB saveDB    : save to DB
14. 加载DB loadDB    : load from DB
"""