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
  def addThemeClass(self, tgroups):
    """
    添加或者修改分类名称 , 如果已经有的会直接更改名称, 如果groupID没有-则新添一个分组<br>

    Parameters:
     - tgroups
    """
    pass

  def findThemeClass(self):
    """
    查询所有主题分类
    """
    pass

  def addTheme(self, theme):
    """
    添加主题,修改<br>
    主题ID,创建者ID , 主题名称 , 主题Logo , 主题描述 , 主题分类<br>
    className	String	分类名称<br>
    uid	String	创建者ID<br>
    name	String	主题分类名称<br>
    describe	String	主题描述<br>
    img	String	主题Logo地址<br>

    Parameters:
     - theme
    """
    pass

  def updateTheme(self, theme):
    """
    主题,修改<br>
    主题ID,创建者ID , 主题名称 , 主题Logo , 主题描述 , 主题分类<br>
    className	String	分类名称<br>
    uid	String	创建者ID<br>
    name	String	主题分类名称<br>
    describe	String	主题描述<br>
    img	String	主题Logo地址<br>

    Parameters:
     - theme
    """
    pass

  def findThemeById(self, tid):
    """
    Parameters:
     - tid
    """
    pass

  def findTheme(self, className, ugroups, userName, page, cou):
    """
    主题列表<br>
    参数 包含 一下参数<br>
    className	String	分类名称<br>
    ugroups	list<string> 用户组ID<br>
    userName	String	用户昵称<br>

    Parameters:
     - className
     - ugroups
     - userName
     - page
     - cou
    """
    pass

  def hideTheme(self, tid, hide):
    """
    隐藏主题
    qid	String	题目唯一ID
    hide	Integer	题目状态 0 不隐藏 1 为隐藏

    Parameters:
     - tid
     - hide
    """
    pass

  def addQuestion(self, ques):
    """
    添加题目<br>
    qid	String	问题唯一ID<br>
    tid	String	主题ID<br>
    name	String	题目名称<br>
    describe	String	题目描述<br>
    imgUrls	String	添加图片URL<br>
    createDate Long	添加主题实践<br>

    Parameters:
     - ques
    """
    pass

  def editQuestion(self, ques):
    """
    编辑题目 <br>
    qid	String	问题唯一ID<br>
    uid	String	发布人ID<br>
    tid	String	主题ID<br>
    name	String	题目名称<br>
    describe	String	题目描述<br>
    imgUrls	String	添加图片URL<br>
    createDate Long	添加主题实践<br>

    Parameters:
     - ques
    """
    pass

  def findQuestionByID(self, qid):
    """
    Parameters:
     - qid
    """
    pass

  def findQuestion(self, hide, name, describe, theme, qid, uid, ansStop, publishStart, publishEnd, ansStart, shareNum, shareEnd, usergroup, userType, page, cou):
    """
    查询题目 , 获取题目列表<br>
    hide	Integer	是否隐藏 0 否 1 是<br>
    name	String	题目<br>
    describe	String	题目描述<br>
    theme	String	主题-> 将主题名 通过| 链接起来<br>
    qid	String	题目ID<br>
    publishStart	Long	发布时间段开始 - <br>
    publishEnd	Long	发布时间段结束 -<br>
    ansStart	Long	回答数开始<br>
    ansStop	Long	回答次数结束<br>
    shareNum	Long	分享次数开始<br>
    shareEnd	Long	分享次数 结束<br>
    uid	String	用户ID<br>
    usergroup string	用户组类别 用户组ID <br>
    userType int	用户类别<br>
    page int	用户类别<br>
    cou int	用户类别<br>

    Parameters:
     - hide
     - name
     - describe
     - theme
     - qid
     - uid
     - ansStop
     - publishStart
     - publishEnd
     - ansStart
     - shareNum
     - shareEnd
     - usergroup
     - userType
     - page
     - cou
    """
    pass

  def addAnswer(self, answer):
    """
    添加答案 <br>
    内容 , 图片URL ,uid(发布人),createDate(发布时间)<br>
    qid	String	题目唯一ID<br>
    img	String	回答的附加图片<br>
    uid	String	发布用户ID<br>
    content	String	回答内容<br>
    cdate	Long	发布时间<br>

    Parameters:
     - answer
    """
    pass

  def editAnswer(self, anwer):
    """
    展开答案,获取答案列表<br>
    可根据需求修改要编辑的字段<br>

    Parameters:
     - anwer
    """
    pass

  def findAnswer(self, qid, aid, context, quesType, fr, to, page, cou):
    """
    展开答案,获取答案列表

    Parameters:
     - qid
     - aid
     - context
     - quesType
     - fr
     - to
     - page
     - cou
    """
    pass

  def hideAnswer(self, aid, hide):
    """
    隐藏/显示答案<br>
    aid	String	回答的唯一ID<br>
    hide	Integer	回答状态 0 不隐藏 1 为隐藏<br>

    Parameters:
     - aid
     - hide
    """
    pass

  def findAnswerByID(self, aid):
    """
    Parameters:
     - aid
    """
    pass

  def hideQuestion(self, qid, hide):
    """
    Parameters:
     - qid
     - hide
    """
    pass

  def editTheme(self, theme):
    """
    编辑主题

    Parameters:
     - theme
    """
    pass

  def findAnsQues(self, utype, anscon, aid, ansuname, ansuid, quescon, qid, sortType, sorta, sortz, ugroup, start, count):
    """
    search the question , to find the answer .

    Parameters:
     - utype
     - anscon
     - aid
     - ansuname
     - ansuid
     - quescon
     - qid
     - sortType
     - sorta
     - sortz
     - ugroup
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

  def addThemeClass(self, tgroups):
    """
    添加或者修改分类名称 , 如果已经有的会直接更改名称, 如果groupID没有-则新添一个分组<br>

    Parameters:
     - tgroups
    """
    self.send_addThemeClass(tgroups)
    return self.recv_addThemeClass()

  def send_addThemeClass(self, tgroups):
    self._oprot.writeMessageBegin('addThemeClass', TMessageType.CALL, self._seqid)
    args = addThemeClass_args()
    args.tgroups = tgroups
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_addThemeClass(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = addThemeClass_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "addThemeClass failed: unknown result");

  def findThemeClass(self):
    """
    查询所有主题分类
    """
    self.send_findThemeClass()
    return self.recv_findThemeClass()

  def send_findThemeClass(self):
    self._oprot.writeMessageBegin('findThemeClass', TMessageType.CALL, self._seqid)
    args = findThemeClass_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findThemeClass(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findThemeClass_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findThemeClass failed: unknown result");

  def addTheme(self, theme):
    """
    添加主题,修改<br>
    主题ID,创建者ID , 主题名称 , 主题Logo , 主题描述 , 主题分类<br>
    className	String	分类名称<br>
    uid	String	创建者ID<br>
    name	String	主题分类名称<br>
    describe	String	主题描述<br>
    img	String	主题Logo地址<br>

    Parameters:
     - theme
    """
    self.send_addTheme(theme)
    return self.recv_addTheme()

  def send_addTheme(self, theme):
    self._oprot.writeMessageBegin('addTheme', TMessageType.CALL, self._seqid)
    args = addTheme_args()
    args.theme = theme
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_addTheme(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = addTheme_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "addTheme failed: unknown result");

  def updateTheme(self, theme):
    """
    主题,修改<br>
    主题ID,创建者ID , 主题名称 , 主题Logo , 主题描述 , 主题分类<br>
    className	String	分类名称<br>
    uid	String	创建者ID<br>
    name	String	主题分类名称<br>
    describe	String	主题描述<br>
    img	String	主题Logo地址<br>

    Parameters:
     - theme
    """
    self.send_updateTheme(theme)
    return self.recv_updateTheme()

  def send_updateTheme(self, theme):
    self._oprot.writeMessageBegin('updateTheme', TMessageType.CALL, self._seqid)
    args = updateTheme_args()
    args.theme = theme
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_updateTheme(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = updateTheme_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "updateTheme failed: unknown result");

  def findThemeById(self, tid):
    """
    Parameters:
     - tid
    """
    self.send_findThemeById(tid)
    return self.recv_findThemeById()

  def send_findThemeById(self, tid):
    self._oprot.writeMessageBegin('findThemeById', TMessageType.CALL, self._seqid)
    args = findThemeById_args()
    args.tid = tid
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findThemeById(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findThemeById_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findThemeById failed: unknown result");

  def findTheme(self, className, ugroups, userName, page, cou):
    """
    主题列表<br>
    参数 包含 一下参数<br>
    className	String	分类名称<br>
    ugroups	list<string> 用户组ID<br>
    userName	String	用户昵称<br>

    Parameters:
     - className
     - ugroups
     - userName
     - page
     - cou
    """
    self.send_findTheme(className, ugroups, userName, page, cou)
    return self.recv_findTheme()

  def send_findTheme(self, className, ugroups, userName, page, cou):
    self._oprot.writeMessageBegin('findTheme', TMessageType.CALL, self._seqid)
    args = findTheme_args()
    args.className = className
    args.ugroups = ugroups
    args.userName = userName
    args.page = page
    args.cou = cou
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findTheme(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findTheme_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findTheme failed: unknown result");

  def hideTheme(self, tid, hide):
    """
    隐藏主题
    qid	String	题目唯一ID
    hide	Integer	题目状态 0 不隐藏 1 为隐藏

    Parameters:
     - tid
     - hide
    """
    self.send_hideTheme(tid, hide)
    return self.recv_hideTheme()

  def send_hideTheme(self, tid, hide):
    self._oprot.writeMessageBegin('hideTheme', TMessageType.CALL, self._seqid)
    args = hideTheme_args()
    args.tid = tid
    args.hide = hide
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_hideTheme(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = hideTheme_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "hideTheme failed: unknown result");

  def addQuestion(self, ques):
    """
    添加题目<br>
    qid	String	问题唯一ID<br>
    tid	String	主题ID<br>
    name	String	题目名称<br>
    describe	String	题目描述<br>
    imgUrls	String	添加图片URL<br>
    createDate Long	添加主题实践<br>

    Parameters:
     - ques
    """
    self.send_addQuestion(ques)
    return self.recv_addQuestion()

  def send_addQuestion(self, ques):
    self._oprot.writeMessageBegin('addQuestion', TMessageType.CALL, self._seqid)
    args = addQuestion_args()
    args.ques = ques
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_addQuestion(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = addQuestion_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "addQuestion failed: unknown result");

  def editQuestion(self, ques):
    """
    编辑题目 <br>
    qid	String	问题唯一ID<br>
    uid	String	发布人ID<br>
    tid	String	主题ID<br>
    name	String	题目名称<br>
    describe	String	题目描述<br>
    imgUrls	String	添加图片URL<br>
    createDate Long	添加主题实践<br>

    Parameters:
     - ques
    """
    self.send_editQuestion(ques)
    return self.recv_editQuestion()

  def send_editQuestion(self, ques):
    self._oprot.writeMessageBegin('editQuestion', TMessageType.CALL, self._seqid)
    args = editQuestion_args()
    args.ques = ques
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_editQuestion(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = editQuestion_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "editQuestion failed: unknown result");

  def findQuestionByID(self, qid):
    """
    Parameters:
     - qid
    """
    self.send_findQuestionByID(qid)
    return self.recv_findQuestionByID()

  def send_findQuestionByID(self, qid):
    self._oprot.writeMessageBegin('findQuestionByID', TMessageType.CALL, self._seqid)
    args = findQuestionByID_args()
    args.qid = qid
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findQuestionByID(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findQuestionByID_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findQuestionByID failed: unknown result");

  def findQuestion(self, hide, name, describe, theme, qid, uid, ansStop, publishStart, publishEnd, ansStart, shareNum, shareEnd, usergroup, userType, page, cou):
    """
    查询题目 , 获取题目列表<br>
    hide	Integer	是否隐藏 0 否 1 是<br>
    name	String	题目<br>
    describe	String	题目描述<br>
    theme	String	主题-> 将主题名 通过| 链接起来<br>
    qid	String	题目ID<br>
    publishStart	Long	发布时间段开始 - <br>
    publishEnd	Long	发布时间段结束 -<br>
    ansStart	Long	回答数开始<br>
    ansStop	Long	回答次数结束<br>
    shareNum	Long	分享次数开始<br>
    shareEnd	Long	分享次数 结束<br>
    uid	String	用户ID<br>
    usergroup string	用户组类别 用户组ID <br>
    userType int	用户类别<br>
    page int	用户类别<br>
    cou int	用户类别<br>

    Parameters:
     - hide
     - name
     - describe
     - theme
     - qid
     - uid
     - ansStop
     - publishStart
     - publishEnd
     - ansStart
     - shareNum
     - shareEnd
     - usergroup
     - userType
     - page
     - cou
    """
    self.send_findQuestion(hide, name, describe, theme, qid, uid, ansStop, publishStart, publishEnd, ansStart, shareNum, shareEnd, usergroup, userType, page, cou)
    return self.recv_findQuestion()

  def send_findQuestion(self, hide, name, describe, theme, qid, uid, ansStop, publishStart, publishEnd, ansStart, shareNum, shareEnd, usergroup, userType, page, cou):
    self._oprot.writeMessageBegin('findQuestion', TMessageType.CALL, self._seqid)
    args = findQuestion_args()
    args.hide = hide
    args.name = name
    args.describe = describe
    args.theme = theme
    args.qid = qid
    args.uid = uid
    args.ansStop = ansStop
    args.publishStart = publishStart
    args.publishEnd = publishEnd
    args.ansStart = ansStart
    args.shareNum = shareNum
    args.shareEnd = shareEnd
    args.usergroup = usergroup
    args.userType = userType
    args.page = page
    args.cou = cou
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findQuestion(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findQuestion_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findQuestion failed: unknown result");

  def addAnswer(self, answer):
    """
    添加答案 <br>
    内容 , 图片URL ,uid(发布人),createDate(发布时间)<br>
    qid	String	题目唯一ID<br>
    img	String	回答的附加图片<br>
    uid	String	发布用户ID<br>
    content	String	回答内容<br>
    cdate	Long	发布时间<br>

    Parameters:
     - answer
    """
    self.send_addAnswer(answer)
    return self.recv_addAnswer()

  def send_addAnswer(self, answer):
    self._oprot.writeMessageBegin('addAnswer', TMessageType.CALL, self._seqid)
    args = addAnswer_args()
    args.answer = answer
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_addAnswer(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = addAnswer_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "addAnswer failed: unknown result");

  def editAnswer(self, anwer):
    """
    展开答案,获取答案列表<br>
    可根据需求修改要编辑的字段<br>

    Parameters:
     - anwer
    """
    self.send_editAnswer(anwer)
    return self.recv_editAnswer()

  def send_editAnswer(self, anwer):
    self._oprot.writeMessageBegin('editAnswer', TMessageType.CALL, self._seqid)
    args = editAnswer_args()
    args.anwer = anwer
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_editAnswer(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = editAnswer_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "editAnswer failed: unknown result");

  def findAnswer(self, qid, aid, context, quesType, fr, to, page, cou):
    """
    展开答案,获取答案列表

    Parameters:
     - qid
     - aid
     - context
     - quesType
     - fr
     - to
     - page
     - cou
    """
    self.send_findAnswer(qid, aid, context, quesType, fr, to, page, cou)
    return self.recv_findAnswer()

  def send_findAnswer(self, qid, aid, context, quesType, fr, to, page, cou):
    self._oprot.writeMessageBegin('findAnswer', TMessageType.CALL, self._seqid)
    args = findAnswer_args()
    args.qid = qid
    args.aid = aid
    args.context = context
    args.quesType = quesType
    args.fr = fr
    args.to = to
    args.page = page
    args.cou = cou
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findAnswer(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findAnswer_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findAnswer failed: unknown result");

  def hideAnswer(self, aid, hide):
    """
    隐藏/显示答案<br>
    aid	String	回答的唯一ID<br>
    hide	Integer	回答状态 0 不隐藏 1 为隐藏<br>

    Parameters:
     - aid
     - hide
    """
    self.send_hideAnswer(aid, hide)
    return self.recv_hideAnswer()

  def send_hideAnswer(self, aid, hide):
    self._oprot.writeMessageBegin('hideAnswer', TMessageType.CALL, self._seqid)
    args = hideAnswer_args()
    args.aid = aid
    args.hide = hide
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_hideAnswer(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = hideAnswer_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "hideAnswer failed: unknown result");

  def findAnswerByID(self, aid):
    """
    Parameters:
     - aid
    """
    self.send_findAnswerByID(aid)
    return self.recv_findAnswerByID()

  def send_findAnswerByID(self, aid):
    self._oprot.writeMessageBegin('findAnswerByID', TMessageType.CALL, self._seqid)
    args = findAnswerByID_args()
    args.aid = aid
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findAnswerByID(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findAnswerByID_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findAnswerByID failed: unknown result");

  def hideQuestion(self, qid, hide):
    """
    Parameters:
     - qid
     - hide
    """
    self.send_hideQuestion(qid, hide)
    return self.recv_hideQuestion()

  def send_hideQuestion(self, qid, hide):
    self._oprot.writeMessageBegin('hideQuestion', TMessageType.CALL, self._seqid)
    args = hideQuestion_args()
    args.qid = qid
    args.hide = hide
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_hideQuestion(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = hideQuestion_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "hideQuestion failed: unknown result");

  def editTheme(self, theme):
    """
    编辑主题

    Parameters:
     - theme
    """
    self.send_editTheme(theme)
    return self.recv_editTheme()

  def send_editTheme(self, theme):
    self._oprot.writeMessageBegin('editTheme', TMessageType.CALL, self._seqid)
    args = editTheme_args()
    args.theme = theme
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_editTheme(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = editTheme_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "editTheme failed: unknown result");

  def findAnsQues(self, utype, anscon, aid, ansuname, ansuid, quescon, qid, sortType, sorta, sortz, ugroup, start, count):
    """
    search the question , to find the answer .

    Parameters:
     - utype
     - anscon
     - aid
     - ansuname
     - ansuid
     - quescon
     - qid
     - sortType
     - sorta
     - sortz
     - ugroup
     - start
     - count
    """
    self.send_findAnsQues(utype, anscon, aid, ansuname, ansuid, quescon, qid, sortType, sorta, sortz, ugroup, start, count)
    return self.recv_findAnsQues()

  def send_findAnsQues(self, utype, anscon, aid, ansuname, ansuid, quescon, qid, sortType, sorta, sortz, ugroup, start, count):
    self._oprot.writeMessageBegin('findAnsQues', TMessageType.CALL, self._seqid)
    args = findAnsQues_args()
    args.utype = utype
    args.anscon = anscon
    args.aid = aid
    args.ansuname = ansuname
    args.ansuid = ansuid
    args.quescon = quescon
    args.qid = qid
    args.sortType = sortType
    args.sorta = sorta
    args.sortz = sortz
    args.ugroup = ugroup
    args.start = start
    args.count = count
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_findAnsQues(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = findAnsQues_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "findAnsQues failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["addThemeClass"] = Processor.process_addThemeClass
    self._processMap["findThemeClass"] = Processor.process_findThemeClass
    self._processMap["addTheme"] = Processor.process_addTheme
    self._processMap["updateTheme"] = Processor.process_updateTheme
    self._processMap["findThemeById"] = Processor.process_findThemeById
    self._processMap["findTheme"] = Processor.process_findTheme
    self._processMap["hideTheme"] = Processor.process_hideTheme
    self._processMap["addQuestion"] = Processor.process_addQuestion
    self._processMap["editQuestion"] = Processor.process_editQuestion
    self._processMap["findQuestionByID"] = Processor.process_findQuestionByID
    self._processMap["findQuestion"] = Processor.process_findQuestion
    self._processMap["addAnswer"] = Processor.process_addAnswer
    self._processMap["editAnswer"] = Processor.process_editAnswer
    self._processMap["findAnswer"] = Processor.process_findAnswer
    self._processMap["hideAnswer"] = Processor.process_hideAnswer
    self._processMap["findAnswerByID"] = Processor.process_findAnswerByID
    self._processMap["hideQuestion"] = Processor.process_hideQuestion
    self._processMap["editTheme"] = Processor.process_editTheme
    self._processMap["findAnsQues"] = Processor.process_findAnsQues

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

  def process_addThemeClass(self, seqid, iprot, oprot):
    args = addThemeClass_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = addThemeClass_result()
    result.success = self._handler.addThemeClass(args.tgroups)
    oprot.writeMessageBegin("addThemeClass", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findThemeClass(self, seqid, iprot, oprot):
    args = findThemeClass_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findThemeClass_result()
    result.success = self._handler.findThemeClass()
    oprot.writeMessageBegin("findThemeClass", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_addTheme(self, seqid, iprot, oprot):
    args = addTheme_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = addTheme_result()
    result.success = self._handler.addTheme(args.theme)
    oprot.writeMessageBegin("addTheme", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_updateTheme(self, seqid, iprot, oprot):
    args = updateTheme_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = updateTheme_result()
    result.success = self._handler.updateTheme(args.theme)
    oprot.writeMessageBegin("updateTheme", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findThemeById(self, seqid, iprot, oprot):
    args = findThemeById_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findThemeById_result()
    result.success = self._handler.findThemeById(args.tid)
    oprot.writeMessageBegin("findThemeById", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findTheme(self, seqid, iprot, oprot):
    args = findTheme_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findTheme_result()
    result.success = self._handler.findTheme(args.className, args.ugroups, args.userName, args.page, args.cou)
    oprot.writeMessageBegin("findTheme", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_hideTheme(self, seqid, iprot, oprot):
    args = hideTheme_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = hideTheme_result()
    result.success = self._handler.hideTheme(args.tid, args.hide)
    oprot.writeMessageBegin("hideTheme", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_addQuestion(self, seqid, iprot, oprot):
    args = addQuestion_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = addQuestion_result()
    result.success = self._handler.addQuestion(args.ques)
    oprot.writeMessageBegin("addQuestion", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_editQuestion(self, seqid, iprot, oprot):
    args = editQuestion_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = editQuestion_result()
    result.success = self._handler.editQuestion(args.ques)
    oprot.writeMessageBegin("editQuestion", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findQuestionByID(self, seqid, iprot, oprot):
    args = findQuestionByID_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findQuestionByID_result()
    result.success = self._handler.findQuestionByID(args.qid)
    oprot.writeMessageBegin("findQuestionByID", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findQuestion(self, seqid, iprot, oprot):
    args = findQuestion_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findQuestion_result()
    result.success = self._handler.findQuestion(args.hide, args.name, args.describe, args.theme, args.qid, args.uid, args.ansStop, args.publishStart, args.publishEnd, args.ansStart, args.shareNum, args.shareEnd, args.usergroup, args.userType, args.page, args.cou)
    oprot.writeMessageBegin("findQuestion", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_addAnswer(self, seqid, iprot, oprot):
    args = addAnswer_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = addAnswer_result()
    result.success = self._handler.addAnswer(args.answer)
    oprot.writeMessageBegin("addAnswer", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_editAnswer(self, seqid, iprot, oprot):
    args = editAnswer_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = editAnswer_result()
    result.success = self._handler.editAnswer(args.anwer)
    oprot.writeMessageBegin("editAnswer", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findAnswer(self, seqid, iprot, oprot):
    args = findAnswer_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findAnswer_result()
    result.success = self._handler.findAnswer(args.qid, args.aid, args.context, args.quesType, args.fr, args.to, args.page, args.cou)
    oprot.writeMessageBegin("findAnswer", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_hideAnswer(self, seqid, iprot, oprot):
    args = hideAnswer_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = hideAnswer_result()
    result.success = self._handler.hideAnswer(args.aid, args.hide)
    oprot.writeMessageBegin("hideAnswer", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findAnswerByID(self, seqid, iprot, oprot):
    args = findAnswerByID_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findAnswerByID_result()
    result.success = self._handler.findAnswerByID(args.aid)
    oprot.writeMessageBegin("findAnswerByID", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_hideQuestion(self, seqid, iprot, oprot):
    args = hideQuestion_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = hideQuestion_result()
    result.success = self._handler.hideQuestion(args.qid, args.hide)
    oprot.writeMessageBegin("hideQuestion", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_editTheme(self, seqid, iprot, oprot):
    args = editTheme_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = editTheme_result()
    result.success = self._handler.editTheme(args.theme)
    oprot.writeMessageBegin("editTheme", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_findAnsQues(self, seqid, iprot, oprot):
    args = findAnsQues_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = findAnsQues_result()
    result.success = self._handler.findAnsQues(args.utype, args.anscon, args.aid, args.ansuname, args.ansuid, args.quescon, args.qid, args.sortType, args.sorta, args.sortz, args.ugroup, args.start, args.count)
    oprot.writeMessageBegin("findAnsQues", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class addThemeClass_args:
  """
  Attributes:
   - tgroups
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'tgroups', (TType.STRUCT,(GroupList, GroupList.thrift_spec)), None, ), # 1
  )

  def __init__(self, tgroups=None,):
    self.tgroups = tgroups

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
          self.tgroups = []
          (_etype52, _size49) = iprot.readListBegin()
          for _i53 in xrange(_size49):
            _elem54 = GroupList()
            _elem54.read(iprot)
            self.tgroups.append(_elem54)
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
    oprot.writeStructBegin('addThemeClass_args')
    if self.tgroups is not None:
      oprot.writeFieldBegin('tgroups', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.tgroups))
      for iter55 in self.tgroups:
        iter55.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.tgroups)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class addThemeClass_result:
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
    oprot.writeStructBegin('addThemeClass_result')
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

