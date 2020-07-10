# CREATE DATABASE IF NOT EXISTS ops  DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
# CREATE TABLE users (id  INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,username varchar(32),age int, tel varchar(11), email varchar(50));

import pymysql
# import configmgt
from . import configmgt

FILENAME = "/home/vagrant/51reboot/zuoye/day5/utils/db_config.cfg"
SECTIONS = "dbinfo"

def connet():
    cfg, ok = configmgt.ReadConfig(FILENAME, SECTIONS)
    if not cfg:
        return cfg, False
    try:
        conn = pymysql.connect(
            host=cfg['host'],
            user=cfg['user'],
            password=cfg['password'],
            database=cfg['database'],
            port=int(cfg['port']),
        )
    except:
        return None
    return conn

def insert(sql,*args, **kwargs):
    conn = connet()
    if not conn:
        return "Connect DB fail.", False
    cur = conn.cursor()
    try:
        cur.executemany(sql)
        conn.commit()
        return "Insert Success.", True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def update(sql,*args, **kwargs):
    conn = connet()
    if not conn:
        return "Connect DB fail.", False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        if  cur.rowcount == 0:
            return "Update Fail.", False
        conn.commit()
        return "Update Success.", True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def select(sql,*args, **kwargs):
    conn = connet()
    if not conn:
        return "Connect DB fail.", False
    cur = conn.cursor()
    try:
        cur.execute(sql)
    except Exception as e:
        return e, False
    else:
        rows = cur.fetchall()
        return rows, True
    finally:
        cur.close()
        conn.close()

def delete(sql,*args, **kwargs):
    conn = connet()
    if not conn:
        return "Connect DB fail.", False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        if cur.rowcount == 0:
            return "Delete Fail.", False
        conn.commit()
        return "Delete Success.", True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

