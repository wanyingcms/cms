#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django import forms
from back_user.models import *
from utils.redisUtil import *
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")


# Create your views here.


#定义表单模型
class LoginForm(forms.Form):
    username=forms.CharField(label='用户名：',max_length=100)
    password=forms.CharField(label='密码：',widget=forms.PasswordInput)

def login(req):
    response = HttpResponse()
    response.set_cookie("username","123123")
    return render_to_response("login.html")

#登录方法
def dologin(req):
    print '........'
    if req.method == 'POST':
        uf = LoginForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            print 'username =',username,'password = ',password
            #查询用户
            user = BackuserUserinfo.objects.filter(username__exact=username,userpwd__exact=password)

            if user:
                print 'login success......'
                #登录信息存入redis
                cookid = req.COOKIES
                print cookid
                response = HttpResponseRedirect("/back_user/cmsindex/")
                response.set_cookie("username",username)

                redisSet(username,'123123123',30*60)
                return response
            else:
                print 'login fail......'
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


def cmsindex(req):
    print 'cookie ===', req.COOKIES
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
    return render_to_response('main/left.html',{'indexdata':[1,2,3]})

def allusediv(req):
    return render_to_response('main/allUseDiv.html')
def footer(req):
    return render_to_response('main/footer.html')
def top(req):
    return render_to_response('main/top.html')
def welcome(req):
    return render_to_response('main/welcome.html')
