
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
class Test_zh_xtsz_clya_clbj:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    # 鼠标悬浮到策略预案  点击策略编辑
    def zh_xtsz_clya_clbj(self):
        #输入悬浮到策略预案
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz_clya)).perform()
        time.sleep(1)
        # 进行点击策略编辑
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj).click()


   #添加新策略
    def zh_xtsz_clya_clbj_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_tjclbj))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_tjclbj).click()

    # 保存
    def zh_xtsz_clya_clbj_02(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_bc))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_bc).click()

    # 取消
    def zh_xtsz_clya_clbj_03(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_qx))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_qx).click()


    # 提示语
    def zh_xtsz_clya_clbj_tsy(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_yabj_tsy))
        return self.driver.find_element(*loc.zh_xtsz_clya_yabj_tsy).text



     #输入名称
    def zh_xtsz_clya_clbj_04(self,mc):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_mc))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_mc).send_keys(mc)

     #名称清除
    def zh_xtsz_clya_clbj_024(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_mc))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_mc).clear()




     #类型
    def zh_xtsz_clya_clbj_05(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_lx))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_lx).click()


    # 类型下拉---选择程序自动策略
    def zh_xtsz_clya_clbj_06(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_lxxl))
        self.driver.find_elements(*loc.zh_xtsz_clya_clbj_lxxl)[1].click()




   #分组
    def zh_xtsz_clya_clbj_07(self):
        #分组
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_fz))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_fz).click()
        # 分组下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_fzxl))
        self.driver.execute_script("arguments[0].scrollIntoView(false);", self.driver.find_elements(*loc.zh_xtsz_clya_clbj_fzxl)[1])
        self.driver.find_elements(*loc.zh_xtsz_clya_clbj_fzxl)[1].click()





    #影响区域
    def zh_xtsz_clya_clbj_08(self):
        #影响区域
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_ysqy))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_ysqy).click()
        time.sleep(1)
        #影响区域下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_ysqyxl))
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_elements(*loc.zh_xtsz_clya_clbj_ysqyxl)[-1])
        self.driver.find_elements(*loc.zh_xtsz_clya_clbj_ysqyxl)[-1].click()



    #搜索框输入
    def zh_xtsz_clya_clbj_09(self,ssk):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_ssk))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_ssk).send_keys(ssk)

    #搜索框清除
    def zh_xtsz_clya_clbj_010(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_ssk))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_ssk).clear()

    # 搜索框确定
    def zh_xtsz_clya_clbj_011(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_sskqd))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_sskqd).click()

    #列表最后一个
    def zh_xtsz_clya_clbj_012(self):
        #列表最后一个进行点击
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_lbzhyg))
        self.driver.find_elements(*loc.zh_xtsz_clya_clbj_lbzhyg)[-1].click()


    #点击关预案
    def zh_xtsz_clya_clbj_013(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_glya))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_glya).click()

    # 关联预案最后一个
    def zh_xtsz_clya_clbj_014(self):

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_glyazhyg))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_glyazhyg).click()

    #点击确定
    def zh_xtsz_clya_clbj_015(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_qd))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_qd).click()


    # 编辑
    def zh_xtsz_clya_clbj_016(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_bj))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_bj).click()


    # 删除
    def zh_xtsz_clya_clbj_017(self):
        # 删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_sc))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_sc).click()
        # 删除弹出框
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_sctck))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_sctck).click()


    # 类型下拉---选择时间自动策略
    def zh_xtsz_clya_clbj_018(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_lxxl))
        self.driver.find_elements(*loc.zh_xtsz_clya_clbj_lxxl)[0].click()


    # 时间保存
    def zh_xtsz_clya_clbj_019(self):
        # 时间保存
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_sjbc))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_sjbc).click()


     #触发周期
    def zh_xtsz_clya_clbj_020(self):
        # 触发周期
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_cfzq))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_cfzq).click()
        # 触发周期下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_cfzqxl))
        self.driver.find_elements(*loc.zh_xtsz_clya_clbj_cfzqxl)[0].click()


     #触发时间
    def zh_xtsz_clya_clbj_021(self,cfsj):

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_cfsj))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_cfsj).send_keys(Keys.BACKSPACE*10)
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_cfsj).send_keys(cfsj)



     #选择时间范围  ---开始
    def zh_xtsz_clya_clbj_022(self,k1):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_xzsjfwks))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_xzsjfwks).send_keys(k1)



  #选择时间范围  --结束
    def zh_xtsz_clya_clbj_023(self,k2):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_xzsjfwjs))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_xzsjfwjs).send_keys(k2)


    #选择时间范围  ---开始----删除
    def zh_xtsz_clya_clbj_025(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_xzsjfwks_sc))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_xzsjfwks_sc).click()

    #选择时间范围  ---结束----删除
    def zh_xtsz_clya_clbj_026(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_xzsjfwjs_sc))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_xzsjfwjs_sc).click()


    #二级分类
    def zh_xtsz_clya_clbj_028(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_ejfl))
        self.driver.find_element(*loc.zh_xtsz_clya_clbj_ejfl).click()
        time.sleep(2)
        # 二级分类下拉
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_clya_clbj_ejflxl))
        self.driver.find_elements(*loc.zh_xtsz_clya_clbj_ejflxl)[0].click()






