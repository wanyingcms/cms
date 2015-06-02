#coding:utf-8

from thrift.protocol import TBinaryProtocol, TMultiplexedProtocol
from thrift.transport import TSocket
from yythrift.FaqService import *
from yythrift.ttypes import Theme, GroupList

from utils.dictutils import safeObtainDict

transport = TSocket.TSocket("192.168.0.35", 9090)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
protocols = TMultiplexedProtocol.TMultiplexedProtocol(protocol, "faqService")

#添加主题
def th_addTheme(**kw):
    theme = Theme(tid='dfdfg', name=kw['name'], describe=kw['describe'], imgUrl=kw['imgUrl'], uid=kw['uid'], status=kw['status'], groupid=kw['groupid'])
    transport.open()
    client = Client(protocols)
    result = client.addTheme(theme)
    transport.close()
    return result

#编辑主题
def th_editTheme(**kw):
    theme = Theme(tid=kw['tid'], name=kw['name'], describe=kw['describe'], imgUrl=kw['imgUrl'], uid=kw['uid'], status=kw['status'], groupid=kw['groupid'])
    transport.open()
    client = Client(protocols)
    result = client.editTheme(theme)
    transport.close()
    return result

#查询主题列表
def th_findTheme(**kw):
    # print 111
    # transport.open()
    # print 222
    # client = Client(protocols)
    # print 333
    # result = client.findTheme(kw['className'], ['name'], uid=kw['uid'], page=kw['page'], cou=kw['cou'])
    # print 444
    # transport.close()
    # print 555
    # return result
    pass

#主题分类列表
def th_findThemeClass(**kw):
    transport.open()
    client = Client(protocols)
    try:
        result = client.findThemeClass()
    except BaseException, e:
        print e
        result = None
    transport.close()
    return result

#添加/编辑主题分类
def th_addThemeClass(list):
    print list
    print '----------------------'
    transport.open()
    client = Client(protocols)
    try:
        result = client.addThemeClass(list)
    except BaseException, e:
        print e
        result = False
    transport.close()
    return result

