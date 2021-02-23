import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）


import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_zh_stsz_dtgl_ykpz:

    # 添加表达式---点击保存
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_zh_stsz_dtgl_ykpz_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        # 鼠标悬浮到资产管理 点击遥控配置
        access_web[14].zh_xtsz_zcgl_ykpz()
        time.sleep(3)
        # 添加表达式
        access_web[14].zh_xtsz_zcgl_ykpz_01()
        # 点击保存
        access_web[14].zh_xtsz_zcgl_ykpz_02()
        assert access_web[14].zh_xtsz_zcgl_ykpz_tsy()=="请选择设备类型"



    # 设备类型 - --点击保存
    def test_zh_stsz_dtgl_ykpz_02(self,access_web):
        time.sleep(3)
        # 添加表达式
        access_web[14].zh_xtsz_zcgl_ykpz_01()
        # 设备类型
        access_web[14].zh_xtsz_zcgl_ykpz_03()
        # 点击保存
        access_web[14].zh_xtsz_zcgl_ykpz_02()
        assert access_web[14].zh_xtsz_zcgl_ykpz_tsy()=="请选择状态"


     #状态 - --点击保存
    def test_zh_stsz_dtgl_ykpz_03(self,access_web):
        time.sleep(3)
        # 添加表达式
        access_web[14].zh_xtsz_zcgl_ykpz_01()
        # 设备类型
        access_web[14].zh_xtsz_zcgl_ykpz_03()
        # 状态
        access_web[14].zh_xtsz_zcgl_ykpz_04()
        # 版本清除
        access_web[14].zh_xtsz_zcgl_ykpz_05()
        # 点击保存
        access_web[14].zh_xtsz_zcgl_ykpz_02()
        assert access_web[14].zh_xtsz_zcgl_ykpz_tsy()=="请输入版本"

    # 输入版本 - --点击保存
    def test_zh_stsz_dtgl_ykpz_04(self, access_web):
        time.sleep(3)
        # 添加表达式
        access_web[14].zh_xtsz_zcgl_ykpz_01()
        # 设备类型
        access_web[14].zh_xtsz_zcgl_ykpz_03()
        # 状态
        access_web[14].zh_xtsz_zcgl_ykpz_04()
        # 版本清除
        access_web[14].zh_xtsz_zcgl_ykpz_05()
        # 版本输入
        access_web[14].zh_xtsz_zcgl_ykpz_06(8)
        # 点击保存
        access_web[14].zh_xtsz_zcgl_ykpz_02()
        assert access_web[14].zh_xtsz_zcgl_ykpz_tsy() == "请输入值(0~255)"



    # 输入值 - --点击保存(边界值测试)
    def test_zh_stsz_dtgl_ykpz_05(self, access_web):
        time.sleep(3)
        # 添加表达式
        access_web[14].zh_xtsz_zcgl_ykpz_01()
        # 设备类型
        access_web[14].zh_xtsz_zcgl_ykpz_03()
        # 状态
        access_web[14].zh_xtsz_zcgl_ykpz_04()
        # 版本清除
        access_web[14].zh_xtsz_zcgl_ykpz_05()
        # 版本输入
        access_web[14].zh_xtsz_zcgl_ykpz_06(8)
        # 输入值
        access_web[14].zh_xtsz_zcgl_ykpz_08(-1)
        # 点击保存
        access_web[14].zh_xtsz_zcgl_ykpz_02()
        assert access_web[14].zh_xtsz_zcgl_ykpz_tsy() == "请输入值(0~255)"

    # 输入值 - --点击保存---(边界值测试)
    def test_zh_stsz_dtgl_ykpz_06(self, access_web):
        time.sleep(3)
        # 添加表达式
        access_web[14].zh_xtsz_zcgl_ykpz_01()
        # 设备类型
        access_web[14].zh_xtsz_zcgl_ykpz_03()
        # 状态
        access_web[14].zh_xtsz_zcgl_ykpz_04()
        # 版本清除
        access_web[14].zh_xtsz_zcgl_ykpz_05()
        # 版本输入
        access_web[14].zh_xtsz_zcgl_ykpz_06(8)
        # 输入值
        access_web[14].zh_xtsz_zcgl_ykpz_08(256)
        # 点击保存
        access_web[14].zh_xtsz_zcgl_ykpz_02()
        assert access_web[14].zh_xtsz_zcgl_ykpz_tsy() == "请输入值(0~255)"

    # 输入值 - --点击保存---(边界值测试)
    def test_zh_stsz_dtgl_ykpz_07(self, access_web):
        time.sleep(3)
        # 添加表达式
        access_web[14].zh_xtsz_zcgl_ykpz_01()
        # 设备类型
        access_web[14].zh_xtsz_zcgl_ykpz_03()
        # 状态
        access_web[14].zh_xtsz_zcgl_ykpz_04()
        # 版本清除
        access_web[14].zh_xtsz_zcgl_ykpz_05()
        # 版本输入
        access_web[14].zh_xtsz_zcgl_ykpz_06(8)
        # 输入值
        access_web[14].zh_xtsz_zcgl_ykpz_08(66)
        # 点击保存
        access_web[14].zh_xtsz_zcgl_ykpz_02()
        assert access_web[14].zh_xtsz_zcgl_ykpz_tsy() == "添加成功"

    def test_zh_stsz_dtgl_ykpz_08(self, access_web):
        time.sleep(3)
        # 添加表达式
        access_web[14].zh_xtsz_zcgl_ykpz_01()
        # 设备类型
        access_web[14].zh_xtsz_zcgl_ykpz_03()
        # 状态
        access_web[14].zh_xtsz_zcgl_ykpz_04()
        # 版本清除
        access_web[14].zh_xtsz_zcgl_ykpz_05()
        # 版本输入
        access_web[14].zh_xtsz_zcgl_ykpz_06(8)
        # 输入值
        access_web[14].zh_xtsz_zcgl_ykpz_08(66)
        # 点击保存
        access_web[14].zh_xtsz_zcgl_ykpz_02()
        assert access_web[14].zh_xtsz_zcgl_ykpz_tsy() == "已存在"

    def test_zh_stsz_dtgl_ykpz_09(self, access_web):
        time.sleep(3)
        # 上测---设备类型
        access_web[14].zh_xtsz_zcgl_ykpz_011()
        # 查询
        access_web[14].zh_xtsz_zcgl_ykpz_012()
        # 列表点击最后一个
        access_web[14].zh_xtsz_zcgl_ykpz_09()
        # 版本清除
        access_web[14].zh_xtsz_zcgl_ykpz_05()
        # 版本输入
        access_web[14].zh_xtsz_zcgl_ykpz_06(9)
        # 点击保存
        access_web[14].zh_xtsz_zcgl_ykpz_02()
        assert access_web[14].zh_xtsz_zcgl_ykpz_tsy() == "修改成功"



    # 列表点击最后一个-，点击删除
    def test_zh_stsz_dtgl_ykpz_010(self, access_web):
        time.sleep(3)
        # 上测---设备类型
        access_web[14].zh_xtsz_zcgl_ykpz_011()
        # 查询
        access_web[14].zh_xtsz_zcgl_ykpz_012()
        # 列表点击最后一个
        access_web[14].zh_xtsz_zcgl_ykpz_09()
        # 删除
        access_web[14].zh_xtsz_zcgl_ykpz_010()
        assert access_web[14].zh_xtsz_zcgl_ykpz_tsy() == "删除成功"
