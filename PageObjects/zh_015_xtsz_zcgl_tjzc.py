
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件

from selenium.webdriver.common.keys import Keys
import time
class Test_zh_xtsz_zcgl_tjzc:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()



    # 鼠标悬浮资产管理--- 点击添加资产
    def zh_xtsz_zcgl_tjzc(self):
        #鼠标悬浮资产管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_zcgl)).perform()
        # 点击添加资产
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_tjzc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_tjzc).click()


    #类型
    def zh_xtsz_zcgl_tjzc_01(self):
        #类型
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_tjzc_lx))
        self.driver.find_element(*loc.zh_xtsz_zcgl_tjzc_lx).click()


    #类型下拉---火灾手报
    def zh_xtsz_zcgl_tjzc_02(self):
        #类型下拉---火灾手报
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_tjzc_lxxl))
        #滚动
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_element(*loc.zh_xtsz_zcgl_tjzc_lxxl))
        self.driver.find_element(*loc.zh_xtsz_zcgl_tjzc_lxxl).click()



    # 点击保存
    def zh_xtsz_zcgl_tjzc_03(self):

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_tjzc_bc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_tjzc_bc).click()

    #提示语
    def zh_xtsz_zcgl_tjzc_tsy(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_tjzc_tsy))
        return self.driver.find_element(*loc.zh_xtsz_zcgl_tjzc_tsy).text






   #输入名称
    def zh_xtsz_zcgl_tjzc_04(self,mc):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_tjzc_mc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_tjzc_mc).send_keys(mc)


     # 名称进行清除
    def zh_xtsz_zcgl_tjzc_05(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_tjzc_mc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_tjzc_mc).clear()



    #输入桩号
    def zh_xtsz_zcgl_tjzc_06(self,zh):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_tjzc_zh))
        self.driver.find_element(*loc.zh_xtsz_zcgl_tjzc_zh).send_keys(zh)



   #选择区域-
    def zh_xtsz_zcgl_tjzc_07(self):
        #区域
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_tjzc_qy))
        self.driver.find_element(*loc.zh_xtsz_zcgl_tjzc_qy).click()
        # 区域下拉内容
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_tjzc_qyxl))
        self.driver.find_elements(*loc.zh_xtsz_zcgl_tjzc_qyxl)[2].click()

    # 额定功率进行清空
    def zh_xtsz_zcgl_tjzc_08(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_tjzc_edgl))
        self.driver.find_element(*loc.zh_xtsz_zcgl_tjzc_edgl).send_keys(Keys.BACK_SPACE*8)

    # 输入额定功率
    def zh_xtsz_zcgl_tjzc_09(self,edgl):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_tjzc_edgl))
        self.driver.find_element(*loc.zh_xtsz_zcgl_tjzc_edgl).send_keys(edgl)



