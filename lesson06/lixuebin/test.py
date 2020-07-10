# import configparser
# def ReadConf(section, key=None, filename='mysql.ini'):
#     try:
#         config = configparser.ConfigParser()
#         config.read(filename)
#         if not config.sections():
#             return "configure file error", False
#
#         if key:
#             if section in config.sections():
#                 return dict(config[section])['key'], True
#             else:
#                 return 'section not exists', False
#         else:
#             return dict(config[section]), True
#     except Exception as e:
#         return False
#
# msg, ok = (ReadConf('mysqld'))
# print(msg)
import pymysql

def MyConn():
    try:
        connect = pymysql.connect(
            host='127.0.0.1',
            username='lixuebin',
            password='lixuebin@123456',
            port=3306,
            database='ops',
        )
    except:
        return None
    return connect

conn = MyConn()


print(conn)
if not conn:
    print("connect Failed")
cursor = MyConn().cursor()
