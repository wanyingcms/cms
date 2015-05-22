#coding:UTF-8
import redis

#r = redis.StrictRedis(host='localhost',port=6379,db=0)
#r.set('b','1231')
#连接池
pool = redis.ConnectionPool(host='localhost',port=6379,db=0)
r = redis.Redis(connection_pool=pool)

def redisSet(key,value):
    r.set(key,value)

def redisSet(key,value,time):
    r.set(key,value,time)

def redisGet(key):
    value=r.get(key)
    return value

def redisDelKey(key):
    r.delete(key)

#管道 方法自己封装，例如 pipe.set('foo','bar').sadd('aa','bb').incr('loginnum').execute()
pipe = r.pipeline()


#订阅消息队列
p = r.pubsub()

#当A打开B的聊天窗口时，
#如果B不在线，B订阅A，A不订阅B；
#如果B在线，双方同时互相订阅
#订阅channel用 user-loginname 作为channel名
def subscribe(loginname):
    p.subscribe('user-'+loginname)
    getMsg()

#发布聊天信息
def publish(channel , content):
    r.publish(channel,content)



def getMsg():
    for message in p.listen():
        print(message)



