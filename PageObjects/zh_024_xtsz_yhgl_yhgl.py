
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
class Test_zh_xtsz_yhgl_yhgl:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    # 输入悬浮到用户管理---点击用户管理
    def zh_xtsz_yhgl(self):
        #输入悬浮到用户管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_yhgl)).perform()
        time.sleep(1)
        # 点击用户管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl))
        self.driver.find_element(*loc.zh_xtsz_yhgl_yhgl).click()

    # 提示语
    def zh_xtsz_yhgl_yhgl_tsy(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_tsy))
        return self.driver.find_element(*loc.zh_xtsz_yhgl_yhgl_tsy).text

   #点击添加新用户
    def zh_xtsz_yhgl_yhgl_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_tjxyh))
        self.driver.find_element(*loc.zh_xtsz_yhgl_yhgl_tjxyh).click()


    # 账号搜索框--输入
    def zh_xtsz_yhgl_yhgl_02(self,zh):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_zhssk))
        self.driver.find_element(*loc.zh_xtsz_yhgl_yhgl_zhssk).send_keys(zh)

    # 账号搜索框--清除
    def zh_xtsz_yhgl_yhgl_03(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_zhssk))
        self.driver.find_element(*loc.zh_xtsz_yhgl_yhgl_zhssk).clear()

    # 查询
    def zh_xtsz_yhgl_yhgl_04(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_cx))
        self.driver.find_element(*loc.zh_xtsz_yhgl_yhgl_cx).click()

    #保存
    def zh_xtsz_yhgl_yhgl_05(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_bc))
        self.driver.find_element(*loc.zh_xtsz_yhgl_yhgl_bc).click()


    #删除
    def zh_xtsz_yhgl_yhgl_06(self):
        # 删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_sc))
        self.driver.find_element(*loc.zh_xtsz_yhgl_yhgl_sc).click()
        # 删除弹出框点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_sctck))
        self.driver.find_element(*loc.zh_xtsz_yhgl_yhgl_sctck).click()



    #账号
    def zh_xtsz_yhgl_yhgl_07(self,zh):
        #账号
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_zh))
        self.driver.find_element(*loc.zh_xtsz_yhgl_yhgl_zh).send_keys(zh)


    #角色
    def zh_xtsz_yhgl_yhgl_08(self):
        #角色
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_js))
        self.driver.find_element(*loc.zh_xtsz_yhgl_yhgl_js).click()
        # 角色下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_jsxl))
        self.driver.find_elements(*loc.zh_xtsz_yhgl_yhgl_jsxl)[0].click()





    # 输入姓名
    def zh_xtsz_yhgl_yhgl_09(self,xm):
        # 姓名
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_xm))
        self.driver.find_element(*loc.zh_xtsz_yhgl_yhgl_xm).send_keys(xm)




   #列表最后一个
    def zh_xtsz_yhgl_yhgl_010(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_lb))
        self.driver.find_elements(*loc.zh_xtsz_yhgl_yhgl_lb)[-1].click()



    # 姓名清除
    def zh_xtsz_yhgl_yhgl_011(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yhgl_yhgl_xm))
        self.driver.find_element(*loc.zh_xtsz_yhgl_yhgl_xm).clear()



