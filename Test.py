# print('Hello, World!')
# from module import a,

import re
import json
from enum import Enum

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

a = 'pythonpythonpythonpythonec'

r = re.findall('(python){3}', a)

print(r)

json_str = '{"name":"dai", "age":18}'

student = json.loads(json_str)
print(student)

student2 = [
    {'name': 'dai', 'age': 18, 'type': ['a', 'b']},
    {'name': 'li', 'age': 11, 'type': ['c', 'e']}
]

json_str2 = json.dumps(student2)

print(type(json_str2))
print(json_str2)


class VIP(Enum):
    YELLOW = 1
    BLACK = 2


def curve_pre():
    aa = 25

    def curve(x):
        return aa * x * x

    return curve


f = curve_pre()

print(f(2))
print(f.__closure__)
print(f.__closure__[0].cell_contents)


def add(x, y):
    return x + y


f = lambda x, y: x + y

f1 = lambda x, y: x if x > y else y

list_x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r = map(lambda x: x * x, list_x)

print(f(1, 2))
print(f1(1, 2))
print(list(r))
