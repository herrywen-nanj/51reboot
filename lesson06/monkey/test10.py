def auth(username, password):
    if username == 'monkey' and password == "123456":
        return True
    else:
        return False

def permission(username, perm=None):
    if username == 'monkey' and perm in ['del', 'update']:
        return True
    else:
        return False


def AuthPerm(func):

    def wrapper(*args, **kwargs):



        print(args)
        if not auth(args[0], args[1]):
            print("Auth fail")
            return False

        if not permission(args[0]):
            print("Perm fail")
            return False

        func(*args, **kwargs)

    return wrapper





@AuthPerm
def updateUser(username, password, action):
    # 操作
    #action del username
    print("Update succ.")

# @AuthPerm
# def deleteUser(username, password, action):
#
#     # 操作
#     #action del username
#     print("Delete succ.")


msg = updateUser('monkeyxxx', '123456', 'update')
print(msg)