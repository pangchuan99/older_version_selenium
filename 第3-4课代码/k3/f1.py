#from selenium import webdriver
#要操作下拉框：from selenium.webdriver.support.select import Select
#要操作键盘：from selenium.webdriver.common.keys import Keys
#要用系统时间：from datetime import datetime
#要操作Excel：from openpyxl import load_workbook
#from selenium.webdriver import ActionChains  #鼠标事件



import  requests
import json


url="http://web.juhe.cn:8080/constellation/getAll"

data123={
    "key":"cde5e16435cd0217f505a88898b60707",
    "consName":"水瓶座",
    "type":"today"
}

r=requests.get(url,params=data123)

print(json.dumps(r.json(), indent=4, ensure_ascii=False))