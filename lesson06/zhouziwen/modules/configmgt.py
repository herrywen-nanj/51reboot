import configparser

def ReadConfig(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return "Config init is empty", False
    if key:
        if section in config.sections():
            return dict(config[section])[key], True
        else:
            return 'section not found', False
    else:
        return dict(config[section]), True

# result, ok = ReadConfig('config.ini','dbinfo','host')
# print(result)