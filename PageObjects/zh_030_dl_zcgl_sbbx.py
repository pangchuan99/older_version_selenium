
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
class Test_zcgl_sbbx:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    def dl_zcgl(self):
        #输入悬浮到资产管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.dl_zcgl)).perform()
        time.sleep(1)
        # 点击设备报修
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx))
        self.driver.find_element(*loc.dl_zcgl_xbbx).click()


    # 提示语---
    def dl_zcgl_xbbx_tsy(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.dl_zcgl_tsy))
        return self.driver.find_element(*loc.dl_zcgl_tsy).text


    #报修工单
    def dl_zcgl_xbbx_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_jl_sb))
        self.driver.find_elements(*loc.dl_zcgl_xbbx_gd_jl_sb)[1].click()



    #报修工单---添加报修
    def dl_zcgl_xbbx_02(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_tjbx))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_tjbx).click()


    #报修工单---报修原因搜索框
    def dl_zcgl_xbbx_03(self,bxyy):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_bxyyssk))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_bxyyssk).send_keys(bxyy)

    # 报修工单---报修原因搜索框---清除
    def dl_zcgl_xbbx_08(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_bxyyssk))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_bxyyssk).clear()

    # 报修工单---查询
    def dl_zcgl_xbbx_04(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_cx))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_cx).click()



    # 报修工单---删除
    def dl_zcgl_xbbx_05(self):
        #删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_sc))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_sc).click()
        # 删除弹出框点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_sctck))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_sctck).click()



    # 报修工单---保存
    def dl_zcgl_xbbx_06(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_bc))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_bc).click()


    # 报修工单---完成
    def dl_zcgl_xbbx_07(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_wc))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_wc).click()




    # 报修工单---设备名称
    def dl_zcgl_xbbx_09(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_sbmc))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_sbmc).click()



 # 报修工单---设备类型
    def dl_zcgl_xbbx_010(self):
        #设备类型
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_sblx))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_sblx).click()
        # 设备类型下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_sblx_xl))
        self.driver.find_elements(*loc.dl_zcgl_xbbx_gd_sblx_xl)[1].click()



# 报修工单---设备名称--设备名称
    def dl_zcgl_xbbx_011(self):
        #设备名称
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_sbmcsbmc))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_sbmcsbmc).click()
        # 设备名称下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_sbmcsbmc_xl))
        self.driver.execute_script("arguments[0].scrollIntoView(false);", self.driver.find_elements(*loc.dl_zcgl_xbbx_gd_sbmcsbmc_xl)[-1])
        self.driver.find_elements(*loc.dl_zcgl_xbbx_gd_sbmcsbmc_xl)[-1].click()


   # 报修工单---确定
    def dl_zcgl_xbbx_012(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_qd))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_qd).click()



    # 报修工单---报修原因清除
    def dl_zcgl_xbbx_013(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_bxyy))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_bxyy).clear()

    # 报修工单---报修原因输入
    def dl_zcgl_xbbx_014(self,bxyy):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_bxyy))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_bxyy).send_keys(bxyy)




  # 报修工单---报修人员清除
    def dl_zcgl_xbbx_015(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_bxry))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_bxry).clear()

    # 报修工单---报修人员输入
    def dl_zcgl_xbbx_016(self,bxry):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_bxry))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_bxry).send_keys(bxry)



  # 报修工单---报修时间
    def dl_zcgl_xbbx_017(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_bxsj))
        self.driver.find_element(*loc.dl_zcgl_xbbx_gd_bxsj).click()




  # 报修工单---列表最后一个
    def dl_zcgl_xbbx_018(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zcgl_xbbx_gd_lb))
        self.driver.find_elements(*loc.dl_zcgl_xbbx_gd_lb)[-1].click()

