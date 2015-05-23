#coding:utf-8
__author__ = 'root'
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")
from back_user.models import *
#from books.models import Publisher

#publiser_list = Publisher.objects.all()

#print publiser_list[2].__dict__

#print(u'\1142341')

#print json.dumps('{\'state_province\': u\'bj\', \'city\': u\'beijing\', \'name\': u\'zhoujia\', \'country\': u\'Chinese\', \'_state\': <django.db.models.base.ModelState object at 0x7fef4c264810>, \'website\': u\'www.zhoujia.com\', \'address\': u\'beijing\', \'id\': 3L}')

class Backuser_Backmenu(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,BackuserBackmenu):
            return {'id':o.id, 'title':o.title,
                    'parentid':o.parentid,'url':o.url}
        return json.JSONEncoder.default(self,o)



def menuList():
    allmenu = BackuserBackmenu.objects.all()
    menus = {}
    for pmenu in allmenu:
        for cmenu in allmenu:
            if pmenu.id == cmenu.parentid:
                if menus.__contains__(pmenu.title):
                    menus[pmenu.title].append(json.loads(json.dumps(cmenu,cls=Backuser_Backmenu)))
                else:
                    menus[pmenu.title]=[json.loads(json.dumps(cmenu,cls=Backuser_Backmenu))]
    return menus




#print menuList()


