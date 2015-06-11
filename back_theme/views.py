#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from back_virtualuser.views import showVirtualUserGroup, showVirtualUser
import json
import xlwt

from yythrift.ttypes import GroupList
from thrift_theme import th_editTheme, th_addTheme, th_findTheme, th_findThemeClass, th_addThemeClass

##### 跳转页面 start #####
#主题管理首页
def themeIndex(req):
    #获取主题分类
    themeType = showThemeType()
    #获取运维人员列表
    backUser = showBackUser()
    return render_to_response('theme.html', {'themeType': themeType, 'backUser': backUser, })

#跳转添加主题页面
def addThemePage(req):
    #获取主题分类
    themeType = showThemeType()
    #TODO 差个获取当前用户权限 读虚拟用户分组
    #获取虚拟用户分组
    vUserGroup = showVirtualUserGroup()
    #获取全部虚拟用户
    vUser = showVirtualUser(req, all=True)
    return render_to_response('addTheme.html', {'themeType': themeType, 'vUserGroup': vUserGroup, 'vUser': vUser})


#跳转编辑主题页面
def editThemePage(req):
    #获取主题分类
    themeType = showThemeType()

    #获取要修改的主题 没有接口
    themeId = req.GET['tid']
    #TODO 没有获取主题接口
    tType = '4'
    vUserID = '001'
    vUserName = '前端001'
    tTitle = '测试标题'
    tContent = '测试一下啊啊啊啊啊'
    tImg = ''
    questions =15
    answers = 18

    return render_to_response('editTheme.html', {'themeId': themeId, 'themeType': themeType, 'tType': tType, 'vUserID': vUserID, 'vUserName': vUserName,
                                                 'tTitle': tTitle, 'tContent': tContent, 'tImg': tImg,
                                                 'questions': questions, 'answers': answers, })

#初始化分类弹窗
def initThemeType(req):
    response_data = th_findThemeClass()
    row = []
    for group in response_data:
        row.append({'childNumber': group.childNumber, 'glid': group.glid, 'gname': group.gname})
    return HttpResponse(json.dumps(row), content_type="application/json")

##### 跳转页面 end #####

##### 功能操作 start #####

#保存主题分类
def saveThemeType(req):
    row = req.POST['rowNum']
    list = []
    for i in range(int(row)+1):
        classId = req.POST['classId'+str(i)]
        className = req.POST['className'+str(i)]
        if className is None or className == '':
            continue
        else:
            className = className.encode("utf-8")
        print className
        print '======================'
        if(classId == '0'):
            #增加分类
            themeClass = GroupList(gname=className, gtype=3, childNumber=0)
            list.append(themeClass)
        else:
            #修改分类
            themeClass = GroupList(glid=classId, gname=className, gtype=3)
            list.append(themeClass)

    if th_addThemeClass(list):
        result = {'message': '保存成功', 'status': 200}
    else:
        result = {'message': '保存失败', 'status': 100}

    return HttpResponse(json.dumps(result), content_type="application/json")


