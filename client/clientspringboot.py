import grpc
from base_package import springbootdata_pb2, springbootdata_pb2_grpc

_HOST = 'localhost'
_PORT = '30081'


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # 监听频道
    client = springbootdata_pb2_grpc.TestGrpcServiceStub(channel=conn)  # 客户端使用Stub类发送请求,参数为频道,为了绑定链接
    response = client.testMethod(springbootdata_pb2.TestRequest(id='333', name='hello,world!'))  # 返回的结果就是proto中定义的类
    print(response)


if __name__ == '__main__':
    run()