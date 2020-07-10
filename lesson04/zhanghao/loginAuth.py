import opLog

logger = opLog.opLog()

'''验证账号和密码是否正确,如果正确返回True,否则返回False
'''


def loginAuth(username, password):
    username_password = ("51reboot", "123456")
    if username == username_password[0] and password == username_password[1]:
        msg = "{} login success.".format(username)
        logger.debug(msg)
        return msg, True
    else:
        msg = "username or password error, Please login again."
        logger.debug(msg)
        return msg, False
