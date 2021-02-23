import requests

url = "http://49.235.92.12:6009/api/v1/login"

for i in range(1, 11):
    username = "test"+str(i)
    body = {
        "username": username,
        "password": "123456"
    }
    r = requests.post(url, json=body)
    print(r.json())
    token = r.json()["token"]
    with open("token_user.txt", "a") as fp:
        fp.write(token+","+username+"\n")