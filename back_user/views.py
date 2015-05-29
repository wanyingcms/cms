#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django import forms
from utils.dbutils import menuList
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")
from back_user.models import *
from utils.redisUtil import *
import json
import uuid
import datetime



# Create your views here.


#定义登录表单模型
class LoginForm(forms.Form):
    username=forms.CharField(label='用户名：',max_length=100)
    password=forms.CharField(label='密码：',widget=forms.PasswordInput)

def login(req):

    return render_to_response("login.html")

#登录方法
def dologin(req):
    if req.method == 'POST':
        uf = LoginForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #查询用户
            user = BackuserUserinfo.objects.filter(username__exact=username,userpwd__exact=password)

            if user:
                #登录信息存入redis
                cookid = req.COOKIES
                response = HttpResponseRedirect("/back_user/cmsindex/")
                response.set_cookie("username",username)

                redisSet(username,username,30*60)
                return response
            else:
                return HttpResponseRedirect('/back_user/login')
    else:
        uf = LoginForm()
    return render_to_response('login.html',{'uf',uf})


#退出 ： 登录存redis  key username : value cookid
# 首先根据cookid 查出 cook中存储的用户名， 用用户名查处登录埘的key
# 然后比较这连个key是否一致，如果一致则说明是同样个人，可以删除redis中登录信息
def logout(req):
    cookid = req.COOKIES['username']
    username = redisGet(cookid)
    loginkey = redisGet(username)
    if loginkey:
        redisDelKey(username)

    return HttpResponseRedirect('/back_user/login')

#密码修改窗口
def toEditPassword(req):

    return render_to_response('main/modifyPassword.html')



#定义登录表单模型
class ChangePWDForm(forms.Form):
    oldPassword=forms.CharField(label='旧密码：',widget=forms.PasswordInput)
    newPassword=forms.CharField(label='新密码：',widget=forms.PasswordInput)
    newPassword2=forms.CharField(label='新密码确认：',widget=forms.PasswordInput)

#修改密码
def editPassword(req):
    cf = ChangePWDForm(req.POST)
    if cf.is_valid():
        oldPassword = cf.cleaned_data['oldPassword']
        newPassword = cf.cleaned_data['newPassword']
        newPassword2 = cf.cleaned_data['newPassword2']
        username = req.COOKIES["username"]
        user = BackuserUserinfo.objects.get(username__exact=username)
        if user and oldPassword == user.userpwd:
            user.userpwd=newPassword
            user.save()

            #修改完成之后，删除用户登录状态
            cookid = req.COOKIES['username']
            username = redisGet(cookid)
            loginkey = redisGet(username)
            if loginkey:
                redisDelKey(username)
                #return render_to_response('main/modifyPassword.html',{"errorMsg":"修改成功！","result":"1"})
                return HttpResponse(json.dumps({"result":"1","errorMsg":"修改成功！"}))
        else:
            return render_to_response('main/modifyPassword.html',{"errorMsg":"密码不正确！"})


def cmsindex(req):
    #response = HttpResponse()
    #response.set_cookie("username","123123")
    #return response('main/main.html')
    return render_to_response('main/main.html')




#'''def publisherdate(req):
#    data = gridDataModel()
#    data.setTotal(10)
#    #print getAllPublisher()
#    data.setRows(getAllPublisher())
#    return HttpResponse(json.dumps(data.__dict__))'''


def indexleft(req):

    menus = menuList()
    print menus
    for menuname,cmenu in menus.items():
        print '=====',menuname, cmenu
    return render_to_response('main/left.html',{'indexdata':menus})

def allusediv(req):
    return render_to_response('main/allUseDiv.html')
def footer(req):
    return render_to_response('main/footer.html')
def top(req):
    return render_to_response('main/top.html')
def welcome(req):
    return render_to_response('main/welcome.html')





#后台用户管理
def showUsers(request):
    return render(request, 'management/showUsers.html',)

#获取后台用户
def showUsersToJson(request):

    startStr = request.GET['start']
    limitStr = request.GET['limit']
    show = request.GET['show']
    print 'sss' in request.GET
    if show == 'init':
        total = BackuserUserinfo.objects.count()
        userdata = BackuserUserinfo.objects.all()[int(startStr):int(limitStr)+int(startStr)]
        pass
    else:
        pass


    rows = []
    for user in userdata:
        rows.append({"id": user.id, "username": user.username, "comments": user.comments, "logins": user.logins,
                     "answers": user.answers, "questions": user.questions, "lastlogintime": user.lastlogintime.strftime('%Y-%m-%d %H:%M:%S'),
                     "createtime": user.createtime.strftime('%Y-%m-%d %H:%M:%S'), "createid": user.comments, "userstatus": user.comments, })

    response_data = {'total': total, 'rows': rows, }

    return HttpResponse(json.dumps(response_data), content_type="application/json")


