
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
class Test_zh_xtsz_lxrpz:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()



    # 鼠标悬浮---系统设置
    # 账户进行鼠标悬浮---系统设置,点击联系人配置
    def zh_xtsz_lxrpz(self):
        #点击系统设置
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz)).perform()
        # 点击联系人配置
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz))
        self.driver.find_element(*loc.zh_xtsz_lxrpz).click()








    #左侧点击添加
    def zh_xtsz_lxrpz_01(self):
        # 点击左侧添加
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zctj))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_zctj).click()

    #左侧类型-公司
    def zh_xtsz_lxrpz_02(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zclx))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_zclx).click()
        #类型下拉内容--公司
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zclxxl))
        self.driver.find_elements(*loc.zh_xtsz_lxrpz_zclxxl)[0].click()

    # 左侧名称
    def zh_xtsz_lxrpz_03(self,mc):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zcmc))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_zcmc).send_keys(mc)


    # 左侧保存
    def zh_xtsz_lxrpz_04(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zcbc))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_zcbc).click()

    # 左侧类型-部门
    def zh_xtsz_lxrpz_05(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zclx))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_zclx).click()
        # 类型下拉内容---部门
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zclxxl))
        self.driver.find_elements(*loc.zh_xtsz_lxrpz_zclxxl)[1].click()

    # 左侧公司-公司
    def zh_xtsz_lxrpz_06(self):
        #公司
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zcgs))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_zcgs).click()
        # 公司下拉内容选择最后一个
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zcgsxl))
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_elements(*loc.zh_xtsz_lxrpz_zcgsxl)[-1])
        self.driver.find_elements(*loc.zh_xtsz_lxrpz_zcgsxl)[-1].click()


    # 左侧名称进行清空
    def zh_xtsz_lxrpz_07(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zcmc))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_zcmc).clear()



    # 点击保存提示语是 ---添加成功
    def zh_xtsz_lxrpz_08(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_tsy))
        return self.driver.find_element(*loc.zh_xtsz_lxrpz_tsy).text


    #左侧选择选择一个
    def zh_xtsz_lxrpz_09(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zclbzhyg))
        self.driver.find_elements(*loc.zh_xtsz_lxrpz_zclbzhyg)[-1].click()

    #删除
    def zh_xtsz_lxrpz_010(self):
        #点击删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zcsc))
        self.driver.find_elements(*loc.zh_xtsz_lxrpz_zcsc).click()
        #删除弹出框点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zcsctck))
        self.driver.find_elements(*loc.zh_xtsz_lxrpz_zcsctck).click()




     #点击添加新成员-
    def zh_xtsz_lxrpz_011(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_tjxcy))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_tjxcy).click()



    # 点击保存
    def zh_xtsz_lxrpz_012(self):

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_bc))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_bc).click()


    #点击保存提示语是 公司、部门、电话和名字为必填
    def zh_xtsz_lxrpz_013(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_tsy))
        return self.driver.find_element(*loc.zh_xtsz_lxrpz_tsy).text




    #输入姓名--
    def zh_xtsz_lxrpz_014(self,xm):
        # 姓名
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_xm))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_xm).send_keys(xm)






    # 性别---
    def zh_xtsz_lxrpz_015(self):
        # 性别
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_xb))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_xb).click()
        # 性别下拉框
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_xbxl))
        self.driver.find_elements(*loc.zh_xtsz_lxrpz_xbxl)[0].click()


    # 电话
    def zh_xtsz_lxrpz_016(self,dh):
        #电话
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_dh))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_dh).send_keys(dh)







    # 公司--
    def zh_xtsz_lxrpz_017(self):
        #公司
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_gs))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_gs).click()
        # 公司下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_gsxl))
        self.driver.execute_script("arguments[0].scrollIntoView(false);", self.driver.find_elements(*loc.zh_xtsz_lxrpz_gsxl)[-1])
        self.driver.find_elements(*loc.zh_xtsz_lxrpz_gsxl)[-1].click()




    # 部门-
    def zh_xtsz_lxrpz_018(self):
        #部门
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_bm))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_bm).click()
        # 部门下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_bmxl))
        self.driver.execute_script("arguments[0].scrollIntoView(false);", self.driver.find_elements(*loc.zh_xtsz_lxrpz_bmxl)[-1])
        self.driver.find_elements(*loc.zh_xtsz_lxrpz_bmxl)[-1].click()

    # 职位
    def zh_xtsz_lxrpz_019(self,zw):

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zw))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_zw).send_keys(zw)




    # 列表点击最后一个
    def zh_xtsz_lxrpz_020(self):
        # 列表最后一个
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_lbzhyg))
        self.driver.find_elements(*loc.zh_xtsz_lxrpz_lbzhyg)[-1].click()

    # 修改姓名
    def zh_xtsz_lxrpz_021(self,xm):
        # 姓名清除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_xm))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_xm).clear()
        #姓名
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_xm))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_xm).send_keys(xm)



    # 删除
    def zh_xtsz_lxrpz_022(self):

        # 点击删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_sc))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_sc).click()
        # 点击删除弹出框点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_sctck))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_sctck).click()






    # 左侧列表点击最后一个
    def zh_xtsz_lxrpz_023(self):
        # 点击左侧列表最后一个
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zclbzhyg))
        self.driver.find_elements(*loc.zh_xtsz_lxrpz_zclbzhyg)[-1].click()




    #左侧 删除
    def zh_xtsz_lxrpz_024(self):
        # 点击删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zcsc))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_zcsc).click()

        # 点击删除弹出框--点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_zcsctck))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_zcsctck).click()




    # 姓名搜索框
    def zh_xtsz_lxrpz_025(self,xm):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_xmssk))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_xmssk).send_keys(xm)


   # 查询
    def zh_xtsz_lxrpz_026(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_cx))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_cx).click()




    # 姓名搜索框清除
    def zh_xtsz_lxrpz_027(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_xmssk))
        self.driver.find_element(*loc.zh_xtsz_lxrpz_xmssk).clear()



    #单独的提示语----删除成功
    def zh_xtsz_lxrpz_028(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lxrpz_tsysccg))
        return self.driver.find_element(*loc.zh_xtsz_lxrpz_tsysccg).text



