
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
import allure


class Test_zhjk_sbjk_gjy:



    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    # 鼠标悬浮到综合监控---点击设备监控
    @allure.step("鼠标悬浮到综合监控---点击设备监控")
    def dl_zhjk_sbjk_gjy(self):
        #鼠标悬浮到综合监控
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.dl_zhjk)).perform()
        time.sleep(1)
        # 点击设备监控
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk))
        self.driver.find_element(*loc.dl_zhjk_sbjk).click()


    # 提示语---
    @allure.step("提示语---")
    def dl_zhjk_sbjk_gjy_tsy(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_tsy))
        return self.driver.find_element(*loc.dl_zhjk_sbjk_tsy).text

    # 提示语1---
    @allure.step("提示语1---")
    def dl_zhjk_sbjk_gjy_tsy1(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_tsy1))
        return self.driver.find_element(*loc.dl_zhjk_sbjk_tsy1).text

    #点击头孢堡隧道
    @allure.step("点击头孢堡隧道")
    def dl_zhjk_sbjk_gjy_01(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_gjysd))
        self.driver.find_element(*loc.dl_zhjk_sbjk_gjysd).click()


    #左侧搜索框
    @allure.step("左侧搜索框")
    def dl_zhjk_sbjk_gjy_02(self,ssk):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_zcssk))
        self.driver.find_element(*loc.dl_zhjk_sbjk_zcssk).send_keys(ssk)

    # 左侧搜索框清除
    @allure.step("左侧搜索框清除")
    def dl_zhjk_sbjk_gjy_010(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_zcssk))
        self.driver.find_element(*loc.dl_zhjk_sbjk_zcssk).clear()


    #左侧搜索框到点击确定
    @allure.step("左侧搜索框到点击确定")
    def dl_zhjk_sbjk_gjy_03(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_zcssk_qd))
        self.driver.find_element(*loc.dl_zhjk_sbjk_zcssk_qd).click()


    # 左侧列表点击第一个
    @allure.step("左侧列表点击第一个")
    def dl_zhjk_sbjk_gjy_04(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_zclb))
        self.driver.find_elements(*loc.dl_zhjk_sbjk_zclb)[0].click()


    #点击双面车道指示器状态---远程正面通行
    #射流风机  远程关
    #交通灯   远程红
    #照明      远程开
    @allure.step("点击双面车道指示器状态---远程正面通行----射流风机  远程关---- 交通灯   远程红-----照明      远程开")
    def dl_zhjk_sbjk_gjy_05(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_zcssk_zt))
        self.driver.find_elements(*loc.dl_zhjk_sbjk_zcssk_zt)[0].click()



    #点击双面车道指示器状态---远程禁止
    # 射流风机  远程正转
    # 交通灯   远程黄
    @allure.step("点击双面车道指示器状态---远程禁止----射流风机  远程正转-----交通灯   远程黄")
    def dl_zhjk_sbjk_gjy_06(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_zcssk_zt))
        self.driver.find_elements(*loc.dl_zhjk_sbjk_zcssk_zt)[1].click()

    # 交通灯   远程绿
    @allure.step("点击双面车道指示器状态---远程反面通行----交通灯   远程绿")
    def dl_zhjk_sbjk_gjy_07(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_zcssk_zt))
        self.driver.find_elements(*loc.dl_zhjk_sbjk_zcssk_zt)[2].click()


    # 点击双面车道指示器状态---远程转向
    # 射流风机  远程反转
    # 照明      远程关
    @allure.step("点击双面车道指示器状态   远程转向 -----射流风机  远程反转----照明      远程关")
    def dl_zhjk_sbjk_gjy_08(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_zcssk_zt))
        self.driver.find_elements(*loc.dl_zhjk_sbjk_zcssk_zt)[-1].click()


     #双面车道指示器状态---显示状态
    @allure.step("双面车道指示器状态---显示状态")
    def dl_zhjk_sbjk_gjy_09(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_sbzt))
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_element(*loc.dl_zhjk_sbjk_sbzt))
        return self.driver.find_element(*loc.dl_zhjk_sbjk_sbzt).text


    #情报板信息下发
    #可变速标志---速度设置
    @allure.step("情报板信息下发-------可变速标志   速度设置")
    def dl_zhjk_sbjk_gjy_011(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_qbbxxxf))
        self.driver.find_element(*loc.dl_zhjk_sbjk_qbbxxxf).click()

    #情报板信息下发---输入内容
    def dl_zhjk_sbjk_gjy_012(self,k1):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_qbbxxxf_nr1))
        # self.driver.find_element(*loc.dl_zhjk_sbjk_qbbxxxf_nr1).click()
        self.driver.find_element(*loc.dl_zhjk_sbjk_qbbxxxf_nr1).click()

        self.driver.switch_to.active_element.send_keys(k1)
        self.driver.find_element(*loc.dl_zhjk_sbjk_qbbxxxf_nr1).send_keys(Keys.ENTER)
        self.driver.find_element(*loc.dl_zhjk_sbjk_qbbxxxf_nr1).send_keys(Keys.ENTER)
        self.driver.find_element(*loc.dl_zhjk_sbjk_qbbxxxf_nr1).send_keys(Keys.ENTER)

    #情报板信息下发-----下发
    def dl_zhjk_sbjk_gjy_013(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_qbbxxxf_xf))
        self.driver.find_element(*loc.dl_zhjk_sbjk_qbbxxxf_xf).click()


    #情报板信息下发-----获取内容
    def dl_zhjk_sbjk_gjy_014(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_qbbxxxf_hqnr))
        return self.driver.find_element(*loc.dl_zhjk_sbjk_qbbxxxf_hqnr).text


    # 情报板信息下发-----删除内容
    def dl_zhjk_sbjk_gjy_015(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_qbbxxxf_sc1))
        self.driver.find_element(*loc.dl_zhjk_sbjk_qbbxxxf_sc1).click()


    # 可变速标志---速度设置
    def dl_zhjk_sbjk_gjy_016(self,r):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_sdszssk))

        self.driver.find_element(*loc.dl_zhjk_sbjk_sdszssk).send_keys(r)



    # 可变速标志---速度设置-----设置
    def dl_zhjk_sbjk_gjy_017(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_sdszssk_sz))
        self.driver.find_element(*loc.dl_zhjk_sbjk_sdszssk_sz).click()


    # 可变速标志---速度设置 清空
    def dl_zhjk_sbjk_gjy_018(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_sdszssk))
        self.driver.find_element(*loc.dl_zhjk_sbjk_sdszssk).send_keys(Keys.BACK_SPACE*5)


    # 可变速标志---当前速度
    def dl_zhjk_sbjk_gjy_019(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_sdszssk_sd))
        return self.driver.find_elements(*loc.dl_zhjk_sbjk_sdszssk_sd)[-1].text




    #情报板  左上角--请选择  然后点击下拉内容
    def dl_zhjk_sbjk_gjy_020(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_qbbxxxf_qxz))
        self.driver.find_element(*loc.dl_zhjk_sbjk_qbbxxxf_qxz).click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_qbbxxxf_qxzxlnr))
        self.driver.execute_script("arguments[0].scrollIntoView(false);", self.driver.find_elements(*loc.dl_zhjk_sbjk_qbbxxxf_qxzxlnr)[0])
        self.driver.find_elements(*loc.dl_zhjk_sbjk_qbbxxxf_qxzxlnr)[0].click()

    # 情报板 ---取消
    def dl_zhjk_sbjk_gjy_021(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_qbbxxxf_qx12))
        self.driver.find_element(*loc.dl_zhjk_sbjk_qbbxxxf_qx12).click()


    # 限速标志---取消
    def dl_zhjk_sbjk_gjy_022(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_sdszssk_qx))
        self.driver.find_element(*loc.dl_zhjk_sbjk_sdszssk_qx).click()



    #枪机 ---视频 点击X
    def dl_zhjk_sbjk_gjy_023(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_sdszssk_qx))
        self.driver.find_element(*loc.dl_zhjk_sbjk_sdszssk_qx).click()

    # 左下侧设备名称
    def dl_zhjk_sbjk_gjy_025(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_sdszssk_sd))
        return self.driver.find_elements(*loc.dl_zhjk_sbjk_sdszssk_sd)[0].text


    #路段点击设备组
    def dl_zhjk_sbjk_gjy_026(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_lusbz))
        self.driver.find_elements(*loc.dl_zhjk_sbjk_lusbz)[-5].click()



    #点击键盘上的回车键
    def dl_zhjk_sbjk_gjy_027(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_zcssk))
        self.driver.find_element(*loc.dl_zhjk_sbjk_zcssk).send_keys(Keys.ENTER)


    #双面车道指示器-------他是进行还原最初状态的
    def dl_zhjk_sbjk_gjy_029(self,a1,access_web):
        if a1=="远程正面通行":
            # 点击双面车道指示器状态---远程正面通行
            time.sleep(5)
            access_web[35].dl_zhjk_sbjk_gjy_05()

            time.sleep(3)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"

            time.sleep(3)
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程正面通行"

        elif a1=="远程禁止":
            # 点击双面车道指示器状态---远程禁止.
            time.sleep(5)
            access_web[35].dl_zhjk_sbjk_gjy_06()

            time.sleep(3)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"

            time.sleep(3)
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程禁止"

        elif a1=="远程反面通行":
            # 点击双面车道指示器状态---远程反面通行
            time.sleep(5)
            access_web[35].dl_zhjk_sbjk_gjy_07()

            time.sleep(3)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"

            time.sleep(3)
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程反面通行"

        elif a1=="远程转向":
            # 点击双面车道指示器状态---远程转向
            time.sleep(5)
            access_web[35].dl_zhjk_sbjk_gjy_08()

            time.sleep(3)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"

            time.sleep(3)
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程转向"




    # 射流风机--------他是进行还原最初状态的
    def dl_zhjk_sbjk_gjy_030(self, a2, access_web):
        if a2 =="远程关":
            # 射流风机  远程关
            time.sleep(70)
            access_web[35].dl_zhjk_sbjk_gjy_05()
            time.sleep(3)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"
            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程关"

        elif a2=="远程正转":
            # 射流风机  远程关
            time.sleep(70)
            access_web[35].dl_zhjk_sbjk_gjy_05()
            time.sleep(3)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"
            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程关"
            # 射流风机  远程正转
            time.sleep(70)
            access_web[35].dl_zhjk_sbjk_gjy_06()
            time.sleep(3)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"
            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程正转"

        elif a2=="远程反转":
            # 射流风机  远程关
            time.sleep(70)
            access_web[35].dl_zhjk_sbjk_gjy_05()
            time.sleep(3)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"
            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程关"
            # 射流风机  远程反转
            time.sleep(70)
            access_web[35].dl_zhjk_sbjk_gjy_08()
            time.sleep(3)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"
            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程反转"
        # 洞口交通灯4控--------他是进行还原最初状态的









    def dl_zhjk_sbjk_gjy_031(self, a2, access_web):
        if a2 == "远程红":
            # 射流风机  远程红
            time.sleep(5)

            # 洞口交通灯4控---远程红
            access_web[35].dl_zhjk_sbjk_gjy_05()

            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"
            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程红"

        elif a2 == "远程黄":

            time.sleep(5)

            #洞口交通灯4控---远程黄
            access_web[35].dl_zhjk_sbjk_gjy_06()

            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"


            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程黄"

        elif a2 == "远程绿":

            time.sleep(5)

            # 洞口交通灯4控---远程绿
            access_web[35].dl_zhjk_sbjk_gjy_07()

            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"

            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程绿"

        elif a2 == "远程红+转向":

            time.sleep(5)

            # 洞口交通灯4控--远程红+转向
            access_web[35].dl_zhjk_sbjk_gjy_08()

            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"

            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程红+转向"


    # 可变速限速标志---数据报表
    @allure.step("可变速限速标志---数据报表")
    def dl_zhjk_sbjk_gjy_032(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_kbsbz_sjbb))
        self.driver.find_element(*loc.dl_zhjk_sbjk_kbsbz_sjbb).click()


    #可变速限速标志---获取值
    @allure.step("可变速限速标志---获取值")
    def dl_zhjk_sbjk_gjy_033(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_kbsbz_sjbb_xsz))
        return self.driver.find_element(*loc.dl_zhjk_sbjk_kbsbz_sjbb_xsz).text


    #可变速限速标志---基本信息
    @allure.step("可变速限速标志---基本信息")
    def dl_zhjk_sbjk_gjy_034(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.dl_zhjk_sbjk_kbsbz_jbxx))
        self.driver.find_element(*loc.dl_zhjk_sbjk_kbsbz_jbxx).click()

    #加强照明----获取他的初始值
    def dl_zhjk_sbjk_gjy_035(self,a2,access_web):

        if a2=="远程关":
            time.sleep(3)
            # 交通灯   远程关
            time.sleep(3)
            access_web[35].dl_zhjk_sbjk_gjy_08()

            time.sleep(2)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程关"

        elif a2=="远程开":

            # 交通灯   远程开
            time.sleep(3)
            access_web[35].dl_zhjk_sbjk_gjy_05()
            time.sleep(1.5)
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"
            assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程开"




