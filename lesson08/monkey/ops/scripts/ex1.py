import requests

class ServerError(Exception):
    pass



# def f1():
#     try:
#         print('1' + 2)
#     except TypeError as e:
#         pass
#
#
# f1()


def connectServer():
    try:
        req = requests.get("httpxsfafdasfasdf://www.baidu.com")
        print(req.text)
    except Exception as e:
        raise ServerError()


connectServer()