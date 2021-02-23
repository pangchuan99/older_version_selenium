

import websocket
from websocket import ABNF
import json
import _thread
import time
import ssl
from common.hashPwd import HashPwd

url = "wss://gsm.jdjinsui.com/wss/?EIO=3&transport=websocket"  # 接口地址
# wav_path="C:/Users/huaixiao/Music/1.mp3"   #音频文件地址

def on_message(ws, message):
   print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("close connection")

def on_open(ws):
    def run(*args):
        content = {
            "code":"user.login",
            "body": {
                "name": '18780887830',
                "password":"278a97d3b74b6ff8da2c66d33842c210"
            },
            "token":"null",
            "timestamp": time.time(),
            "sign": "aDlPwGnEeYR0uLGOMsfjWBbmeum_MiZ2",
            "nonestr": "8f88c6a0-99f4-42f9-ae99-c40e4d7efleb",
            "extra": "null"
        }
        ws.send(json.dumps(content))
        # step = 3200
        # with open(wav_path, 'rb') as f:
        #     while True:
        #         read_data = f.read(step)
        #         if read_data:
        #             ws.send(read_data, ABNF.OPCODE_BINARY)
        #         if len(read_data) < step:
        #             break
        #         time.sleep(0.1)
        #
        # ws.send('', ABNF.OPCODE_BINARY)
        time.sleep(1.5)
        # ws.close()
    _thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})