class findThemeClass_args:

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
    oprot.writeStructBegin('findThemeClass_args')
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

class findThemeClass_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(GroupList, GroupList.thrift_spec)), None, ), # 0
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
          (_etype59, _size56) = iprot.readListBegin()
          for _i60 in xrange(_size56):
            _elem61 = GroupList()
            _elem61.read(iprot)
            self.success.append(_elem61)
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
    oprot.writeStructBegin('findThemeClass_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter62 in self.success:
        iter62.write(oprot)
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

class addTheme_args:
  """
  Attributes:
   - theme
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'theme', (Theme, Theme.thrift_spec), None, ), # 1
  )

  def __init__(self, theme=None,):
    self.theme = theme

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
          self.theme = Theme()
          self.theme.read(iprot)
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
    oprot.writeStructBegin('addTheme_args')
    if self.theme is not None:
      oprot.writeFieldBegin('theme', TType.STRUCT, 1)
      self.theme.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.theme)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class addTheme_result:
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
    oprot.writeStructBegin('addTheme_result')
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

class updateTheme_args:
  """
  Attributes:
   - theme
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'theme', (Theme, Theme.thrift_spec), None, ), # 1
  )

  def __init__(self, theme=None,):
    self.theme = theme

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
          self.theme = Theme()
          self.theme.read(iprot)
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
    oprot.writeStructBegin('updateTheme_args')
    if self.theme is not None:
      oprot.writeFieldBegin('theme', TType.STRUCT, 1)
      self.theme.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.theme)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class updateTheme_result:
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
    oprot.writeStructBegin('updateTheme_result')
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

