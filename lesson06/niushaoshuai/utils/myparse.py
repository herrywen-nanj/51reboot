#!/usr/bin/python
# coding:UTF-8
#import ConfigParser # py2
import configparser

def getconfig(filename, section, key=None):
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


def setconfig(filename, section='', key='', value=''):
    cf = ConfigParser.ConfigParser()
    cf.read(filename)
    if not cf.has_section(section):
        cf.add_section(section)
    cf.set(section, key, value)
    cf.write(open(filename, 'w'))


def delconfig(filename, *pa):
    cf = ConfigParser.ConfigParser()
    cf.read(filename)
    if len(pa) > 2:
        print
        "paragram is too much"
    elif len(pa) == 2 and cf.remove_option(pa[0], pa[1]):
        cf.write(open(filename, 'w'))
    elif len(pa) == 1 and cf.remove_section(pa[0]):
        cf.write(open(filename, 'w'))
    else:
        print
        'section or option is not exist'


if __name__ == '__main__':
    conf = getconfig('../Config.ini', 'dbconfig')
    print(conf)
    #setconfig('im.conf', 'imlog2', 'port', '1090')
    #delconfig('im.conf', 'imlog2')