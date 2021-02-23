
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件
import time
class Test_zh_xtsz_zcgl_zclb:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()



    # 鼠标悬浮到资产管理-----点击资产列表
    def zh_xtsz_zcgl_zclb(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_zcgl)).perform()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_zclb))
        self.driver.find_element(*loc.zh_xtsz_zcgl_zclb).click()

   #设备名称搜索框
    def zh_xtsz_zcgl_zclb_01(self,sbmc):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_zclb_sbmc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_zclb_sbmc).send_keys(sbmc)

    #点击查询
    def zh_xtsz_zcgl_zclb_02(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_zclb_cx))
        self.driver.find_element(*loc.zh_xtsz_zcgl_zclb_cx).click()






    # 点击列表最后一个
    def zh_xtsz_zcgl_zclb_03(self):
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_zclb_lb))
            self.driver.find_elements(*loc.zh_xtsz_zcgl_zclb_lb)[-1].click()



    # 详细编辑
    def zh_xtsz_zcgl_zclb_04(self):

            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_zclb_xxbj))
            self.driver.find_element(*loc.zh_xtsz_zcgl_zclb_xxbj).click()

    #名称
    def zh_xtsz_zcgl_zclb_05(self, sbmc):
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_zclb_mc))
            self.driver.find_element(*loc.zh_xtsz_zcgl_zclb_mc).clear()
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_zclb_mc))
            self.driver.find_element(*loc.zh_xtsz_zcgl_zclb_mc).send_keys(sbmc)


    # 保存
    def zh_xtsz_zcgl_zclb_06(self):

            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_zclb_bc))
            self.driver.find_element(*loc.zh_xtsz_zcgl_zclb_bc).click()

    #提示语
    def zh_xtsz_zcgl_zclb_tsy(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_zclb_tsy))
        return self.driver.find_element(*loc.zh_xtsz_zcgl_zclb_tsy).text





    # 详细编辑里面的  资产列表
    def zh_xtsz_zcgl_zclb_07(self):

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_zclb_xxbjzclb))
        self.driver.find_element(*loc.zh_xtsz_zcgl_zclb_xxbjzclb).click()



    # 删除
    def zh_xtsz_zcgl_zclb_08(self):
        # 删除
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_zclb_sc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_zclb_sc).click()

        # 删除弹出框  点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_zclb_sctck))
        self.driver.find_element(*loc.zh_xtsz_zcgl_zclb_sctck).click()