class findThemeById_args:
  """
  Attributes:
   - tid
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'tid', None, None, ), # 1
  )

  def __init__(self, tid=None,):
    self.tid = tid

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
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('findThemeById_args')
    if self.tid is not None:
      oprot.writeFieldBegin('tid', TType.STRING, 1)
      oprot.writeString(self.tid)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.tid)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class findThemeById_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Theme, Theme.thrift_spec), None, ), # 0
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
        if ftype == TType.STRUCT:
          self.success = Theme()
          self.success.read(iprot)
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
    oprot.writeStructBegin('findThemeById_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
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

class findTheme_args:
  """
  Attributes:
   - className
   - ugroups
   - userName
   - page
   - cou
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'className', None, None, ), # 1
    (2, TType.LIST, 'ugroups', (TType.STRING,None), None, ), # 2
    (3, TType.STRING, 'userName', None, None, ), # 3
    (4, TType.I32, 'page', None, None, ), # 4
    (5, TType.I32, 'cou', None, None, ), # 5
  )

  def __init__(self, className=None, ugroups=None, userName=None, page=None, cou=None,):
    self.className = className
    self.ugroups = ugroups
    self.userName = userName
    self.page = page
    self.cou = cou

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
          self.className = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.ugroups = []
          (_etype66, _size63) = iprot.readListBegin()
          for _i67 in xrange(_size63):
            _elem68 = iprot.readString();
            self.ugroups.append(_elem68)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.userName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.page = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.cou = iprot.readI32();
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
    oprot.writeStructBegin('findTheme_args')
    if self.className is not None:
      oprot.writeFieldBegin('className', TType.STRING, 1)
      oprot.writeString(self.className)
      oprot.writeFieldEnd()
    if self.ugroups is not None:
      oprot.writeFieldBegin('ugroups', TType.LIST, 2)
      oprot.writeListBegin(TType.STRING, len(self.ugroups))
      for iter69 in self.ugroups:
        oprot.writeString(iter69)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.userName is not None:
      oprot.writeFieldBegin('userName', TType.STRING, 3)
      oprot.writeString(self.userName)
      oprot.writeFieldEnd()
    if self.page is not None:
      oprot.writeFieldBegin('page', TType.I32, 4)
      oprot.writeI32(self.page)
      oprot.writeFieldEnd()
    if self.cou is not None:
      oprot.writeFieldBegin('cou', TType.I32, 5)
      oprot.writeI32(self.cou)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.className)
    value = (value * 31) ^ hash(self.ugroups)
    value = (value * 31) ^ hash(self.userName)
    value = (value * 31) ^ hash(self.page)
    value = (value * 31) ^ hash(self.cou)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class findTheme_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(Theme, Theme.thrift_spec)), None, ), # 0
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
          (_etype73, _size70) = iprot.readListBegin()
          for _i74 in xrange(_size70):
            _elem75 = Theme()
            _elem75.read(iprot)
            self.success.append(_elem75)
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
    oprot.writeStructBegin('findTheme_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter76 in self.success:
        iter76.write(oprot)
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

class hideTheme_args:
  """
  Attributes:
   - tid
   - hide
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'tid', None, None, ), # 1
    (2, TType.I32, 'hide', None, None, ), # 2
  )

  def __init__(self, tid=None, hide=None,):
    self.tid = tid
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
          self.tid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
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
    oprot.writeStructBegin('hideTheme_args')
    if self.tid is not None:
      oprot.writeFieldBegin('tid', TType.STRING, 1)
      oprot.writeString(self.tid)
      oprot.writeFieldEnd()
    if self.hide is not None:
      oprot.writeFieldBegin('hide', TType.I32, 2)
      oprot.writeI32(self.hide)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.tid)
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

class hideTheme_result:
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
    oprot.writeStructBegin('hideTheme_result')
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

class addQuestion_args:
  """
  Attributes:
   - ques
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'ques', (Question, Question.thrift_spec), None, ), # 1
  )

  def __init__(self, ques=None,):
    self.ques = ques

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
          self.ques = Question()
          self.ques.read(iprot)
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
    oprot.writeStructBegin('addQuestion_args')
    if self.ques is not None:
      oprot.writeFieldBegin('ques', TType.STRUCT, 1)
      self.ques.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.ques)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class addQuestion_result:
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
    oprot.writeStructBegin('addQuestion_result')
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

