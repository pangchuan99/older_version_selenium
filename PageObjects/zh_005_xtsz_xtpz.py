from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

from selenium.webdriver.common.action_chains import ActionChains                                 #鼠标事件

from selenium.webdriver.common.keys import Keys                                                  #键盘输入



class Test_zh_xtsz_xtpz:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    def zh_xtsz_xtpz(self):
        #账户进行鼠标悬浮---系统设置,点击系统配置
        #鼠标悬浮---系统设置
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.zh_xtsz))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zh_xtsz)).perform()
        #点击系统配置
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz))
        self.driver.find_element(*loc.zh_xtsz_xtpz).click()

     #系统配置里面的内容进行定位修改
    def zh_xtsz_xtpz_sr(self,al,a2,a3,a4,a5,a6):
        #系统名称
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_xtmc))
        self.driver.find_element(*loc.zh_xtsz_xtpz_xtmc).clear()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_xtmc))
        self.driver.find_element(*loc.zh_xtsz_xtpz_xtmc).send_keys(al)

        #字体大小
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_ztdx))
        self.driver.find_element(*loc.zh_xtsz_xtpz_ztdx).send_keys(Keys.CONTROL,'a')
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_ztdx))
        self.driver.find_element(*loc.zh_xtsz_xtpz_ztdx).send_keys(a2)
        #图片宽度
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_tpkd))
        self.driver.find_element(*loc.zh_xtsz_xtpz_tpkd).send_keys(Keys.CONTROL,'a')
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_tpkd))
        self.driver.find_element(*loc.zh_xtsz_xtpz_tpkd).send_keys(a3)
        #图片高度
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_tpgd))
        self.driver.find_element(*loc.zh_xtsz_xtpz_tpgd).send_keys(Keys.CONTROL,'a')
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_tpgd))
        self.driver.find_element(*loc.zh_xtsz_xtpz_tpgd).send_keys(a4)
        #居左距离
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_jzjl))
        self.driver.find_element(*loc.zh_xtsz_xtpz_jzjl).send_keys(Keys.CONTROL,'a')
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_jzjl))
        self.driver.find_element(*loc.zh_xtsz_xtpz_jzjl).send_keys(a5)

        # 居右距离
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_jyjl))
        self.driver.find_element(*loc.zh_xtsz_xtpz_jyjl).send_keys(Keys.CONTROL,'a')
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_jyjl))
        self.driver.find_element(*loc.zh_xtsz_xtpz_jyjl).send_keys(a6)

        #点击保存
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_bc))
        self.driver.find_element(*loc.zh_xtsz_xtpz_bc).click()
    #提示框修改成功
    def zh_xtsz_xtpz_tsy(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zh_xtsz_xtpz_tsy))
        return self.driver.find_element(*loc.zh_xtsz_xtpz_tsy).text


















