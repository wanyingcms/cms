#coding:utf-8

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def sendMessage(self, toUid, fr, type, content):
    """
    发送消息<br>

    Parameters:
     - toUid
     - fr
     - type
     - content
    """
    pass

  def resaveAllMessage(self, lastDate, types, date, coontent):
    """
    最新消息<br>
    lastDate	Long	上次接收消息时间<br>
    types Integer	消息类型: 1 文本消息 ,2 图片消息,3 语音消息 , 4  我的回答<br>
    date	Long		发送消息时间<br>
    coontent	String	消息内容<br>

    Parameters:
     - lastDate
     - types
     - date
     - coontent
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def sendMessage(self, toUid, fr, type, content):
    """
    发送消息<br>

    Parameters:
     - toUid
     - fr
     - type
     - content
    """
    self.send_sendMessage(toUid, fr, type, content)
    return self.recv_sendMessage()

  def send_sendMessage(self, toUid, fr, type, content):
    self._oprot.writeMessageBegin('sendMessage', TMessageType.CALL, self._seqid)
    args = sendMessage_args()
    args.toUid = toUid
    args.fr = fr
    args.type = type
    args.content = content
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_sendMessage(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = sendMessage_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "sendMessage failed: unknown result");

  def resaveAllMessage(self, lastDate, types, date, coontent):
    """
    最新消息<br>
    lastDate	Long	上次接收消息时间<br>
    types Integer	消息类型: 1 文本消息 ,2 图片消息,3 语音消息 , 4  我的回答<br>
    date	Long		发送消息时间<br>
    coontent	String	消息内容<br>

    Parameters:
     - lastDate
     - types
     - date
     - coontent
    """
    self.send_resaveAllMessage(lastDate, types, date, coontent)
    return self.recv_resaveAllMessage()

  def send_resaveAllMessage(self, lastDate, types, date, coontent):
    self._oprot.writeMessageBegin('resaveAllMessage', TMessageType.CALL, self._seqid)
    args = resaveAllMessage_args()
    args.lastDate = lastDate
    args.types = types
    args.date = date
    args.coontent = coontent
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_resaveAllMessage(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = resaveAllMessage_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "resaveAllMessage failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["sendMessage"] = Processor.process_sendMessage
    self._processMap["resaveAllMessage"] = Processor.process_resaveAllMessage

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_sendMessage(self, seqid, iprot, oprot):
    args = sendMessage_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = sendMessage_result()
    result.success = self._handler.sendMessage(args.toUid, args.fr, args.type, args.content)
    oprot.writeMessageBegin("sendMessage", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_resaveAllMessage(self, seqid, iprot, oprot):
    args = resaveAllMessage_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = resaveAllMessage_result()
    result.success = self._handler.resaveAllMessage(args.lastDate, args.types, args.date, args.coontent)
    oprot.writeMessageBegin("resaveAllMessage", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class sendMessage_args:
  """
  Attributes:
   - toUid
   - fr
   - type
   - content
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'toUid', None, None, ), # 1
    (2, TType.STRING, 'fr', None, None, ), # 2
    (3, TType.STRING, 'type', None, None, ), # 3
    (4, TType.STRING, 'content', None, None, ), # 4
  )

  def __init__(self, toUid=None, fr=None, type=None, content=None,):
    self.toUid = toUid
    self.fr = fr
    self.type = type
    self.content = content

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.toUid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.fr = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.type = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.content = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('sendMessage_args')
    if self.toUid is not None:
      oprot.writeFieldBegin('toUid', TType.STRING, 1)
      oprot.writeString(self.toUid)
      oprot.writeFieldEnd()
    if self.fr is not None:
      oprot.writeFieldBegin('fr', TType.STRING, 2)
      oprot.writeString(self.fr)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.STRING, 3)
      oprot.writeString(self.type)
      oprot.writeFieldEnd()
    if self.content is not None:
      oprot.writeFieldBegin('content', TType.STRING, 4)
      oprot.writeString(self.content)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.toUid)
    value = (value * 31) ^ hash(self.fr)
    value = (value * 31) ^ hash(self.type)
    value = (value * 31) ^ hash(self.content)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class sendMessage_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.BOOL, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.BOOL:
          self.success = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('sendMessage_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.BOOL, 0)
      oprot.writeBool(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class resaveAllMessage_args:
  """
  Attributes:
   - lastDate
   - types
   - date
   - coontent
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'lastDate', None, None, ), # 1
    (2, TType.I32, 'types', None, None, ), # 2
    (3, TType.I64, 'date', None, None, ), # 3
    (4, TType.STRING, 'coontent', None, None, ), # 4
  )

  def __init__(self, lastDate=None, types=None, date=None, coontent=None,):
    self.lastDate = lastDate
    self.types = types
    self.date = date
    self.coontent = coontent

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.lastDate = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.types = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.date = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.coontent = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('resaveAllMessage_args')
    if self.lastDate is not None:
      oprot.writeFieldBegin('lastDate', TType.I64, 1)
      oprot.writeI64(self.lastDate)
      oprot.writeFieldEnd()
    if self.types is not None:
      oprot.writeFieldBegin('types', TType.I32, 2)
      oprot.writeI32(self.types)
      oprot.writeFieldEnd()
    if self.date is not None:
      oprot.writeFieldBegin('date', TType.I64, 3)
      oprot.writeI64(self.date)
      oprot.writeFieldEnd()
    if self.coontent is not None:
      oprot.writeFieldBegin('coontent', TType.STRING, 4)
      oprot.writeString(self.coontent)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.lastDate)
    value = (value * 31) ^ hash(self.types)
    value = (value * 31) ^ hash(self.date)
    value = (value * 31) ^ hash(self.coontent)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class resaveAllMessage_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING,None), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype87, _size84) = iprot.readListBegin()
          for _i88 in xrange(_size84):
            _elem89 = iprot.readString();
            self.success.append(_elem89)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('resaveAllMessage_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRING, len(self.success))
      for iter90 in self.success:
        oprot.writeString(iter90)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
