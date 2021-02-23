import requests

url = "http://www.example.com/"

# xml
body = '''
<?xml version=“1.0” encoding = “UTF-8”?>
<COM>
<REQ name="上海-悠悠">
<USER_ID>yoyoketang</USER_ID>
<COMMODITY_ID>123456</COMMODITY_ID>
<SESSION_ID>absbnmasbnfmasbm1213</SESSION_ID>
</REQ>
</COM>
'''

# r = requests.post(url, data=body.encode("utf-8"))
r = requests.post(url)
print(r.text)