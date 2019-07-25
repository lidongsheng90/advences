#-*- coding:utf-8 -*-
__author__ = 'lds'
__date__ = '2019/3/25 22:45'


def ask(name='boby'):
    return name

class Person:
    def __init__(self):
        print ('boby1')

def decorator_func():
    print ('desc start')
    return ask

my_ask = decorator_func()
print (my_ask)
print(my_ask('toms'))

obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print (item())