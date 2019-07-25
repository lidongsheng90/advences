#-*- coding:utf-8 -*-
__author__ = 'lds'
__date__ = '2019/3/27 16:34'


#这是一个闭包
def singleton(cls):
    instances = {}

    def _singleton(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
            return instances[cls]

    return  _singleton