
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
class Test_zbgl_dfgl:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    def dl_zbgl_dfgl(self):
        #输入悬浮到值班管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.dl_zbgl)).perform()
        time.sleep(1)
        # 点击到访管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl))
        self.driver.find_element(*loc.dl_zbgl_dfgl).click()


    # 提示语---
    def dl_zbgl_dfgl_tsy(self):

        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_tsy))
        return self.driver.find_element(*loc.dl_zbgl_dfgl_tsy).text

    # 点击添加新记录
    def dl_zbgl_dfgl_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_tjxjl))
        self.driver.find_element(*loc.dl_zbgl_dfgl_tjxjl).click()



    #保存
    def dl_zbgl_dfgl_02(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_bc))
        self.driver.find_element(*loc.dl_zbgl_dfgl_bc).click()

    # 姓名
    def dl_zbgl_dfgl_03(self,xm):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_xm))
        self.driver.find_element(*loc.dl_zbgl_dfgl_xm).send_keys(xm)



    # 性别---性别下拉内容选择
    def dl_zbgl_dfgl_04(self):
        #性别
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_xb))
        self.driver.find_element(*loc.dl_zbgl_dfgl_xb).click()
        # 性别下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_xbxl))
        self.driver.find_elements(*loc.dl_zbgl_dfgl_xbxl)[-1].click()


    #联系电话
    def dl_zbgl_dfgl_05(self, lxdh):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_lxdh))
        self.driver.find_element(*loc.dl_zbgl_dfgl_lxdh).send_keys(lxdh)

    #证件号码
    def dl_zbgl_dfgl_06(self,zjhm):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_zjhm))
        self.driver.find_element(*loc.dl_zbgl_dfgl_zjhm).send_keys(zjhm)



     # 到访时间
    def dl_zbgl_dfgl_07(self,dfsj):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_dfsj))
        self.driver.find_element(*loc.dl_zbgl_dfgl_dfsj).send_keys(dfsj)

    #姓名搜索框
    def dl_zbgl_dfgl_08(self,xmssk):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_xmssk))
        self.driver.find_element(*loc.dl_zbgl_dfgl_xmssk).send_keys(xmssk)

    # 查询
    def dl_zbgl_dfgl_09(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_cx))
        self.driver.find_element(*loc.dl_zbgl_dfgl_cx).click()

     # 列表取最后一个
    def dl_zbgl_dfgl_010(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_lb))
        self.driver.find_elements(*loc.dl_zbgl_dfgl_lb)[-1].click()



     # 离开时间
    def dl_zbgl_dfgl_011(self,lksj):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_lksj))
        self.driver.find_element(*loc.dl_zbgl_dfgl_lksj).send_keys(lksj)




    #删除--删除弹出框点击确定
    def dl_zbgl_dfgl_012(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_sc))
        self.driver.find_element(*loc.dl_zbgl_dfgl_sc).click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_dfgl_sctck))
        self.driver.find_element(*loc.dl_zbgl_dfgl_sctck).click()

