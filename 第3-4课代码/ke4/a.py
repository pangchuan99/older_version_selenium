import requests

url = "http://49.235.92.12:9000/api/v1/login"

h = {
    "token": "xxxxxxxxxxxxxxx"
}

querystring = {
    "key1": "value1"
}

# Content-Type: application/json
body = {
    "username": "test3",
    "password": "123456"
}

c = {
    "sessionid": "xxxxxxxxx"
}
r = requests.post(url,
                  cookies=c,
                  json=body,
                  # params=querystring,
                  headers=h)
print(r.text)

token = r.json()["token"]
print("获取到的token:%s"%token)

code = r.json()["code"]
print(code)

msg = r.json()["msg"]
print(msg)

if msg == "login success!":
    print("登陆成功")
else:
    print("登陆失败")

# 断言
# assert msg == "login success!"