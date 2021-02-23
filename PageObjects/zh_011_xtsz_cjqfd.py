
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件

from selenium.webdriver.common.keys import Keys                                                  #键盘事件
import time
class Test_zh_xtsz_cjqfd:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()



    # 鼠标悬浮---系统设置
    # 账户进行鼠标悬浮---系统设置,点击车检器分段
    def zh_xtsz_cjqfd(self):
        #点击系统设置
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz)).perform()
        # 点击车检器分段
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd))
        self.driver.find_element(*loc.zh_xtsz_cjqfd).click()


     #点击添加新配置
    def zh_xtsz_cjqfd_01(self):
        #点击添加新配置
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_tjxpz))
        self.driver.find_element(*loc.zh_xtsz_cjqfd_tjxpz).click()

    #点击保存
    def zh_xtsz_cjqfd_02(self):

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_bc))
        self.driver.find_element(*loc.zh_xtsz_cjqfd_bc).click()

    #点击保存提示语是 ----起始设备、结束设备和车道数为必填项
    def zh_xtsz_cjqfd_03(self):
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_tsy))
            return self.driver.find_element(*loc.zh_xtsz_cjqfd_tsy).text


    # 方向
    def zh_xtsz_cjqfd_04(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_fx))
        self.driver.find_element(*loc.zh_xtsz_cjqfd_fx).click()
        #方向下拉内容
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_fxxlnr))
        self.driver.find_elements(*loc.zh_xtsz_cjqfd_fxxlnr)[-1].click()

    #起始设备-
    def zh_xtsz_cjqfd_05(self):
        #起始设备
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_qssb))
        self.driver.find_element(*loc.zh_xtsz_cjqfd_qssb).click()
        # 起始设备下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_qssbxl))
        self.driver.find_elements(*loc.zh_xtsz_cjqfd_qssbxl)[0].click()


    # 结束设备
    def zh_xtsz_cjqfd_06(self):
        #结束设备
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_jssb))
        self.driver.find_element(*loc.zh_xtsz_cjqfd_jssb).click()
        # 结束设备下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_jssbxl))
        self.driver.find_elements(*loc.zh_xtsz_cjqfd_jssbxl)[0].click()



    # 车道数---清除
    def zh_xtsz_cjqfd_07(self):

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_cds))
        self.driver.find_element(*loc.zh_xtsz_cjqfd_cds).send_keys(Keys.BACKSPACE*8)



    #车道数输入
    def zh_xtsz_cjqfd_08(self,cds):
        # 车道数
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_cds))
        self.driver.find_element(*loc.zh_xtsz_cjqfd_cds).send_keys(cds)





    #列表最后一个进行点击
    def zh_xtsz_cjqfd_09(self):
        # 列表最后一个
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_lb))
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_elements(*loc.zh_xtsz_cjqfd_lb)[-1])
        self.driver.find_elements(*loc.zh_xtsz_cjqfd_lb)[-1].click()






    #删除
    def zh_xtsz_cjqfd_010(self):
        # 点击删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_sc))
        self.driver.find_element(*loc.zh_xtsz_cjqfd_sc).click()
        # 点击删除--弹出框--点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_cjqfd_sctck))
        self.driver.find_element(*loc.zh_xtsz_cjqfd_sctck).click()


