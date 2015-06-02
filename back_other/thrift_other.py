#coding:utf-8

from thrift.protocol import TBinaryProtocol, TMultiplexedProtocol
from thrift.transport import TSocket
from yythrift.SystemService import *
from yythrift.ttypes import Question
from utils.dictutils import safeObtainDict, safeObtainDictToInt, safeObtainDictToTime

transport = TSocket.TSocket("192.168.0.35", 9090)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
protocols = TMultiplexedProtocol.TMultiplexedProtocol(protocol, "systemService")

#关于我们
def th_findAbout(webOrMob):
    transport.open()
    client = Client(protocols)
    try:
        result = client.findAbout(webOrMob)
    except BaseException, e:
        print e
        result = None
    transport.close()
    return result

def th_updateAbout(webcontent, appcontent):
    transport.open()
    client = Client(protocols)
    try:
        result = client.updateAbout(webcontent, appcontent)
    except BaseException, e:
        print e
        result = None
    transport.close()
    return result


#服务条款
def th_findService():
    transport.open()
    client = Client(protocols)
    try:
        result = client.findService()
    except BaseException, e:
        print e
        result = None
    transport.close()
    return result
def th_udpateService(content):
    transport.open()
    client = Client(protocols)
    try:
        result = client.udpateService(content)
    except BaseException, e:
        print e
        result = None
    transport.close()
    return result
