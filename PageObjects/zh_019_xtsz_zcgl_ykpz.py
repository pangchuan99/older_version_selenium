
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
class Test_zh_xtsz_zcgl_ykpz:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()


    #鼠标悬浮到资产管理 点击遥控配置
    def zh_xtsz_zcgl_ykpz(self):
        #资产管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_zcgl)).perform()
        #遥控配置
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz).click()


   #添加表达式
    def zh_xtsz_zcgl_ykpz_01(self):
        #添加表达式
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_tjbds))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz_tjbds).click()

    # 点击保存
    def zh_xtsz_zcgl_ykpz_02(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_bc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz_bc).click()

    # 提示语
    def zh_xtsz_zcgl_ykpz_tsy(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_tsy))
        return self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz_tsy).text

    # 设备类型
    def zh_xtsz_zcgl_ykpz_03(self):
        # 点击设备类型
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_sblx))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz_sblx).click()
        # 点击设备类型下拉框
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_sblxxl))
        self.driver.find_elements(*loc.zh_xtsz_zcgl_ykpz_sblxxl)[0].click()




    #状态
    def zh_xtsz_zcgl_ykpz_04(self):
        # 状态
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_zt))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz_zt).click()
        # 状态下拉框
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_ztxl))
        self.driver.find_elements(*loc.zh_xtsz_zcgl_ykpz_ztxl)[0].click()

     #版本清除
    def zh_xtsz_zcgl_ykpz_05(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_bb))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz_bb).send_keys(Keys.BACK_SPACE*8)

    #版本输入
    def zh_xtsz_zcgl_ykpz_06(self,bb):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_bb))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz_bb).send_keys(bb)




    #值清除
    def zh_xtsz_zcgl_ykpz_07(self):
        # 值
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_z))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz_z).clear()


    # 输入值
    def zh_xtsz_zcgl_ykpz_08(self,z):
        # 值
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_z))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz_z).send_keys(z)



    #列表点击最后一个
    def zh_xtsz_zcgl_ykpz_09(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_lbzhyg))
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_elements(*loc.zh_xtsz_zcgl_ykpz_lbzhyg)[-1])
        self.driver.find_elements(*loc.zh_xtsz_zcgl_ykpz_lbzhyg)[-1].click()


    #删除
    def zh_xtsz_zcgl_ykpz_010(self):
        # 删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_sc))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz_sc).click()

        # 删除弹出框 点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_sctck))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz_sctck).click()

    #上测---设备类型
    def zh_xtsz_zcgl_ykpz_011(self):
        # 上测---设备类型
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_sblxxz))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz_sblxxz).click()
        time.sleep(1)
        # 上测---设备类型下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_sblxxzxl))
        self.driver.find_elements(*loc.zh_xtsz_zcgl_ykpz_sblxxzxl)[1].click()

   #查询
    def zh_xtsz_zcgl_ykpz_012(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_zcgl_ykpz_cx))
        self.driver.find_element(*loc.zh_xtsz_zcgl_ykpz_cx).click()
