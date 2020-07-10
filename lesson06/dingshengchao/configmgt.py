import configparser
'''
config = configparser.ConfigParser()

config.read('51reboot.ini')
print(config.sections())

print(dict(config['mysqld'])['symbolic-links'])
'''

def ReadConfig(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return "config init is empty", False

    if key:
        if section in config.sections():
            return dict(config[section])[key], True
        else:
            return '', False
    else:
        return dict(config[section]), True


result, ok = ReadConfig('51reboot.ini', 'mysqld', 'socket')
# print(ok)
# print(result)