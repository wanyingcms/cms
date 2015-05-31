#!/usr/bin/env python
 #coding:utf8

import sys
#Hbase.thrift生成的py文件放在这里
sys.path.append('/usr/local/lib/python2.7/site-packages/gen-py')
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import time

from hbase import Hbase
#如ColumnDescriptor 等在hbase.ttypes中定义
from hbase.ttypes import *

#print 'thrift begin...................'

transport = TSocket.TSocket('192.168.56.101', 19090)
 # Buffering is critical. Raw sockets are very slow
 # 还可以用TFramedTransport,也是高效传输方式
transport = TTransport.TBufferedTransport(transport)
 # Wrap in a protocol
 #传输协议和传输过程是分离的，可以支持多协议
protocol = TBinaryProtocol.TBinaryProtocol(transport)
 #客户端代表一个用户
client = Hbase.Client(protocol)
 #打开连接
transport.open()


#查询所有表名
def getTables():
    return client.getTableNames()

#创建表
def createTable(tableName,*family):
    try:
        family = []
        for col in family:
            family.append(ColumnDescriptor( name = col,maxVersions = 1 ))

        client.createTable(tableName, family)

        print client.getTableNames()

    except AlreadyExists, tx:
        print "Thrift exception"
        print '%s' % (tx.message)

#getRegions
def getTableRegions(tableName):

    return client.getTableRegions(tableName)


def getTcell(tableName,key,name):

    cell = client.getVer(tableName,key,name,1,{'type','1'})
    return cell

def write(tableName,row,content):
        mutations = []
        for key,value in content.items():
            mutations.append(Mutation(column=key ,value=value))

        #mutations=[Mutation(column="content:",value="con"),Mutation(column="content:",value="type")]
        client.mutateRow(tableName,row,mutations,None)


def read(self):
        scannerId = self.client.scannerOpen(self.tableName,"member",["contents:",])
        while True:
                try:
                        result = self.client.scannerGet(scannerId)
                except:
                        break
                contents = result.columns["contents:"].value
                #print contents
        self.client.scannerClose(scannerId)

def scannerOpenWithScan(tableName,scan,attributes):
    scanId = client.scannerOpenWithScan(tableName,scan,attributes)
    return scanId
#test....
#print getTcell('cheatstab','1','con')
#createTable('classroom','name','student','teacher','other')

'''struct TScan {
  1:optional Text startRow,
  2:optional Text stopRow,
  3:optional i64 timestamp,
  4:optional list<Text> columns,
  5:optional i32 caching,
  6:optional Text filterString
}'''

scan = TScan('zhangsan_lisi_20150601_1','zhangsan_lisi_20150601_2',None,['content:type'],None,None)



write("cheatstab","wangwu_zhangsan_20150609_"+time.time().__str__(),{"content:con1":"haha,nihao,woshizhoujia","content:type1":"1"})

id = scannerOpenWithScan("cheatstab",scan,None)
print 'id=',id
result = client.scannerGetList(id,10)
print result
