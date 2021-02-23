import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_zh_stsz_dtgl_cjpz:


    @pytest.mark.parametrize("data", LD.zcdl)
    def test_zh_stsz_dtgl_cjpz_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        # 鼠标悬浮资产管理点击厂家配置
        access_web[16].zh_xtsz_zcgl_cjpz()
        time.sleep(2)
        # 添加厂家
        access_web[16].zh_xtsz_zcgl_cjpz_01()
        # 点击保存
        access_web[16].zh_xtsz_zcgl_cjpz_02()
        assert access_web[16].zh_xtsz_zcgl_cjpz_tsy()=="请选择设备类型"



    # 设备类型---点击保存
    def test_zh_stsz_dtgl_cjpz_02(self,access_web):
        time.sleep(4)
        # 添加厂家
        access_web[16].zh_xtsz_zcgl_cjpz_01()
        # 设备类型
        access_web[16].zh_xtsz_zcgl_cjpz_04()
        # 点击保存
        access_web[16].zh_xtsz_zcgl_cjpz_02()
        assert access_web[16].zh_xtsz_zcgl_cjpz_tsy() == "请选择状态"




    # 厂家名称---版本清除---点击保存
    def test_zh_stsz_dtgl_cjpz_03(self,access_web):
        time.sleep(4)
        # 添加厂家
        access_web[16].zh_xtsz_zcgl_cjpz_01()
        # 设备类型
        access_web[16].zh_xtsz_zcgl_cjpz_04()
        # 厂家名称
        access_web[16].zh_xtsz_zcgl_cjpz_05(123)
        # 版本清除
        access_web[16].zh_xtsz_zcgl_cjpz_06()
        # 点击保存
        access_web[16].zh_xtsz_zcgl_cjpz_02()
        assert access_web[16].zh_xtsz_zcgl_cjpz_tsy() == "请输入版本"




    # 版本---点击保存
    def test_zh_stsz_dtgl_cjpz_04(self, access_web):
        time.sleep(4)
        # 添加厂家
        access_web[16].zh_xtsz_zcgl_cjpz_01()
        # 设备类型
        access_web[16].zh_xtsz_zcgl_cjpz_04()
        # 厂家名称
        access_web[16].zh_xtsz_zcgl_cjpz_05(123)
        # 版本清除
        access_web[16].zh_xtsz_zcgl_cjpz_06()
        # 版本输入
        access_web[16].zh_xtsz_zcgl_cjpz_07(456)
        # 点击保存
        access_web[16].zh_xtsz_zcgl_cjpz_02()
        assert access_web[16].zh_xtsz_zcgl_cjpz_tsy() == "请输入通讯方式"




    # 通讯方式---点击保存
    def test_zh_stsz_dtgl_cjpz_05(self, access_web):
        time.sleep(4)
        # 添加厂家
        access_web[16].zh_xtsz_zcgl_cjpz_01()
        # 设备类型
        access_web[16].zh_xtsz_zcgl_cjpz_04()
        # 厂家名称
        access_web[16].zh_xtsz_zcgl_cjpz_05(123)
        # 版本清除
        access_web[16].zh_xtsz_zcgl_cjpz_06()
        # 版本输入
        access_web[16].zh_xtsz_zcgl_cjpz_07(456)
        # 通讯方式
        access_web[16].zh_xtsz_zcgl_cjpz_08(789)
        # 点击保存
        access_web[16].zh_xtsz_zcgl_cjpz_02()
        assert access_web[16].zh_xtsz_zcgl_cjpz_tsy() == "请输入脚本名称"



    # 脚步名称-----点击保存
    def test_zh_stsz_dtgl_cjpz_06(self, access_web):
        time.sleep(4)
        # 添加厂家
        access_web[16].zh_xtsz_zcgl_cjpz_01()
        # 设备类型
        access_web[16].zh_xtsz_zcgl_cjpz_04()
        # 厂家名称
        access_web[16].zh_xtsz_zcgl_cjpz_05(123)
        # 版本清除
        access_web[16].zh_xtsz_zcgl_cjpz_06()
        # 版本输入
        access_web[16].zh_xtsz_zcgl_cjpz_07(456)
        # 通讯方式
        access_web[16].zh_xtsz_zcgl_cjpz_08(789)
        # 脚本名称
        access_web[16].zh_xtsz_zcgl_cjpz_09("012")
        # 点击保存
        access_web[16].zh_xtsz_zcgl_cjpz_02()
        assert access_web[16].zh_xtsz_zcgl_cjpz_tsy() == "添加成功！"


    def test_zh_stsz_dtgl_cjpz_07(self, access_web):
        time.sleep(4)
        # 列表最后一个
        access_web[16].zh_xtsz_zcgl_cjpz_010()
        # 版本清除
        access_web[16].zh_xtsz_zcgl_cjpz_06()
        # 版本输入
        access_web[16].zh_xtsz_zcgl_cjpz_07(99999)
        # 点击保存
        access_web[16].zh_xtsz_zcgl_cjpz_02()
        assert access_web[16].zh_xtsz_zcgl_cjpz_tsy() == "修改成功！"


    def test_zh_stsz_dtgl_cjpz_08(self, access_web):
        time.sleep(5)
        # 列表最后一个
        access_web[16].zh_xtsz_zcgl_cjpz_010()
        # 删除
        access_web[16].zh_xtsz_zcgl_cjpz_03()
        assert access_web[16].zh_xtsz_zcgl_cjpz_tsy() == "删除成功!"

