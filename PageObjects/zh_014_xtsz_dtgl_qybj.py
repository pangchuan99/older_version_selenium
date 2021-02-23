
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件

import time
class Test_zh_xtsz_dtgl_qybj:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()


    #鼠标悬浮到地图管理 点击区域编辑
    def zh_xtsz_dtgl_qybj(self):

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_dtgl)).perform()
        # 区域编辑
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj))
        self.driver.find_element(*loc.zh_xtsz_dtgl_qybj).click()


     #点击添加新区域
    def zh_xtsz_dtgl_qybj_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj_tjxqy))
        self.driver.find_element(*loc.zh_xtsz_dtgl_qybj_tjxqy).click()

    #点击查询
    def zh_xtsz_dtgl_qybj_02(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj_cx))
        self.driver.find_element(*loc.zh_xtsz_dtgl_qybj_cx).click()


    # 点击保存
    def zh_xtsz_dtgl_qybj_03(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj_bc))
        self.driver.find_element(*loc.zh_xtsz_dtgl_qybj_bc).click()



     #提示语
    def zh_xtsz_dtgl_qybj_tsy(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj_tsy))
        return self.driver.find_element(*loc.zh_xtsz_dtgl_qybj_tsy).text


    # 点击区域类型
    def zh_xtsz_dtgl_qybj_04(self):

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj_qylx))
        self.driver.find_element(*loc.zh_xtsz_dtgl_qybj_qylx).click()

        # 点击区域类型下拉框内容---（结构区域）
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj_qylxxl))
        self.driver.find_elements(*loc.zh_xtsz_dtgl_qybj_qylxxl)[1].click()




    #输入名称名称
    def zh_xtsz_dtgl_qybj_05(self,mc):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj_mc))
        self.driver.find_element(*loc.zh_xtsz_dtgl_qybj_mc).send_keys(mc)


    #名称清除
    def zh_xtsz_dtgl_qybj_06(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj_mc))
        self.driver.find_element(*loc.zh_xtsz_dtgl_qybj_mc).clear()







    #  对应结构物
    def zh_xtsz_dtgl_qybj_07(self,):

        # 点击对应结构物
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj_dyjgw))
        self.driver.find_element(*loc.zh_xtsz_dtgl_qybj_dyjgw).click()

        # 点击对应结构物下拉框内容
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj_dyjgwxl))
        self.driver.find_elements(*loc.zh_xtsz_dtgl_qybj_dyjgwxl)[0].click()





    #点击列表最后一个
    def zh_xtsz_dtgl_qybj_08(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj_lb))
        self.driver.find_elements(*loc.zh_xtsz_dtgl_qybj_lb)[-1].click()





    # 进行删除
    def zh_xtsz_dtgl_qybj_09(self,):

        # 点击删除
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj_sc))
        self.driver.find_element(*loc.zh_xtsz_dtgl_qybj_sc).click()

        # 点击删除--弹出框点击确定
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_qybj_sctck))
        self.driver.find_element(*loc.zh_xtsz_dtgl_qybj_sctck).click()












