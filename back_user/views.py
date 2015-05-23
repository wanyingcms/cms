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
        print '=====',menuname,cmenu
    return render_to_response('main/left.html',{'indexdata':menus})

def allusediv(req):
    return render_to_response('main/allUseDiv.html')
def footer(req):
    return render_to_response('main/footer.html')
def top(req):
    return render_to_response('main/top.html')
def welcome(req):
    return render_to_response('main/welcome.html')




