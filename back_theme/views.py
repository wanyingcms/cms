#coding:utf-8
from django.shortcuts import render_to_response
from back_user.models import BackuserMenuuser
import json
import xlwt

#主题管理首页
def themeindex(req):
    return render_to_response('theme.html')

#查询主题列表
def searchTheme(req):

    theme = req.GET['theme']
    if theme == 'init':
        #初始化页面时 没有搜索条件参数
        #TODO 假数据等待接口
        response_data = {"colmodel":[],"rows":[{"address":"CZ88.NET","city":"啊啊啊啊啊啊啊啊保留地址","end":"0.255.255.255","id":1,"start":"0.0.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.0.0.255","id":2,"start":"1.0.0.0"},{"address":"电信","city":"福建省","end":"1.0.3.255","id":3,"start":"1.0.1.0"},{"address":"CZ88.NET","city":"ddd","end":"1.0.7.255","id":4,"start":"1.0.4.0"},{"address":"CZ88.NET","city":"泰国","end":"1.0.255.255","id":5,"start":"1.0.128.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.31.255","id":6,"start":"1.0.16.0"},{"address":"电信","city":"广东省","end":"1.0.63.255","id":7,"start":"1.0.32.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.127.255","id":8,"start":"1.0.64.0"},{"address":"电信","city":"广东省","end":"1.0.15.255","id":9,"start":"1.0.8.0"},{"address":"电信","city":"福建省","end":"1.1.0.255","id":10,"start":"1.1.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.1.1.255","id":11,"start":"1.1.1.0"},{"address":"电信","city":"福建省","end":"1.1.7.255","id":12,"start":"1.1.2.0"},{"address":"电信","city":"广东省","end":"1.1.63.255","id":13,"start":"1.1.8.0"},{"address":"CZ88.NET","city":"日本","end":"1.1.127.255","id":14,"start":"1.1.64.0"},{"address":"CZ88.NET","city":"泰国","end":"1.1.255.255","id":15,"start":"1.1.128.0"},{"address":"电信","city":"福建省","end":"1.2.1.255","id":16,"start":"1.2.0.0"},{"address":"北龙中网科技有限公司","city":"北京市","end":"1.2.2.255","id":17,"start":"1.2.2.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.3","id":18,"start":"1.2.3.0"},{"address":"CZ88.NET","city":"印度尼西亚","end":"1.2.3.4","id":19,"start":"1.2.3.4"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.255","id":20,"start":"1.2.3.5"}],"total":126}
    else:
        #搜索
        showThemeType = req.GET['showThemeType']
        showBackUser = req.GET['showBackUser']
        createUser = req.GET['createUser']
        #TODO 假数据等待接口
        response_data = {"colmodel":[],"rows":[{"address":"CZ88.NET","city":"ffffff保留地址","end":"0.255.255.255","id":1,"start":"0.0.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.0.0.255","id":2,"start":"1.0.0.0"},{"address":"电信","city":"福建省","end":"1.0.3.255","id":3,"start":"1.0.1.0"},{"address":"CZ88.NET","city":"ddd","end":"1.0.7.255","id":4,"start":"1.0.4.0"},{"address":"CZ88.NET","city":"泰国","end":"1.0.255.255","id":5,"start":"1.0.128.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.31.255","id":6,"start":"1.0.16.0"},{"address":"电信","city":"广东省","end":"1.0.63.255","id":7,"start":"1.0.32.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.127.255","id":8,"start":"1.0.64.0"},{"address":"电信","city":"广东省","end":"1.0.15.255","id":9,"start":"1.0.8.0"},{"address":"电信","city":"福建省","end":"1.1.0.255","id":10,"start":"1.1.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.1.1.255","id":11,"start":"1.1.1.0"},{"address":"电信","city":"福建省","end":"1.1.7.255","id":12,"start":"1.1.2.0"},{"address":"电信","city":"广东省","end":"1.1.63.255","id":13,"start":"1.1.8.0"},{"address":"CZ88.NET","city":"日本","end":"1.1.127.255","id":14,"start":"1.1.64.0"},{"address":"CZ88.NET","city":"泰国","end":"1.1.255.255","id":15,"start":"1.1.128.0"},{"address":"电信","city":"福建省","end":"1.2.1.255","id":16,"start":"1.2.0.0"},{"address":"北龙中网科技有限公司","city":"北京市","end":"1.2.2.255","id":17,"start":"1.2.2.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.3","id":18,"start":"1.2.3.0"},{"address":"CZ88.NET","city":"印度尼西亚","end":"1.2.3.4","id":19,"start":"1.2.3.4"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.255","id":20,"start":"1.2.3.5"}],"total":126}

    return HttpResponse(json.dumps(response_data), content_type="application/json")

#获取分类列表
def showThemeType(req):
    #TODO 假数据等待接口
    response_data = [ {'text' : '技术类', 'value' : '1'},
                               {'text' : '生活类', 'value' : '2'},
                               {'text' : '妹子类', 'value' : '3'},
                               {'text' : '吃喝玩乐类', 'value' : '4'} ]
    return HttpResponse(json.dumps(response_data), content_type="application/json")

#获取运维人员列表
def showBackUser(req):
    #TODO 假数据 暂无真数据
    #users = BackuserMenuuser.objcets.all()
    response_data = [ {'text' : '运维1号', 'value' : '1'},
                      {'text' : '运维2号', 'value' : '5'},
                               {'text' : '运维3号', 'value' : '2'},
                               {'text' : '运维4号', 'value' : '3'},
                               {'text' : '运维5号', 'value' : '4'} ]

    return HttpResponse(json.dumps(response_data), content_type="application/json")

#隐藏主题
def hideTheme(req):
    tid = req.GET['tid']
    print tid
    #TODO 等待处理隐藏主题操作接口
    response_data = {'message': 'ok'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

#导出excel
def exportExcel(req):
    path = '/home/qiuxy/PycharmProjects/cms-master/temp/001.xls'
    createExcel(path)
    return HttpResponse(path, content_type="application/json")

def createExcel(path):
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet(u'sheet1')
    createXLSTitle(sheet)
    for i in range(20):
        createXLS(sheet, i)
    wbk.save(path)

def createXLSTitle(sheet):
    #TODO 假数据
    sheet.write(0,0,u'ID')
    sheet.write(0,1,u'主题名称')
    sheet.write(0,2,u'创建者')

def createXLS(sheet,index):
    #TODO 假数据
    row = index+1
    sheet.write(row,0,index)
    sheet.write(row,1,u'测试')
    sheet.write(row,2,u'运维001')