#初始化添加用户页
def initAddUser(request):
    #获取所有权限
    sql = 'select b.id id,b.title title,p.title ptitle,p.id pid from backuser_backmenu b left join backuser_backmenu p on p.id = b.parentid'
    menuData = BackuserBackmenu.objects.raw(sql)
    resultData = {}
    for menu in menuData:
        if menu.ptitle is None:
            if menu.ptitle not in resultData:
                resultData[menu.id] = {menu.title: []}
            continue
        if menu.pid not in resultData:
            resultData[menu.pid] = {menu.ptitle: []}
        resultData[menu.pid][menu.ptitle].append({menu.id: menu.title})
    return render(request, 'management/initEditUser.html', {'actionURL': '/addUser', 'resultData': resultData, })

#初始化编辑用户页
def initEditUser(request):
    uid = request.GET['uid']
    buser = BackuserUserinfo.objects.get(id=uid)
    #获取所有权限
    sql = 'select b.id id,b.title title,p.title ptitle,p.id pid from backuser_backmenu b left join backuser_backmenu p on p.id = b.parentid'
    menuData = BackuserBackmenu.objects.raw(sql)
    resultData = {}
    for menu in menuData:
        if menu.ptitle is None:
            if menu.ptitle not in resultData:
                resultData[menu.id] = {menu.title: []}
            continue
        if menu.pid not in resultData:
            resultData[menu.pid] = {menu.ptitle: []}
        resultData[menu.pid][menu.ptitle].append({menu.id: menu.title})
    #获取用户权限
    usermenuData = BackuserMenuuser.objects.filter(userid=uid)
    menuStr = ''
    for menu in usermenuData:
        menuStr = menuStr + menu.menuid + ','
    return render(request, 'management/initEditUser.html', {'actionURL': '/editUser', 'user': buser, 'menuStr': menuStr, 'resultData': resultData})

#增加用户
def addUser(request):
    username = request.POST['username']
    id = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(username))).replace('-', '')
    comments = request.POST['comments']
    userpwd = request.POST['userpwd']
    nowTime = datetime.datetime.now()
    buser = BackuserUserinfo(id=id, username=username, comments=comments, userpwd=userpwd,
                            logins=0, answers=0, questions=0, lastlogintime=nowTime,
                            createtime=nowTime, createid=1, userstatus=1,)
    #权限
    menupower = request.POST['menupower']
    menus = menupower.split(',')
    for m in menus:
        if len(m) == 0:
            continue
        muid = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(id.join(m)))).replace('-', '')
        mu = BackuserMenuuser(id=muid, userid=id, menuid=m)
        mu.save()
    buser.save()
    return render(request, 'management/showUsers.html', {'data': BackuserUserinfo.objects.all()})

#编辑用户
def editUser(request):
    uid = request.POST['uid']
    buser = BackuserUserinfo.objects.get(id=uid)
    buser.username = request.POST['username']
    buser.comments = request.POST['comments']
    buser.save()
    #权限
    menupower = request.POST['menupower']
    menus = menupower.split(',')
    #删原来的权限
    BackuserMenuuser.objects.filter(userid=uid).delete()
    for m in menus:
        if len(m) == 0:
            continue
        print m
        muid = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(uid.join(m)))).replace('-', '')
        mu = BackuserMenuuser(id=muid, userid=uid, menuid=m)
        mu.save()

    return render(request, 'management/showUsers.html', {'data': BackuserUserinfo.objects.all()})

#删除用户
def removeUser(request):
    uid = request.GET['uid']
    buser = BackuserUserinfo.objects.get(id=uid)
    buser.delete()
    return render(request, 'management/showUsers.html', {'data': BackuserUserinfo.objects.all()})

#修改用户状态
def modifyUserStatus(request):
    uid = request.GET['uid']
    ustatus= request.GET['ustatus']
    buser = BackuserUserinfo.objects.get(id=uid)
    buser.userstatus = ustatus
    buser.save()
    return render(request, 'management/showUsers.html', {'data': BackuserUserinfo.objects.all()})

#菜单管理
def menuManager(request):
    #获取所有菜单
    sql = 'select b.id id,b.title title,b.url url,p.title ptitle from backuser_backmenu b left join backuser_backmenu p on p.id = b.parentid'
    menuData = BackuserBackmenu.objects.raw(sql)
    #获取父级菜单
    parentData = BackuserBackmenu.objects.filter(parentid=0)
    return render(request, 'management/MenuManager.html', {'menuData': menuData, 'parentData': parentData}, )

#添加菜单
def addMenu(request):
    url = request.POST['url']
    menu = BackuserBackmenu(id=str(uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.uuid1()))).replace('-', ''), title=request.POST['title'], url=url, parentid=request.POST['pid'])
    menu.save()
    #获取所有菜单
    sql = 'select b.id id,b.title title,b.url url,p.title ptitle from backuser_backmenu b left join backuser_backmenu p on p.id = b.parentid'
    menuData = BackuserBackmenu.objects.raw(sql)

    #获取父级菜单
    parentData = BackuserBackmenu.objects.filter(parentid=0)
    return render(request, 'management/MenuManager.html', {'menuData': menuData, 'parentData': parentData}, )
