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
  def findSensitive(self):
    """
    查询所有敏感词<br>
    """
    pass

  def addSensitive(self, words):
    """
    添加敏感词<br>

    Parameters:
     - words
    """
    pass

  def delSensitive(self, words):
    """
    删除敏感词<br>

    Parameters:
     - words
    """
    pass

  def updateAbout(self, webContent, appContent):
    """
    修改关于我们<br>

    Parameters:
     - webContent
     - appContent
    """
    pass

  def findAbout(self, webOrMob):
    """
    获取关于我们<br>

    Parameters:
     - webOrMob
    """
    pass

  def findService(self):
    """
    查询服务条款<br>
    """
    pass

  def udpateService(self, content):
    """
    更新服务条款<br>

    Parameters:
     - content
    """
    pass

  def publishNewAppVersion(self, appversion):
    """
    发布/编辑版本<br>
    issueDate	Long	发布时间<br>
    os	String	发布[平台 , IOS 和 ANDROID<br>
    vnum	Integer	版本号<br>
    url	String	下载地址<br>
    describe	String	更新说明<br>
    remark	String	备注<br>
    userGroup	String	更新用户组, 多字符串通过 ‘|’ 拼接<br>
    canal	String	渠道,多字符串通过 ‘|’ 拼接<br>
    option	String	可选, 多字符串通过 ‘|’ 拼接<br>
    havato	String	需要强制更新的, 多字符串通过 ‘|’ 拼接<br>

    Parameters:
     - appversion
    """
    pass

  def findHistoryVersions(self, os, vnum, canal, remark, describe, timeStart, timeEnd, start, count):
    """
    历史版本列表<br>
    os	String	平台 . <br>
    canal	String	渠道<br>
    vnum	Integer	版本号<br>
    remark	String	备注<br>
    describe	String	更新说明<br>
    timeStemp	String	时间段 , [开始时间Long]-[结束时间Long]<br>
    start	Integer	从start 开始返回<br>
    count	Integer	总共返回条数<br>

    Parameters:
     - os
     - vnum
     - canal
     - remark
     - describe
     - timeStart
     - timeEnd
     - start
     - count
    """
    pass

  def udpateAppversion(self, versions):
    """
    更新版本信息;

    Parameters:
     - versions
    """
    pass

  def findAllSysMesg(self, staTime, endTime, content, start, count):
    """
    系统消息列表<br>
    staTime	Long	时间段开始<br>
    endTime	Long	时间段结束<br>
    content	String	发布内容<br>
    start	Integer	返回开始条数<br>
    count	Integer	返回数据条数<br>

    Parameters:
     - staTime
     - endTime
     - content
     - start
     - count
    """
    pass

  def addEditSysMesg(self, cdate, types, userGroup, content):
    """
    添加/编辑-系统消息<br>
    cdate	Long	发布时间<br>
    types	Integer	发布消息形式 , 0系统消息(默认),1 推送消息<br>
    userGroup String	接收消息的用户组<br>
    content	String	消息内容, 就支持文本信息<br>

    Parameters:
     - cdate
     - types
     - userGroup
     - content
    """
    pass

  def findAdvice(self, uid, mobile, timeBegin, timeEnd, content, start, count):
    """
    查询意见反馈<br>
    uid	String	用户昵称或者用户昵称<br>
    mobile	String	用户手机号<br>
    beginEnd	String	查询时间段 [begin(Long)]-[end(Long)] <br>
    content	String	反馈内容<br>
    start	Integer	从排序后数据开始返回index.<br>
    count	Integer	返回总数据条数<br>

    Parameters:
     - uid
     - mobile
     - timeBegin
     - timeEnd
     - content
     - start
     - count
    """
    pass

  def holdReport(self, pid, types):
    """
    保留举报<br>
    pid	String	要保留题目或者回答的ID<br>
    types Integer 0 表示题目,1 表示回答<br>

    Parameters:
     - pid
     - types
    """
    pass

  def hideQuesOrAns(self, type, id, hide):
    """
    隐藏-题目/答案<br>

    Parameters:
     - type
     - id
     - hide
    """
    pass

  def findReports(self, isdeal, quesAns, groupId, themeIds, startTime, endtime, shareStart, shareEnd, repStart, repEnd, start, count):
    """
    查询举报

    Parameters:
     - isdeal
     - quesAns
     - groupId
     - themeIds
     - startTime
     - endtime
     - shareStart
     - shareEnd
     - repStart
     - repEnd
     - start
     - count
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def findSensitive(self):
    """
    查询所有敏感词<br>
    """
    self.send_findSensitive()
    return self.recv_findSensitive()

  def send_findSensitive(self):
    self._oprot.writeMessageBegin('findSensitive', TMessageType.CALL, self._seqid)
    args = findSensitive_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findSensitive(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findSensitive_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findSensitive failed: unknown result");

  def addSensitive(self, words):
    """
    添加敏感词<br>

    Parameters:
     - words
    """
    self.send_addSensitive(words)
    return self.recv_addSensitive()

  def send_addSensitive(self, words):
    self._oprot.writeMessageBegin('addSensitive', TMessageType.CALL, self._seqid)
    args = addSensitive_args()
    args.words = words
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_addSensitive(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = addSensitive_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "addSensitive failed: unknown result");

  def delSensitive(self, words):
    """
    删除敏感词<br>

    Parameters:
     - words
    """
    self.send_delSensitive(words)
    return self.recv_delSensitive()

  def send_delSensitive(self, words):
    self._oprot.writeMessageBegin('delSensitive', TMessageType.CALL, self._seqid)
    args = delSensitive_args()
    args.words = words
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_delSensitive(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = delSensitive_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "delSensitive failed: unknown result");

  def updateAbout(self, webContent, appContent):
    """
    修改关于我们<br>

    Parameters:
     - webContent
     - appContent
    """
    self.send_updateAbout(webContent, appContent)
    return self.recv_updateAbout()

  def send_updateAbout(self, webContent, appContent):
    self._oprot.writeMessageBegin('updateAbout', TMessageType.CALL, self._seqid)
    args = updateAbout_args()
    args.webContent = webContent
    args.appContent = appContent
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_updateAbout(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = updateAbout_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "updateAbout failed: unknown result");

  def findAbout(self, webOrMob):
    """
    获取关于我们<br>

    Parameters:
     - webOrMob
    """
    self.send_findAbout(webOrMob)
    return self.recv_findAbout()

  def send_findAbout(self, webOrMob):
    self._oprot.writeMessageBegin('findAbout', TMessageType.CALL, self._seqid)
    args = findAbout_args()
    args.webOrMob = webOrMob
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findAbout(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findAbout_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findAbout failed: unknown result");

  def findService(self):
    """
    查询服务条款<br>
    """
    self.send_findService()
    return self.recv_findService()

  def send_findService(self):
    self._oprot.writeMessageBegin('findService', TMessageType.CALL, self._seqid)
    args = findService_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findService(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findService_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findService failed: unknown result");

  def udpateService(self, content):
    """
    更新服务条款<br>

    Parameters:
     - content
    """
    self.send_udpateService(content)
    return self.recv_udpateService()

  def send_udpateService(self, content):
    self._oprot.writeMessageBegin('udpateService', TMessageType.CALL, self._seqid)
    args = udpateService_args()
    args.content = content
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_udpateService(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = udpateService_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "udpateService failed: unknown result");

  def publishNewAppVersion(self, appversion):
    """
    发布/编辑版本<br>
    issueDate	Long	发布时间<br>
    os	String	发布[平台 , IOS 和 ANDROID<br>
    vnum	Integer	版本号<br>
    url	String	下载地址<br>
    describe	String	更新说明<br>
    remark	String	备注<br>
    userGroup	String	更新用户组, 多字符串通过 ‘|’ 拼接<br>
    canal	String	渠道,多字符串通过 ‘|’ 拼接<br>
    option	String	可选, 多字符串通过 ‘|’ 拼接<br>
    havato	String	需要强制更新的, 多字符串通过 ‘|’ 拼接<br>

    Parameters:
     - appversion
    """
    self.send_publishNewAppVersion(appversion)
    return self.recv_publishNewAppVersion()

  def send_publishNewAppVersion(self, appversion):
    self._oprot.writeMessageBegin('publishNewAppVersion', TMessageType.CALL, self._seqid)
    args = publishNewAppVersion_args()
    args.appversion = appversion
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_publishNewAppVersion(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = publishNewAppVersion_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "publishNewAppVersion failed: unknown result");

  def findHistoryVersions(self, os, vnum, canal, remark, describe, timeStart, timeEnd, start, count):
    """
    历史版本列表<br>
    os	String	平台 . <br>
    canal	String	渠道<br>
    vnum	Integer	版本号<br>
    remark	String	备注<br>
    describe	String	更新说明<br>
    timeStemp	String	时间段 , [开始时间Long]-[结束时间Long]<br>
    start	Integer	从start 开始返回<br>
    count	Integer	总共返回条数<br>

    Parameters:
     - os
     - vnum
     - canal
     - remark
     - describe
     - timeStart
     - timeEnd
     - start
     - count
    """
    self.send_findHistoryVersions(os, vnum, canal, remark, describe, timeStart, timeEnd, start, count)
    return self.recv_findHistoryVersions()

  def send_findHistoryVersions(self, os, vnum, canal, remark, describe, timeStart, timeEnd, start, count):
    self._oprot.writeMessageBegin('findHistoryVersions', TMessageType.CALL, self._seqid)
    args = findHistoryVersions_args()
    args.os = os
    args.vnum = vnum
    args.canal = canal
    args.remark = remark
    args.describe = describe
    args.timeStart = timeStart
    args.timeEnd = timeEnd
    args.start = start
    args.count = count
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findHistoryVersions(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findHistoryVersions_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findHistoryVersions failed: unknown result");

  def udpateAppversion(self, versions):
    """
    更新版本信息;

    Parameters:
     - versions
    """
    self.send_udpateAppversion(versions)
    return self.recv_udpateAppversion()

  def send_udpateAppversion(self, versions):
    self._oprot.writeMessageBegin('udpateAppversion', TMessageType.CALL, self._seqid)
    args = udpateAppversion_args()
    args.versions = versions
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_udpateAppversion(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = udpateAppversion_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "udpateAppversion failed: unknown result");

  def findAllSysMesg(self, staTime, endTime, content, start, count):
    """
    系统消息列表<br>
    staTime	Long	时间段开始<br>
    endTime	Long	时间段结束<br>
    content	String	发布内容<br>
    start	Integer	返回开始条数<br>
    count	Integer	返回数据条数<br>

    Parameters:
     - staTime
     - endTime
     - content
     - start
     - count
    """
    self.send_findAllSysMesg(staTime, endTime, content, start, count)
    return self.recv_findAllSysMesg()

  def send_findAllSysMesg(self, staTime, endTime, content, start, count):
    self._oprot.writeMessageBegin('findAllSysMesg', TMessageType.CALL, self._seqid)
    args = findAllSysMesg_args()
    args.staTime = staTime
    args.endTime = endTime
    args.content = content
    args.start = start
    args.count = count
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findAllSysMesg(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findAllSysMesg_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findAllSysMesg failed: unknown result");

  def addEditSysMesg(self, cdate, types, userGroup, content):
    """
    添加/编辑-系统消息<br>
    cdate	Long	发布时间<br>
    types	Integer	发布消息形式 , 0系统消息(默认),1 推送消息<br>
    userGroup String	接收消息的用户组<br>
    content	String	消息内容, 就支持文本信息<br>

    Parameters:
     - cdate
     - types
     - userGroup
     - content
    """
    self.send_addEditSysMesg(cdate, types, userGroup, content)
    return self.recv_addEditSysMesg()

  def send_addEditSysMesg(self, cdate, types, userGroup, content):
    self._oprot.writeMessageBegin('addEditSysMesg', TMessageType.CALL, self._seqid)
    args = addEditSysMesg_args()
    args.cdate = cdate
    args.types = types
    args.userGroup = userGroup
    args.content = content
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_addEditSysMesg(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = addEditSysMesg_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "addEditSysMesg failed: unknown result");

  def findAdvice(self, uid, mobile, timeBegin, timeEnd, content, start, count):
    """
    查询意见反馈<br>
    uid	String	用户昵称或者用户昵称<br>
    mobile	String	用户手机号<br>
    beginEnd	String	查询时间段 [begin(Long)]-[end(Long)] <br>
    content	String	反馈内容<br>
    start	Integer	从排序后数据开始返回index.<br>
    count	Integer	返回总数据条数<br>

    Parameters:
     - uid
     - mobile
     - timeBegin
     - timeEnd
     - content
     - start
     - count
    """
    self.send_findAdvice(uid, mobile, timeBegin, timeEnd, content, start, count)
    return self.recv_findAdvice()

  def send_findAdvice(self, uid, mobile, timeBegin, timeEnd, content, start, count):
    self._oprot.writeMessageBegin('findAdvice', TMessageType.CALL, self._seqid)
    args = findAdvice_args()
    args.uid = uid
    args.mobile = mobile
    args.timeBegin = timeBegin
    args.timeEnd = timeEnd
    args.content = content
    args.start = start
    args.count = count
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findAdvice(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findAdvice_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findAdvice failed: unknown result");

  def holdReport(self, pid, types):
    """
    保留举报<br>
    pid	String	要保留题目或者回答的ID<br>
    types Integer 0 表示题目,1 表示回答<br>

    Parameters:
     - pid
     - types
    """
    self.send_holdReport(pid, types)
    return self.recv_holdReport()

  def send_holdReport(self, pid, types):
    self._oprot.writeMessageBegin('holdReport', TMessageType.CALL, self._seqid)
    args = holdReport_args()
    args.pid = pid
    args.types = types
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_holdReport(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = holdReport_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "holdReport failed: unknown result");

  def hideQuesOrAns(self, type, id, hide):
    """
    隐藏-题目/答案<br>

    Parameters:
     - type
     - id
     - hide
    """
    self.send_hideQuesOrAns(type, id, hide)
    return self.recv_hideQuesOrAns()

  def send_hideQuesOrAns(self, type, id, hide):
    self._oprot.writeMessageBegin('hideQuesOrAns', TMessageType.CALL, self._seqid)
    args = hideQuesOrAns_args()
    args.type = type
    args.id = id
    args.hide = hide
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_hideQuesOrAns(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = hideQuesOrAns_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "hideQuesOrAns failed: unknown result");

  def findReports(self, isdeal, quesAns, groupId, themeIds, startTime, endtime, shareStart, shareEnd, repStart, repEnd, start, count):
    """
    查询举报

    Parameters:
     - isdeal
     - quesAns
     - groupId
     - themeIds
     - startTime
     - endtime
     - shareStart
     - shareEnd
     - repStart
     - repEnd
     - start
     - count
    """
    self.send_findReports(isdeal, quesAns, groupId, themeIds, startTime, endtime, shareStart, shareEnd, repStart, repEnd, start, count)
    return self.recv_findReports()

  def send_findReports(self, isdeal, quesAns, groupId, themeIds, startTime, endtime, shareStart, shareEnd, repStart, repEnd, start, count):
    self._oprot.writeMessageBegin('findReports', TMessageType.CALL, self._seqid)
    args = findReports_args()
    args.isdeal = isdeal
    args.quesAns = quesAns
    args.groupId = groupId
    args.themeIds = themeIds
    args.startTime = startTime
    args.endtime = endtime
    args.shareStart = shareStart
    args.shareEnd = shareEnd
    args.repStart = repStart
    args.repEnd = repEnd
    args.start = start
    args.count = count
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findReports(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findReports_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findReports failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["findSensitive"] = Processor.process_findSensitive
    self._processMap["addSensitive"] = Processor.process_addSensitive
    self._processMap["delSensitive"] = Processor.process_delSensitive
    self._processMap["updateAbout"] = Processor.process_updateAbout
    self._processMap["findAbout"] = Processor.process_findAbout
    self._processMap["findService"] = Processor.process_findService
    self._processMap["udpateService"] = Processor.process_udpateService
    self._processMap["publishNewAppVersion"] = Processor.process_publishNewAppVersion
    self._processMap["findHistoryVersions"] = Processor.process_findHistoryVersions
    self._processMap["udpateAppversion"] = Processor.process_udpateAppversion
    self._processMap["findAllSysMesg"] = Processor.process_findAllSysMesg
    self._processMap["addEditSysMesg"] = Processor.process_addEditSysMesg
    self._processMap["findAdvice"] = Processor.process_findAdvice
    self._processMap["holdReport"] = Processor.process_holdReport
    self._processMap["hideQuesOrAns"] = Processor.process_hideQuesOrAns
    self._processMap["findReports"] = Processor.process_findReports

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

  def process_findSensitive(self, seqid, iprot, oprot):
    args = findSensitive_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findSensitive_result()
    result.success = self._handler.findSensitive()
    oprot.writeMessageBegin("findSensitive", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_addSensitive(self, seqid, iprot, oprot):
    args = addSensitive_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = addSensitive_result()
    result.success = self._handler.addSensitive(args.words)
    oprot.writeMessageBegin("addSensitive", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_delSensitive(self, seqid, iprot, oprot):
    args = delSensitive_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = delSensitive_result()
    result.success = self._handler.delSensitive(args.words)
    oprot.writeMessageBegin("delSensitive", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_updateAbout(self, seqid, iprot, oprot):
    args = updateAbout_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = updateAbout_result()
    result.success = self._handler.updateAbout(args.webContent, args.appContent)
    oprot.writeMessageBegin("updateAbout", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findAbout(self, seqid, iprot, oprot):
    args = findAbout_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findAbout_result()
    result.success = self._handler.findAbout(args.webOrMob)
    oprot.writeMessageBegin("findAbout", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findService(self, seqid, iprot, oprot):
    args = findService_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findService_result()
    result.success = self._handler.findService()
    oprot.writeMessageBegin("findService", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_udpateService(self, seqid, iprot, oprot):
    args = udpateService_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = udpateService_result()
    result.success = self._handler.udpateService(args.content)
    oprot.writeMessageBegin("udpateService", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_publishNewAppVersion(self, seqid, iprot, oprot):
    args = publishNewAppVersion_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = publishNewAppVersion_result()
    result.success = self._handler.publishNewAppVersion(args.appversion)
    oprot.writeMessageBegin("publishNewAppVersion", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findHistoryVersions(self, seqid, iprot, oprot):
    args = findHistoryVersions_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findHistoryVersions_result()
    result.success = self._handler.findHistoryVersions(args.os, args.vnum, args.canal, args.remark, args.describe, args.timeStart, args.timeEnd, args.start, args.count)
    oprot.writeMessageBegin("findHistoryVersions", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_udpateAppversion(self, seqid, iprot, oprot):
    args = udpateAppversion_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = udpateAppversion_result()
    result.success = self._handler.udpateAppversion(args.versions)
    oprot.writeMessageBegin("udpateAppversion", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findAllSysMesg(self, seqid, iprot, oprot):
    args = findAllSysMesg_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findAllSysMesg_result()
    result.success = self._handler.findAllSysMesg(args.staTime, args.endTime, args.content, args.start, args.count)
    oprot.writeMessageBegin("findAllSysMesg", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_addEditSysMesg(self, seqid, iprot, oprot):
    args = addEditSysMesg_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = addEditSysMesg_result()
    result.success = self._handler.addEditSysMesg(args.cdate, args.types, args.userGroup, args.content)
    oprot.writeMessageBegin("addEditSysMesg", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findAdvice(self, seqid, iprot, oprot):
    args = findAdvice_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findAdvice_result()
    result.success = self._handler.findAdvice(args.uid, args.mobile, args.timeBegin, args.timeEnd, args.content, args.start, args.count)
    oprot.writeMessageBegin("findAdvice", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_holdReport(self, seqid, iprot, oprot):
    args = holdReport_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = holdReport_result()
    result.success = self._handler.holdReport(args.pid, args.types)
    oprot.writeMessageBegin("holdReport", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_hideQuesOrAns(self, seqid, iprot, oprot):
    args = hideQuesOrAns_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = hideQuesOrAns_result()
    result.success = self._handler.hideQuesOrAns(args.type, args.id, args.hide)
    oprot.writeMessageBegin("hideQuesOrAns", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findReports(self, seqid, iprot, oprot):
    args = findReports_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findReports_result()
    result.success = self._handler.findReports(args.isdeal, args.quesAns, args.groupId, args.themeIds, args.startTime, args.endtime, args.shareStart, args.shareEnd, args.repStart, args.repEnd, args.start, args.count)
    oprot.writeMessageBegin("findReports", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class findSensitive_args:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('findSensitive_args')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class findSensitive_result:
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
          (_etype115, _size112) = iprot.readListBegin()
          for _i116 in xrange(_size112):
            _elem117 = iprot.readString();
            self.success.append(_elem117)
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
    oprot.writeStructBegin('findSensitive_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRING, len(self.success))
      for iter118 in self.success:
        oprot.writeString(iter118)
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

class addSensitive_args:
  """
  Attributes:
   - words
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'words', (TType.STRING,None), None, ), # 1
  )

  def __init__(self, words=None,):
    self.words = words

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
        if ftype == TType.LIST:
          self.words = []
          (_etype122, _size119) = iprot.readListBegin()
          for _i123 in xrange(_size119):
            _elem124 = iprot.readString();
            self.words.append(_elem124)
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
    oprot.writeStructBegin('addSensitive_args')
    if self.words is not None:
      oprot.writeFieldBegin('words', TType.LIST, 1)
      oprot.writeListBegin(TType.STRING, len(self.words))
      for iter125 in self.words:
        oprot.writeString(iter125)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.words)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class addSensitive_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
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
        if ftype == TType.STRING:
          self.success = iprot.readString();
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
    oprot.writeStructBegin('addSensitive_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
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

class delSensitive_args:
  """
  Attributes:
   - words
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'words', (TType.STRING,None), None, ), # 1
  )

  def __init__(self, words=None,):
    self.words = words

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
        if ftype == TType.LIST:
          self.words = []
          (_etype129, _size126) = iprot.readListBegin()
          for _i130 in xrange(_size126):
            _elem131 = iprot.readString();
            self.words.append(_elem131)
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
    oprot.writeStructBegin('delSensitive_args')
    if self.words is not None:
      oprot.writeFieldBegin('words', TType.LIST, 1)
      oprot.writeListBegin(TType.STRING, len(self.words))
      for iter132 in self.words:
        oprot.writeString(iter132)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.words)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class delSensitive_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
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
        if ftype == TType.STRING:
          self.success = iprot.readString();
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
    oprot.writeStructBegin('delSensitive_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
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

class updateAbout_args:
  """
  Attributes:
   - webContent
   - appContent
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'webContent', None, None, ), # 1
    (2, TType.STRING, 'appContent', None, None, ), # 2
  )

  def __init__(self, webContent=None, appContent=None,):
    self.webContent = webContent
    self.appContent = appContent

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
          self.webContent = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.appContent = iprot.readString();
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
    oprot.writeStructBegin('updateAbout_args')
    if self.webContent is not None:
      oprot.writeFieldBegin('webContent', TType.STRING, 1)
      oprot.writeString(self.webContent)
      oprot.writeFieldEnd()
    if self.appContent is not None:
      oprot.writeFieldBegin('appContent', TType.STRING, 2)
      oprot.writeString(self.appContent)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.webContent)
    value = (value * 31) ^ hash(self.appContent)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class updateAbout_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
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
        if ftype == TType.STRING:
          self.success = iprot.readString();
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
    oprot.writeStructBegin('updateAbout_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
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

class findAbout_args:
  """
  Attributes:
   - webOrMob
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'webOrMob', None, None, ), # 1
  )

  def __init__(self, webOrMob=None,):
    self.webOrMob = webOrMob

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
        if ftype == TType.I32:
          self.webOrMob = iprot.readI32();
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
    oprot.writeStructBegin('findAbout_args')
    if self.webOrMob is not None:
      oprot.writeFieldBegin('webOrMob', TType.I32, 1)
      oprot.writeI32(self.webOrMob)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.webOrMob)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class findAbout_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
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
        if ftype == TType.STRING:
          self.success = iprot.readString();
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
    oprot.writeStructBegin('findAbout_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
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

class findService_args:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('findService_args')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class findService_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
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
        if ftype == TType.STRING:
          self.success = iprot.readString();
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
    oprot.writeStructBegin('findService_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
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

class udpateService_args:
  """
  Attributes:
   - content
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'content', None, None, ), # 1
  )

  def __init__(self, content=None,):
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
    oprot.writeStructBegin('udpateService_args')
    if self.content is not None:
      oprot.writeFieldBegin('content', TType.STRING, 1)
      oprot.writeString(self.content)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
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

