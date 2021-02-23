
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
class Test_zh_xtsz_zcgl_cjpz:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()



    #鼠标悬浮资产管理点击厂家配置
    def zh_xtsz_zcgl_cjpz(self):
        WebDriverWait()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_zcgl)).perform()
        # 厂家配置
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz))
        self.driver.find_element(*loc.zh_xtsz_zcgl_cjpz).click()



   #添加厂家
    def zh_xtsz_zcgl_cjpz_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz_tjcj))
        self.driver.find_element(*loc.zh_xtsz_zcgl_cjpz_tjcj).click()


    # 点击保存
    def zh_xtsz_zcgl_cjpz_02(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz_bc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_cjpz_bc).click()

     #删除
    def zh_xtsz_zcgl_cjpz_03(self):
        # 删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz_sc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_cjpz_sc).click()
        # 删除弹出框点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz_sctck))
        self.driver.find_element(*loc.zh_xtsz_zcgl_cjpz_sctck).click()

    # 提示语---请选择设备类型
    def zh_xtsz_zcgl_cjpz_tsy(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz_tsy))
        return self.driver.find_element(*loc.zh_xtsz_zcgl_cjpz_tsy).text




    # 设备类型
    def zh_xtsz_zcgl_cjpz_04(self):
        # 设备类型
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz_sblx))
        self.driver.find_element(*loc.zh_xtsz_zcgl_cjpz_sblx).click()
        time.sleep(1)
        # 设备类型下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz_sblxxl))
        self.driver.find_elements(*loc.zh_xtsz_zcgl_cjpz_sblxxl)[0].click()


    # 厂家名称
    def zh_xtsz_zcgl_cjpz_05(self,cjmc):
        # 厂家名称
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz_cjmc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_cjpz_cjmc).send_keys(cjmc)

    # 版本清除
    def zh_xtsz_zcgl_cjpz_06(self):
        # 版本
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz_bb))
        self.driver.find_element(*loc.zh_xtsz_zcgl_cjpz_bb).send_keys(Keys.BACKSPACE*8)



    # 版本输入
    def zh_xtsz_zcgl_cjpz_07(self,bb):
        # 版本
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz_bb))
        self.driver.find_element(*loc.zh_xtsz_zcgl_cjpz_bb).send_keys(bb)

    # 通讯方式
    def zh_xtsz_zcgl_cjpz_08(self, txfs):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz_txfs))
        self.driver.find_element(*loc.zh_xtsz_zcgl_cjpz_txfs).send_keys(txfs)



    # 脚本名称
    def zh_xtsz_zcgl_cjpz_09(self,jbmc):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz_jbmc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_cjpz_jbmc).send_keys(jbmc)



    #列表最后一个
    def zh_xtsz_zcgl_cjpz_010(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_cjpz_lb))
        self.driver.find_elements(*loc.zh_xtsz_zcgl_cjpz_lb)[-1].click()