class editQuestion_args:
  """
  Attributes:
   - ques
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'ques', (Question, Question.thrift_spec), None, ), # 1
  )

  def __init__(self, ques=None,):
    self.ques = ques

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
          self.ques = Question()
          self.ques.read(iprot)
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
    oprot.writeStructBegin('editQuestion_args')
    if self.ques is not None:
      oprot.writeFieldBegin('ques', TType.STRUCT, 1)
      self.ques.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.ques)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class editQuestion_result:
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
    oprot.writeStructBegin('editQuestion_result')
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

class findQuestionByID_args:
  """
  Attributes:
   - qid
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'qid', None, None, ), # 1
  )

  def __init__(self, qid=None,):
    self.qid = qid

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
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('findQuestionByID_args')
    if self.qid is not None:
      oprot.writeFieldBegin('qid', TType.STRING, 1)
      oprot.writeString(self.qid)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.qid)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class findQuestionByID_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Question, Question.thrift_spec), None, ), # 0
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
        if ftype == TType.STRUCT:
          self.success = Question()
          self.success.read(iprot)
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
    oprot.writeStructBegin('findQuestionByID_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
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

class findQuestion_args:
  """
  Attributes:
   - hide
   - name
   - describe
   - theme
   - qid
   - uid
   - ansStop
   - publishStart
   - publishEnd
   - ansStart
   - shareNum
   - shareEnd
   - usergroup
   - userType
   - page
   - cou
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'hide', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.STRING, 'describe', None, None, ), # 3
    (4, TType.STRING, 'theme', None, None, ), # 4
    (5, TType.STRING, 'qid', None, None, ), # 5
    (6, TType.STRING, 'uid', None, None, ), # 6
    (7, TType.I64, 'ansStop', None, None, ), # 7
    (8, TType.I64, 'publishStart', None, None, ), # 8
    (9, TType.I64, 'publishEnd', None, None, ), # 9
    (10, TType.I64, 'ansStart', None, None, ), # 10
    (11, TType.I64, 'shareNum', None, None, ), # 11
    (12, TType.I64, 'shareEnd', None, None, ), # 12
    (13, TType.STRING, 'usergroup', None, None, ), # 13
    (14, TType.I32, 'userType', None, None, ), # 14
    (15, TType.I32, 'page', None, None, ), # 15
    (16, TType.I32, 'cou', None, None, ), # 16
  )

  def __init__(self, hide=None, name=None, describe=None, theme=None, qid=None, uid=None, ansStop=None, publishStart=None, publishEnd=None, ansStart=None, shareNum=None, shareEnd=None, usergroup=None, userType=None, page=None, cou=None,):
    self.hide = hide
    self.name = name
    self.describe = describe
    self.theme = theme
    self.qid = qid
    self.uid = uid
    self.ansStop = ansStop
    self.publishStart = publishStart
    self.publishEnd = publishEnd
    self.ansStart = ansStart
    self.shareNum = shareNum
    self.shareEnd = shareEnd
    self.usergroup = usergroup
    self.userType = userType
    self.page = page
    self.cou = cou

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
          self.hide = iprot.readI32();
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
          self.theme = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.qid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.uid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.ansStop = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I64:
          self.publishStart = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I64:
          self.publishEnd = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I64:
          self.ansStart = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I64:
          self.shareNum = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.I64:
          self.shareEnd = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.STRING:
          self.usergroup = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.I32:
          self.userType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 15:
        if ftype == TType.I32:
          self.page = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 16:
        if ftype == TType.I32:
          self.cou = iprot.readI32();
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
    oprot.writeStructBegin('findQuestion_args')
    if self.hide is not None:
      oprot.writeFieldBegin('hide', TType.I32, 1)
      oprot.writeI32(self.hide)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.describe is not None:
      oprot.writeFieldBegin('describe', TType.STRING, 3)
      oprot.writeString(self.describe)
      oprot.writeFieldEnd()
    if self.theme is not None:
      oprot.writeFieldBegin('theme', TType.STRING, 4)
      oprot.writeString(self.theme)
      oprot.writeFieldEnd()
    if self.qid is not None:
      oprot.writeFieldBegin('qid', TType.STRING, 5)
      oprot.writeString(self.qid)
      oprot.writeFieldEnd()
    if self.uid is not None:
      oprot.writeFieldBegin('uid', TType.STRING, 6)
      oprot.writeString(self.uid)
      oprot.writeFieldEnd()
    if self.ansStop is not None:
      oprot.writeFieldBegin('ansStop', TType.I64, 7)
      oprot.writeI64(self.ansStop)
      oprot.writeFieldEnd()
    if self.publishStart is not None:
      oprot.writeFieldBegin('publishStart', TType.I64, 8)
      oprot.writeI64(self.publishStart)
      oprot.writeFieldEnd()
    if self.publishEnd is not None:
      oprot.writeFieldBegin('publishEnd', TType.I64, 9)
      oprot.writeI64(self.publishEnd)
      oprot.writeFieldEnd()
    if self.ansStart is not None:
      oprot.writeFieldBegin('ansStart', TType.I64, 10)
      oprot.writeI64(self.ansStart)
      oprot.writeFieldEnd()
    if self.shareNum is not None:
      oprot.writeFieldBegin('shareNum', TType.I64, 11)
      oprot.writeI64(self.shareNum)
      oprot.writeFieldEnd()
    if self.shareEnd is not None:
      oprot.writeFieldBegin('shareEnd', TType.I64, 12)
      oprot.writeI64(self.shareEnd)
      oprot.writeFieldEnd()
    if self.usergroup is not None:
      oprot.writeFieldBegin('usergroup', TType.STRING, 13)
      oprot.writeString(self.usergroup)
      oprot.writeFieldEnd()
    if self.userType is not None:
      oprot.writeFieldBegin('userType', TType.I32, 14)
      oprot.writeI32(self.userType)
      oprot.writeFieldEnd()
    if self.page is not None:
      oprot.writeFieldBegin('page', TType.I32, 15)
      oprot.writeI32(self.page)
      oprot.writeFieldEnd()
    if self.cou is not None:
      oprot.writeFieldBegin('cou', TType.I32, 16)
      oprot.writeI32(self.cou)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.hide)
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.describe)
    value = (value * 31) ^ hash(self.theme)
    value = (value * 31) ^ hash(self.qid)
    value = (value * 31) ^ hash(self.uid)
    value = (value * 31) ^ hash(self.ansStop)
    value = (value * 31) ^ hash(self.publishStart)
    value = (value * 31) ^ hash(self.publishEnd)
    value = (value * 31) ^ hash(self.ansStart)
    value = (value * 31) ^ hash(self.shareNum)
    value = (value * 31) ^ hash(self.shareEnd)
    value = (value * 31) ^ hash(self.usergroup)
    value = (value * 31) ^ hash(self.userType)
    value = (value * 31) ^ hash(self.page)
    value = (value * 31) ^ hash(self.cou)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class findQuestion_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(Question, Question.thrift_spec)), None, ), # 0
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
          (_etype80, _size77) = iprot.readListBegin()
          for _i81 in xrange(_size77):
            _elem82 = Question()
            _elem82.read(iprot)
            self.success.append(_elem82)
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
    oprot.writeStructBegin('findQuestion_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter83 in self.success:
        iter83.write(oprot)
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

class addAnswer_args:
  """
  Attributes:
   - answer
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'answer', (Answer, Answer.thrift_spec), None, ), # 1
  )

  def __init__(self, answer=None,):
    self.answer = answer

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
          self.answer = Answer()
          self.answer.read(iprot)
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
    oprot.writeStructBegin('addAnswer_args')
    if self.answer is not None:
      oprot.writeFieldBegin('answer', TType.STRUCT, 1)
      self.answer.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.answer)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class addAnswer_result:
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
    oprot.writeStructBegin('addAnswer_result')
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

