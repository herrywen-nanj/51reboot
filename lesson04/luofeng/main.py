#!/usr/bin/env python
# -*- encoding:utf8 -*-
#*******************************************
# Author: LuoFeng
# Date: 2019-06-22
# Filename: main.py
# Describe:
#*******************************************

import json
import sys
from logzero import logger
from user_manager_func import login, add_user, check_users, del_user, update_user, query_user,export_data_to_cvsfile

filename = 'user_data_file.txt'
csv_file = 'userdata.csv'
audit_log_file = 'user_oper_audit.log'

def main():
    result = json.loads(login())
    if not result.get('status'):
        while True:
            action = input("Please input your operation: ").strip()

            if len(action) == 0:  # 如果为空， 则提示
                print("Input info invalid, Please input again.")
                continue

            if action == "add":
                context = input("please enter userinfo, format(username age tel email address):").strip()
                userinfo = context.split()
                try:
                    add_user(
                        filename = filename,
                        userinfo = userinfo
                    )

                except Exception as e:
                    print(e)

            elif action == "del":
                username = input("Please enter the user you want to delete: ").strip()
                del_user(
                    filename = filename,
                    username = username
                )

            elif action == "update":
                context = input("Please enter the user to update, format(username age tel email address):").strip()
                userinfo = context.split()
                try:
                    update_user(
                        filename = filename,
                        username = userinfo[0],
                        userinfo = userinfo
                    )

                except Exception as e:
                    print(e)

            elif action == "query":
                username = input("User information query, please enter user name: ").strip()
                query_user(
                    filename = filename,
                    username = username
                )

            elif action == "export":
                export_data_to_cvsfile(filename = filename)

            elif action == "exit":
                sys.exit()

            else:
                print("invalid action.")

if __name__ == '__main__':
    main()
