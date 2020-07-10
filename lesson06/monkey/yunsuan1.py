

class Cp(object):

    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __add__(self, other):
        return self.age + other.age

    def __str__(self):
        return "51reboot.com"

    def __dir__(self):
        return []






xiaoming = Cp(20)
print(dir(xiaoming))