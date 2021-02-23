import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_jkxt_cjqfd:


    @pytest.mark.parametrize("data", LD.zcdl)
    def test_jkxt_cjqfd_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        # 账户进行鼠标悬浮---系统设置,点击车检器分段
        access_web[19].zh_xtsz_cjqfd()
        time.sleep(4)
        # 点击添加新配置
        access_web[19].zh_xtsz_cjqfd_01()
        # 点击保存
        access_web[19].zh_xtsz_cjqfd_02()
        time.sleep(1)
        assert  access_web[19].zh_xtsz_cjqfd_03()=="起始设备、结束设备和车道数为必填项"





    #
    def test_jkxt_cjqfd_02(self,access_web):
        time.sleep(2)
        # 点击添加新配置
        access_web[19].zh_xtsz_cjqfd_01()
        # 方向
        access_web[19].zh_xtsz_cjqfd_04()
        # 点击保存
        access_web[19].zh_xtsz_cjqfd_02()
        assert  access_web[19].zh_xtsz_cjqfd_03()=="起始设备、结束设备和车道数为必填项"


    # 起始设备--点击保存
    def test_jkxt_cjqfd_03(self,access_web):
        time.sleep(2)
        # 点击添加新配置
        access_web[19].zh_xtsz_cjqfd_01()
        # 方向
        access_web[19].zh_xtsz_cjqfd_04()
        # 起始设备-
        access_web[19].zh_xtsz_cjqfd_05()
        # 点击保存
        access_web[19].zh_xtsz_cjqfd_02()
        assert  access_web[19].zh_xtsz_cjqfd_03()=="起始设备、结束设备和车道数为必填项"

    #清除车道数--- 结束设备--点击保存
    def test_jkxt_cjqfd_04(self, access_web):
        # 点击添加新配置
        access_web[19].zh_xtsz_cjqfd_01()
        # 方向
        access_web[19].zh_xtsz_cjqfd_04()
        # 起始设备-
        access_web[19].zh_xtsz_cjqfd_05()
        # 结束设备
        access_web[19].zh_xtsz_cjqfd_06()
        # 车道数---清除
        access_web[19].zh_xtsz_cjqfd_07()
        # 点击保存
        access_web[19].zh_xtsz_cjqfd_02()
        assert access_web[19].zh_xtsz_cjqfd_03() == "起始设备、结束设备和车道数为必填项"



    # 车道数--点击保存
    def test_jkxt_cjqfd_05(self, access_web):
        # 点击添加新配置
        access_web[19].zh_xtsz_cjqfd_01()
        # 方向
        access_web[19].zh_xtsz_cjqfd_04()
        # 起始设备-
        time.sleep(1)
        access_web[19].zh_xtsz_cjqfd_05()
        # 结束设备
        time.sleep(1)
        access_web[19].zh_xtsz_cjqfd_06()
        # 车道数---清除
        time.sleep(1)
        access_web[19].zh_xtsz_cjqfd_07()
        # 车道数输入
        access_web[19].zh_xtsz_cjqfd_08(11380)
        # 点击保存
        access_web[19].zh_xtsz_cjqfd_02()
        assert access_web[19].zh_xtsz_cjqfd_03() == "添加成功"


   #列表最后一个进行点击---车道数进行修改--点击保存
    def test_jkxt_cjqfd_06(self, access_web):
        time.sleep(3)
        # 列表最后一个进行点击
        access_web[19].zh_xtsz_cjqfd_09()
        # 车道数---清除
        access_web[19].zh_xtsz_cjqfd_07()
        # 车道数输入
        access_web[19].zh_xtsz_cjqfd_08(2580)
        # 点击保存
        access_web[19].zh_xtsz_cjqfd_02()
        time.sleep(1)
        assert access_web[19].zh_xtsz_cjqfd_03() == "修改成功"



   #列表最后一个进行点击----点击删除
    def test_jkxt_cjqfd_07(self, access_web):
        time.sleep(2)
        # 列表最后一个进行点击
        access_web[19].zh_xtsz_cjqfd_09()
        # 删除
        access_web[19].zh_xtsz_cjqfd_010()

        time.sleep(1)
        assert access_web[19].zh_xtsz_cjqfd_03() == "删除成功"





