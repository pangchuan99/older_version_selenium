
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件
import time
class Test_zh_xtsz_dtgl_ysbd:

    def wait_elePresence(self):
        pass

    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    #元素绑定
    def zh_xtsz_dtgl_ysbd(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_dtgl)).perform()
        # 点击画面列表
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_ysbd))
        self.driver.find_element(*loc.zh_xtsz_dtgl_ysbd).click()


    #点击添加新画面-点击保存提示语
    def zh_xtsz_dtgl_ysbd_01(self):
        # 定位到火灾手报
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_ysbd_sb))
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_elements(*loc.zh_xtsz_dtgl_ysbd_sb)[117])
        start=self.driver.find_elements(*loc.zh_xtsz_dtgl_ysbd_sb)[117]
        end=self.driver.find_element(*loc.zh_xtsz_dtgl_ysbd_div)
        ActionChains(self.driver).drag_and_drop(start,end).perform()
        time.sleep(3)

    #提示语---必须包含画面名称
    def zh_xtsz_dtgl_hmlb_tsy01_1(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_tsy1))
        return self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_tsy1).text
