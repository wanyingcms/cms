#coding:utf-8
__author__ = 'root'
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite1.settings")
from books.models import Publisher

#publiser_list = Publisher.objects.all()

#print publiser_list[2].__dict__

#print(u'\1142341')

#print json.dumps('{\'state_province\': u\'bj\', \'city\': u\'beijing\', \'name\': u\'zhoujia\', \'country\': u\'Chinese\', \'_state\': <django.db.models.base.ModelState object at 0x7fef4c264810>, \'website\': u\'www.zhoujia.com\', \'address\': u\'beijing\', \'id\': 3L}')
class PublisherEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,Publisher):
            return {'name':obj.name , 'address':obj.address,
                    'city':obj.city , 'country':obj.country,
                    'state_province':obj.state_province,'website':obj.website}
        return json.JSONEncoder.default(self,obj)

def getAllPublisher():
    publiser_list = Publisher.objects.all()
    pub = []
    for publister in publiser_list:
        #print  json.dumps(publister,cls=PublisherEncoder)
        print json.dumps(publister,cls=PublisherEncoder)
       #jsonstr = json.dump(publister,cls=PublisherEncoder).__str__()
        pub.append(json.loads(json.dumps(publister,cls=PublisherEncoder)))
    return pub
    #return json.dumps(pub)
    #return class_to_dict(publiser_list)


print getAllPublisher()


