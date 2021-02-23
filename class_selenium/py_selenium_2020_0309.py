# from selenium import webdriver
# # from selenium.webdriver.support.wait import WebDriverWait #显示等待类
# # from selenium.webdriver.support import  expected_conditions as EC
# # from selenium.webdriver.common.by import By  #定位的元素
# import time
# from selenium.webdriver.common.action_chains import ActionChains #鼠标事件
#
# driver=webdriver.Chrome()
#
#
# driver.get("http://172.16.1.26:8089/signin.html?redirect=/monitor/browser")
# driver.maximize_window()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="body"]/div/form/div[1]/div/div/input').send_keys("13547324646")
# driver.find_element_by_xpath('//*[@id="body"]/div/form/div[2]/div/div/input').send_keys("a1234567")
# driver.find_element_by_xpath('//*[@id="body"]/div/form/div[3]/div/button').click()
#
# time.sleep(20)
# ele=driver.find_element_by_xpath('//*[contains(text(),"值班管理")]')
# time.sleep(15)
# ActionChains(driver).move_to_element(driver.find_element_by_xpath(ele)).perform()
#
#
import json
d1 = {"a": None,
      "b": False,
      "c": True,
      "d":"BAB2",
      "e": ["1", 12],
      "f": ("1n", 90),
      "g": {"h": 1,
      "i": "11",
      "j": True}
}

print(type(d1))
print(d1)
#

js = json.dumps(d1)
print(type(js))
print(js)
js_json=json.loads(js)
print(type(js_json))
print(js_json)


# js_json=json.dumps()#字典转json
# json=json.loads()#json 转字典
# eval()#转字符串

# aa=str(d1)
# print(type(aa))
# print(aa)
#
#
# bb=eval(aa)
# print(type(bb))
# print(bb)
# print(bb["b"])



# import  json
# a={"a":"True","b":"bbb"}
# print(type(a))
# print(a)
# a1=json.dumps(a)
# print(type(a1))
# print(a1)