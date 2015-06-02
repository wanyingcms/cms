#coding:utf-8
__author__ = 'qiuxy'
import time

#获取dict中的key 没有返回None
def safeObtainDict(dict, key):
    if key in dict:
        return dict[key]
    else:
        return None

#获取dict中的key 没有返回0
def safeObtainDictToInt(dict, key):
    num = safeObtainDict(dict, key)
    if num is None or num == '':
        return 0
    else:
        return int(num)
#获取dict中的时间key 有返回时间戳 没有返回0
def safeObtainDictToTime(dict, key):
    times = safeObtainDict(dict, key)
    if times is None or times == '' or times == 0:
        return 0
    else:
        return long(time.mktime(time.strptime(times, '%Y-%m-%d %H:%M:%S'))*1000)