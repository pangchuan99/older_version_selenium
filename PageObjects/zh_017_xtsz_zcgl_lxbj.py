
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件
import time
class Test_zh_xtsz_zcgl_lxbj:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    #鼠标悬浮到地图管理 点击类型编辑
    def zh_xtsz_zcgl_lxbj(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_zcgl)).perform()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj))
        self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj).click()


   #添加类型
    def zh_xtsz_zcgl_lxbj_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_tjlx))
        self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj_tjlx).click()


    # 类型名称搜索框
    def zh_xtsz_zcgl_lxbj_02(self,lxmcssk):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_lxmcssk))
        self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj_lxmcssk).send_keys(lxmcssk)

    # 查询
    def zh_xtsz_zcgl_lxbj_03(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_cx))
        self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj_cx).click()

    # 点击保存
    def zh_xtsz_zcgl_lxbj_04(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_bc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj_bc).click()


    #删除
    def zh_xtsz_zcgl_lxbj_05(self):
        # 删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_sc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj_sc).click()
        #点击删除后  弹出框点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_sctck))
        self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj_sctck).click()

    # 提示语
    def zh_xtsz_zcgl_lxbj_tsy(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_tsy))
        return self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj_tsy).text






    # 输入类型ID
    def zh_xtsz_zcgl_lxbj_06(self,lxid):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_lxid))
        self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj_lxid).send_keys(lxid)








    # 选择分组ID
    def zh_xtsz_zcgl_lxbj_07(self):
        # 点击分组ID
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_fzid))
        self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj_fzid).click()
        time.sleep(1)
        # 点击分组ID下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_fzidxl))
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_elements(*loc.zh_xtsz_zcgl_lxbj_fzidxl)[-1])
        self.driver.find_elements(*loc.zh_xtsz_zcgl_lxbj_fzidxl)[-1].click()



    # 输入类型名称
    def zh_xtsz_zcgl_lxbj_08(self,lxmc):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_lxmc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj_lxmc).send_keys(lxmc)




    # 输入类型参数(变量名)
    def zh_xtsz_zcgl_lxbj_09(self,lxcsblm):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_lxcsblm))
        self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj_lxcsblm).send_keys(lxcsblm)




    #列表点击最后一个
    def zh_xtsz_zcgl_lxbj_010(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_lb))
        self.driver.find_elements(*loc.zh_xtsz_zcgl_lxbj_lb)[-1].click()



    #类型名称清除
    def zh_xtsz_zcgl_lxbj_011(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_lxmc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj_lxmc).clear()

















