#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json

#真实用户管理
def realuserIndex(req):
    #获取真实用户分组
    rGroup = showRealUserGroup()
    return render_to_response('realuser.html', {'rGroup': rGroup})

#获取虚拟用户分组
def showRealUserGroup():
    #TODO 假数据等待接口
    data = [{'text' : '前端', 'value' : '1'},
                      {'text' : '后台', 'value' : '2'},
                               {'text' : '安卓', 'value' : '5'},
                               {'text' : 'IOS', 'value' : '3'},
                               {'text' : '啥都会', 'value' : '4'} ]
    return data

#查询虚拟用户
def searchRealUser(req):
    response_data = {"colmodel":[],"rows":[{"address":"CZ88.NET","city":"啊啊啊啊啊啊啊啊保留地址","end":"0.255.255.255","id":1,"start":"0.0.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.0.0.255","id":2,"start":"1.0.0.0"},{"address":"电信","city":"福建省","end":"1.0.3.255","id":3,"start":"1.0.1.0"},{"address":"CZ88.NET","city":"ddd","end":"1.0.7.255","id":4,"start":"1.0.4.0"},{"address":"CZ88.NET","city":"泰国","end":"1.0.255.255","id":5,"start":"1.0.128.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.31.255","id":6,"start":"1.0.16.0"},{"address":"电信","city":"广东省","end":"1.0.63.255","id":7,"start":"1.0.32.0"},{"address":"CZ88.NET","city":"日本","end":"1.0.127.255","id":8,"start":"1.0.64.0"},{"address":"电信","city":"广东省","end":"1.0.15.255","id":9,"start":"1.0.8.0"},{"address":"电信","city":"福建省","end":"1.1.0.255","id":10,"start":"1.1.0.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.1.1.255","id":11,"start":"1.1.1.0"},{"address":"电信","city":"福建省","end":"1.1.7.255","id":12,"start":"1.1.2.0"},{"address":"电信","city":"广东省","end":"1.1.63.255","id":13,"start":"1.1.8.0"},{"address":"CZ88.NET","city":"日本","end":"1.1.127.255","id":14,"start":"1.1.64.0"},{"address":"CZ88.NET","city":"泰国","end":"1.1.255.255","id":15,"start":"1.1.128.0"},{"address":"电信","city":"福建省","end":"1.2.1.255","id":16,"start":"1.2.0.0"},{"address":"北龙中网科技有限公司","city":"北京市","end":"1.2.2.255","id":17,"start":"1.2.2.0"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.3","id":18,"start":"1.2.3.0"},{"address":"CZ88.NET","city":"印度尼西亚","end":"1.2.3.4","id":19,"start":"1.2.3.4"},{"address":"CZ88.NET","city":"澳大利亚","end":"1.2.3.255","id":20,"start":"1.2.3.5"}],"total":126}
    return HttpResponse(json.dumps(response_data), content_type="application/json")