
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件
import time
class Test_zh_xtsz_dtgl_hmlb:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()


    #  鼠标悬浮地图管理--------点击画面列表
    def zh_xtsz_dtgl_hmlb(self):
        # 鼠标悬浮地图管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_dtgl)).perform()
        # 点击画面列表
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb))
        self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb).click()

    #点击添加新画面
    def zh_xtsz_dtgl_hmlb_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_tjxhm))
        self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_tjxhm).click()


    #名称搜索框
    def zh_xtsz_dtgl_hmlb_02(self,mcssk):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_mcssk))
        self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_mcssk).send_keys(mcssk)

    # 点击查询
    def zh_xtsz_dtgl_hmlb_03(self):

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_cx))
        self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_cx).click()

    #保存
    def zh_xtsz_dtgl_hmlb_04(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_bc))
        self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_bc).click()

    #删除
    def zh_xtsz_dtgl_hmlb_05(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_sc))
        self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_sc).click()
        #删除弹出框点击确定
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_sctck))
        self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_sctck).click()

    #提示语
    def zh_xtsz_dtgl_hmlb_06(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_tsy))
        return self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_tsy).text




    #名称
    def zh_xtsz_dtgl_hmlb_07(self,mc):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_mc))
        self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_mc).send_keys(mc)

    # 画面列表--隧道
    def zh_xtsz_dtgl_hmlb_08(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_hmlb))
        self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_hmlb).click()
        #画面列表下拉内容
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_hmlbxl))
        self.driver.find_elements(*loc.zh_xtsz_dtgl_hmlb_hmlbxl)[1].click()

    # 选择结构物
    def zh_xtsz_dtgl_hmlb_09(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_jgw))
        self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_jgw).click()
        # 结构物下拉内容
        time.sleep(1)
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_jgwxl))
        self.driver.find_elements(*loc.zh_xtsz_dtgl_hmlb_jgwxl)[0].click()


    # 矢量底图
    def zh_xtsz_dtgl_hmlb_010(self,zldt):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_zldt))
        self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_zldt).send_keys(zldt)





    #列表最后一个
    def zh_xtsz_dtgl_hmlb_011(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_lb))
        self.driver.find_elements(*loc.zh_xtsz_dtgl_hmlb_lb)[-1].click()


    #名称--------进行清除
    def zh_xtsz_dtgl_hmlb_012(self):

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_mc))
        self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_mc).clear()

    # 名称搜索框----进行清除
    def zh_xtsz_dtgl_hmlb_013(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_dtgl_hmlb_mcssk))
        self.driver.find_element(*loc.zh_xtsz_dtgl_hmlb_mcssk).clear()
















