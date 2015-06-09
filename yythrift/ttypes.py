#coding:utf-8

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class GroupList:
  """
   用户分组结构<br>
   
   分组的ID , 唯一标识<br>
   分组名称<br>
   该分类下有多少个主题 <br>
  组了类型, 1 表示 虚拟用户组 2, 表示 真实用户组 ,3 表示主题分类

  Attributes:
   - glid
   - gname
   - gtype
   - childNumber
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'glid', None, None, ), # 1
    (2, TType.STRING, 'gname', None, None, ), # 2
    (3, TType.I32, 'gtype', None, None, ), # 3
    (4, TType.I64, 'childNumber', None, None, ), # 4
  )

  def __init__(self, glid=None, gname=None, gtype=None, childNumber=None,):
    self.glid = glid
    self.gname = gname
    self.gtype = gtype
    self.childNumber = childNumber

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
          self.glid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.gname = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.gtype = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.childNumber = iprot.readI64();
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
    oprot.writeStructBegin('GroupList')
    if self.glid is not None:
      oprot.writeFieldBegin('glid', TType.STRING, 1)
      oprot.writeString(self.glid)
      oprot.writeFieldEnd()
    if self.gname is not None:
      oprot.writeFieldBegin('gname', TType.STRING, 2)
      oprot.writeString(self.gname)
      oprot.writeFieldEnd()
    if self.gtype is not None:
      oprot.writeFieldBegin('gtype', TType.I32, 3)
      oprot.writeI32(self.gtype)
      oprot.writeFieldEnd()
    if self.childNumber is not None:
      oprot.writeFieldBegin('childNumber', TType.I64, 4)
      oprot.writeI64(self.childNumber)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.glid)
    value = (value * 31) ^ hash(self.gname)
    value = (value * 31) ^ hash(self.gtype)
    value = (value * 31) ^ hash(self.childNumber)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class User:
  """
  Attributes:
   - uid
   - nickName
   - mobile
   - passwd
   - remark
   - quesNumber
   - answerNUmber
   - laud
   - signNumber
   - lastSignDate
   - createDate
   - stopDate
   - hide
   - stop
   - groupid
   - utype
   - img
   - imgs
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'uid', None, None, ), # 1
    (2, TType.STRING, 'nickName', None, None, ), # 2
    (3, TType.STRING, 'mobile', None, None, ), # 3
    (4, TType.STRING, 'passwd', None, None, ), # 4
    (5, TType.STRING, 'remark', None, None, ), # 5
    (6, TType.I32, 'quesNumber', None, None, ), # 6
    (7, TType.I32, 'answerNUmber', None, None, ), # 7
    (8, TType.I32, 'laud', None, None, ), # 8
    (9, TType.I32, 'signNumber', None, None, ), # 9
    (10, TType.I64, 'lastSignDate', None, None, ), # 10
    (11, TType.I64, 'createDate', None, None, ), # 11
    (12, TType.I64, 'stopDate', None, None, ), # 12
    (13, TType.I32, 'hide', None, None, ), # 13
    (14, TType.I32, 'stop', None, None, ), # 14
    (15, TType.STRING, 'groupid', None, None, ), # 15
    (16, TType.I32, 'utype', None, None, ), # 16
    (17, TType.STRING, 'img', None, None, ), # 17
    (18, TType.STRING, 'imgs', None, None, ), # 18
  )

  def __init__(self, uid=None, nickName=None, mobile=None, passwd=None, remark=None, quesNumber=None, answerNUmber=None, laud=None, signNumber=None, lastSignDate=None, createDate=None, stopDate=None, hide=None, stop=None, groupid=None, utype=None, img=None, imgs=None,):
    self.uid = uid
    self.nickName = nickName
    self.mobile = mobile
    self.passwd = passwd
    self.remark = remark
    self.quesNumber = quesNumber
    self.answerNUmber = answerNUmber
    self.laud = laud
    self.signNumber = signNumber
    self.lastSignDate = lastSignDate
    self.createDate = createDate
    self.stopDate = stopDate
    self.hide = hide
    self.stop = stop
    self.groupid = groupid
    self.utype = utype
    self.img = img
    self.imgs = imgs

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
          self.uid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.nickName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.mobile = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.passwd = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.remark = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.quesNumber = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.answerNUmber = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.laud = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I32:
          self.signNumber = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I64:
          self.lastSignDate = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I64:
          self.createDate = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.I64:
          self.stopDate = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.I32:
          self.hide = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.I32:
          self.stop = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 15:
        if ftype == TType.STRING:
          self.groupid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 16:
        if ftype == TType.I32:
          self.utype = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 17:
        if ftype == TType.STRING:
          self.img = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 18:
        if ftype == TType.STRING:
          self.imgs = iprot.readString();
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
    oprot.writeStructBegin('User')
    if self.uid is not None:
      oprot.writeFieldBegin('uid', TType.STRING, 1)
      oprot.writeString(self.uid)
      oprot.writeFieldEnd()
    if self.nickName is not None:
      oprot.writeFieldBegin('nickName', TType.STRING, 2)
      oprot.writeString(self.nickName)
      oprot.writeFieldEnd()
    if self.mobile is not None:
      oprot.writeFieldBegin('mobile', TType.STRING, 3)
      oprot.writeString(self.mobile)
      oprot.writeFieldEnd()
    if self.passwd is not None:
      oprot.writeFieldBegin('passwd', TType.STRING, 4)
      oprot.writeString(self.passwd)
      oprot.writeFieldEnd()
    if self.remark is not None:
      oprot.writeFieldBegin('remark', TType.STRING, 5)
      oprot.writeString(self.remark)
      oprot.writeFieldEnd()
    if self.quesNumber is not None:
      oprot.writeFieldBegin('quesNumber', TType.I32, 6)
      oprot.writeI32(self.quesNumber)
      oprot.writeFieldEnd()
    if self.answerNUmber is not None:
      oprot.writeFieldBegin('answerNUmber', TType.I32, 7)
      oprot.writeI32(self.answerNUmber)
      oprot.writeFieldEnd()
    if self.laud is not None:
      oprot.writeFieldBegin('laud', TType.I32, 8)
      oprot.writeI32(self.laud)
      oprot.writeFieldEnd()
    if self.signNumber is not None:
      oprot.writeFieldBegin('signNumber', TType.I32, 9)
      oprot.writeI32(self.signNumber)
      oprot.writeFieldEnd()
    if self.lastSignDate is not None:
      oprot.writeFieldBegin('lastSignDate', TType.I64, 10)
      oprot.writeI64(self.lastSignDate)
      oprot.writeFieldEnd()
    if self.createDate is not None:
      oprot.writeFieldBegin('createDate', TType.I64, 11)
      oprot.writeI64(self.createDate)
      oprot.writeFieldEnd()
    if self.stopDate is not None:
      oprot.writeFieldBegin('stopDate', TType.I64, 12)
      oprot.writeI64(self.stopDate)
      oprot.writeFieldEnd()
    if self.hide is not None:
      oprot.writeFieldBegin('hide', TType.I32, 13)
      oprot.writeI32(self.hide)
      oprot.writeFieldEnd()
    if self.stop is not None:
      oprot.writeFieldBegin('stop', TType.I32, 14)
      oprot.writeI32(self.stop)
      oprot.writeFieldEnd()
    if self.groupid is not None:
      oprot.writeFieldBegin('groupid', TType.STRING, 15)
      oprot.writeString(self.groupid)
      oprot.writeFieldEnd()
    if self.utype is not None:
      oprot.writeFieldBegin('utype', TType.I32, 16)
      oprot.writeI32(self.utype)
      oprot.writeFieldEnd()
    if self.img is not None:
      oprot.writeFieldBegin('img', TType.STRING, 17)
      oprot.writeString(self.img)
      oprot.writeFieldEnd()
    if self.imgs is not None:
      oprot.writeFieldBegin('imgs', TType.STRING, 18)
      oprot.writeString(self.imgs)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.uid)
    value = (value * 31) ^ hash(self.nickName)
    value = (value * 31) ^ hash(self.mobile)
    value = (value * 31) ^ hash(self.passwd)
    value = (value * 31) ^ hash(self.remark)
    value = (value * 31) ^ hash(self.quesNumber)
    value = (value * 31) ^ hash(self.answerNUmber)
    value = (value * 31) ^ hash(self.laud)
    value = (value * 31) ^ hash(self.signNumber)
    value = (value * 31) ^ hash(self.lastSignDate)
    value = (value * 31) ^ hash(self.createDate)
    value = (value * 31) ^ hash(self.stopDate)
    value = (value * 31) ^ hash(self.hide)
    value = (value * 31) ^ hash(self.stop)
    value = (value * 31) ^ hash(self.groupid)
    value = (value * 31) ^ hash(self.utype)
    value = (value * 31) ^ hash(self.img)
    value = (value * 31) ^ hash(self.imgs)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Theme:
  """
  Attributes:
   - tid
   - name
   - describe
   - imgUrl
   - uid
   - openTimes
   - quesNum
   - ansNum
   - status
   - groupid
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'tid', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.STRING, 'describe', None, None, ), # 3
    (4, TType.STRING, 'imgUrl', None, None, ), # 4
    (5, TType.STRING, 'uid', None, None, ), # 5
    (6, TType.I32, 'openTimes', None, None, ), # 6
    (7, TType.I64, 'quesNum', None, None, ), # 7
    (8, TType.I64, 'ansNum', None, None, ), # 8
    (9, TType.I32, 'status', None, None, ), # 9
    (10, TType.STRING, 'groupid', None, None, ), # 10
  )

  def __init__(self, tid=None, name=None, describe=None, imgUrl=None, uid=None, openTimes=None, quesNum=None, ansNum=None, status=None, groupid=None,):
    self.tid = tid
    self.name = name
    self.describe = describe
    self.imgUrl = imgUrl
    self.uid = uid
    self.openTimes = openTimes
    self.quesNum = quesNum
    self.ansNum = ansNum
    self.status = status
    self.groupid = groupid

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
          self.tid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.describe = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.imgUrl = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.uid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.openTimes = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.quesNum = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I64:
          self.ansNum = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I32:
          self.status = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRING:
          self.groupid = iprot.readString();
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
    oprot.writeStructBegin('Theme')
    if self.tid is not None:
      oprot.writeFieldBegin('tid', TType.STRING, 1)
      oprot.writeString(self.tid)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.describe is not None:
      oprot.writeFieldBegin('describe', TType.STRING, 3)
      oprot.writeString(self.describe)
      oprot.writeFieldEnd()
    if self.imgUrl is not None:
      oprot.writeFieldBegin('imgUrl', TType.STRING, 4)
      oprot.writeString(self.imgUrl)
      oprot.writeFieldEnd()
    if self.uid is not None:
      oprot.writeFieldBegin('uid', TType.STRING, 5)
      oprot.writeString(self.uid)
      oprot.writeFieldEnd()
    if self.openTimes is not None:
      oprot.writeFieldBegin('openTimes', TType.I32, 6)
      oprot.writeI32(self.openTimes)
      oprot.writeFieldEnd()
    if self.quesNum is not None:
      oprot.writeFieldBegin('quesNum', TType.I64, 7)
      oprot.writeI64(self.quesNum)
      oprot.writeFieldEnd()
    if self.ansNum is not None:
      oprot.writeFieldBegin('ansNum', TType.I64, 8)
      oprot.writeI64(self.ansNum)
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.I32, 9)
      oprot.writeI32(self.status)
      oprot.writeFieldEnd()
    if self.groupid is not None:
      oprot.writeFieldBegin('groupid', TType.STRING, 10)
      oprot.writeString(self.groupid)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.tid)
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.describe)
    value = (value * 31) ^ hash(self.imgUrl)
    value = (value * 31) ^ hash(self.uid)
    value = (value * 31) ^ hash(self.openTimes)
    value = (value * 31) ^ hash(self.quesNum)
    value = (value * 31) ^ hash(self.ansNum)
    value = (value * 31) ^ hash(self.status)
    value = (value * 31) ^ hash(self.groupid)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Question:
  """
  Attributes:
   - qid
   - name
   - theme
   - uid
   - describe
   - imgUrls
   - createDate
   - ansNum
   - report
   - share
   - hide
   - hold
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'qid', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.STRING, 'theme', None, None, ), # 3
    (4, TType.STRING, 'uid', None, None, ), # 4
    (5, TType.STRING, 'describe', None, None, ), # 5
    (6, TType.STRING, 'imgUrls', None, None, ), # 6
    (7, TType.I64, 'createDate', None, None, ), # 7
    (8, TType.I32, 'ansNum', None, None, ), # 8
    (9, TType.I32, 'report', None, None, ), # 9
    (10, TType.I32, 'share', None, None, ), # 10
    (11, TType.I32, 'hide', None, None, ), # 11
    (12, TType.I32, 'hold', None, None, ), # 12
  )

  def __init__(self, qid=None, name=None, theme=None, uid=None, describe=None, imgUrls=None, createDate=None, ansNum=None, report=None, share=None, hide=None, hold=None,):
    self.qid = qid
    self.name = name
    self.theme = theme
    self.uid = uid
    self.describe = describe
    self.imgUrls = imgUrls
    self.createDate = createDate
    self.ansNum = ansNum
    self.report = report
    self.share = share
    self.hide = hide
    self.hold = hold

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
          self.qid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.theme = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.uid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.describe = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.imgUrls = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.createDate = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.ansNum = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I32:
          self.report = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I32:
          self.share = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I32:
          self.hide = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.I32:
          self.hold = iprot.readI32();
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
    oprot.writeStructBegin('Question')
    if self.qid is not None:
      oprot.writeFieldBegin('qid', TType.STRING, 1)
      oprot.writeString(self.qid)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.theme is not None:
      oprot.writeFieldBegin('theme', TType.STRING, 3)
      oprot.writeString(self.theme)
      oprot.writeFieldEnd()
    if self.uid is not None:
      oprot.writeFieldBegin('uid', TType.STRING, 4)
      oprot.writeString(self.uid)
      oprot.writeFieldEnd()
    if self.describe is not None:
      oprot.writeFieldBegin('describe', TType.STRING, 5)
      oprot.writeString(self.describe)
      oprot.writeFieldEnd()
    if self.imgUrls is not None:
      oprot.writeFieldBegin('imgUrls', TType.STRING, 6)
      oprot.writeString(self.imgUrls)
      oprot.writeFieldEnd()
    if self.createDate is not None:
      oprot.writeFieldBegin('createDate', TType.I64, 7)
      oprot.writeI64(self.createDate)
      oprot.writeFieldEnd()
    if self.ansNum is not None:
      oprot.writeFieldBegin('ansNum', TType.I32, 8)
      oprot.writeI32(self.ansNum)
      oprot.writeFieldEnd()
    if self.report is not None:
      oprot.writeFieldBegin('report', TType.I32, 9)
      oprot.writeI32(self.report)
      oprot.writeFieldEnd()
    if self.share is not None:
      oprot.writeFieldBegin('share', TType.I32, 10)
      oprot.writeI32(self.share)
      oprot.writeFieldEnd()
    if self.hide is not None:
      oprot.writeFieldBegin('hide', TType.I32, 11)
      oprot.writeI32(self.hide)
      oprot.writeFieldEnd()
    if self.hold is not None:
      oprot.writeFieldBegin('hold', TType.I32, 12)
      oprot.writeI32(self.hold)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.qid)
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.theme)
    value = (value * 31) ^ hash(self.uid)
    value = (value * 31) ^ hash(self.describe)
    value = (value * 31) ^ hash(self.imgUrls)
    value = (value * 31) ^ hash(self.createDate)
    value = (value * 31) ^ hash(self.ansNum)
    value = (value * 31) ^ hash(self.report)
    value = (value * 31) ^ hash(self.share)
    value = (value * 31) ^ hash(self.hide)
    value = (value * 31) ^ hash(self.hold)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Answer:
  """
  Attributes:
   - aid
   - uid
   - qid
   - content
   - imgurl
   - report
   - laud
   - share
   - hide
   - createDate
   - hold
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'aid', None, None, ), # 1
    (2, TType.STRING, 'uid', None, None, ), # 2
    (3, TType.STRING, 'qid', None, None, ), # 3
    (4, TType.STRING, 'content', None, None, ), # 4
    (5, TType.STRING, 'imgurl', None, None, ), # 5
    (6, TType.I32, 'report', None, None, ), # 6
    (7, TType.I32, 'laud', None, None, ), # 7
    (8, TType.I32, 'share', None, None, ), # 8
    (9, TType.I32, 'hide', None, None, ), # 9
    (10, TType.I64, 'createDate', None, None, ), # 10
    (11, TType.I32, 'hold', None, None, ), # 11
  )

  def __init__(self, aid=None, uid=None, qid=None, content=None, imgurl=None, report=None, laud=None, share=None, hide=None, createDate=None, hold=None,):
    self.aid = aid
    self.uid = uid
    self.qid = qid
    self.content = content
    self.imgurl = imgurl
    self.report = report
    self.laud = laud
    self.share = share
    self.hide = hide
    self.createDate = createDate
    self.hold = hold

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
          self.aid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.uid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.qid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.content = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.imgurl = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.report = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.laud = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.share = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I32:
          self.hide = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I64:
          self.createDate = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I32:
          self.hold = iprot.readI32();
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
    oprot.writeStructBegin('Answer')
    if self.aid is not None:
      oprot.writeFieldBegin('aid', TType.STRING, 1)
      oprot.writeString(self.aid)
      oprot.writeFieldEnd()
    if self.uid is not None:
      oprot.writeFieldBegin('uid', TType.STRING, 2)
      oprot.writeString(self.uid)
      oprot.writeFieldEnd()
    if self.qid is not None:
      oprot.writeFieldBegin('qid', TType.STRING, 3)
      oprot.writeString(self.qid)
      oprot.writeFieldEnd()
    if self.content is not None:
      oprot.writeFieldBegin('content', TType.STRING, 4)
      oprot.writeString(self.content)
      oprot.writeFieldEnd()
    if self.imgurl is not None:
      oprot.writeFieldBegin('imgurl', TType.STRING, 5)
      oprot.writeString(self.imgurl)
      oprot.writeFieldEnd()
    if self.report is not None:
      oprot.writeFieldBegin('report', TType.I32, 6)
      oprot.writeI32(self.report)
      oprot.writeFieldEnd()
    if self.laud is not None:
      oprot.writeFieldBegin('laud', TType.I32, 7)
      oprot.writeI32(self.laud)
      oprot.writeFieldEnd()
    if self.share is not None:
      oprot.writeFieldBegin('share', TType.I32, 8)
      oprot.writeI32(self.share)
      oprot.writeFieldEnd()
    if self.hide is not None:
      oprot.writeFieldBegin('hide', TType.I32, 9)
      oprot.writeI32(self.hide)
      oprot.writeFieldEnd()
    if self.createDate is not None:
      oprot.writeFieldBegin('createDate', TType.I64, 10)
      oprot.writeI64(self.createDate)
      oprot.writeFieldEnd()
    if self.hold is not None:
      oprot.writeFieldBegin('hold', TType.I32, 11)
      oprot.writeI32(self.hold)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.aid)
    value = (value * 31) ^ hash(self.uid)
    value = (value * 31) ^ hash(self.qid)
    value = (value * 31) ^ hash(self.content)
    value = (value * 31) ^ hash(self.imgurl)
    value = (value * 31) ^ hash(self.report)
    value = (value * 31) ^ hash(self.laud)
    value = (value * 31) ^ hash(self.share)
    value = (value * 31) ^ hash(self.hide)
    value = (value * 31) ^ hash(self.createDate)
    value = (value * 31) ^ hash(self.hold)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Message:
  """
  Attributes:
   - fuid
   - tuid
   - msgType
   - msg
   - sendTime
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'fuid', None, None, ), # 1
    (2, TType.STRING, 'tuid', None, None, ), # 2
    (3, TType.I32, 'msgType', None, None, ), # 3
    (4, TType.STRING, 'msg', None, None, ), # 4
    (5, TType.I64, 'sendTime', None, None, ), # 5
  )

  def __init__(self, fuid=None, tuid=None, msgType=None, msg=None, sendTime=None,):
    self.fuid = fuid
    self.tuid = tuid
    self.msgType = msgType
    self.msg = msg
    self.sendTime = sendTime

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
          self.fuid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.tuid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.msgType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.msg = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.sendTime = iprot.readI64();
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
    oprot.writeStructBegin('Message')
    if self.fuid is not None:
      oprot.writeFieldBegin('fuid', TType.STRING, 1)
      oprot.writeString(self.fuid)
      oprot.writeFieldEnd()
    if self.tuid is not None:
      oprot.writeFieldBegin('tuid', TType.STRING, 2)
      oprot.writeString(self.tuid)
      oprot.writeFieldEnd()
    if self.msgType is not None:
      oprot.writeFieldBegin('msgType', TType.I32, 3)
      oprot.writeI32(self.msgType)
      oprot.writeFieldEnd()
    if self.msg is not None:
      oprot.writeFieldBegin('msg', TType.STRING, 4)
      oprot.writeString(self.msg)
      oprot.writeFieldEnd()
    if self.sendTime is not None:
      oprot.writeFieldBegin('sendTime', TType.I64, 5)
      oprot.writeI64(self.sendTime)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.fuid)
    value = (value * 31) ^ hash(self.tuid)
    value = (value * 31) ^ hash(self.msgType)
    value = (value * 31) ^ hash(self.msg)
    value = (value * 31) ^ hash(self.sendTime)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Version:
  """
  Attributes:
   - issueDate
   - sys
   - vnum
   - url
   - describe
   - remark
   - userGroup
   - canal
   - option
   - haveto
   - vid
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'issueDate', None, None, ), # 1
    (2, TType.STRING, 'sys', None, None, ), # 2
    (3, TType.STRING, 'vnum', None, None, ), # 3
    (4, TType.STRING, 'url', None, None, ), # 4
    (5, TType.STRING, 'describe', None, None, ), # 5
    (6, TType.STRING, 'remark', None, None, ), # 6
    (7, TType.STRING, 'userGroup', None, None, ), # 7
    (8, TType.STRING, 'canal', None, None, ), # 8
    (9, TType.STRING, 'option', None, None, ), # 9
    (10, TType.STRING, 'haveto', None, None, ), # 10
    (11, TType.STRING, 'vid', None, None, ), # 11
  )

  def __init__(self, issueDate=None, sys=None, vnum=None, url=None, describe=None, remark=None, userGroup=None, canal=None, option=None, haveto=None, vid=None,):
    self.issueDate = issueDate
    self.sys = sys
    self.vnum = vnum
    self.url = url
    self.describe = describe
    self.remark = remark
    self.userGroup = userGroup
    self.canal = canal
    self.option = option
    self.haveto = haveto
    self.vid = vid

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
          self.issueDate = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.sys = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.vnum = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.url = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.describe = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.remark = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.userGroup = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.canal = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.option = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRING:
          self.haveto = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.STRING:
          self.vid = iprot.readString();
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
    oprot.writeStructBegin('Version')
    if self.issueDate is not None:
      oprot.writeFieldBegin('issueDate', TType.I64, 1)
      oprot.writeI64(self.issueDate)
      oprot.writeFieldEnd()
    if self.sys is not None:
      oprot.writeFieldBegin('sys', TType.STRING, 2)
      oprot.writeString(self.sys)
      oprot.writeFieldEnd()
    if self.vnum is not None:
      oprot.writeFieldBegin('vnum', TType.STRING, 3)
      oprot.writeString(self.vnum)
      oprot.writeFieldEnd()
    if self.url is not None:
      oprot.writeFieldBegin('url', TType.STRING, 4)
      oprot.writeString(self.url)
      oprot.writeFieldEnd()
    if self.describe is not None:
      oprot.writeFieldBegin('describe', TType.STRING, 5)
      oprot.writeString(self.describe)
      oprot.writeFieldEnd()
    if self.remark is not None:
      oprot.writeFieldBegin('remark', TType.STRING, 6)
      oprot.writeString(self.remark)
      oprot.writeFieldEnd()
    if self.userGroup is not None:
      oprot.writeFieldBegin('userGroup', TType.STRING, 7)
      oprot.writeString(self.userGroup)
      oprot.writeFieldEnd()
    if self.canal is not None:
      oprot.writeFieldBegin('canal', TType.STRING, 8)
      oprot.writeString(self.canal)
      oprot.writeFieldEnd()
    if self.option is not None:
      oprot.writeFieldBegin('option', TType.STRING, 9)
      oprot.writeString(self.option)
      oprot.writeFieldEnd()
    if self.haveto is not None:
      oprot.writeFieldBegin('haveto', TType.STRING, 10)
      oprot.writeString(self.haveto)
      oprot.writeFieldEnd()
    if self.vid is not None:
      oprot.writeFieldBegin('vid', TType.STRING, 11)
      oprot.writeString(self.vid)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.issueDate)
    value = (value * 31) ^ hash(self.sys)
    value = (value * 31) ^ hash(self.vnum)
    value = (value * 31) ^ hash(self.url)
    value = (value * 31) ^ hash(self.describe)
    value = (value * 31) ^ hash(self.remark)
    value = (value * 31) ^ hash(self.userGroup)
    value = (value * 31) ^ hash(self.canal)
    value = (value * 31) ^ hash(self.option)
    value = (value * 31) ^ hash(self.haveto)
    value = (value * 31) ^ hash(self.vid)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Advice:
  """
  Attributes:
   - rowkey
   - uid
   - signName
   - mobile
   - content
   - createDate
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'rowkey', None, None, ), # 1
    (2, TType.STRING, 'uid', None, None, ), # 2
    (3, TType.STRING, 'signName', None, None, ), # 3
    (4, TType.STRING, 'mobile', None, None, ), # 4
    (5, TType.STRING, 'content', None, None, ), # 5
    (6, TType.I64, 'createDate', None, None, ), # 6
  )

  def __init__(self, rowkey=None, uid=None, signName=None, mobile=None, content=None, createDate=None,):
    self.rowkey = rowkey
    self.uid = uid
    self.signName = signName
    self.mobile = mobile
    self.content = content
    self.createDate = createDate

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
          self.rowkey = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.uid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.signName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.mobile = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.content = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.createDate = iprot.readI64();
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
    oprot.writeStructBegin('Advice')
    if self.rowkey is not None:
      oprot.writeFieldBegin('rowkey', TType.STRING, 1)
      oprot.writeString(self.rowkey)
      oprot.writeFieldEnd()
    if self.uid is not None:
      oprot.writeFieldBegin('uid', TType.STRING, 2)
      oprot.writeString(self.uid)
      oprot.writeFieldEnd()
    if self.signName is not None:
      oprot.writeFieldBegin('signName', TType.STRING, 3)
      oprot.writeString(self.signName)
      oprot.writeFieldEnd()
    if self.mobile is not None:
      oprot.writeFieldBegin('mobile', TType.STRING, 4)
      oprot.writeString(self.mobile)
      oprot.writeFieldEnd()
    if self.content is not None:
      oprot.writeFieldBegin('content', TType.STRING, 5)
      oprot.writeString(self.content)
      oprot.writeFieldEnd()
    if self.createDate is not None:
      oprot.writeFieldBegin('createDate', TType.I64, 6)
      oprot.writeI64(self.createDate)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.rowkey)
    value = (value * 31) ^ hash(self.uid)
    value = (value * 31) ^ hash(self.signName)
    value = (value * 31) ^ hash(self.mobile)
    value = (value * 31) ^ hash(self.content)
    value = (value * 31) ^ hash(self.createDate)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Report:
  """
  Attributes:
   - rowkey
   - cid
   - type
   - theme
   - content
   - date
   - share
   - repo
   - types
   - deal
   - issave
   - hide
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'rowkey', None, None, ), # 1
    (2, TType.STRING, 'cid', None, None, ), # 2
    (3, TType.I32, 'type', None, None, ), # 3
    (4, TType.STRING, 'theme', None, None, ), # 4
    (5, TType.STRING, 'content', None, None, ), # 5
    (6, TType.I32, 'date', None, None, ), # 6
    (7, TType.I32, 'share', None, None, ), # 7
    (8, TType.I32, 'repo', None, None, ), # 8
    (9, TType.I32, 'types', None, None, ), # 9
    (10, TType.I32, 'deal', None, None, ), # 10
    (11, TType.I32, 'issave', None, None, ), # 11
    (12, TType.I32, 'hide', None, None, ), # 12
  )

  def __init__(self, rowkey=None, cid=None, type=None, theme=None, content=None, date=None, share=None, repo=None, types=None, deal=None, issave=None, hide=None,):
    self.rowkey = rowkey
    self.cid = cid
    self.type = type
    self.theme = theme
    self.content = content
    self.date = date
    self.share = share
    self.repo = repo
    self.types = types
    self.deal = deal
    self.issave = issave
    self.hide = hide

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
          self.rowkey = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.cid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.theme = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.content = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.date = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.share = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.repo = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I32:
          self.types = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I32:
          self.deal = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I32:
          self.issave = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.I32:
          self.hide = iprot.readI32();
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
    oprot.writeStructBegin('Report')
    if self.rowkey is not None:
      oprot.writeFieldBegin('rowkey', TType.STRING, 1)
      oprot.writeString(self.rowkey)
      oprot.writeFieldEnd()
    if self.cid is not None:
      oprot.writeFieldBegin('cid', TType.STRING, 2)
      oprot.writeString(self.cid)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 3)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.theme is not None:
      oprot.writeFieldBegin('theme', TType.STRING, 4)
      oprot.writeString(self.theme)
      oprot.writeFieldEnd()
    if self.content is not None:
      oprot.writeFieldBegin('content', TType.STRING, 5)
      oprot.writeString(self.content)
      oprot.writeFieldEnd()
    if self.date is not None:
      oprot.writeFieldBegin('date', TType.I32, 6)
      oprot.writeI32(self.date)
      oprot.writeFieldEnd()
    if self.share is not None:
      oprot.writeFieldBegin('share', TType.I32, 7)
      oprot.writeI32(self.share)
      oprot.writeFieldEnd()
    if self.repo is not None:
      oprot.writeFieldBegin('repo', TType.I32, 8)
      oprot.writeI32(self.repo)
      oprot.writeFieldEnd()
    if self.types is not None:
      oprot.writeFieldBegin('types', TType.I32, 9)
      oprot.writeI32(self.types)
      oprot.writeFieldEnd()
    if self.deal is not None:
      oprot.writeFieldBegin('deal', TType.I32, 10)
      oprot.writeI32(self.deal)
      oprot.writeFieldEnd()
    if self.issave is not None:
      oprot.writeFieldBegin('issave', TType.I32, 11)
      oprot.writeI32(self.issave)
      oprot.writeFieldEnd()
    if self.hide is not None:
      oprot.writeFieldBegin('hide', TType.I32, 12)
      oprot.writeI32(self.hide)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.rowkey)
    value = (value * 31) ^ hash(self.cid)
    value = (value * 31) ^ hash(self.type)
    value = (value * 31) ^ hash(self.theme)
    value = (value * 31) ^ hash(self.content)
    value = (value * 31) ^ hash(self.date)
    value = (value * 31) ^ hash(self.share)
    value = (value * 31) ^ hash(self.repo)
    value = (value * 31) ^ hash(self.types)
    value = (value * 31) ^ hash(self.deal)
    value = (value * 31) ^ hash(self.issave)
    value = (value * 31) ^ hash(self.hide)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SysMesg:
  """
  Attributes:
   - cdate
   - type
   - userGroup
   - content
   - hide
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'cdate', None, None, ), # 1
    (2, TType.I32, 'type', None, None, ), # 2
    (3, TType.STRING, 'userGroup', None, None, ), # 3
    (4, TType.STRING, 'content', None, None, ), # 4
    (5, TType.I32, 'hide', None, None, ), # 5
  )

  def __init__(self, cdate=None, type=None, userGroup=None, content=None, hide=None,):
    self.cdate = cdate
    self.type = type
    self.userGroup = userGroup
    self.content = content
    self.hide = hide

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
          self.cdate = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.userGroup = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.content = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.hide = iprot.readI32();
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
    oprot.writeStructBegin('SysMesg')
    if self.cdate is not None:
      oprot.writeFieldBegin('cdate', TType.I64, 1)
      oprot.writeI64(self.cdate)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 2)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.userGroup is not None:
      oprot.writeFieldBegin('userGroup', TType.STRING, 3)
      oprot.writeString(self.userGroup)
      oprot.writeFieldEnd()
    if self.content is not None:
      oprot.writeFieldBegin('content', TType.STRING, 4)
      oprot.writeString(self.content)
      oprot.writeFieldEnd()
    if self.hide is not None:
      oprot.writeFieldBegin('hide', TType.I32, 5)
      oprot.writeI32(self.hide)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.cdate)
    value = (value * 31) ^ hash(self.type)
    value = (value * 31) ^ hash(self.userGroup)
    value = (value * 31) ^ hash(self.content)
    value = (value * 31) ^ hash(self.hide)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
