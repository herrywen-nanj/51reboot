class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Python(People):

    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.height = height

    def say(self):
        return "{},{},{}".format(self.age, self.name, self.height)


lk = Python("laaa", 12, "140")
print(lk.say())
