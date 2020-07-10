

'''程序猿
'''
class Programmer(object):

    # 构造函数
    def __init__(self, name, age):
        self.name = name        # 可以公开访问
        self.age = age
        self.height = 179

    def say(self, workd):
        return "www.51reboot.com" + workd


class PythonProgrammer(Programmer):

    def __init__(self, name, age, pythoner):
        super(PythonProgrammer, self).__init__(name, age)
        self.pythoner = pythoner


p = PythonProgrammer("monkey", 12, "python zhichan")
print(p.name, p.age, p.height, p.pythoner)
print(p.say('123'))
        