
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件
import time
class Test_zh_xtsz_lkpz:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()



    # 鼠标悬浮---系统设置
    # 账户进行鼠标悬浮---系统设置,点击路况配置
    def zh_xtsz_lkpz(self):
        #点击系统设置
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz)).perform()
        # 点击路况配置
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz))
        self.driver.find_element(*loc.zh_xtsz_lkpz).click()



     #点击添加配置--选择图标类型点击保存
    def zh_xtsz_lkpz_01(self):
        #点击添加配置
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tjpz))
        self.driver.find_element(*loc.zh_xtsz_lkpz_tjpz).click()

    # 点击保存
    def zh_xtsz_lkpz_02(self):
        #点击保存
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_bc))
        self.driver.find_element(*loc.zh_xtsz_lkpz_bc).click()
    #提示语
    def zh_xtsz_lkpz_03(self):
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tsy))
            return self.driver.find_element(*loc.zh_xtsz_lkpz_tsy).text



    # 选择图标类型
    def zh_xtsz_lkpz_04(self):
        #图标类型
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tb))
        self.driver.find_elements(*loc.zh_xtsz_lkpz_tb)[0].click()
        #点击图标下拉内容
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tbxl))
        self.driver.find_element(*loc.zh_xtsz_lkpz_tbxl).click()



    # 事件类型
    def zh_xtsz_lkpz_05(self):

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_sj))
        self.driver.find_elements(*loc.zh_xtsz_lkpz_sj)[0].click()
        # 点击事件类型下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_sjxlxl))
        self.driver.find_elements(*loc.zh_xtsz_lkpz_sjxlxl)[1].click()




    # 事件等级
    def zh_xtsz_lkpz_06(self):

        #事件等级
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_sjdj))
        self.driver.find_elements(*loc.zh_xtsz_lkpz_sjdj)[0].click()
        # 点击事件等级下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_sjdjxl))
        self.driver.find_elements(*loc.zh_xtsz_lkpz_sjdjxl)[-1].click()






    #
    # # 点击添加配置--选择图标类型 事件类型点击保存
    # def zh_xtsz_lkpz_tb_sjlx(self):
    #     # 点击添加配置
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tjpz))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_tjpz).click()
    #     # 点击图标
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tb))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_tb).click()
    #     # 点击图标下拉内容
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tbxl))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_tbxl).click()
    #     # 点击事件类型
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_sj))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_sj).click()
    #     # 点击事件下拉内容
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_sjxl))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_sjxl).click()
    #     # 点击保存
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_bc))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_bc).click()
    # #验证提示语  请选择事件类型
    # def zh_xtsz_lkpz_tsy3(self):
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tsy))
    #     return self.driver.find_element(*loc.zh_xtsz_lkpz_tsy).text




    #
    #
    #  # 点击添加配置--选择图标类型 事件类型 事件等级 点击保存
    # def zh_xtsz_lkpz_all(self):
    #     # 点击添加配置
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tjpz))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_tjpz).click()
    #     # 点击图标
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tb))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_tb).click()
    #     # 点击图标下拉内容
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tbxl))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_tbxl).click()
    #     # 点击事件类型
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_sj))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_sj).click()
    #     # 点击事件下拉内容
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_sjxl))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_sjxl).click()
    #     # 点击事件等级
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_sjdj))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_sjdj).click()
    #     # 点击事件等级下拉
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_sjdjxl))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_sjdjxl).click()
    #
    #     # 点击保存
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_bc))
    #     self.driver.find_element(*loc.zh_xtsz_lkpz_bc).click()
    # #验证提示语---路况配置已存在
    # def zh_xtsz_lkpz_tsy4(self):
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tsy))
    #     return self.driver.find_element(*loc.zh_xtsz_lkpz_tsy).text
    #
    #
    #
