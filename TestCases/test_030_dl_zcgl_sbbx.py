import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





# @pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数
class  Test_dl_zcgl_sbbx:

    #点击提交
    # @pytest.mark.usefixtures("sx")
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_dl_zcgl_sbbx_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 输入悬浮到资产管理---点击设备报修
        access_web[31].dl_zcgl()
        time.sleep(1)
        # 报修工单
        access_web[31].dl_zcgl_xbbx_01()
        # 报修工单---添加报修
        access_web[31].dl_zcgl_xbbx_02()
        # 报修工单---保存
        access_web[31].dl_zcgl_xbbx_06()
        assert access_web[31].dl_zcgl_xbbx_tsy()=="设备名称为必填"



    def test_dl_zcgl_sbbx_02(self,access_web):
        time.sleep(2)
        # 报修工单
        access_web[31].dl_zcgl_xbbx_01()
        # 报修工单---添加报修
        access_web[31].dl_zcgl_xbbx_02()
        # 报修工单---设备名称
        time.sleep(1)
        access_web[31].dl_zcgl_xbbx_09()
        # 报修工单---设备类型
        time.sleep(1)
        access_web[31].dl_zcgl_xbbx_010()

        # 报修工单---设备名称--设备名称
        time.sleep(1)
        access_web[31].dl_zcgl_xbbx_011()
        # 报修工单---确定
        time.sleep(1)
        access_web[31].dl_zcgl_xbbx_012()
        # 报修工单---报修原因输入
        time.sleep(1)
        access_web[31].dl_zcgl_xbbx_014("自动添加11")
        # 报修工单---保存
        access_web[31].dl_zcgl_xbbx_06()
        assert access_web[31].dl_zcgl_xbbx_tsy() == "添加成功"



    def test_dl_zcgl_sbbx_03(self,access_web):
        time.sleep(2)
        # 报修工单
        access_web[31].dl_zcgl_xbbx_01()
        # 报修工单---添加报修
        access_web[31].dl_zcgl_xbbx_02()
        # 报修工单---报修原因搜索框---清除
        access_web[31].dl_zcgl_xbbx_08()
        # 报修工单---报修原因搜索框
        time.sleep(1)
        access_web[31].dl_zcgl_xbbx_03("自动添加")
        # 报修工单---查询
        time.sleep(1)
        access_web[31].dl_zcgl_xbbx_04()
        # 报修工单---列表最后一个
        access_web[31].dl_zcgl_xbbx_018()
        # 报修工单---报修原因清除
        time.sleep(1)
        access_web[31].dl_zcgl_xbbx_013()
        # 报修工单---报修原因输入
        time.sleep(1)
        access_web[31].dl_zcgl_xbbx_014("自动添加1")
        # 报修工单---保存
        access_web[31].dl_zcgl_xbbx_06()
        assert access_web[31].dl_zcgl_xbbx_tsy() == "修改成功"



    def test_dl_zcgl_sbbx_04(self,access_web):
        time.sleep(3)
        # 报修工单
        access_web[31].dl_zcgl_xbbx_01()
        # 报修工单---添加报修
        time.sleep(1)
        access_web[31].dl_zcgl_xbbx_02()
        # 报修工单---报修原因搜索框---清除
        time.sleep(1)
        access_web[31].dl_zcgl_xbbx_08()
        # 报修工单---报修原因搜索框
        time.sleep(1)
        access_web[31].dl_zcgl_xbbx_03("自动添加1")
        # 报修工单---列表最后一个
        time.sleep(1)
        access_web[31].dl_zcgl_xbbx_018()
        # 报修工单---删除
        access_web[31].dl_zcgl_xbbx_05()
        assert access_web[31].dl_zcgl_xbbx_tsy() == "删除成功"


