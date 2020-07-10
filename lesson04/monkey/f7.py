
# 可变参数的位置参数
def optf(x, y, z, *reboot, **wwwreboot):
    '''
        * tuple
        ** dict
    '''

    print("x = {}".format(x))
    print("y = {}".format(y))
    print("z = {}".format(z))
    print(reboot, type(reboot))
    if len(reboot) < 2:
        print("length 1")
    else:
        print("length >2")

    print("wwwreboot {}, type: {}".format(wwwreboot, type(wwwreboot)))




optf(1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 8, name="51reboot", age=20)