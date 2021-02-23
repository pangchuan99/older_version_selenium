
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
class Test_zh_xtsz_zcgl_ztbds:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()


    #鼠标悬浮资产管理点击状态表达式
    def zh_xtsz_zcgl_ztbds(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_zcgl)).perform()
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ztbds).click()

   #添加表达式
    def zh_xtsz_zcgl_ztbds_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_tjbds))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ztbds_tjbds).click()



    # 点击保存
    def zh_xtsz_zcgl_ztbds_02(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_bc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ztbds_bc).click()

    #删除
    def zh_xtsz_zcgl_ztbds_03(self):
        # 删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_sc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ztbds_sc).click()
        #点击删除 弹出框点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_sctck))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ztbds_sctck).click()

    # 提示语
    def zh_xtsz_zcgl_ztbds_tsy(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_lxbj_tsy))
        return self.driver.find_element(*loc.zh_xtsz_zcgl_lxbj_tsy).text






    # 设备类型选择
    def zh_xtsz_zcgl_ztbds_04(self):
        # 设备类型
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_sblx))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ztbds_sblx).click()
        time.sleep(1)
        # 设备类型下拉框
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_sblxxl))
        self.driver.find_elements(*loc.zh_xtsz_zcgl_ztbds_sblxxl)[0].click()



   # 状态选择
    def zh_xtsz_zcgl_ztbds_05(self):
        #状态
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_zt))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ztbds_zt).click()
        time.sleep(1)
        # 状态下拉框
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_ztxl))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ztbds_ztxl).click()


    # 版本清空
    def zh_xtsz_zcgl_ztbds_06(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_bb))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ztbds_bb).send_keys(Keys.BACKSPACE*8)

    # 版本输入
    def zh_xtsz_zcgl_ztbds_07(self,bb):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_bb))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ztbds_bb).send_keys(bb)



     # 表达式输入
    def zh_xtsz_zcgl_ztbds_08(self,bds):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_bds))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ztbds_bds).send_keys(bds)




     #分页
    def zh_xtsz_zcgl_ztbds_09(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_fy))
        self.driver.find_elements(*loc.zh_xtsz_zcgl_ztbds_fy)[-2].click()

    # 列表最后一个
    def zh_xtsz_zcgl_ztbds_010(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_lb))
        self.driver.find_elements(*loc.zh_xtsz_zcgl_ztbds_lb)[-1].click()


    # 点击删除
    def zh_xtsz_zcgl_ztbds_011(self):
        #点击删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_sc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ztbds_sc).click()
        # 点击删除弹出框--点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ztbds_sctck))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ztbds_sctck).click()











