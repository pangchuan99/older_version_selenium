
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
class Test_zh_xtsz_clya_yabj:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    # 输入悬浮到策略预案---点击预案编辑
    def zh_xtsz_clya_yabj(self):
        #输入悬浮到策略预案
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_clya)).perform()
        time.sleep(1)
        # 进行点击预案编辑
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj).click()


   #点击 +
    def zh_xtsz_clya_yabj_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_tj))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_tj).click()


    # 点击保存
    def zh_xtsz_clya_yabj_02(self):

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_bc))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_bc).click()

    # 提示语
    def zh_xtsz_clya_yabj_tsy(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_tsy))
        return self.driver.find_element(*loc.zh_xtsz_clya_yabj_tsy).text





    #输入名称
    def zh_xtsz_clya_yabj_03(self,mc):
        #名称
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_mc))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_mc).send_keys(mc)



    # 类型
    def zh_xtsz_clya_yabj_04(self):
        # 类型
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_lx))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_lx).click()
        time.sleep(1)
        # 类型下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_lxxl))
        self.driver.execute_script("arguments[0].scrollIntoView(false);", self.driver.find_elements(*loc.zh_xtsz_clya_yabj_lxxl)[-1])
        self.driver.find_elements(*loc.zh_xtsz_clya_yabj_lxxl)[-1].click()






    # 影响区域
    def zh_xtsz_clya_yabj_05(self):
        #影响区域
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_ysqy))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_ysqy).click()
        # 影响区域下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_ysqyxl))
        self.driver.find_elements(*loc.zh_xtsz_clya_yabj_ysqyxl)[4].click()

    # 列表最后一个
    def zh_xtsz_clya_yabj_06(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_lbzhyg))
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_elements(*loc.zh_xtsz_clya_yabj_lbzhyg)[-1])
        time.sleep(1.5)
        self.driver.find_elements(*loc.zh_xtsz_clya_yabj_lbzhyg)[-1].click()

    # 点击下侧+
    def zh_xtsz_clya_yabj_07(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xctj))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xctj).click()

    # 下侧 选择类型
    def zh_xtsz_clya_yabj_08(self):
        # 下侧 选择类型
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xcxzlx))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xcxzlx).click()
        # 下侧 选择类型下拉内容（双面车道指示器）
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xcxzlx))
        self.driver.execute_script("arguments[0].scrollIntoView(false);", self.driver.find_element(*loc.zh_xtsz_clya_yabj_xcxzlxxl))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xcxzlxxl).click()

    # 下侧弹出框点击全选
    def zh_xtsz_clya_yabj_09(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xctckqx))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xctckqx).click()


    # 点击绑定
    def zh_xtsz_clya_yabj_010(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xcbd))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xcbd).click()

    # 点击下侧全选
    def zh_xtsz_clya_yabj_011(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xcqx))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xcqx).click()

    # 优先级清除
    def zh_xtsz_clya_yabj_012(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xcyxj))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xcyxj).clear()

    # 优先级输入
    def zh_xtsz_clya_yabj_013(self,yxj):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xcyxj))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xcyxj).send_keys(yxj)

    # 间隔清除
    def zh_xtsz_clya_yabj_014(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xcjg))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xcjg).clear()

    # 间隔输入
    def zh_xtsz_clya_yabj_015(self,jg):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xcjg))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xcjg).send_keys(jg)


    # 是否确认
    def zh_xtsz_clya_yabj_016(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xcsfqr))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xcsfqr).click()

    #选择双面车道指示器
    def zh_xtsz_clya_yabj_017(self):
        # 选择双面车道指示器
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xcsmcdzsq))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xcsmcdzsq).click()
        # 选择双面车道指示器下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xcsmcdzsqxl))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xcsmcdzsqxl).click()


    # 下侧保存.
    def zh_xtsz_clya_yabj_018(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xcbc))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xcbc).click()



    #下侧列表点击最后一个
    def zh_xtsz_clya_yabj_019(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xclbzhyg))
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_element(*loc.zh_xtsz_clya_yabj_xclbzhyg))
        time.sleep(1)
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xclbzhyg).click()



    # 下侧  （—）
    def zh_xtsz_clya_yabj_020(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xczcsc))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xczcsc).click()




    # 删除弹出框
    def zh_xtsz_clya_yabj_022(self):
        #删除弹出框
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_sctck))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_sctck).click()


   #取消
    def zh_xtsz_clya_yabj_023(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_qx))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_qx).click()

    #删除  -
    def zh_xtsz_clya_yabj_024(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_sc))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_sc).click()


   #名称清除
    def zh_xtsz_clya_yabj_025(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_mc))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_mc).clear()




   #修改
    def zh_xtsz_clya_yabj_026(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_xg))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_xg).click()



   #搜索框
    def zh_xtsz_clya_yabj_027(self,ssk):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_ssk))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_ssk).send_keys(ssk)

    # 搜索框清除
    def zh_xtsz_clya_yabj_028(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_ssk))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_ssk).clear()

   #搜索框确定
    def zh_xtsz_clya_yabj_029(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_sskqd))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_sskqd).click()


  #搜索框键盘回车
    def zh_xtsz_clya_yabj_030(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_ssk))
        self.driver.find_element(*loc.zh_xtsz_clya_yabj_ssk).send_keys(Keys.ENTER)
