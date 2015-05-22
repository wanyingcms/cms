#!/usr/bin/env python
 #coding:utf8

import sys
#Hbase.thrift生成的py文件放在这里
sys.path.append('/usr/local/lib/python2.7/site-packages/gen-py')
#from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

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
print client.getTableNames()

try:
#    colusername = ColumnDescriptor( name = 'username:',maxVersions = 1 )
#    colpass = ColumnDescriptor( name = 'pass:',maxVersions = 1 )
#    colage = ColumnDescriptor( name = 'age:',maxVersions = 1 )
#    colinfo = ColumnDescriptor( name = 'info:',maxVersions = 1 )

#    client.createTable('tusers', [colusername,colpass,colage,colinfo])

    print client.getTableNames()

except AlreadyExists, tx:
    print "Thrift exception"
    print '%s' % (tx.message)


