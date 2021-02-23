
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件

from selenium.webdriver.common.keys import Keys                                    #键盘输入
import time
class Test_zh_xtsz_zcgl_jczpz:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()


    #鼠标悬浮到资产列表点击检测值配置
    def zh_xtsz_zcgl_jczpz(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_zcgl)).perform()
        # 检测值配置
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz))
        self.driver.find_element(*loc.zh_xtsz_zcgl_jczpz).click()

   #添加配置
    def zh_xtsz_zcgl_jczpz_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz_tjpz))
        self.driver.find_element(*loc.zh_xtsz_zcgl_jczpz_tjpz).click()


    # 点击保存
    def zh_xtsz_zcgl_jczpz_02(self):

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz_bc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_jczpz_bc).click()

    #删除
    def zh_xtsz_zcgl_jczpz_03(self):
        # 删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz_sc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_jczpz_sc).click()
        # 删除弹出框
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz_sctck))
        self.driver.find_element(*loc.zh_xtsz_zcgl_jczpz_sctck).click()



    # 提示语---请选择设备类型
    def zh_xtsz_zcgl_jczpz_tsy(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz_tsy))
        return self.driver.find_element(*loc.zh_xtsz_zcgl_jczpz_tsy).text


    # 设备类型
    def zh_xtsz_zcgl_jczpz_04(self):
        # 设备类型
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz_sblx))
        self.driver.find_element(*loc.zh_xtsz_zcgl_jczpz_sblx).click()
        # 设备类型下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz_sblxxl))
        self.driver.find_elements(*loc.zh_xtsz_zcgl_jczpz_sblxxl)[0].click()


    # 清除版本
    def zh_xtsz_zcgl_jczpz_05(self):
        #清除版本
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz_bb))
        self.driver.find_element(*loc.zh_xtsz_zcgl_jczpz_bb).send_keys(Keys.BACK_SPACE*8)

    # 版本输入
    def zh_xtsz_zcgl_jczpz_06(self,bb):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz_bb))
        self.driver.find_element(*loc.zh_xtsz_zcgl_jczpz_bb).send_keys(bb)


    # 表达式
    def zh_xtsz_zcgl_jczpz_07(self,bds):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz_bds))
        self.driver.find_element(*loc.zh_xtsz_zcgl_jczpz_bds).send_keys(bds)



    #点击列表最后一个
    def zh_xtsz_zcgl_jczpz_08(self):
        # 点击列表最后一个
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz_lbzhyg))
        self.driver.find_elements(*loc.zh_xtsz_zcgl_jczpz_lbzhyg)[-1].click()


    # 删除
    def zh_xtsz_zcgl_jczpz_09(self):
        # 点击删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz_sc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_jczpz_sc).click()
        # 删除弹出框---点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_jczpz_sctck))
        self.driver.find_element(*loc.zh_xtsz_zcgl_jczpz_sctck).click()


