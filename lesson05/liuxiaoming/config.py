import configparser

def ReadConfig(filename,section,key=None):
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