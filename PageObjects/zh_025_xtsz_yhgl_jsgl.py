
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
class Test_zh_xtsz_yhgl_jsgl:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    # 鼠标悬浮到用户管理---点击角色管理
    def zh_xtsz_jsgl(self):
        #输入悬浮到用户管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_yhgl)).perform()
        time.sleep(1)
        # 点击角色管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_jsgl))
        self.driver.find_element(*loc.zh_xtsz_yhgl_jsgl).click()


    # 提示语
    def zh_xtsz_yhgl_jsgl_tsy(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_jsgl_tsy))
        return self.driver.find_element(*loc.zh_xtsz_yhgl_jsgl_tsy).text



   #添加新角色
    def zh_xtsz_yhgl_jsgl_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_jsgl_tjxjs))
        self.driver.find_element(*loc.zh_xtsz_yhgl_jsgl_tjxjs).click()

    # 保存
    def zh_xtsz_yhgl_jsgl_02(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_jsgl_bc))
        self.driver.find_element(*loc.zh_xtsz_yhgl_jsgl_bc).click()





   #输入角色名
    def zh_xtsz_yhgl_jsgl_03(self,jsm):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_jsgl_jsm))
        self.driver.find_element(*loc.zh_xtsz_yhgl_jsgl_jsm).send_keys(jsm)


    # 角色名清除
    def zh_xtsz_yhgl_jsgl_04(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_jsgl_jsm))
        self.driver.find_element(*loc.zh_xtsz_yhgl_jsgl_jsm).clear()


    #类型
    def zh_xtsz_yhgl_jsgl_05(self):
        # 类型
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_jsgl_lx))
        self.driver.find_element(*loc.zh_xtsz_yhgl_jsgl_lx).click()
        # 类型下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_jsgl_lxxl))
        self.driver.find_elements(*loc.zh_xtsz_yhgl_jsgl_lxxl)[-1].click()

    #权限
    def zh_xtsz_yhgl_jsgl_06(self):
        # 选择权限
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_jsgl_qx))
        self.driver.find_elements(*loc.zh_xtsz_yhgl_jsgl_qx)[1].click()



    #列表最后一个
    def zh_xtsz_yhgl_jsgl_07(self):
        # 列表点击最后一个
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_jsgl_lb))
        self.driver.execute_script("arguments[0].scrollIntoView(false);", self.driver.find_elements(*loc.zh_xtsz_yhgl_jsgl_lb)[-1])
        self.driver.find_elements(*loc.zh_xtsz_yhgl_jsgl_lb)[-1].click()



    # 点击删除
    def zh_xtsz_yhgl_jsgl_08(self):
        # 删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_jsgl_sc))
        self.driver.find_element(*loc.zh_xtsz_yhgl_jsgl_sc).click()
        # 删除弹出框
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_jsgl_sc_tck))
        self.driver.find_element(*loc.zh_xtsz_yhgl_jsgl_sc_tck).click()





