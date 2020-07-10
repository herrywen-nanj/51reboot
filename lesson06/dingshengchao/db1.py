import pymysql
conn = pymysql.connect(
    host = "10.0.2.15",
    user = "dingsc",
    password= "123456",
    database = "ops",
    port = 3306,
)
cur = conn.cursor()
#sql = '''insert into users(username,age,tel,email)  values('monkey2', 12,'132xxx','monkey2@51reboot.com');'''
#sql = '''update users set age = 20 where username = "monkey2";'''
#sql = '''select * from users;'''
sql = '''delete fdfd from users;'''
print(sql)

cur.execute(sql)
conn.commit()
data = cur.fetchall()
print(data)
cur.close()
conn.close()