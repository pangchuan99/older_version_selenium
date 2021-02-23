
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
class Test_zbgl_pbgl:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    def dl_zbgl_pbgl(self):
        #输入悬浮到值班管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.dl_zbgl)).perform()
        time.sleep(1)
        # 点击排班管理
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl))
        self.driver.find_element(*loc.dl_zbgl_pbgl).click()


    # 提示语---
    def dl_zbgl_pbgl_01(self):

        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_tsy))
        return self.driver.find_element(*loc.dl_zbgl_pbgl_tsy).text

    #班组---左侧---班组
    def dl_zbgl_pbgl_02(self):
        # 点击班组
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bpjl))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bpjl).click()

    # 班组---左侧--班组里面进行点击-----添加
    def dl_zbgl_pbgl_03(self):
        # 点击班组
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_zj))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_zj).click()


    # 班组---左侧--班组里面进行点击添加后--弹出框--- 输入名称
    def dl_zbgl_pbgl_04(self,qsrbzmc):
        # 点击班组
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_qsrbzmc))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_qsrbzmc).send_keys(qsrbzmc)

    # 班组---左侧--班组里面进行点击添加后--弹出框--- 输入名称--点击确定
    def dl_zbgl_pbgl_05(self):
        # 点击班组
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_qd))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_qd).click()



    # 班组---点击添加新组员
    def dl_zbgl_pbgl_06(self):
        # 点击班组
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_tjxzy))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_tjxzy).click()


    # 班组---点击保存
    def dl_zbgl_pbgl_07(self):
        # 点击班组
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_bc))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_bc).click()

     #班组---班组
    def dl_zbgl_pbgl_08(self):
        # 班组
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_bz))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_bz).click()

    #班组--- 班组下拉内容(取最后一个)
    def dl_zbgl_pbgl_09(self):
        # 班组
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_bzxl))
        self.driver.find_elements(*loc.dl_zbgl_pbgl_bz_bzxl)[-1].click()


    # 班组---姓名
    def dl_zbgl_pbgl_010(self):
        # 姓名
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_xm))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_xm).click()

    # 班组---姓名下拉内容(取第一个)
    def dl_zbgl_pbgl_011(self):
        # 姓名下拉内容
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_xmxl1))
        self.driver.execute_script("arguments[0].scrollIntoView(false);", self.driver.find_element(*loc.dl_zbgl_pbgl_bz_xmxl1))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_xmxl1).click()



    #班组---添加新组员列表取最后一个
    def dl_zbgl_pbgl_012(self):
        # 添加新组员列表取最后一个
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_tjxzylb))
        self.driver.find_elements(*loc.dl_zbgl_pbgl_bz_tjxzylb)[-1].click()



    #班组---备注
    def dl_zbgl_pbgl_013(self,bzbz):
        #备注
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_bzbz))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_bzbz).send_keys(bzbz)


    #班组---删除
    def dl_zbgl_pbgl_014(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_sc))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_sc).click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_sctck))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_sctck).click()



    # 班组---左侧列表取最后一个---进行双击点击
    def dl_zbgl_pbgl_015(self,mc):
        #左侧列表取最后一个
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbglbz_zcbzlbzhyg))
        self.driver.find_element(*loc.dl_zbgl_pbglbz_zcbzlbzhyg).click()
        time.sleep(4)
        ActionChains(self.driver).double_click(self.driver.find_element(*loc.dl_zbgl_pbglbz_zcbzlbzhyg)).perform()
        time.sleep(4)
        ActionChains(self.driver).double_click(self.driver.find_element(*loc.dl_zbgl_pbglbz_zcbzlbzhyg)).perform()
        time.sleep(4)
        self.driver.find_element(*loc.dl_zbgl_pbglbz_zcbzlbzhyg).click()
        time.sleep(4)
        self.driver.find_element(*loc.dl_zbgl_pbglbz_zcbzlbzhyg).clear()
        time.sleep(4)
        self.driver.find_element(*loc.dl_zbgl_pbglbz_zcbzlbzhyg).send_keys(Keys.CONTROL,'a')
        time.sleep(4)
        self.driver.find_element(*loc.dl_zbgl_pbglbz_zcbzlbzhyg).send_keys(mc)


    #班组---点击最后一个进行选择
    def dl_zbgl_pbgl_016(self):
        # 点击最后一个进行选择
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_zcxz))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_zcxz).click()


     # 班组---点击左侧这边的删除
    def dl_zbgl_pbgl_017(self):
        #  点击左侧这边的删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_zcsc))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_zcsc).click()
        # 删除弹出框点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bz_zcsctck))
        self.driver.find_element(*loc.dl_zbgl_pbgl_bz_zcsctck).click()


    # 左侧--点击排班
    def dl_zbgl_pbgl_018(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bpjl))
        self.driver.find_elements(*loc.dl_zbgl_pbgl_bpjl)[1].click()


    # 排班---- 点击今日日历
    def dl_zbgl_pbgl_019(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_pb_rl))
        self.driver.find_element(*loc.dl_zbgl_pbgl_pb_rl).click()


    # 排班----班组--下拉内容
    def dl_zbgl_pbgl_020(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_pb_bz))
        self.driver.find_element(*loc.dl_zbgl_pbgl_pb_bz).click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_pb_bzxl))
        self.driver.find_elements(*loc.dl_zbgl_pbgl_pb_bzxl)[-1].click()



    #确定
    def dl_zbgl_pbgl_021(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_pb_qd))
        self.driver.find_element(*loc.dl_zbgl_pbgl_pb_qd).click()


    # 左侧--点击交接班
    def dl_zbgl_pbgl_022(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_bpjl))
        self.driver.find_elements(*loc.dl_zbgl_pbgl_bpjl)[2].click()

    #交接班---提交
    def dl_zbgl_pbgl_023(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_jjb_tj))
        self.driver.find_element(*loc.dl_zbgl_pbgl_jjb_tj).click()

    # 交接班----今日完成工作
    def dl_zbgl_pbgl_024(self,wb):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_jjb_jrwcgz))
        self.driver.find_element(*loc.dl_zbgl_pbgl_jjb_jrwcgz).send_keys(wb)

    # 交接班----点击+
    def dl_zbgl_pbgl_025(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_jjb_jh))
        self.driver.find_element(*loc.dl_zbgl_pbgl_jjb_jh).click()


    # 交接班----点击+号后---选择最后一个
    def dl_zbgl_pbgl_026(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_jjb_bz))
        self.driver.find_elements(*loc.dl_zbgl_pbgl_jjb_bz)[-1].click()



    # 交接班----点击确定
    def dl_zbgl_pbgl_027(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_jjb_qd))
        self.driver.find_element(*loc.dl_zbgl_pbgl_jjb_qd).click()




   # 交接班----今日完成工作（文本内容进行清空）
    def dl_zbgl_pbgl_028(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zbgl_pbgl_jjb_jrwcgz))
        self.driver.find_element(*loc.dl_zbgl_pbgl_jjb_jrwcgz).clear()




