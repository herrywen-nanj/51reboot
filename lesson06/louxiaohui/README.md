
## 日志

时间为w3c格式

```bash
# cat log/app.log                
27/Jun/2019 00:00:35 v4_pymysql_ConfigParser.py[line:143] DEBUG login succeed
27/Jun/2019 00:04:20 v4_pymysql_ConfigParser.py[line:144] DEBUG login succeed
27/Jun/2019 00:42:48 v4_pymysql_ConfigParser.py[line:144] DEBUG login succeed
27/Jun/2019 00:43:18 v4_pymysql_ConfigParser.py[line:109] INFO Insert succ.
27/Jun/2019 00:43:18 v4_pymysql_ConfigParser.py[line:110] DEBUG insert into users(username, age, tel, email) values('test006', 23, '18233335685', '6672@qq.com');
```

## 操作

```bash

[root@51reboot louxiaohui]# ./v4_pymysql_ConfigParser.py 
Please input your username: admin
Please input your password: 123456
Please input the action and info: list
There is no user in system, status: False
Please input the action and info: load
load succeed.
Please input the action and info: 
invalid input info,pls input again
Please input the action and info: list
+----------+-----+-------------+-----------------------+
|   name   | age |     tel     |         email         |
+----------+-----+-------------+-----------------------+
| monkey10 |  10 |    132xxx   | monkey10@51reboot.com |
| monkey11 |  11 |    132xxx   | monkey11@51reboot.com |
| monkey12 |  12 |    132xxx   | monkey12@51reboot.com |
| monkey13 |  13 |    132xxx   | monkey13@51reboot.com |
| monkey14 |  14 |    132xxx   | monkey14@51reboot.com |
| monkey15 |  15 |    132xxx   | monkey15@51reboot.com |
| monkey16 |  16 |    132xxx   | monkey16@51reboot.com |
| monkey17 |  17 |    132xxx   | monkey17@51reboot.com |
| monkey18 |  18 |    132xxx   | monkey18@51reboot.com |
| monkey19 |  19 |    132xxx   | monkey19@51reboot.com |
| monkey20 |  20 |    132xxx   | monkey20@51reboot.com |
| monkey21 |  21 |    132xxx   | monkey21@51reboot.com |
| monkey22 |  22 |    132xxx   | monkey22@51reboot.com |
| monkey23 |  23 |    132xxx   | monkey23@51reboot.com |
| monkey24 |  24 |    132xxx   | monkey24@51reboot.com |
| monkey25 |  25 |    132xxx   | monkey25@51reboot.com |
| monkey26 |  26 |    132xxx   | monkey26@51reboot.com |
| monkey27 |  27 |    132xxx   | monkey27@51reboot.com |
| monkey28 |  28 |    132xxx   | monkey28@51reboot.com |
| monkey29 |  29 |    132xxx   | monkey29@51reboot.com |
| test010  |  25 | 18233335686 |      6673@qq.com      |
| test009  |  25 | 18233335686 |      6673@qq.com      |
| test007  |  24 | 18233335686 |      6673@qq.com      |
+----------+-----+-------------+-----------------------+
Please input the action and info: add test006 23 18233335685 6672@qq.com
add 'test006 23 18233335685 6672@qq.com' succeed, status: True
Please input the action and info: list
+----------+-----+-------------+-----------------------+
|   name   | age |     tel     |         email         |
+----------+-----+-------------+-----------------------+
| monkey10 |  10 |    132xxx   | monkey10@51reboot.com |
| monkey11 |  11 |    132xxx   | monkey11@51reboot.com |
| monkey12 |  12 |    132xxx   | monkey12@51reboot.com |
| monkey13 |  13 |    132xxx   | monkey13@51reboot.com |
| monkey14 |  14 |    132xxx   | monkey14@51reboot.com |
| monkey15 |  15 |    132xxx   | monkey15@51reboot.com |
| monkey16 |  16 |    132xxx   | monkey16@51reboot.com |
| monkey17 |  17 |    132xxx   | monkey17@51reboot.com |
| monkey18 |  18 |    132xxx   | monkey18@51reboot.com |
| monkey19 |  19 |    132xxx   | monkey19@51reboot.com |
| monkey20 |  20 |    132xxx   | monkey20@51reboot.com |
| monkey21 |  21 |    132xxx   | monkey21@51reboot.com |
| monkey22 |  22 |    132xxx   | monkey22@51reboot.com |
| monkey23 |  23 |    132xxx   | monkey23@51reboot.com |
| monkey24 |  24 |    132xxx   | monkey24@51reboot.com |
| monkey25 |  25 |    132xxx   | monkey25@51reboot.com |
| monkey26 |  26 |    132xxx   | monkey26@51reboot.com |
| monkey27 |  27 |    132xxx   | monkey27@51reboot.com |
| monkey28 |  28 |    132xxx   | monkey28@51reboot.com |
| monkey29 |  29 |    132xxx   | monkey29@51reboot.com |
| test010  |  25 | 18233335686 |      6673@qq.com      |
| test009  |  25 | 18233335686 |      6673@qq.com      |
| test007  |  24 | 18233335686 |      6673@qq.com      |
| test006  |  23 | 18233335685 |      6672@qq.com      |
+----------+-----+-------------+-----------------------+
Please input the action and info: save
save to user_info.csv succeed, status: True

``
