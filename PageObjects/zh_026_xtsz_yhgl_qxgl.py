
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
class Test_zh_xtsz_yhgl_qxgl:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()


    # 输入悬浮到用户管理---点击权限管理
    def zh_xtsz_qxgl(self):
        #输入悬浮到用户管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_yhgl)).perform()
        time.sleep(1)
        # 点击权限管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_qxgl))
        self.driver.find_element(*loc.zh_xtsz_yhgl_qxgl).click()


    # 提示语-
    def zh_xtsz_yhgl_qxgl_tsy(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_jsgl_tsy))
        return self.driver.find_element(*loc.zh_xtsz_yhgl_jsgl_tsy).text

   #添加新权限
    def zh_xtsz_yhgl_qxgl_01(self):
        #点击 添加新权限
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_qxgl_tjxqx))
        self.driver.find_element(*loc.zh_xtsz_yhgl_qxgl_tjxqx).click()


    # 点击保存
    def zh_xtsz_yhgl_qxgl_02(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_qxgl_bc))
        self.driver.find_element(*loc.zh_xtsz_yhgl_qxgl_bc).click()


    #删除
    def zh_xtsz_yhgl_qxgl_03(self):
        # 删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_qxgl_sc))
        self.driver.find_element(*loc.zh_xtsz_yhgl_qxgl_sc).click()
        # 删除弹出框点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_qxgl_sctck))
        self.driver.find_element(*loc.zh_xtsz_yhgl_qxgl_sctck).click()




   #输入权限代码
    def zh_xtsz_yhgl_qxgl_04(self,qxdm):
        #权限代码
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_qxgl_qxdm))
        self.driver.find_element(*loc.zh_xtsz_yhgl_qxgl_qxdm).send_keys(qxdm)

    # 清除权限代码
    def zh_xtsz_yhgl_qxgl_05(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_qxgl_qxdm))
        self.driver.find_element(*loc.zh_xtsz_yhgl_qxgl_qxdm).clear()


    # 输入权限名称
    def zh_xtsz_yhgl_qxgl_06(self,qxmc):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_qxgl_qxmc))
        self.driver.find_element(*loc.zh_xtsz_yhgl_qxgl_qxmc).send_keys(qxmc)


    # 清除权限名称
    def zh_xtsz_yhgl_qxgl_07(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_qxgl_qxmc))
        self.driver.find_element(*loc.zh_xtsz_yhgl_qxgl_qxmc).clear()




    #列表最后一个
    def zh_xtsz_yhgl_qxgl_08(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_qxgl_lb))
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_elements(*loc.zh_xtsz_yhgl_qxgl_lb)[-1])
        self.driver.find_elements(*loc.zh_xtsz_yhgl_qxgl_lb)[-1].click()



