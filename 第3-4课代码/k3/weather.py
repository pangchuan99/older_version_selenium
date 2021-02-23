import requests
import json

url = "http://apis.juhe.cn/simpleWeather/query"
querystring = {
    "key": "5a731258401fc3af244873d094ac6564",
    "city": "苏州"
}
# params
r = requests.post(url, parms=querystring)

# 返回的结果
print(r.text)  # str
print(type(r.text))
print(r.json())
print(type(r.json()))
print(r.status_code)
print(r.headers)
print(r.headers['Content-Type'])
print(r.cookies)


print(dict(r.cookies))
print(r.cookies['aliyungf_tc'])
# print(r.encoding)
# print(r.url)
# print(r.content)  # byte
# print(r.content.decode("utf-8"))  # r.text出现乱码时候
#
# print(json.dumps(r.json(), indent=4, ensure_ascii=False))
