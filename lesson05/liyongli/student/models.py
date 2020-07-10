# -*- coding:utf-8 -*-
# author: lyl
import peewee
import configmgt


config_file = 'db_config.ini'
admin_user = {"username": "51reboot", "password": '123456', "roles": "admin"}

def initialize():
    cfg, ok = configmgt.ReadConfig(config_file, 'rebootdb')
    if not ok:
        print(cfg)
        exit(1)
    return cfg


config = initialize()

try:
    db = peewee.MySQLDatabase(database=config['database'], host=config['host'], user=config['username'], passwd=config['password'])
except Exception as e:
    print(e)



class student(peewee.Model):
    id = peewee.PrimaryKeyField()
    username = peewee.CharField(32,unique=True)
    age = peewee.IntegerField(11)
    phone = peewee.CharField(11)
    email = peewee.CharField(50)

    class Meta:
        database = db


class user(peewee.Model):
    id = peewee.PrimaryKeyField()
    username = peewee.CharField(32, unique=True)
    password = peewee.CharField(32)
    roles = peewee.CharField(10)

    class Meta:
        database = db


if __name__ == "__main__":
    try:
        student.create_table()
    except Exception as e:
        print(e)

    try:
        user.create_table()
        user.insert(admin_user).execute()
    except Exception as e:
        print(e)
