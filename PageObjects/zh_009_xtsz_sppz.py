
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件
import time
class Test_zh_xtsz_yppz:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()



    # 鼠标悬浮---系统设置
    # 账户进行鼠标悬浮---系统设置,点击音频配置
    def zh_xtsz_yppz(self):
        #点击系统设置
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz)).perform()
        # 点击音频配置
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz))
        self.driver.find_element(*loc.zh_xtsz_yppz).click()

     #点击添加新配置--点击保存
    def zh_xtsz_yppz_01(self):
        #点击添加新配置
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_tjxpz))
        self.driver.find_element(*loc.zh_xtsz_yppz_tjxpz).click()
        #点击保存
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_bc))
        self.driver.find_element(*loc.zh_xtsz_yppz_bc).click()

    #点击保存提示语是 音频ID、版本号和名字为必填
    def zh_xtsz_yppz_01_1(self):
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tsy))
            return self.driver.find_element(*loc.zh_xtsz_lkpz_tsy).text





    # 输入音频ID  点击保存
    def zh_xtsz_yppz_02(self,ypid):
        #输入音频ID
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_ypid))
        self.driver.find_element(*loc.zh_xtsz_yppz_ypid).send_keys(ypid)
        # 点击保存
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_bc))
        self.driver.find_element(*loc.zh_xtsz_yppz_bc).click()


    # 点击保存提示语是 音频ID、版本号和名字为必填
    def zh_xtsz_yppz_012(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tsy))
        return self.driver.find_element(*loc.zh_xtsz_lkpz_tsy).text







  # 输入音频名称  点击保存
    def zh_xtsz_yppz_03(self,ypmc):
        #输入音频名称
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_ypmc))
        self.driver.find_element(*loc.zh_xtsz_yppz_ypmc).send_keys(ypmc)
        # 点击保存
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_bc))
        self.driver.find_element(*loc.zh_xtsz_yppz_bc).click()


    # 点击保存提示语是 音频ID、版本号和名字为必填
    def zh_xtsz_yppz_03_3(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tsy))
        return self.driver.find_element(*loc.zh_xtsz_lkpz_tsy).text





    # 输入版本号  点击保存
    def zh_xtsz_yppz_04(self,bbh):
        # 输入版本号
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_bbh))
        self.driver.find_element(*loc.zh_xtsz_yppz_bbh).send_keys(bbh)
        # 点击保存
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_bc))
        self.driver.find_element(*loc.zh_xtsz_yppz_bc).click()

    # 点击保存提示语是 添加成功
    def zh_xtsz_yppz_04_4(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tsy))
        return self.driver.find_element(*loc.zh_xtsz_lkpz_tsy).text




    # 修改版本号  点击保存
    def zh_xtsz_yppz_05(self, bbh):
        # 点击分组
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_fy))
        fy=self.driver.find_elements(*loc.zh_xtsz_yppz_fy)
        for i in fy[-2:-1]:
            i.click()
        # 点击列表最后一个
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_lbzhyg))
        self.driver.find_element(*loc.zh_xtsz_yppz_lbzhyg).click()
        # 清空版本号
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_bbh))
        self.driver.find_element(*loc.zh_xtsz_yppz_bbh).clear()
        # 输入版本号
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_bbh))
        self.driver.find_element(*loc.zh_xtsz_yppz_bbh).send_keys(bbh)
        # 点击保存
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_bc))
        self.driver.find_element(*loc.zh_xtsz_yppz_bc).click()



     # 点击保存提示语是 修改成功
    def zh_xtsz_yppz_05_5(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tsy))
        return self.driver.find_element(*loc.zh_xtsz_lkpz_tsy).text

        # 修改版本号  点击保存

    def zh_xtsz_yppz_06(self):

        # 点击列表最后一个
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_lbzhyg))
        self.driver.find_element(*loc.zh_xtsz_yppz_lbzhyg).click()

        # 点击删除
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_sc))
        self.driver.find_element(*loc.zh_xtsz_yppz_sc).click()
        # 点击删除弹出框---点击确定
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_yppz_sctck))
        self.driver.find_element(*loc.zh_xtsz_yppz_sctck).click()
        # 点击保存提示语是 修改成功

    def zh_xtsz_yppz_06_6(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.zh_xtsz_lkpz_tsy))
        return self.driver.find_element(*loc.zh_xtsz_lkpz_tsy).text




