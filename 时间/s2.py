from selenium import webdriver
import time
# 初始化
driver = webdriver.Chrome()
# 打开指定网址
driver.get("https://www.so.com")
driver.maximize_window()
# 定位设置元素
driver.find_element_by_id("input").send_keys("仁和ERP")
driver.find_element_by_id("search-button").click()
time.sleep(5)
# names= driver.find_elements_by_xpath('//*[@class="res-list"]//h3 ')
# lists= "仁和ERP - ERP管理系统,生产管理系统,人事考勤系统,进销存软件"
names= driver.find_elements_by_xpath('//*[@class="res-list"]//p[@class="res-linkinfo"]')
lists= "www.renhxy.com-快照"
# names= driver.find_elements_by_xpath('//*[@class="res-list"]//p[@class="res-linkinfo"]//cite')
for i in names:
    a =i.text
    print(a)
    if a in lists:
       driver.execute_script("arguments[0].scrollIntoView(false);",i)
       # b=i.find_element_by_xpath('//*[@class="res-list"]//*[contains(text()," - ERP管理系统,生产管理系统,人事考勤系统,进销存软件")]')
       # i.find_element_by_xpath('//*[@class="res-list"]//*[contains(text()," - ERP")]').click()
       b1=i.find_element_by_xpath('//h3//a').text
       print("打印出来的 {}".format(b1))
       i.find_element_by_xpath('//h3//a').click()
