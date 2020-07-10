from . import serialize_data
from . import logger


FIELDS = ['username', 'age', 'tel', 'email']

class User(object):
    def user_add(self,users, info_list):
        """
        用户添加功能
        :param users: 存储于文件中的用户信息字典
        :param info_list: 用户输入信息列表
        :return:
        """
        msg = ''
        flag = False
        if len(info_list) != 5:
            msg = '数据长度不等于5，请重新输入'
            return msg, flag
        username = info_list[1]
        age = info_list[2]
        tel = info_list[3]
        email = info_list[4]

        # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
        if username in users.keys():
            msg = '用户已存在，请重新输入'
            flag = False
        else:
            # users[username] = {'username': username, "age": age, "tel": tel, "email": email}
            users[username] = dict(zip(FIELDS, info_list[1:]))
            # 打印结果信息
            msg = "Add {} succ.".format(username)
            logger.logger(msg)
            flag = True
        return msg, flag

    def user_del(self,users, info_list):
        """
        用户删除功能
        :param users: 存储于文件中的用户信息字典
        :param info_list: 要删除的用户列表
        :return:
        """
        msg = ''
        flag = False
        if len(info_list) != 2:
            msg = '数据长度不等于2，请重新输入'
            return msg, flag
        username = info_list[1]
        result = users.pop(username, None)
        if result != None:
            msg = '%s已删除' % username
            logger.logger(msg)
            flag = True
        else:
            msg = '%s不存在' % username
            flag = False
        return msg, flag

    def user_update(self,users, info_list):
        """
        用户更新功能
        :param users: 存储于文件中的用户信息字典
        :param info_list: 要删除的用户列表
        :return:
        """
        msg = ''
        flag = False
        if len(info_list) != 6:
            msg = '数据长度不等于6，请重新输入'
            return msg, flag
        # update monkey1 set age = 20
        username = info_list[1]
        where = info_list[2]
        field = info_list[3]
        fuhao = info_list[-2]
        val = info_list[-1]

        if where != "set" or fuhao != "=":
            msg = "Update method error."
            flag = False
            return msg, flag

        if username not in users.keys():
            msg = '用户%s不存在' % username
            flag = False
        else:
            if users[username].get(field, None) == None:
                msg = '%s字段不存在' % field
                flag = False
            else:
                users[username][field] = val
                msg = '用户%s,%s已更新为%s' % (username, field, val)
                logger.logger(msg)
                flag = True
        return msg, flag

    def user_list(self,users):
        """
        用户展示功能
        :param users: 存储于文件中的用户信息字典
        :return:
        """
        msg = ''
        flag = True
        # 如果没有一条记录， 那么提示为空
        if len(users) < 1:
            msg = '列表为空'
            flag = False
            return msg, flag
        tmp = []
        for k, v in users.items():
            tmp.append(list(v.values()))
        result = serialize_data.serialize_data(tmp)

        return result, flag

    def user_find(self,users, info_list):
        """
        用户查找功能
        :param users: 存储于文件中的用户信息字典
        :param info_list:  输入的用户信息列表
        :return:
        """
        msg = ''

        flag = True
        if len(info_list) != 2:
            msg = '数据长度不等于2，请重新输入'
            flag = False
            return msg, flag

        username = info_list[1]

        tmp = []
        if username in users.keys():
            # tmp.append([username, users.get(username)['age'], users.get(username)['tel'],
            #             users.get(username)['email']])
            msg = serialize_data.serialize_data([list(users.get(username).values())])
        else:
            msg = '%s不存在' % username
            flag = False
        # result = serialize_data(tmp)
        return msg, flag

    def user_display(self,users, info_list):
        """
        数据分页功能
        :param users: 存储于文件中的用户信息字典
        :param info_list: 输入的用户信息列表
        :return:
        """
        # 分页 display page 1 pagesize 5
        msg = ''
        flag = True
        pagesize = 0
        if len(info_list) >= 3 and len(info_list) <= 5:
            # pagesize = 5
            if len(info_list) == 3:
                if info_list[1] == 'page':
                    pagesize = 5
                else:
                    msg = 'Display info invalid. Please input again.'
                    flag = False
                    return msg, flag
            else:
                if info_list[1] == "page" and info_list[3] == "pagesize":
                    pagesize = int(info_list[-1])
                else:
                    msg = "Display method error."
                    flag = False
                    return msg, flag

        page = int(info_list[2])
        # pagesize = int(info_list[-1])

        result = []
        for k, v in users.items():
            result.append(list(v.values()))

        start = (page - 1) * pagesize
        end = start + pagesize
        msg = serialize_data.serialize_data(result[start:end])
        return msg, flag