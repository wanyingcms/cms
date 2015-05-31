#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from back_theme.views import showBackUser, showThemeType, showVirtualUserGroup
import json
import xlwt

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
    #获取主题列表
    theme = showTheme('init', req)
    return render_to_response('addQuestion.html', {'vUserGroup': vUserGroup, 'theme': theme, })

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

#保存题目
def saveQuestion(req):
    pass

#隐藏题目
def hideQuestion(req):
    pass

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

#查询题目列表
def searchQuestion(req):

    question = req.GET['question']
    if question == 'init':
        #初始化页面时 没有搜索条件参数
        #TODO 假数据等待接口
        response_data = {"colmodel":[],"rows":[{"address":"CZ88.NET","city":"啊啊啊啊啊啊啊啊保留地址","end":"0.255.255.255","id":1,"start":"0.0.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.0.0.255","id":2,"start":"1.0.0.0"},{"address":"电信","city":"福建省","end":"1.0.3.255","id":3,"start":"1.0.1.0"},{"address":"CZ88.NET","city":"ddd","end":"1.0.7.255","id":4,"start":"1.0.4.0"},{"address":"CZ88.NET","city":"泰国","end":"1.0.255.255","id":5,"start":"1.0.128.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.31.255","id":6,"start":"1.0.16.0"},{"address":"电信","city":"广东省","end":"1.0.63.255","id":7,"start":"1.0.32.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.127.255","id":8,"start":"1.0.64.0"},{"address":"电信","city":"广东省","end":"1.0.15.255","id":9,"start":"1.0.8.0"},{"address":"电信","city":"福建省","end":"1.1.0.255","id":10,"start":"1.1.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.1.1.255","id":11,"start":"1.1.1.0"},{"address":"电信","city":"福建省","end":"1.1.7.255","id":12,"start":"1.1.2.0"},{"address":"电信","city":"广东省","end":"1.1.63.255","id":13,"start":"1.1.8.0"},{"address":"CZ88.NET","city":"日本","end":"1.1.127.255","id":14,"start":"1.1.64.0"},{"address":"CZ88.NET","city":"泰国","end":"1.1.255.255","id":15,"start":"1.1.128.0"},{"address":"电信","city":"福建省","end":"1.2.1.255","id":16,"start":"1.2.0.0"},{"address":"北龙中网科技有限公司","city":"北京市","end":"1.2.2.255","id":17,"start":"1.2.2.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.3","id":18,"start":"1.2.3.0"},{"address":"CZ88.NET","city":"印度尼西亚","end":"1.2.3.4","id":19,"start":"1.2.3.4"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.255","id":20,"start":"1.2.3.5"}],"total":126}
    else:
        #搜索
        showThemeType = req.GET['showThemeType']
        showBackUser = req.GET['showBackUser']
        createUser = req.GET['createUser']
        print showThemeType,showBackUser,createUser
        #TODO 假数据等待接口
        response_data = {"colmodel":[],"rows":[{"address":"CZ88.NET","city":"ffffff保留地址","end":"0.255.255.255","id":1,"start":"0.0.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.0.0.255","id":2,"start":"1.0.0.0"},{"address":"电信","city":"福建省","end":"1.0.3.255","id":3,"start":"1.0.1.0"},{"address":"CZ88.NET","city":"ddd","end":"1.0.7.255","id":4,"start":"1.0.4.0"},{"address":"CZ88.NET","city":"泰国","end":"1.0.255.255","id":5,"start":"1.0.128.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.31.255","id":6,"start":"1.0.16.0"},{"address":"电信","city":"广东省","end":"1.0.63.255","id":7,"start":"1.0.32.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.127.255","id":8,"start":"1.0.64.0"},{"address":"电信","city":"广东省","end":"1.0.15.255","id":9,"start":"1.0.8.0"},{"address":"电信","city":"福建省","end":"1.1.0.255","id":10,"start":"1.1.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.1.1.255","id":11,"start":"1.1.1.0"},{"address":"电信","city":"福建省","end":"1.1.7.255","id":12,"start":"1.1.2.0"},{"address":"电信","city":"广东省","end":"1.1.63.255","id":13,"start":"1.1.8.0"},{"address":"CZ88.NET","city":"日本","end":"1.1.127.255","id":14,"start":"1.1.64.0"},{"address":"CZ88.NET","city":"泰国","end":"1.1.255.255","id":15,"start":"1.1.128.0"},{"address":"电信","city":"福建省","end":"1.2.1.255","id":16,"start":"1.2.0.0"},{"address":"北龙中网科技有限公司","city":"北京市","end":"1.2.2.255","id":17,"start":"1.2.2.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.3","id":18,"start":"1.2.3.0"},{"address":"CZ88.NET","city":"印度尼西亚","end":"1.2.3.4","id":19,"start":"1.2.3.4"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.255","id":20,"start":"1.2.3.5"}],"total":126}

    return HttpResponse(json.dumps(response_data), content_type="application/json")