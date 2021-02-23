import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_zh_stsz_dtgl_zclb:

    # 设备名称输入内容点击查询
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_zh_stsz_dtgl_zclb_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(3)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        # 鼠标悬浮到资产管理-----点击资产列表
        access_web[11].zh_xtsz_zcgl_zclb()
        time.sleep(25)
        # 设备名称搜索框
        access_web[11].zh_xtsz_zcgl_zclb_01("自动测试代码")
        # 点击查询
        access_web[11].zh_xtsz_zcgl_zclb_02()




    def test_zh_stsz_dtgl_zclb_02(self, access_web):
        time.sleep(2)
        # 点击列表最后一个
        access_web[11].zh_xtsz_zcgl_zclb_03()
        # 详细编辑
        time.sleep(2)
        access_web[11].zh_xtsz_zcgl_zclb_04()
        # 名称
        time.sleep(2)
        access_web[11].zh_xtsz_zcgl_zclb_05("修改自动化代码")
        # 保存
        access_web[11].zh_xtsz_zcgl_zclb_06()
        assert access_web[11].zh_xtsz_zcgl_zclb_tsy()=="修改成功!"







    def test_zh_stsz_dtgl_zclb_03(self, access_web):
        time.sleep(4)
        # 详细编辑里面的  资产列表
        access_web[11].zh_xtsz_zcgl_zclb_07()
        # 点击列表最后一个
        access_web[11].zh_xtsz_zcgl_zclb_03()
        # 删除
        access_web[11].zh_xtsz_zcgl_zclb_08()
        assert access_web[11].zh_xtsz_zcgl_zclb_tsy()=="删除成功!"




