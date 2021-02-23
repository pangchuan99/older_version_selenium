import requests
import re
url = "http://49.235.92.12:8020/admin/login/?next=/admin/"

# session
s = requests.session()

r1 = s.get(url)
# print(r1.text)

# name='csrfmiddlewaretoken' value='iLcxsmkHkErCy6v6qHPiiCrYMXzs7FJC5muR40hTjmNbG3BWEIA1dBwjEkuuESjw'

csrf_token = re.findall("'csrfmiddlewaretoken' value='(.+?)'", r1.text)
print(csrf_token[0])

body = {
    "csrfmiddlewaretoken": csrf_token[0],
    "username": "admin",
    "password": "yoyo123456",
    "next": "/admin/"
}

r2 = s.post(url, data=body)

if "站点管理 | Django 站点管理员" in r2.text:
    print("登录成功")
else:
    print("登录失败！")