class Student:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number


student = Student("성규", 13)
print(student.name)
print(student.number)
