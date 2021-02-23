import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_zh_stsz_dtgl_qybj:


    # 添加配置---点击保存
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_zh_stsz_dtgl_jczpz_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(1.5)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        access_web[15].zh_xtsz_zcgl_jczpz()
        time.sleep(2)
        # 添加配置
        access_web[15].zh_xtsz_zcgl_jczpz_01()
        # 点击保存
        access_web[15].zh_xtsz_zcgl_jczpz_02()
        assert  access_web[15].zh_xtsz_zcgl_jczpz_tsy()=="请选择设备类型"


    # 设备类型---点击保存
    def test_zh_stsz_dtgl_jczpz_02(self, access_web):
        time.sleep(2)
        # 添加配置
        access_web[15].zh_xtsz_zcgl_jczpz_01()
        # 设备类型
        access_web[15].zh_xtsz_zcgl_jczpz_04()
        # 清除版本
        access_web[15].zh_xtsz_zcgl_jczpz_05()
        # 点击保存
        access_web[15].zh_xtsz_zcgl_jczpz_02()
        assert access_web[15].zh_xtsz_zcgl_jczpz_tsy() == "请输入版本"



    # 版本---点击保存
    def test_zh_stsz_dtgl_jczpz_03(self, access_web):
        time.sleep(3)
        # 添加配置
        access_web[15].zh_xtsz_zcgl_jczpz_01()
        # 设备类型
        access_web[15].zh_xtsz_zcgl_jczpz_04()
        # 清除版本
        access_web[15].zh_xtsz_zcgl_jczpz_05()
        # 版本输入
        access_web[15].zh_xtsz_zcgl_jczpz_06(9)
        # 点击保存
        access_web[15].zh_xtsz_zcgl_jczpz_02()
        assert access_web[15].zh_xtsz_zcgl_jczpz_tsy() == "请输入表达式"



    # 表达式--点击保存
    # @pytest.mark.usefixtures("refresh_page")
    def test_zh_stsz_dtgl_jczpz_04(self, access_web):
        time.sleep(4)
        # 添加配置
        access_web[15].zh_xtsz_zcgl_jczpz_01()
        # 设备类型
        access_web[15].zh_xtsz_zcgl_jczpz_04()
        # 清除版本
        access_web[15].zh_xtsz_zcgl_jczpz_05()
        # 版本输入
        access_web[15].zh_xtsz_zcgl_jczpz_06(9)
        # 表达式
        access_web[15].zh_xtsz_zcgl_jczpz_07(9)
        # 点击保存
        access_web[15].zh_xtsz_zcgl_jczpz_02()
        assert access_web[15].zh_xtsz_zcgl_jczpz_tsy() == "添加成功！"




    # 选择设备类型-输入版本--输入表达式--点击保存
    def test_zh_stsz_dtgl_jczpz_05(self, access_web):
        time.sleep(4)
        # 添加配置
        access_web[15].zh_xtsz_zcgl_jczpz_01()
        # 设备类型
        access_web[15].zh_xtsz_zcgl_jczpz_04()
        # 清除版本
        access_web[15].zh_xtsz_zcgl_jczpz_05()
        # 版本输入
        access_web[15].zh_xtsz_zcgl_jczpz_06(9)
        # 表达式
        access_web[15].zh_xtsz_zcgl_jczpz_07(9)
        # 点击保存
        access_web[15].zh_xtsz_zcgl_jczpz_02()
        assert access_web[15].zh_xtsz_zcgl_jczpz_tsy() == "已存在"





    # 列表最后一个进行点击----输修改入表达式--点击保存

    def test_zh_stsz_dtgl_jczpz_06(self, access_web):
        time.sleep(5)
        # 点击列表最后一个
        access_web[15].zh_xtsz_zcgl_jczpz_08()
        # 清除版本
        access_web[15].zh_xtsz_zcgl_jczpz_05()
        # 版本输入
        access_web[15].zh_xtsz_zcgl_jczpz_06(8)
        # 点击保存
        access_web[15].zh_xtsz_zcgl_jczpz_02()
        assert access_web[15].zh_xtsz_zcgl_jczpz_tsy() == "修改成功！"



     # 列表点击最后一个进行点击-----点击删除
    def test_zh_stsz_dtgl_jczpz_07(self, access_web):
        time.sleep(5)
        # 点击列表最后一个
        access_web[15].zh_xtsz_zcgl_jczpz_08()
        # 删除
        access_web[15].zh_xtsz_zcgl_jczpz_09()
        assert access_web[15].zh_xtsz_zcgl_jczpz_tsy() == "删除成功!"