class editAnswer_args:
  """
  Attributes:
   - anwer
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'anwer', (Answer, Answer.thrift_spec), None, ), # 1
  )

  def __init__(self, anwer=None,):
    self.anwer = anwer

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
          self.anwer = Answer()
          self.anwer.read(iprot)
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
    oprot.writeStructBegin('editAnswer_args')
    if self.anwer is not None:
      oprot.writeFieldBegin('anwer', TType.STRUCT, 1)
      self.anwer.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.anwer)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class editAnswer_result:
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
    oprot.writeStructBegin('editAnswer_result')
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

class findAnswer_args:
  """
  Attributes:
   - qid
   - aid
   - context
   - quesType
   - fr
   - to
   - page
   - cou
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'qid', None, None, ), # 1
    (2, TType.STRING, 'aid', None, None, ), # 2
    (3, TType.STRING, 'context', None, None, ), # 3
    (4, TType.STRING, 'quesType', None, None, ), # 4
    (5, TType.I32, 'fr', None, None, ), # 5
    (6, TType.I32, 'to', None, None, ), # 6
    (7, TType.I32, 'page', None, None, ), # 7
    (8, TType.I32, 'cou', None, None, ), # 8
  )

  def __init__(self, qid=None, aid=None, context=None, quesType=None, fr=None, to=None, page=None, cou=None,):
    self.qid = qid
    self.aid = aid
    self.context = context
    self.quesType = quesType
    self.fr = fr
    self.to = to
    self.page = page
    self.cou = cou

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
          self.aid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.context = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.quesType = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.fr = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.to = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.page = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.cou = iprot.readI32();
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
    oprot.writeStructBegin('findAnswer_args')
    if self.qid is not None:
      oprot.writeFieldBegin('qid', TType.STRING, 1)
      oprot.writeString(self.qid)
      oprot.writeFieldEnd()
    if self.aid is not None:
      oprot.writeFieldBegin('aid', TType.STRING, 2)
      oprot.writeString(self.aid)
      oprot.writeFieldEnd()
    if self.context is not None:
      oprot.writeFieldBegin('context', TType.STRING, 3)
      oprot.writeString(self.context)
      oprot.writeFieldEnd()
    if self.quesType is not None:
      oprot.writeFieldBegin('quesType', TType.STRING, 4)
      oprot.writeString(self.quesType)
      oprot.writeFieldEnd()
    if self.fr is not None:
      oprot.writeFieldBegin('fr', TType.I32, 5)
      oprot.writeI32(self.fr)
      oprot.writeFieldEnd()
    if self.to is not None:
      oprot.writeFieldBegin('to', TType.I32, 6)
      oprot.writeI32(self.to)
      oprot.writeFieldEnd()
    if self.page is not None:
      oprot.writeFieldBegin('page', TType.I32, 7)
      oprot.writeI32(self.page)
      oprot.writeFieldEnd()
    if self.cou is not None:
      oprot.writeFieldBegin('cou', TType.I32, 8)
      oprot.writeI32(self.cou)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.qid)
    value = (value * 31) ^ hash(self.aid)
    value = (value * 31) ^ hash(self.context)
    value = (value * 31) ^ hash(self.quesType)
    value = (value * 31) ^ hash(self.fr)
    value = (value * 31) ^ hash(self.to)
    value = (value * 31) ^ hash(self.page)
    value = (value * 31) ^ hash(self.cou)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class findAnswer_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(Answer, Answer.thrift_spec)), None, ), # 0
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
            _elem89 = Answer()
            _elem89.read(iprot)
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
    oprot.writeStructBegin('findAnswer_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter90 in self.success:
        iter90.write(oprot)
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

class hideAnswer_args:
  """
  Attributes:
   - aid
   - hide
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'aid', None, None, ), # 1
    (2, TType.I32, 'hide', None, None, ), # 2
  )

  def __init__(self, aid=None, hide=None,):
    self.aid = aid
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
          self.aid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
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
    oprot.writeStructBegin('hideAnswer_args')
    if self.aid is not None:
      oprot.writeFieldBegin('aid', TType.STRING, 1)
      oprot.writeString(self.aid)
      oprot.writeFieldEnd()
    if self.hide is not None:
      oprot.writeFieldBegin('hide', TType.I32, 2)
      oprot.writeI32(self.hide)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.aid)
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

class hideAnswer_result:
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
    oprot.writeStructBegin('hideAnswer_result')
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

class findAnswerByID_args:
  """
  Attributes:
   - aid
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'aid', None, None, ), # 1
  )

  def __init__(self, aid=None,):
    self.aid = aid

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
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('findAnswerByID_args')
    if self.aid is not None:
      oprot.writeFieldBegin('aid', TType.STRING, 1)
      oprot.writeString(self.aid)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.aid)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class findAnswerByID_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Answer, Answer.thrift_spec), None, ), # 0
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
        if ftype == TType.STRUCT:
          self.success = Answer()
          self.success.read(iprot)
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
    oprot.writeStructBegin('findAnswerByID_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
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

class hideQuestion_args:
  """
  Attributes:
   - qid
   - hide
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'qid', None, None, ), # 1
    (2, TType.I32, 'hide', None, None, ), # 2
  )

  def __init__(self, qid=None, hide=None,):
    self.qid = qid
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
          self.qid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
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
    oprot.writeStructBegin('hideQuestion_args')
    if self.qid is not None:
      oprot.writeFieldBegin('qid', TType.STRING, 1)
      oprot.writeString(self.qid)
      oprot.writeFieldEnd()
    if self.hide is not None:
      oprot.writeFieldBegin('hide', TType.I32, 2)
      oprot.writeI32(self.hide)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.qid)
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

class hideQuestion_result:
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
    oprot.writeStructBegin('hideQuestion_result')
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

class editTheme_args:
  """
  Attributes:
   - theme
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'theme', (Theme, Theme.thrift_spec), None, ), # 1
  )

  def __init__(self, theme=None,):
    self.theme = theme

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
          self.theme = Theme()
          self.theme.read(iprot)
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
    oprot.writeStructBegin('editTheme_args')
    if self.theme is not None:
      oprot.writeFieldBegin('theme', TType.STRUCT, 1)
      self.theme.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.theme)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class editTheme_result:
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
    oprot.writeStructBegin('editTheme_result')
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

