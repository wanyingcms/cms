#coding:utf-8

from thrift.protocol import TBinaryProtocol, TMultiplexedProtocol
from thrift.transport import TSocket
from yythrift.FaqService import *
from yythrift.ttypes import Question
from utils.dictutils import safeObtainDict, safeObtainDictToInt, safeObtainDictToTime

transport = TSocket.TSocket("192.168.0.35", 9090)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
protocols = TMultiplexedProtocol.TMultiplexedProtocol(protocol, "faqService")

#查询题目列表
def th_findQuestion(**kw):
    transport.open()
    client = Client(protocols)
    try:
        result = client.findQuestion(safeObtainDictToInt(kw, 'hide'), safeObtainDict(kw, 'name'), safeObtainDict(kw, 'describe'),
                                 safeObtainDict(kw, 'theme'), safeObtainDict(kw, 'qid'), safeObtainDict(kw, 'uid'),safeObtainDictToInt(kw, 'ansStop'),
                                 safeObtainDictToTime(kw, 'publishStart'), safeObtainDictToTime(kw, 'publishEnd'), safeObtainDictToInt(kw, 'ansStart'),
                                 safeObtainDictToInt(kw, 'shareNum'), safeObtainDictToInt(kw, 'shareEnd'), safeObtainDict(kw, 'usergroup'),
                                 safeObtainDictToInt(kw, 'userType'), safeObtainDictToInt(kw, 'page'), safeObtainDictToInt(kw, 'cou'))
    except BaseException, e:
        print e
        result = None

    transport.close()
    return result

#添加问题
def th_addQuestion(**kw):
    transport.open()
    client = Client(protocols)
    try:
        question = Question(name=kw['name'], theme=kw['theme'],
                      uid=kw['uid'], describe=kw['describe'], imgUrls=kw['imgUrls'],
                      createDate=kw['createDate'], ansNum=kw['ansNum'],
                      report=kw['report'], share=kw['share'],
                      hide=kw['hide'], hold=kw['hold'])
        result = client.addQuestion(question)
    except BaseException, e:
        print e
        result = False

    transport.close()
    return result

#修改问题
def th_editQuestion(**kw):
    transport.open()
    client = Client(protocols)
    try:
        question = Question(qid=kw['qid'], name=kw['name'], theme=kw['theme'],
                      uid=kw['uid'], describe=kw['describe'], imgUrls=kw['imgUrls'],
                      createDate=kw['createDate'], ansNum=kw['ansNum'],
                      report=kw['report'], share=kw['share'],
                      hide=kw['hide'], hold=kw['hold'])
        result = client.editQuestion(question)
    except BaseException, e:
        print e
        result = False

    transport.close()
    return result