class udpateService_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
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
        if ftype == TType.STRING:
          self.success = iprot.readString();
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
    oprot.writeStructBegin('udpateService_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
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

class publishNewAppVersion_args:
  """
  Attributes:
   - appversion
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'appversion', (Version, Version.thrift_spec), None, ), # 1
  )

  def __init__(self, appversion=None,):
    self.appversion = appversion

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
        if ftype == TType.STRUCT:
          self.appversion = Version()
          self.appversion.read(iprot)
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
    oprot.writeStructBegin('publishNewAppVersion_args')
    if self.appversion is not None:
      oprot.writeFieldBegin('appversion', TType.STRUCT, 1)
      self.appversion.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.appversion)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class publishNewAppVersion_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
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
        if ftype == TType.STRING:
          self.success = iprot.readString();
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
    oprot.writeStructBegin('publishNewAppVersion_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
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

class findHistoryVersions_args:
  """
  Attributes:
   - os
   - vnum
   - canal
   - remark
   - describe
   - timeStart
   - timeEnd
   - start
   - count
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'os', None, None, ), # 1
    (2, TType.STRING, 'vnum', None, None, ), # 2
    (3, TType.STRING, 'canal', None, None, ), # 3
    (4, TType.STRING, 'remark', None, None, ), # 4
    (5, TType.STRING, 'describe', None, None, ), # 5
    (6, TType.I64, 'timeStart', None, None, ), # 6
    (7, TType.I64, 'timeEnd', None, None, ), # 7
    (8, TType.I32, 'start', None, None, ), # 8
    (9, TType.I32, 'count', None, None, ), # 9
  )

  def __init__(self, os=None, vnum=None, canal=None, remark=None, describe=None, timeStart=None, timeEnd=None, start=None, count=None,):
    self.os = os
    self.vnum = vnum
    self.canal = canal
    self.remark = remark
    self.describe = describe
    self.timeStart = timeStart
    self.timeEnd = timeEnd
    self.start = start
    self.count = count

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
          self.os = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.vnum = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.canal = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.remark = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.describe = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.timeStart = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.timeEnd = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.start = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I32:
          self.count = iprot.readI32();
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
    oprot.writeStructBegin('findHistoryVersions_args')
    if self.os is not None:
      oprot.writeFieldBegin('os', TType.STRING, 1)
      oprot.writeString(self.os)
      oprot.writeFieldEnd()
    if self.vnum is not None:
      oprot.writeFieldBegin('vnum', TType.STRING, 2)
      oprot.writeString(self.vnum)
      oprot.writeFieldEnd()
    if self.canal is not None:
      oprot.writeFieldBegin('canal', TType.STRING, 3)
      oprot.writeString(self.canal)
      oprot.writeFieldEnd()
    if self.remark is not None:
      oprot.writeFieldBegin('remark', TType.STRING, 4)
      oprot.writeString(self.remark)
      oprot.writeFieldEnd()
    if self.describe is not None:
      oprot.writeFieldBegin('describe', TType.STRING, 5)
      oprot.writeString(self.describe)
      oprot.writeFieldEnd()
    if self.timeStart is not None:
      oprot.writeFieldBegin('timeStart', TType.I64, 6)
      oprot.writeI64(self.timeStart)
      oprot.writeFieldEnd()
    if self.timeEnd is not None:
      oprot.writeFieldBegin('timeEnd', TType.I64, 7)
      oprot.writeI64(self.timeEnd)
      oprot.writeFieldEnd()
    if self.start is not None:
      oprot.writeFieldBegin('start', TType.I32, 8)
      oprot.writeI32(self.start)
      oprot.writeFieldEnd()
    if self.count is not None:
      oprot.writeFieldBegin('count', TType.I32, 9)
      oprot.writeI32(self.count)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.os)
    value = (value * 31) ^ hash(self.vnum)
    value = (value * 31) ^ hash(self.canal)
    value = (value * 31) ^ hash(self.remark)
    value = (value * 31) ^ hash(self.describe)
    value = (value * 31) ^ hash(self.timeStart)
    value = (value * 31) ^ hash(self.timeEnd)
    value = (value * 31) ^ hash(self.start)
    value = (value * 31) ^ hash(self.count)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class findHistoryVersions_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(Version, Version.thrift_spec)), None, ), # 0
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
          (_etype136, _size133) = iprot.readListBegin()
          for _i137 in xrange(_size133):
            _elem138 = Version()
            _elem138.read(iprot)
            self.success.append(_elem138)
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
    oprot.writeStructBegin('findHistoryVersions_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter139 in self.success:
        iter139.write(oprot)
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

class udpateAppversion_args:
  """
  Attributes:
   - versions
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'versions', (Version, Version.thrift_spec), None, ), # 1
  )

  def __init__(self, versions=None,):
    self.versions = versions

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
        if ftype == TType.STRUCT:
          self.versions = Version()
          self.versions.read(iprot)
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
    oprot.writeStructBegin('udpateAppversion_args')
    if self.versions is not None:
      oprot.writeFieldBegin('versions', TType.STRUCT, 1)
      self.versions.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.versions)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class udpateAppversion_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
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
        if ftype == TType.STRING:
          self.success = iprot.readString();
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
    oprot.writeStructBegin('udpateAppversion_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
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

class findAllSysMesg_args:
  """
  Attributes:
   - staTime
   - endTime
   - content
   - start
   - count
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'staTime', None, None, ), # 1
    (2, TType.I64, 'endTime', None, None, ), # 2
    (3, TType.STRING, 'content', None, None, ), # 3
    (4, TType.I32, 'start', None, None, ), # 4
    (5, TType.I32, 'count', None, None, ), # 5
  )

  def __init__(self, staTime=None, endTime=None, content=None, start=None, count=None,):
    self.staTime = staTime
    self.endTime = endTime
    self.content = content
    self.start = start
    self.count = count

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
          self.staTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.endTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.content = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.start = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.count = iprot.readI32();
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
    oprot.writeStructBegin('findAllSysMesg_args')
    if self.staTime is not None:
      oprot.writeFieldBegin('staTime', TType.I64, 1)
      oprot.writeI64(self.staTime)
      oprot.writeFieldEnd()
    if self.endTime is not None:
      oprot.writeFieldBegin('endTime', TType.I64, 2)
      oprot.writeI64(self.endTime)
      oprot.writeFieldEnd()
    if self.content is not None:
      oprot.writeFieldBegin('content', TType.STRING, 3)
      oprot.writeString(self.content)
      oprot.writeFieldEnd()
    if self.start is not None:
      oprot.writeFieldBegin('start', TType.I32, 4)
      oprot.writeI32(self.start)
      oprot.writeFieldEnd()
    if self.count is not None:
      oprot.writeFieldBegin('count', TType.I32, 5)
      oprot.writeI32(self.count)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.staTime)
    value = (value * 31) ^ hash(self.endTime)
    value = (value * 31) ^ hash(self.content)
    value = (value * 31) ^ hash(self.start)
    value = (value * 31) ^ hash(self.count)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class findAllSysMesg_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(SysMesg, SysMesg.thrift_spec)), None, ), # 0
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
          (_etype143, _size140) = iprot.readListBegin()
          for _i144 in xrange(_size140):
            _elem145 = SysMesg()
            _elem145.read(iprot)
            self.success.append(_elem145)
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
    oprot.writeStructBegin('findAllSysMesg_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter146 in self.success:
        iter146.write(oprot)
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

class addEditSysMesg_args:
  """
  Attributes:
   - cdate
   - types
   - userGroup
   - content
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'cdate', None, None, ), # 1
    (2, TType.I32, 'types', None, None, ), # 2
    (3, TType.STRING, 'userGroup', None, None, ), # 3
    (4, TType.STRING, 'content', None, None, ), # 4
  )

  def __init__(self, cdate=None, types=None, userGroup=None, content=None,):
    self.cdate = cdate
    self.types = types
    self.userGroup = userGroup
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
        if ftype == TType.I64:
          self.cdate = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.types = iprot.readI32();
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
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('addEditSysMesg_args')
    if self.cdate is not None:
      oprot.writeFieldBegin('cdate', TType.I64, 1)
      oprot.writeI64(self.cdate)
      oprot.writeFieldEnd()
    if self.types is not None:
      oprot.writeFieldBegin('types', TType.I32, 2)
      oprot.writeI32(self.types)
      oprot.writeFieldEnd()
    if self.userGroup is not None:
      oprot.writeFieldBegin('userGroup', TType.STRING, 3)
      oprot.writeString(self.userGroup)
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
    value = (value * 31) ^ hash(self.cdate)
    value = (value * 31) ^ hash(self.types)
    value = (value * 31) ^ hash(self.userGroup)
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

class addEditSysMesg_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
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
        if ftype == TType.STRING:
          self.success = iprot.readString();
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
    oprot.writeStructBegin('addEditSysMesg_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
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

class findAdvice_args:
  """
  Attributes:
   - uid
   - mobile
   - timeBegin
   - timeEnd
   - content
   - start
   - count
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'uid', None, None, ), # 1
    (2, TType.STRING, 'mobile', None, None, ), # 2
    (3, TType.I64, 'timeBegin', None, None, ), # 3
    (4, TType.I64, 'timeEnd', None, None, ), # 4
    (5, TType.STRING, 'content', None, None, ), # 5
    (6, TType.I32, 'start', None, None, ), # 6
    (7, TType.I32, 'count', None, None, ), # 7
  )

  def __init__(self, uid=None, mobile=None, timeBegin=None, timeEnd=None, content=None, start=None, count=None,):
    self.uid = uid
    self.mobile = mobile
    self.timeBegin = timeBegin
    self.timeEnd = timeEnd
    self.content = content
    self.start = start
    self.count = count

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
          self.mobile = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.timeBegin = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.timeEnd = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.content = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.start = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.count = iprot.readI32();
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
    oprot.writeStructBegin('findAdvice_args')
    if self.uid is not None:
      oprot.writeFieldBegin('uid', TType.STRING, 1)
      oprot.writeString(self.uid)
      oprot.writeFieldEnd()
    if self.mobile is not None:
      oprot.writeFieldBegin('mobile', TType.STRING, 2)
      oprot.writeString(self.mobile)
      oprot.writeFieldEnd()
    if self.timeBegin is not None:
      oprot.writeFieldBegin('timeBegin', TType.I64, 3)
      oprot.writeI64(self.timeBegin)
      oprot.writeFieldEnd()
    if self.timeEnd is not None:
      oprot.writeFieldBegin('timeEnd', TType.I64, 4)
      oprot.writeI64(self.timeEnd)
      oprot.writeFieldEnd()
    if self.content is not None:
      oprot.writeFieldBegin('content', TType.STRING, 5)
      oprot.writeString(self.content)
      oprot.writeFieldEnd()
    if self.start is not None:
      oprot.writeFieldBegin('start', TType.I32, 6)
      oprot.writeI32(self.start)
      oprot.writeFieldEnd()
    if self.count is not None:
      oprot.writeFieldBegin('count', TType.I32, 7)
      oprot.writeI32(self.count)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.uid)
    value = (value * 31) ^ hash(self.mobile)
    value = (value * 31) ^ hash(self.timeBegin)
    value = (value * 31) ^ hash(self.timeEnd)
    value = (value * 31) ^ hash(self.content)
    value = (value * 31) ^ hash(self.start)
    value = (value * 31) ^ hash(self.count)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class findAdvice_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(Advice, Advice.thrift_spec)), None, ), # 0
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
          (_etype150, _size147) = iprot.readListBegin()
          for _i151 in xrange(_size147):
            _elem152 = Advice()
            _elem152.read(iprot)
            self.success.append(_elem152)
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
    oprot.writeStructBegin('findAdvice_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter153 in self.success:
        iter153.write(oprot)
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

class holdReport_args:
  """
  Attributes:
   - pid
   - types
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'pid', None, None, ), # 1
    (2, TType.I32, 'types', None, None, ), # 2
  )

  def __init__(self, pid=None, types=None,):
    self.pid = pid
    self.types = types

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
          self.pid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.types = iprot.readI32();
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
    oprot.writeStructBegin('holdReport_args')
    if self.pid is not None:
      oprot.writeFieldBegin('pid', TType.STRING, 1)
      oprot.writeString(self.pid)
      oprot.writeFieldEnd()
    if self.types is not None:
      oprot.writeFieldBegin('types', TType.I32, 2)
      oprot.writeI32(self.types)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.pid)
    value = (value * 31) ^ hash(self.types)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class holdReport_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
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
        if ftype == TType.STRING:
          self.success = iprot.readString();
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
    oprot.writeStructBegin('holdReport_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
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

class hideQuesOrAns_args:
  """
  Attributes:
   - type
   - id
   - hide
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'type', None, None, ), # 1
    (2, TType.STRING, 'id', None, None, ), # 2
    (3, TType.I32, 'hide', None, None, ), # 3
  )

  def __init__(self, type=None, id=None, hide=None,):
    self.type = type
    self.id = id
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
          self.type = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
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
    oprot.writeStructBegin('hideQuesOrAns_args')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.STRING, 1)
      oprot.writeString(self.type)
      oprot.writeFieldEnd()
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.STRING, 2)
      oprot.writeString(self.id)
      oprot.writeFieldEnd()
    if self.hide is not None:
      oprot.writeFieldBegin('hide', TType.I32, 3)
      oprot.writeI32(self.hide)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.type)
    value = (value * 31) ^ hash(self.id)
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

