import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数

class  Test_dl_zbgl_jjgl:

    #点击提交
    # @pytest.mark.usefixtures("sx")
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_dl_zbgl_dfgl_01(self,sx,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        #鼠标悬浮值班管理--点击接警管理
        access_web[28].dl_zbgl_jjgl()
        time.sleep(2)
        #点击提交
        access_web[28].dl_zbgl_jjgl_01()
        assert access_web[28].dl_zbgl_jjgl_tsy()=="请输入事件开始时间"


    #开始时间--点击提交
    # @pytest.mark.usefixtures("sx")
    def test_dl_zbgl_jjgl_02(self,sx,access_web):
        time.sleep(4)
        # 开始时间
        access_web[28].dl_zbgl_jjgl_02("2020-03-27 08:09:06")
        # 点击提交
        access_web[28].dl_zbgl_jjgl_01()
        assert access_web[27].dl_zbgl_dfgl_tsy()== "请选择事件等级"



    #开始时间-----------------事件等级----------点击提交
    @pytest.mark.usefixtures("sx")
    def test_dl_zbgl_jjgl_03(self,sx,access_web):
        time.sleep(4)
        # 开始时间
        access_web[28].dl_zbgl_jjgl_02("2020-03-27 08:09:06")
        #事件等级
        access_web[28].dl_zbgl_jjgl_04()
        # 点击提交
        access_web[28].dl_zbgl_jjgl_01()

        assert access_web[27].dl_zbgl_dfgl_tsy()== "请选择事件类别"



    # 开始时间-----------------事件等级-----事件类别-----点击提交
    # @pytest.mark.usefixtures("sx")
    def test_dl_zbgl_jjgl_04(self,sx,access_web):
        time.sleep(4)
        # 开始时间
        access_web[28].dl_zbgl_jjgl_02("2020-03-27 08:09:06")
        # 事件等级
        access_web[28].dl_zbgl_jjgl_04()
        #事件类别
        access_web[28].dl_zbgl_jjgl_03()
        # 点击提交
        access_web[28].dl_zbgl_jjgl_01()
        assert access_web[27].dl_zbgl_dfgl_tsy() == "请填写正确的开始桩号"




    # 开始时间-----------------事件等级-----事件类别-------开始桩号--点击提交
    # @pytest.mark.usefixtures("sx")
    def test_dl_zbgl_jjgl_05(self,sx,access_web):
        time.sleep(4)
        # 开始时间
        access_web[28].dl_zbgl_jjgl_02("2020-03-27 08:09:06")
        # 事件等级
        access_web[28].dl_zbgl_jjgl_04()
        #事件类别
        access_web[28].dl_zbgl_jjgl_03()
        #开始桩号
        access_web[28].dl_zbgl_jjgl_05("K1+1")
        # 点击提交
        access_web[28].dl_zbgl_jjgl_01()
        assert access_web[27].dl_zbgl_dfgl_tsy() == "请填写正确的结束桩号"





     # 开始时间-----------------事件等级-----事件类别-------开始桩号-------结束桩号------点击提交
    def test_dl_zbgl_jjgl_06(self, access_web):
        time.sleep(4)
        # 开始时间
        access_web[28].dl_zbgl_jjgl_02("2020-03-27 08:09:06")
        # 事件等级
        access_web[28].dl_zbgl_jjgl_04()
        # 事件类别
        access_web[28].dl_zbgl_jjgl_03()
        # 开始桩号
        access_web[28].dl_zbgl_jjgl_05("K1+1")
        # 开始桩号
        access_web[28].dl_zbgl_jjgl_06("K2+2")
        # 点击提交
        access_web[28].dl_zbgl_jjgl_01()
        assert access_web[27].dl_zbgl_dfgl_tsy() =="提交成功"







