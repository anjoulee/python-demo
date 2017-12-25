class ProgramerCal(object):
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __eq__(self, other):
        if isinstance(other, ProgramerCal):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The type of objec must be ProgramerCal')

    def __add__(self, other):
        if isinstance(other, ProgramerCal):
            return self.age + other.age
        else:
            raise Exception('The type of object must be ProgramerCal')


if __name__ == '__main__':
    p1 = ProgramerCal('Anjoulee', 29)
    p2 = ProgramerCal('Bob', 30)

    print p1 == p1
    print p1 + p2
