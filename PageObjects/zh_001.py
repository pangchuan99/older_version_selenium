
from selenium import  webdriver

from selenium.webdriver.support.wait import WebDriverWait    #显示等待类
                                                             #显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                                                                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
                                                 #八大元素
from Pagelocators.loginpage_locators import LoginPageLocator  as loc                             #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）


from selenium.webdriver.common.keys import Keys                                                  #键盘输入



class dl_denglushouye_yuansu:


    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

          # 登录操作
    #输入登陆账号和密码点击登陆按钮
    def login(self, username, password):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.name_text))
        self.driver.find_element(*loc.name_text).send_keys(username)
        self.driver.find_element(*loc.pwd_text).send_keys(password)
        # 判断一下remeber_user的值，来决定是否勾选
        self.driver.find_element(*loc.login_but).click()

        # 做判断处理
     #输入错误登陆账号和密码  弹出的提示信息  "账号或密码错误"
    def get_errordengluxinxi(self):

        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.tishicuowu))
        return self.driver.find_element(*loc.tishicuowu).text


    #输入登陆账号和密码登陆成功后 进行预期结果跟实际结果进行比对  "系统设置"
    def login_suidaojiance(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.suidaojiesoujiance))
        return self.driver.find_element(*loc.suidaojiesoujiance).text







