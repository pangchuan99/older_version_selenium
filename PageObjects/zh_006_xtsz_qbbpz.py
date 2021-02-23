from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件


from  selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys                                                  #键盘输入





class Test_zh_xtsz_qbbpz:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    def zh_xtsz_qbbpz(self):
        # 账户进行鼠标悬浮---系统设置,点击情报板配置
        # 鼠标悬浮---系统设置
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz)).perform()
        # 点击情报板配置
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz))
        self.driver.find_element(*loc.zh_xtsz_qbbpz).click()

    def zh_xtsz_qbbpz_01(self):
        # 点击添加新类型
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz_tjxlx))
        self.driver.find_element(*loc.zh_xtsz_qbbpz_tjxlx).click()

    def zh_xtsz_qbbpz_02(self):
        # 点击保存
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz_bc))
        self.driver.find_element(*loc.zh_xtsz_qbbpz_bc).click()

     # 点击保存后  提示语———— 请选择厂家
    def zh_xtsz_qbbpz_03(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz_tsy))
        return self.driver.find_element(*loc.zh_xtsz_qbbpz_tsy).text





    def zh_xtsz_qbbpz_04(self):

        # 点击厂家
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz_cj1))
        self.driver.find_element(*loc.zh_xtsz_qbbpz_cj1).click()

        # 点击厂家里面的内容
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz_xlnr))
        self.driver.find_elements(*loc.zh_xtsz_qbbpz_xlnr)[0].click()

    #尺寸
    def zh_xtsz_qbbpz_05(self,a1):
        # 尺寸输入内容
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz_cc))
        self.driver.find_element(*loc.zh_xtsz_qbbpz_cc).send_keys(Keys.CONTROL, 'a')
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz_cc))
        self.driver.find_element(*loc.zh_xtsz_qbbpz_cc).send_keys(a1)

    #字体大小
    def zh_xtsz_qbbpz_06(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz_ztdx))
        self.driver.find_elements(*loc.zh_xtsz_qbbpz_ztdx)[3].click()




    #列表点击最后一个
    def zh_xtsz_qbbpz_07(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz_lb))
        self.driver.find_elements(*loc.zh_xtsz_qbbpz_lb)[-1].click()

    # 修改尺寸
    def zh_xtsz_qbbpz_08(self,a1):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz_cc))
        self.driver.find_element(*loc.zh_xtsz_qbbpz_cc).send_keys(Keys.CONTROL,'a')
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz_cc))
        self.driver.find_element(*loc.zh_xtsz_qbbpz_cc).send_keys(a1)



    #点击删除
    def zh_xtsz_qbbpz_09(self):

        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz_sc))
        self.driver.find_element(*loc.zh_xtsz_qbbpz_sc).click()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_qbbpz_qd))
        self.driver.find_element(*loc.zh_xtsz_qbbpz_qd).click()














