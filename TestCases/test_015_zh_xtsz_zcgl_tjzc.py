import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_zh_stsz_dtgl_tjzc:

    #点击类型  点击保存
    @pytest.mark.parametrize("data", LD.zcdl)
    @pytest.mark.usefixtures("sx")
    def test_zh_stsz_dtgl_tjzc_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        # 鼠标悬浮资产管理--- 点击添加资产
        access_web[10].zh_xtsz_zcgl_tjzc()
        time.sleep(2)
        # 类型
        access_web[10].zh_xtsz_zcgl_tjzc_01()
        time.sleep(2)
        # 类型下拉---选择火灾手报
        access_web[10].zh_xtsz_zcgl_tjzc_02()
        time.sleep(2)
        # 点击保存
        access_web[10].zh_xtsz_zcgl_tjzc_03()
        time.sleep(2)
        assert access_web[10].zh_xtsz_zcgl_tjzc_tsy()=="请输入设备名称"



    #输入名称点击保存
    @pytest.mark.usefixtures("sx")
    def test_zh_stsz_dtgl_tjzc_02(self,access_web):
        time.sleep(3)
        # 类型
        access_web[10].zh_xtsz_zcgl_tjzc_01()
        # 类型下拉---选择火灾手报
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_02()

        time.sleep(2)
        # 输入名称
        access_web[10].zh_xtsz_zcgl_tjzc_04("自动测试代码")
        # 点击保存
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_03()
        assert access_web[10].zh_xtsz_zcgl_tjzc_tsy()=="请填写正确的桩号"



    #输入桩号 点击保存
    @pytest.mark.usefixtures("sx")
    def test_zh_stsz_dtgl_tjzc_03(self,access_web):
        time.sleep(5)
        # 类型
        access_web[10].zh_xtsz_zcgl_tjzc_01()
        # 类型下拉---选择火灾手报
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_02()
        # 输入名称
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_04("自动测试代码")
        # 输入桩号
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_06("K1+22")
        # 点击保存
        access_web[10].zh_xtsz_zcgl_tjzc_03()
        assert access_web[10].zh_xtsz_zcgl_tjzc_tsy()=="请选择区域"





    #区域 点击保存
    @pytest.mark.usefixtures("sx")
    def test_zh_stsz_dtgl_tjzc_04(self,access_web):
        time.sleep(5)
        # 类型
        access_web[10].zh_xtsz_zcgl_tjzc_01()
        # 类型下拉---选择火灾手报
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_02()
        # 输入名称
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_04("自动测试代码")
        # 输入桩号
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_06("K1+22")
        # 额定功率进行清空
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_08()
        # 选择区域-
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_07()
        # 点击保存
        access_web[10].zh_xtsz_zcgl_tjzc_03()
        assert access_web[10].zh_xtsz_zcgl_tjzc_tsy()=="请输入正确的数字"




    # 定额功率 点击保存
    def test_zh_stsz_dtgl_tjzc_05(self, access_web):
        time.sleep(5)
        # 类型
        access_web[10].zh_xtsz_zcgl_tjzc_01()
        # 类型下拉---选择火灾手报
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_02()
        # 输入名称
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_04("自动测试代码")
        # 输入桩号
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_06("K1+22")
        # 额定功率进行清空
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_08()
        # 选择区域-
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_07()
        # 输入额定功率
        time.sleep(2)
        access_web[10].zh_xtsz_zcgl_tjzc_09(123)
        time.sleep(2)
        # 点击保存
        access_web[10].zh_xtsz_zcgl_tjzc_03()
        assert access_web[10].zh_xtsz_zcgl_tjzc_tsy() == "添加成功"