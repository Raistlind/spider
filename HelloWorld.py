# print('Hello, World!')
# from module import a,

import re

print(0x11)

print(ord('a'))

a = [1, 2, 3]
print(id(a))

a[0] = 2

print(id(a))

a = (2, 3, 4)
print(isinstance(a, type((1, 2, 3))))

if True:
    print('hello')

a = 1
b = 0

if a or b:
    print(a)

print(dir())

d = 1, 2, 3
a, b, c = d
e = f = g = 1


#

class Student():
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student('张飞', 22)
print(student1.name)

##

a = 'pythonpythonpythonpython'

r = re.findall('(python){3}', a)

print(r)
