#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
from django import forms
from back_user.models import *

# Create your views here.

def hudong(req):
    print "msg............."
    return render_to_response("p2pmsg.html")


# 用户类型
def userType(req):
    jsonStr = json.dumps([{"text":r"前端技术","value":r"FrontTechnologe"},{"text":r"后端技术","value":r"BackTechnology"},
                          {"text":r"Android","value":r"Android"},
                          {"text":r"iOS","value":r"iOS"},{"text":r"X+Y复合型人才","value":r"XY"},
                          {"text":r"全部","value":r"quanbu"},
                          {"text":r"发包方","value":r"fabao"},{"text":r"大BOSS","value":r"boss"},
                          {"text":r"美眉","value":r"beautifulgirl"}])
    return HttpResponse(jsonStr,content_type="application/json")

#虚拟用户列表
def virtualUserList(req):
    jsonStr = json.dumps([{"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"}])

    return HttpResponse(jsonStr,content_type="application/json")

#真是用户列表
def realUserList(req):
    jsonStr = json.dumps([{"text":"用户1","value":"1"},
                          {"text":"用户2","value":"1"},
                          {"text":"用户3","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"},
                          {"text":"传说中的神","value":"1"}])

    return HttpResponse(jsonStr,content_type="application/json")




def p2pmessage(req):
    jsonStr = json.dumps([{"user":"用户1","sendtime":"2014-10-08","msg":"内容，内容1","type":"1"},
                          {"user":"用户1","sendtime":"2014-10-08","msg":"内容，内容2","type":"1"},
                          {"user":"用户1","sendtime":"2014-10-08","msg":"内容，内容3","type":"2"},
                          {"user":"用户1","sendtime":"2014-10-08","msg":"内容，内容4","type":"2"}])

    return HttpResponse(jsonStr,content_type="application/json")



def viranswer(req):
    jsonStr = json.dumps([{"user":"用户1","sendtime":"2014-10-08","msg":"内容，内容1","zan":"100","msgid":"131434276"},
                          {"user":"用户1","sendtime":"2014-10-08","msg":"内容，内容2","zan":"123","msgid":"131478365"},
                          {"user":"用户1","sendtime":"2014-10-08","msg":"内容，内容3","zan":"234","msgid":"131498342"},
                          {"user":"用户1","sendtime":"2014-10-08","msg":"内容，内容4","zan":"456","msgid":"163184342"}])

    return HttpResponse(jsonStr,content_type="application/json")


#定义回答表单模型
class AnswerForm(forms.Form):
    msgid=forms.CharField(label='messageid：',required=False,max_length=100)
    msgcontent = forms.CharField(label='msgcontent',required=False ,max_length=10000)
    imagefile = forms.ImageField(required=False)


'''回答'''
def reanswer(req):
    print "aaaaaaaa"
    if req.method == 'POST':
        af = AnswerForm(req.POST)
        if af.is_valid():
            msgid = af.cleaned_data['msgid']
            msgcontent = af.cleaned_data['msgcontent']
            if msgid != None and msgid != '':
                #根据回答id发送答案
                print msgid
            elif msgcontent != None and msgcontent!='':
                #直接发送内容
                print msgcontent
            else:

                af = AnswerForm(req.POST,req.FILES)
                print "pic........................"#,af.is_valid()
                pic = req.FILES["imagefile"]
                des_origin_file = open("/root/PycharmProjects/cms/static/img/pic1","ab")
                for chunk in pic.chunks():
                    des_origin_file.write(chunk)
                des_origin_file.close()

    return HttpResponse("{result:1}")



def guanli(req):

    print "msg_admin............."
    return render_to_response("p2padmin.html")



def yunweiList(req):

    users = BackuserUserinfo.objects.all()
    userJson = []
    for user in users:
        print "user====",user.username
        userJson.append({"text":user.username,"value":user.id})

    userJsonStr = json.dumps(userJson)
    print "jsonStr==",userJsonStr
    return HttpResponse(userJsonStr,content_type="application/json")


























