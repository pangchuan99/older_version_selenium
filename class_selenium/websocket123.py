import json
import websocket
def send(url,data):
    print("连接1")
    '''websocket建立连接接收消息'''

    ws = websocket.create_connection(url)      # 创建连接
    print("连接2{}".format(ws))
    ws.send(json.dumps(data) )  # json转化为字符串，必须转化

    results = []
    while True:

        receive = ws.recv()    # 服务器响应数据

        results.append(receive)
        print("连接2{}".format(ws))
    ws.close()

    return results
# url = "wss://gsm.jdjinsui.com/wss/?EIO=3&transport=websocket"

url = "wss://gsm.jdjinsui.com/wss/?EIO=3&transport=websocket"
data={
    "code":"user.login",
    "body": {
        "name": '13547324646',
        "password": '278a97d3b74b6ff8da2c66d33842c210'
    },

     "token": "",
    "timestamp": "1591924758",
    "sign": "aDlPwGnEeYR0uLGOMsfjWBbmeum_MiZ1",
    "nonestr": "8f88c6a0-99f4-42f9-ae99-c40e4d7efdeb",
    "extra": "",
}

a=send(url,data)
b=a.send(data)

print("张三{}".format(b))











