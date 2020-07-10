
## 日志

时间为w3c格式

```
22/Jun/2019 15:22:54 v3_csv_log_func.py[line:128] DEBUG login succeed
22/Jun/2019 15:24:59 v3_csv_log_func.py[line:128] DEBUG login succeed
22/Jun/2019 15:26:34 v3_csv_log_func.py[line:128] DEBUG login succeed
22/Jun/2019 15:27:26 v3_csv_log_func.py[line:128] DEBUG login succeed
22/Jun/2019 15:27:48 v3_csv_log_func.py[line:158] DEBUG user 'test005' has been deleted
```

## 操作

```bash

[root@51reboot louxiaohui]# ./v3_csv_log_func.py   
Please input your username: admin
Please input your password: 123456
Please input the action and info: list
+---------+-----+-------------+-------------+
|   name  | age |     tel     |    email    |
+---------+-----+-------------+-------------+
| test002 |  19 | 18233335681 | 6668@qq.com |
| test001 |  16 | 18233335680 | 6667@qq.com |
| test003 |  20 | 18233335682 | 6669@qq.com |
| test004 |  21 | 18233335683 | 6670@qq.com |
| test005 |  22 | 18233335684 | 6671@qq.com |
| test006 |  23 | 18233335685 | 6672@qq.com |
| test007 |  24 | 18233335686 | 6673@qq.com |
+---------+-----+-------------+-------------+
Please input the action and info: save
test001 {'name': 'test001', 'age': '16', 'tel': '18233335680', 'email': '6667@qq.com'}
test002 {'name': 'test002', 'age': '19', 'tel': '18233335681', 'email': '6668@qq.com'}
test003 {'name': 'test003', 'age': '20', 'tel': '18233335682', 'email': '6669@qq.com'}
test004 {'name': 'test004', 'age': '21', 'tel': '18233335683', 'email': '6670@qq.com'}
test005 {'name': 'test005', 'age': '22', 'tel': '18233335684', 'email': '6671@qq.com'}
test006 {'name': 'test006', 'age': '23', 'tel': '18233335685', 'email': '6672@qq.com'}
test007 {'name': 'test007', 'age': '24', 'tel': '18233335686', 'email': '6673@qq.com'}
save to user_info.csv succeed, status: True
Please input the action and info: find test003 
+---------+-----+-------------+-------------+
|   name  | age |     tel     |    email    |
+---------+-----+-------------+-------------+
| test003 |  20 | 18233335682 | 6669@qq.com |
+---------+-----+-------------+-------------+
Please input the action and info: display page 2 pagesize 3 
+---------+-----+-------------+-------------+
|   name  | age |     tel     |    email    |
+---------+-----+-------------+-------------+
| test004 |  21 | 18233335683 | 6670@qq.com |
| test005 |  22 | 18233335684 | 6671@qq.com |
| test006 |  23 | 18233335685 | 6672@qq.com |
+---------+-----+-------------+-------------+
Please input the action and info: delete test005 
user 'test005' has been deleted, status: True
Please input the action and info: display page 2 pagesize 3
+---------+-----+-------------+-------------+
|   name  | age |     tel     |    email    |
+---------+-----+-------------+-------------+
| test004 |  21 | 18233335683 | 6670@qq.com |
| test006 |  23 | 18233335685 | 6672@qq.com |
| test007 |  24 | 18233335686 | 6673@qq.com |
+---------+-----+-------------+-------------+
Please input the action and info: llist

 invalid action. 
Please input the action and info: list
+---------+-----+-------------+-------------+
|   name  | age |     tel     |    email    |
+---------+-----+-------------+-------------+
| test002 |  19 | 18233335681 | 6668@qq.com |
| test001 |  16 | 18233335680 | 6667@qq.com |
| test003 |  20 | 18233335682 | 6669@qq.com |
| test004 |  21 | 18233335683 | 6670@qq.com |
| test006 |  23 | 18233335685 | 6672@qq.com |
| test007 |  24 | 18233335686 | 6673@qq.com |
+---------+-----+-------------+-------------+
Please input the action and info: exit

``
