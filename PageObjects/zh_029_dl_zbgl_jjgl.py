
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件

from selenium.webdriver.common.keys import Keys                                                  #键盘输入
import time
class Test_zbgl_jjgl:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    def dl_zbgl_jjgl(self):
        #输入悬浮到值班管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.dl_zbgl)).perform()
        time.sleep(1)
        # 点击接警管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_jjgl))
        self.driver.find_element(*loc.dl_zbgl_jjgl).click()


    # 提示语---
    def dl_zbgl_jjgl_tsy(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.dl_zbgl_jjgl_tsy))
        return self.driver.find_element(*loc.dl_zbgl_jjgl_tsy).text


    #提交
    def dl_zbgl_jjgl_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_jjgl_tj))
        self.driver.find_element(*loc.dl_zbgl_jjgl_tj).click()



    #开始时间
    def dl_zbgl_jjgl_02(self,kssj):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_jjgl_kssj))
        self.driver.find_element(*loc.dl_zbgl_jjgl_kssj).send_keys(kssj)

    #事件类别
    def dl_zbgl_jjgl_03(self):
        # 事件类别
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_jjgl_sjlb))
        self.driver.find_element(*loc.dl_zbgl_jjgl_sjlb).click()
        #事件类别下拉内容
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_jjgl_sjlbxl))
        self.driver.find_elements(*loc.dl_zbgl_jjgl_sjlbxl)[0].click()



    # 事件等级
    def dl_zbgl_jjgl_04(self):
        # 事件等级
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_jjgl_sjdj))
        self.driver.find_element(*loc.dl_zbgl_jjgl_sjdj).click()
        # 事件等级下拉内容
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_jjgl_sjdjxl))
        self.driver.find_elements(*loc.dl_zbgl_jjgl_sjdjxl)[0].click()



    # 开始桩号
    def dl_zbgl_jjgl_05(self,kszh):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_jjgl_kszh))
        self.driver.find_element(*loc.dl_zbgl_jjgl_kszh).send_keys(kszh)


    # 结束桩号
    def dl_zbgl_jjgl_06(self,jszh):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_jjgl_jszh))
        self.driver.find_element(*loc.dl_zbgl_jjgl_jszh).send_keys(jszh)



