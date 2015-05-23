#coding:utf-8
__author__ = 'root'

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from utils.redisUtil import *

class QtsAuthenticationMiddleware(object):
    def process_request(self,request):
        #print "path=====",request.path
        if request.path == r'/back_user/login/' or request.path == r'/back_user/dologin/':
            pass
        else:
            cookid = request.COOKIES['username']
            username = redisGet(cookid)
            if username == None:
                return HttpResponseRedirect("/back_user/login/")
            else:
                pass
        #else:
        #    print '....2222'
         #   return render_to_response("login.html")
            #return HttpResponseRedirect("/back_user/login/")

