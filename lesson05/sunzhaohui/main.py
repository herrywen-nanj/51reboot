
from modules import logic
from modules import myprint
from modules import useroperate


def man():
    #入口函数
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 3

    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        username = input("Please input your username: ").strip()
        password = input("Please input your password: ").strip()
        if useroperate.Login_Authentication(username, password):
            print(myprint.Green_Print('登录成功!'))
            print(useroperate.help())
            logic.Logic()
        else:
            print(myprint.Red_print("username or password valid failed."))
            INIT_FAIL_CNT += 1

    print(myprint.Red_print("Game Over."))



if __name__ == '__main__':
    man()

