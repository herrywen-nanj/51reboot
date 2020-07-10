import configparser
'''
config = configparser.ConfigParser()


config.read('db.ini')
print(config.sections())

print(dict(config['mysqld'])['symbolic-links'])
'''

def ReadConfig(filename, section, key=None):
    print(filename)
    config = configparser.ConfigParser()
    config.read(filename)
    print(config.sections())
    if not config.sections():
        return "config init is empty", False

    if key:
        if section in config.sections():
            return dict(config[section])[key], True
        else:
            return '', False
    else:
        return dict(config[section]), True


result, ok = ReadConfig('db.ini', 'mysqld', 'socket')
print(ok)
print(result)

if __name__ == '__main__':
    ReadConfig('db.ini','mysqld','socket')