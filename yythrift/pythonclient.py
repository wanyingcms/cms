from HelloWorldService import Client
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket

# Talk to a server via TCP sockets, using a binary protocol
transport = TSocket.TSocket("192.168.0.233", 8090)
transport.open()
protocol = TBinaryProtocol.TBinaryProtocol(transport)


def test():
    client = Client(protocol)
    print '111111111111111'
    str = client.sayHello("qiu")
    print '2222222222222'
    print str
    print '333333333333'
    print str+'ggg'
    print '44444444444444'

