

class People(object):

    reboot = 'www.baidu.com'

    # 构建函数
    def __init__(self, name, age, height):
        self.name = name
        self._age = age     # 私有属性
        self.__height = height


    def say(self):
        return "My name is {}, {} years old.".format(self.name, self._age)

    @classmethod
    def get_age(cls):
        return monkey.reboot

    @property
    def get_height(self):
        return self.__height


monkey = People('monkey', 12, '179')
print(monkey.say())
print(People.get_age())
print(monkey.get_height)
print(monkey.name)

# for i in dir(monkey):
#     print(i)
# print(monkey._age)
# print(monkey._People__height)
# print(monkey)
# print(monkey.name, monkey.age, monkey.height)
# print(monkey.say())
# print(dir(People))
