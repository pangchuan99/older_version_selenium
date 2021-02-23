from selenium import webdriver
import time
# 初始化
driver = webdriver.Chrome()
# 打开指定网址
driver.get("https://www.baidu.com")
driver.maximize_window()
# 定位设置元素
driver.find_element_by_id("kw").send_keys("仁和ERP - ERP企业管理系统,生产管理系统")
# driver.find_element_by_id("su").click()
time.sleep(5)
names= driver.find_elements_by_xpath('//*[@class="result c-container "]//div[@class="f13"]//*[@class="c-showurl"]')
lists= "www.renhxy.com/product... "
for i in names:
    a = i.text
    print(a)
    if a ==lists:
       driver.execute_script("arguments[0].scrollIntoView(false);",i)
       i.click()


time.sleep(8)
# 多窗口切换
windows = driver.window_handles
driver.switch_to.window(windows[-1])
driver.find_elements_by_xpath('//*[@class="menu"]//ul//a')[0].click()
time.sleep(5)
driver.switch_to.window(windows[-1])
driver.find_elements_by_xpath('//*[@class="menu"]//ul//a')[1].click()
time.sleep(5)
driver.switch_to.window(windows[-1])
driver.find_elements_by_xpath('//*[@class="menu"]//ul//a')[2].click()
time.sleep(5)
driver.switch_to.window(windows[-1])
driver.find_elements_by_xpath('//*[@class="menu"]//ul//a')[3].click()
time.sleep(5)
driver.switch_to.window(windows[-1])
driver.find_elements_by_xpath('//*[@class="menu"]//ul//a')[4].click()
time.sleep(5)
driver.switch_to.window(windows[-1])
driver.find_elements_by_xpath('//*[@class="menu"]//ul//a')[5].click()
time.sleep(5)
driver.switch_to.window(windows[-1])
driver.find_elements_by_xpath('//*[@class="menu"]//ul//a')[-1].click()
