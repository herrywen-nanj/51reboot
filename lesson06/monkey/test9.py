def auth(username, password):
    if username == 'monkey' and password == "123456":
        return True
    else:
        return False

def permission(username, perm):
    if username == 'monkey' and perm in ['del', 'update']:
        return True
    else:
        return False

def deleteUser(username, password, action):
    # 判断有没有登录
    if not auth(username, password):
        print("Auth fail.")
        return False

    # 有没有权限
    if not permission(username, action):
        print("Perm fail.")
        return False

    # 操作
    #action del username
    print("Delete succ.")


def updateUser(username, password, action):
    # 判断有没有登录
    if not auth(username, password):
        print("Auth fail.")
        return False

    # 有没有权限
    if not permission(username, action):
        print("Perm fail.")
        return False

    # 操作
    #action del username
    print("Update succ.")


msg = updateUser('monkey', '123456', 'update')
print(msg)