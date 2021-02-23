from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains #鼠标事件



class Test_xtsz:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    def zh_02(self):
        #账户进行鼠标悬浮
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.zh))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh)).perform()


    # 账户进行鼠标悬浮后 点击系统设置
    def zh_xtsz(self):

        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xllb))
        self.driver.find_elements(*loc.zh_xllb)[1].click()

