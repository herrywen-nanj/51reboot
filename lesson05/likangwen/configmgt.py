import configparser


"""
# 普通用法
config = configparser.ConfigParser()    #初始化对象

config.read('./db.ini')
print(config.sections())    # 打印结果是一个列表，每个元素为db.ini的配置组的名称
print(dict(config['mysqld']))   # 返回结果是一个字典，内容是对应的配置组下的每个配置的内容，并且以key-value形式组合
"""

"""
# 普通版函数用法
## 只返回被定义并且调用的section
def ReadConfig(filename, section):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return "config init is empty", False

    if section in config.sections():
        return dict(config[section]), True
    else:
        return "{} config not found".format(section), False


con = ReadConfig('db.ini', 'aasdasds')  # 如果传递的section在配置文件有定义，那么就会返回对应的配置
print(con)
"""

# 升级版函数用法
## 如果传递了对应的key，会返回对应的key，对查询key配置更友好
def ReadConfig(filname, section, key=None):
    config = configparser.ConfigParser()
    config.read(filname)
    if not config.sections():
        return "config init is empty", False


    if section in config.sections():
        if key:  # 如果有传入key， 判断key是否存在对应的section配置里面
            if key in config[section]:  # 视频这里定义是有问题，如果section存在，key不存在，是会出错的
                return dict(config[section])[key], True  # 返回对应的key的值
            else:
                return '{} key config not found'.format(key), False
        else:   # 没key传入，直接返回对应的section
            return dict(config[section]), True
    else:
        return "{} section config not found".format(section), False

"""
con = ReadConfig('db.ini', 'mysqldasd', 'hahah')  # 如果传递的section在配置文件有定义，那么就会返回对应的配置
print(con)
"""