#coding:utf-8
from django.shortcuts import render_to_response
from thrift_other import th_findAbout, th_findService, th_updateAbout, th_udpateService
from utils.dictutils import safeObtainDict
from django.http import HttpResponse
import json

##### 跳转页面 start #####
#关于我们
def aboutus(req):
    #获取内容
    #web
    webData = th_findAbout(1)
    #app
    appData = th_findAbout(0)
    print webData, appData
    return render_to_response('aboutus.html', {'webData': webData, 'appData': appData})

def service(req):
    #获取内容
    serviceData = th_findService()
    return render_to_response('service.html', {'serviceData': serviceData})

##### 跳转页面 end #####

##### 功能操作 start #####
def saveAboutus(req):
    webData = safeObtainDict(req.POST, 'webData')
    appData = safeObtainDict(req.POST, 'appData')
    if webData is not None:
        webData = webData.encode('utf-8')
    if appData is not None:
        appData = appData.encode('utf-8')

    if th_updateAbout(webData, appData):
        result = {'message': '保存成功', 'status': 200}
    else:
        result = {'message': '保存失败', 'status': 100}
    #获取内容
    return HttpResponse(json.dumps(result), content_type="application/json")

def saveService(req):
    service = safeObtainDict(req.POST, 'service')
    if service is not None:
        service = service.encode('utf-8')
    if th_udpateService(service):
        result = {'message': '保存成功', 'status': 200}
    else:
        result = {'message': '保存失败', 'status': 100}
    #获取内容
    return HttpResponse(json.dumps(result), content_type="application/json")
##### 功能操作 end #####