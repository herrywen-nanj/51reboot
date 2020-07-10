
import pymysql


'''
def __init__(self, host=None, user=None, password="",
                 database=None, port=0, unix_socket=None,
                 charset='', sql_mode=None,
                 read_default_file=None, conv=None, use_unicode=None,
                 client_flag=0, cursorclass=Cursor, init_command=None,
                 connect_timeout=10, ssl=None, read_default_group=None,
                 compress=None, named_pipe=None,
                 autocommit=False, db=None, passwd=None, local_infile=False,
                 max_allowed_packet=16*1024*1024, defer_connect=False,
                 auth_plugin_map=None, read_timeout=None, write_timeout=None,
                 bind_address=None, binary_prefix=False, program_name=None,
                 server_public_key=None):
'''

# 创建连接
conn = pymysql.connect(
    host = "10.0.2.15",
    user = "monkey",
    password= "123456",
    database = "ops",
    port = 3306,
)

'''
CREATE TABLE users
(
id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
username varchar(32),
age int,
tel varchar(11),
email varchar(50)
);
'''

# 创建游标
cur = conn.cursor()

# 增加记录
#sql = '''insert into users(username,age,tel,email)  values('monkey2', 12,'132xxx','monkey2@51reboot.com');'''

# 修改记录
# sql = '''update users set age = 20 where username = "monkey1";'''

# 查询记录
# sql = '''select * from users;'''

# 删除记录
sql = '''delete from users where username = "monkey1"'''

print(sql)

cur.execute(sql)
conn.commit()

# 从游标里获取所有的数据
# data = cur.fetchall()
# data = cur.fetchmany(2)
# print(data)

# 关闭游标
cur.close()

# 关闭连接
conn.close()