class findAnsQues_args:
  """
  Attributes:
   - utype
   - anscon
   - aid
   - ansuname
   - ansuid
   - quescon
   - qid
   - sortType
   - sorta
   - sortz
   - ugroup
   - start
   - count
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'utype', None, None, ), # 1
    (2, TType.STRING, 'anscon', None, None, ), # 2
    (3, TType.STRING, 'aid', None, None, ), # 3
    (4, TType.STRING, 'ansuname', None, None, ), # 4
    (5, TType.STRING, 'ansuid', None, None, ), # 5
    (6, TType.STRING, 'quescon', None, None, ), # 6
    (7, TType.STRING, 'qid', None, None, ), # 7
    (8, TType.I32, 'sortType', None, None, ), # 8
    (9, TType.STRING, 'sorta', None, None, ), # 9
    (10, TType.STRING, 'sortz', None, None, ), # 10
    (11, TType.LIST, 'ugroup', (TType.STRUCT,(GroupList, GroupList.thrift_spec)), None, ), # 11
    (12, TType.I32, 'start', None, None, ), # 12
    (13, TType.I32, 'count', None, None, ), # 13
  )

  def __init__(self, utype=None, anscon=None, aid=None, ansuname=None, ansuid=None, quescon=None, qid=None, sortType=None, sorta=None, sortz=None, ugroup=None, start=None, count=None,):
    self.utype = utype
    self.anscon = anscon
    self.aid = aid
    self.ansuname = ansuname
    self.ansuid = ansuid
    self.quescon = quescon
    self.qid = qid
    self.sortType = sortType
    self.sorta = sorta
    self.sortz = sortz
    self.ugroup = ugroup
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
          self.utype = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.anscon = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.aid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.ansuname = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.ansuid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.quescon = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.qid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.sortType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.sorta = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRING:
          self.sortz = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.LIST:
          self.ugroup = []
          (_etype94, _size91) = iprot.readListBegin()
          for _i95 in xrange(_size91):
            _elem96 = GroupList()
            _elem96.read(iprot)
            self.ugroup.append(_elem96)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.I32:
          self.start = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 13:
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
    oprot.writeStructBegin('findAnsQues_args')
    if self.utype is not None:
      oprot.writeFieldBegin('utype', TType.I32, 1)
      oprot.writeI32(self.utype)
      oprot.writeFieldEnd()
    if self.anscon is not None:
      oprot.writeFieldBegin('anscon', TType.STRING, 2)
      oprot.writeString(self.anscon)
      oprot.writeFieldEnd()
    if self.aid is not None:
      oprot.writeFieldBegin('aid', TType.STRING, 3)
      oprot.writeString(self.aid)
      oprot.writeFieldEnd()
    if self.ansuname is not None:
      oprot.writeFieldBegin('ansuname', TType.STRING, 4)
      oprot.writeString(self.ansuname)
      oprot.writeFieldEnd()
    if self.ansuid is not None:
      oprot.writeFieldBegin('ansuid', TType.STRING, 5)
      oprot.writeString(self.ansuid)
      oprot.writeFieldEnd()
    if self.quescon is not None:
      oprot.writeFieldBegin('quescon', TType.STRING, 6)
      oprot.writeString(self.quescon)
      oprot.writeFieldEnd()
    if self.qid is not None:
      oprot.writeFieldBegin('qid', TType.STRING, 7)
      oprot.writeString(self.qid)
      oprot.writeFieldEnd()
    if self.sortType is not None:
      oprot.writeFieldBegin('sortType', TType.I32, 8)
      oprot.writeI32(self.sortType)
      oprot.writeFieldEnd()
    if self.sorta is not None:
      oprot.writeFieldBegin('sorta', TType.STRING, 9)
      oprot.writeString(self.sorta)
      oprot.writeFieldEnd()
    if self.sortz is not None:
      oprot.writeFieldBegin('sortz', TType.STRING, 10)
      oprot.writeString(self.sortz)
      oprot.writeFieldEnd()
    if self.ugroup is not None:
      oprot.writeFieldBegin('ugroup', TType.LIST, 11)
      oprot.writeListBegin(TType.STRUCT, len(self.ugroup))
      for iter97 in self.ugroup:
        iter97.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.start is not None:
      oprot.writeFieldBegin('start', TType.I32, 12)
      oprot.writeI32(self.start)
      oprot.writeFieldEnd()
    if self.count is not None:
      oprot.writeFieldBegin('count', TType.I32, 13)
      oprot.writeI32(self.count)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.utype)
    value = (value * 31) ^ hash(self.anscon)
    value = (value * 31) ^ hash(self.aid)
    value = (value * 31) ^ hash(self.ansuname)
    value = (value * 31) ^ hash(self.ansuid)
    value = (value * 31) ^ hash(self.quescon)
    value = (value * 31) ^ hash(self.qid)
    value = (value * 31) ^ hash(self.sortType)
    value = (value * 31) ^ hash(self.sorta)
    value = (value * 31) ^ hash(self.sortz)
    value = (value * 31) ^ hash(self.ugroup)
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

class findAnsQues_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(Question, Question.thrift_spec)), None, ), # 0
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
          (_etype101, _size98) = iprot.readListBegin()
          for _i102 in xrange(_size98):
            _elem103 = Question()
            _elem103.read(iprot)
            self.success.append(_elem103)
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
    oprot.writeStructBegin('findAnsQues_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter104 in self.success:
        iter104.write(oprot)
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
