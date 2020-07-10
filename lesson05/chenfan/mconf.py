import configparser
# 配置文件解析模块

def ReadConfig(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return "Config init is empty", False

    if key == None:
        if section in config.sections():
            return dict(config[section][key]), True
        return '', False
    else:
        return dict(config[section]),True

# result,ok = ReadConfig("mysql.ini","mydb","host")
# print(ok)
# print(result)