#查询主题列表
def searchTheme(req):

    #分页参数
    startStr = req.GET['start']
    limitStr = req.GET['limit']
    #当前页数
    nowPage = int(startStr)/int(limitStr) + 1

    theme = req.GET['theme']
    if theme == 'init':
        #初始化页面时 没有搜索条件参数
        #print '=============='
        #test111 = th_findTheme(className='', name='', uid='', page=nowPage, cou=limitStr)
        #print test111
        #print '=============='
        response_data = {"colmodel":[],"rows":[{"address":"CZ88.NET","city":"啊啊啊啊啊啊啊啊保留地址","end":"0.255.255.255","id":1,"start":"0.0.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.0.0.255","id":2,"start":"1.0.0.0"},{"address":"电信","city":"福建省","end":"1.0.3.255","id":3,"start":"1.0.1.0"},{"address":"CZ88.NET","city":"ddd","end":"1.0.7.255","id":4,"start":"1.0.4.0"},{"address":"CZ88.NET","city":"泰国","end":"1.0.255.255","id":5,"start":"1.0.128.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.31.255","id":6,"start":"1.0.16.0"},{"address":"电信","city":"广东省","end":"1.0.63.255","id":7,"start":"1.0.32.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.127.255","id":8,"start":"1.0.64.0"},{"address":"电信","city":"广东省","end":"1.0.15.255","id":9,"start":"1.0.8.0"},{"address":"电信","city":"福建省","end":"1.1.0.255","id":10,"start":"1.1.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.1.1.255","id":11,"start":"1.1.1.0"},{"address":"电信","city":"福建省","end":"1.1.7.255","id":12,"start":"1.1.2.0"},{"address":"电信","city":"广东省","end":"1.1.63.255","id":13,"start":"1.1.8.0"},{"address":"CZ88.NET","city":"日本","end":"1.1.127.255","id":14,"start":"1.1.64.0"},{"address":"CZ88.NET","city":"泰国","end":"1.1.255.255","id":15,"start":"1.1.128.0"},{"address":"电信","city":"福建省","end":"1.2.1.255","id":16,"start":"1.2.0.0"},{"address":"北龙中网科技有限公司","city":"北京市","end":"1.2.2.255","id":17,"start":"1.2.2.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.3","id":18,"start":"1.2.3.0"},{"address":"CZ88.NET","city":"印度尼西亚","end":"1.2.3.4","id":19,"start":"1.2.3.4"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.255","id":20,"start":"1.2.3.5"}],"total":126}
    else:
        #搜索
        showThemeType = req.GET['showThemeType']
        showBackUser = req.GET['showBackUser']
        createUser = req.GET['createUser']

        #test222 = th_findTheme(className=showThemeType, name='', uid='', page=nowPage, cou=limitStr)
        #print test222

        #TODO 假数据等待接口
        response_data = {"colmodel":[],"rows":[{"address":"CZ88.NET","city":"ffffff保留地址","end":"0.255.255.255","id":1,"start":"0.0.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.0.0.255","id":2,"start":"1.0.0.0"},{"address":"电信","city":"福建省","end":"1.0.3.255","id":3,"start":"1.0.1.0"},{"address":"CZ88.NET","city":"ddd","end":"1.0.7.255","id":4,"start":"1.0.4.0"},{"address":"CZ88.NET","city":"泰国","end":"1.0.255.255","id":5,"start":"1.0.128.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.31.255","id":6,"start":"1.0.16.0"},{"address":"电信","city":"广东省","end":"1.0.63.255","id":7,"start":"1.0.32.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.127.255","id":8,"start":"1.0.64.0"},{"address":"电信","city":"广东省","end":"1.0.15.255","id":9,"start":"1.0.8.0"},{"address":"电信","city":"福建省","end":"1.1.0.255","id":10,"start":"1.1.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.1.1.255","id":11,"start":"1.1.1.0"},{"address":"电信","city":"福建省","end":"1.1.7.255","id":12,"start":"1.1.2.0"},{"address":"电信","city":"广东省","end":"1.1.63.255","id":13,"start":"1.1.8.0"},{"address":"CZ88.NET","city":"日本","end":"1.1.127.255","id":14,"start":"1.1.64.0"},{"address":"CZ88.NET","city":"泰国","end":"1.1.255.255","id":15,"start":"1.1.128.0"},{"address":"电信","city":"福建省","end":"1.2.1.255","id":16,"start":"1.2.0.0"},{"address":"北龙中网科技有限公司","city":"北京市","end":"1.2.2.255","id":17,"start":"1.2.2.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.3","id":18,"start":"1.2.3.0"},{"address":"CZ88.NET","city":"印度尼西亚","end":"1.2.3.4","id":19,"start":"1.2.3.4"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.255","id":20,"start":"1.2.3.5"}],"total":126}

    return HttpResponse(json.dumps(response_data), content_type="application/json")

#隐藏主题
def hideTheme(req):
    tid = req.GET['tid']
    #TODO 等待处理隐藏主题操作接口
    response_data = {'message': 'ok'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

#保存添加/编辑主题
def saveTheme(req):

    #上传图片
    uploadFile = req.FILES['Filedata']
    destination = open('/home/qiuxy/aa.jpg', 'wb+')
    for chunk in uploadFile.chunks():
        destination.write(chunk)
    destination.close()

    themeId = req.POST['themeId']
    className = req.POST['className']
    themeTitle = req.POST['themeTitle']

    themeContent = req.POST['themeContent']
    if themeId == '0':
        #保存
        #vUserGroup = req.POST['vUserGroup']
        vUser = req.POST['vUser']

        if th_addTheme(name=themeTitle.encode('utf-8'), describe=themeContent,
                      imgUrl=str(uploadFile), uid=vUser, status=1, groupid=className):
           result = {'message': '保存成功', 'status': 200}
        else:
           result = {'message': '保存失败', 'status': 100}

    else:
        #编辑

        # TODO 暂无editTheme这个接口 等待服务端添加
        if th_editTheme(tid=themeId, Idname=themeTitle.encode('utf-8'), describe=themeContent,
                      imgUrl=str(uploadFile), status=1, groupid=className):
           result = {'message': '保存成功', 'status': 200}
        else:
           result = {'message': '保存失败', 'status': 100}

    return HttpResponse(json.dumps(result), content_type="application/json")


#获取分类列表
def showThemeType():
    #TODO 假数据等待接口
    data = [{'text' : '技术类', 'value' : '1'},
                               {'text' : '生活类', 'value' : '2'},
                               {'text' : '妹子类', 'value' : '3'},
                               {'text' : '吃喝玩乐类', 'value' : '4'} ]
    return data

#获取运维人员列表
def showBackUser():
    #TODO 假数据 暂无真数据
    #users = BackuserMenuuser.objcets.all()
    data = [{'text' : '运维1号', 'value' : '1'},
                      {'text' : '运维2号', 'value' : '5'},
                               {'text' : '运维3号', 'value' : '2'},
                               {'text' : '运维4号', 'value' : '3'},
                               {'text' : '运维5号', 'value' : '4'} ]

    return data

##### 功能操作 end #####

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
