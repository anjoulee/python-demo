class Demo(object):
    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        # public
        self.name = name
        # project
        self._age = age
        # private
        self.__weight = weight

    def get_weight(self):
        return self.__weight


class BackDemo(Demo):
    def __init__(self, name, age, weight, language):
        super(BackDemo, self).__init__(name, age, weight)
        self.language = language


if __name__ == '__main__':
    # demo = BackDemo('aaa', 12, 50)

    demo = BackDemo('aaa', 12, 50, 'Python')
    print dir(demo)
    print demo.__dict__
    # print demo.get_weight()
    # print demo._Demo__weight

    print type(demo)
    print isinstance(demo, Demo)
