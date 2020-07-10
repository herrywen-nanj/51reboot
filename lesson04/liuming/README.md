## 1: 用户管理系统 v3
```bash
v3版数据结构: 
{"username1": {"field1": "value1", "field2": "value2", " field3": "value3", "field4": "value4"}, }


全部用函数编程方式进行模块化
1. 登录认证，用户名密码序列化到文件及从文件反序列化（json模块实现）；
2. 提示可选操作，以及示例.
3. 增删改查和搜索
    3.1 增 add           # add monkey 18 132xxx monkey@51reboot.com
    3.2 删 delete        # delete user_name
    3.3 改 update        # update user_name set field_name = value
    3.4 查 list          # list
    3.5 搜 find          # find user_name
4. 格式化输出
5. 分页输出功能(支持回车翻页，跳转到指定页)
6. csv导入导出
7. 注销登录功能
8. 日志记录功能
    记录用户登录登出
    记录用户增删查改等其他操作(操作成功则记录)

```

<br />

## 主逻辑流程图  
![main_logic_flow_chart](./demon_pictures/主逻辑.jpg)

<br />

## 功能演示
```
# 演示执行
python u_m_s_demo_v2.py
```
> 登陆成功，操作提示  
![operation_prompt](./demon_pictures/operation_prompt.png)

<br />

> 注销登录功能演示  
![delete](./demon_pictures/logout_action.png)

<br />

> 分页功能演示   
![display](./demon_pictures/display_action.png)

<br />

> csv导入功能演示   
![load](./demon_pictures/load_action.png)

<br />

> csv导出功能演示  
![save](./demon_pictures/save_action.png)

<br />

> 增加功能演示  
![add](./demon_pictures/add_action.png)

<br />

> 查询所有功能  
![list](./demon_pictures/list_all_userinfo.png)  

<br />

> 条件查询功能  
![find](./demon_pictures/find_action.png)

<br />

> 更新功能  
![update](./demon_pictures/update_action.png)

<br />

> 删除功能演示  
![delete](./demon_pictures/delete_action.png)

<br />

> 删库跑路功能演示  
![delete](./demon_pictures/clean_action.png)

<br />
