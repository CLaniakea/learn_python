class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1
print(Student.count)
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    print(Student.count)
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        print(Student.count)
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')