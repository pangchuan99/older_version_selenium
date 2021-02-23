
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件
import time
class Test_zh_xtsz_yppz:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()



    # 鼠标悬浮---系统设置
    # 账户进行鼠标悬浮---系统设置,点击音频配置
    def zh_xtsz_yppz(self):
        #点击系统设置
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz)).perform()
        # 点击音频配置
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz))
        self.driver.find_element(*loc.zh_xtsz_yppz).click()

     #点击添加新配置
    def zh_xtsz_yppz_01(self):
        #点击添加新配置
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_tjxpz))
        self.driver.find_element(*loc.zh_xtsz_yppz_tjxpz).click()

    #点击保存
    def zh_xtsz_yppz_02(self):
        #点击保存
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_bc))
        self.driver.find_element(*loc.zh_xtsz_yppz_bc).click()

    #提示语
    def zh_xtsz_yppz_03(self):
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tsy))
            return self.driver.find_element(*loc.zh_xtsz_lkpz_tsy).text





    # 输入音频ID
    def zh_xtsz_yppz_04(self,ypid):
        #输入音频ID
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_ypid))
        self.driver.find_element(*loc.zh_xtsz_yppz_ypid).send_keys(ypid)







  # 输入音频名称
    def zh_xtsz_yppz_05(self,ypmc):
        #输入音频名称
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_ypmc))
        self.driver.find_element(*loc.zh_xtsz_yppz_ypmc).send_keys(ypmc)





    # 输入版本号
    def zh_xtsz_yppz_06(self,bbh):
        # 输入版本号
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_bbh))
        self.driver.find_element(*loc.zh_xtsz_yppz_bbh).send_keys(bbh)

    #音频ID搜索框
    def zh_xtsz_yppz_07(self,ypidssk):
        # 点击分组
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_ypidssk))
        self.driver.find_element(*loc.zh_xtsz_yppz_ypidssk).send_keys(ypidssk)

    #查询
    def zh_xtsz_yppz_08(self):
        # 点击查询
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_cx))
        self.driver.find_element(*loc.zh_xtsz_yppz_cx).click()

    # 列表点击最后一个
    def zh_xtsz_yppz_09(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_lb))
        self.driver.find_elements(*loc.zh_xtsz_yppz_lb)[-1].click()



    # 修改版本号
    def zh_xtsz_yppz_010(self, bbh):
        # 清空版本号
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_bbh))
        self.driver.find_element(*loc.zh_xtsz_yppz_bbh).clear()
        # 输入版本号
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_bbh))
        self.driver.find_element(*loc.zh_xtsz_yppz_bbh).send_keys(bbh)





     #删除
    def zh_xtsz_yppz_011(self):
        # 点击删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_sc))
        self.driver.find_element(*loc.zh_xtsz_yppz_sc).click()
        # 点击删除弹出框---点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_sctck))
        self.driver.find_element(*loc.zh_xtsz_yppz_sctck).click()





