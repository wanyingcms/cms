#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from back_theme.views import showBackUser, showThemeType, showVirtualUserGroup
from thrift_question import th_findQuestion
from utils.dictutils import safeObtainDict, safeObtainDictToTime, safeObtainDictToInt
import json
import time
import xlwt

##### 跳转页面 start #####
#查询题目列表
def questionIndex(req):
    #获取主题分类
    themeType = showThemeType()
    #获取主题列表
    theme = showTheme('init', req)
    #获取运维人员
    backUser = showBackUser()
    return render_to_response('question.html', {'themeType': themeType, 'backUser': backUser, 'theme': theme, })

#跳转添加页
def addQuestionPage(req):
    #虚拟用户组
    vUserGroup = showVirtualUserGroup()
    #获取主题分类

    return render_to_response('addQuestion.html', {'vUserGroup': vUserGroup, })

#跳转编辑页
def editQuestionPage(req):
    #虚拟用户组
    vUserGroup = showVirtualUserGroup()
    #获取主题列表
    theme = showTheme('init', req)
    qid = req.GET['qid']
    #根据ID查问题
    #TODO 等待接口
    question = {'ID': '00001','title': '测试','content':'测试内容','huida':1,'jubao':3,'fenxiang':5}
    return render_to_response('addQuestion.html', {'vUserGroup': vUserGroup, 'theme': theme, 'question': question})

##### 跳转页面 end #####

##### 功能操作 start #####
#保存题目
def saveQuestion(req):
    pass

#隐藏题目
def hideQuestion(req):
    pass

#查询题目列表返回表格数据
def searchToTableData(req):
    result = search(req)
    #拼数据
    rows = []
    for question in result:
        rows.append({"ansNum": question.ansNum, "hide": question.hide, "name": question.name, "qid": question.qid,
                         "createDate": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(question.createDate/1000)), "describe": question.describe, "share": question.share,
                         "theme": question.theme, "report": question.report, "hold": question.hold, "imgUrls": question.imgUrls,
                         "uid": question.uid})
    #TODO 分页总数等接口
    response_data = {'total': 25, 'rows': rows, }

    return HttpResponse(json.dumps(response_data), content_type="application/json")

#查询题目列表返回json数据
def searchToJson(req):
    result = search(req)
    return HttpResponse(json.dumps(result), content_type="application/json")

#查询数据
def search(req):
    #分页参数
    startStr = safeObtainDictToInt(req.GET, 'start')
    limitStr = safeObtainDictToInt(req.GET, 'limit')
    #当前页数
    nowPage = startStr/limitStr + 1
    print startStr,limitStr,nowPage
    #查询参数
    hide = safeObtainDictToInt(req.GET, 'hide')
    name = safeObtainDict(req.GET, 'name')
    describe = safeObtainDict(req.GET, 'describe')
    theme = safeObtainDict(req.GET, 'theme')
    qid = safeObtainDict(req.GET, 'qid')
    uid = safeObtainDict(req.GET, 'uid')
    ansStop = safeObtainDictToInt(req.GET, 'ansStop')
    publishStart = safeObtainDict(req.GET, 'publishStart')
    publishEnd = safeObtainDict(req.GET, 'publishEnd')
    ansStart = safeObtainDictToInt(req.GET, 'ansStart')
    shareEnd = safeObtainDictToInt(req.GET, 'shareEnd')
    shareNum = safeObtainDictToInt(req.GET, 'shareNum')
    usergroup = safeObtainDict(req.GET, 'usergroup')
    userType = safeObtainDictToInt(req.GET, 'userType')

    if name is not None:
        name = name.encode('utf-8')
    if describe is not None:
        describe = describe.encode('utf-8')
    if qid is not None:
        qid = qid.encode('utf-8')
    if uid is not None:
        uid = uid.encode('utf-8')

    #查询
    result = th_findQuestion(page=nowPage, cou=limitStr, hide=hide, name=name,
        describe=describe, theme=theme, qid=qid, uid=uid, ansStop=ansStop, publishStart=publishStart,
        publishEnd=publishEnd, ansStart=ansStart, shareEnd=shareEnd, shareNum=shareNum, usergroup=usergroup,
        userType=userType)

    return result

##### 功能操作 end #####


























#获取主题
def showTheme(method, req):
    if method == 'init':
        #初始化页面时读取所有主题
        #TODO 等待接口
        data = [{'text' : '前端', 'value' : '1'},
                      {'text' : '后台', 'value' : '2'},
                               {'text' : '安卓', 'value' : '5'},
                               {'text' : 'IOS', 'value' : '3'},
                               {'text' : '啥都会', 'value' : '4'} ]
    else:
        #根据选择到主题类型获取主题
        #TODO 等待接口
        typeId = req.GET['typeId']

        if typeId == '1' :
            data = [{'text' : '前端1号', 'value' : '1'},
                      {'text' : '前端2号', 'value' : '3'},
                               {'text' : '前端3号', 'value' : '2'},]
        elif typeId == '2' :
            data = [{'text' : '后台1号', 'value' : '4'},
                          {'text' : '后台2号', 'value' : '5'},
                                   {'text' : '后台3号', 'value' : '6'},]
        else:
            data = [{'text' : '其它1号', 'value' : '7'},
                          {'text' : '其它2号', 'value' : '8'},
                                   {'text' : '其它3号', 'value' : '9'},]
    return data