class hideQuesOrAns_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
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
        if ftype == TType.STRING:
          self.success = iprot.readString();
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
    oprot.writeStructBegin('hideQuesOrAns_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
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

class findReports_args:
  """
  Attributes:
   - isdeal
   - quesAns
   - groupId
   - themeIds
   - startTime
   - endtime
   - shareStart
   - shareEnd
   - repStart
   - repEnd
   - start
   - count
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'isdeal', None, None, ), # 1
    (2, TType.I32, 'quesAns', None, None, ), # 2
    (3, TType.STRING, 'groupId', None, None, ), # 3
    (4, TType.STRING, 'themeIds', None, None, ), # 4
    (5, TType.I64, 'startTime', None, None, ), # 5
    (6, TType.I64, 'endtime', None, None, ), # 6
    (7, TType.I64, 'shareStart', None, None, ), # 7
    (8, TType.I64, 'shareEnd', None, None, ), # 8
    (9, TType.I64, 'repStart', None, None, ), # 9
    (10, TType.I64, 'repEnd', None, None, ), # 10
    (11, TType.I32, 'start', None, None, ), # 11
    (12, TType.I32, 'count', None, None, ), # 12
  )

  def __init__(self, isdeal=None, quesAns=None, groupId=None, themeIds=None, startTime=None, endtime=None, shareStart=None, shareEnd=None, repStart=None, repEnd=None, start=None, count=None,):
    self.isdeal = isdeal
    self.quesAns = quesAns
    self.groupId = groupId
    self.themeIds = themeIds
    self.startTime = startTime
    self.endtime = endtime
    self.shareStart = shareStart
    self.shareEnd = shareEnd
    self.repStart = repStart
    self.repEnd = repEnd
    self.start = start
    self.count = count

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
        if ftype == TType.I32:
          self.isdeal = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.quesAns = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.groupId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.themeIds = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.startTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.endtime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.shareStart = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I64:
          self.shareEnd = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I64:
          self.repStart = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I64:
          self.repEnd = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I32:
          self.start = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.I32:
          self.count = iprot.readI32();
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
    oprot.writeStructBegin('findReports_args')
    if self.isdeal is not None:
      oprot.writeFieldBegin('isdeal', TType.I32, 1)
      oprot.writeI32(self.isdeal)
      oprot.writeFieldEnd()
    if self.quesAns is not None:
      oprot.writeFieldBegin('quesAns', TType.I32, 2)
      oprot.writeI32(self.quesAns)
      oprot.writeFieldEnd()
    if self.groupId is not None:
      oprot.writeFieldBegin('groupId', TType.STRING, 3)
      oprot.writeString(self.groupId)
      oprot.writeFieldEnd()
    if self.themeIds is not None:
      oprot.writeFieldBegin('themeIds', TType.STRING, 4)
      oprot.writeString(self.themeIds)
      oprot.writeFieldEnd()
    if self.startTime is not None:
      oprot.writeFieldBegin('startTime', TType.I64, 5)
      oprot.writeI64(self.startTime)
      oprot.writeFieldEnd()
    if self.endtime is not None:
      oprot.writeFieldBegin('endtime', TType.I64, 6)
      oprot.writeI64(self.endtime)
      oprot.writeFieldEnd()
    if self.shareStart is not None:
      oprot.writeFieldBegin('shareStart', TType.I64, 7)
      oprot.writeI64(self.shareStart)
      oprot.writeFieldEnd()
    if self.shareEnd is not None:
      oprot.writeFieldBegin('shareEnd', TType.I64, 8)
      oprot.writeI64(self.shareEnd)
      oprot.writeFieldEnd()
    if self.repStart is not None:
      oprot.writeFieldBegin('repStart', TType.I64, 9)
      oprot.writeI64(self.repStart)
      oprot.writeFieldEnd()
    if self.repEnd is not None:
      oprot.writeFieldBegin('repEnd', TType.I64, 10)
      oprot.writeI64(self.repEnd)
      oprot.writeFieldEnd()
    if self.start is not None:
      oprot.writeFieldBegin('start', TType.I32, 11)
      oprot.writeI32(self.start)
      oprot.writeFieldEnd()
    if self.count is not None:
      oprot.writeFieldBegin('count', TType.I32, 12)
      oprot.writeI32(self.count)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.isdeal)
    value = (value * 31) ^ hash(self.quesAns)
    value = (value * 31) ^ hash(self.groupId)
    value = (value * 31) ^ hash(self.themeIds)
    value = (value * 31) ^ hash(self.startTime)
    value = (value * 31) ^ hash(self.endtime)
    value = (value * 31) ^ hash(self.shareStart)
    value = (value * 31) ^ hash(self.shareEnd)
    value = (value * 31) ^ hash(self.repStart)
    value = (value * 31) ^ hash(self.repEnd)
    value = (value * 31) ^ hash(self.start)
    value = (value * 31) ^ hash(self.count)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class findReports_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(Report, Report.thrift_spec)), None, ), # 0
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
          (_etype157, _size154) = iprot.readListBegin()
          for _i158 in xrange(_size154):
            _elem159 = Report()
            _elem159.read(iprot)
            self.success.append(_elem159)
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
    oprot.writeStructBegin('findReports_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter160 in self.success:
        iter160.write(oprot)
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
