import saveUser
import opLog
import os
import loadUser

USERFILE = os.path.abspath(os.path.dirname(__file__) + '/51reboot.txt')
logger = opLog.opLog()


def deleteUser(user_info):
    username = user_info[1]
    result = loadUser.loadUser(USERFILE)
    usernames = result.keys()
    if username in usernames:
        result.pop(username)
        saveUser.saveUser(result, USERFILE)
        print("\033[0;31;1muser {} remove success.\033[0m".format(username))
        msg = "user {} remove success.".format(username)
        logger.debug(msg)
    else:
        print("\033[0;31;1muser {} not found.\033[0m".format(username))
    return result
