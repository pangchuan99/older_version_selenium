import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_zh_stsz_dtgl_lxbj:



    @pytest.mark.parametrize("data", LD.zcdl)
    def test_zh_stsz_dtgl_lxbj_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        # 鼠标悬浮到地图管理 点击类型编辑
        access_web[12].zh_xtsz_zcgl_lxbj()
        time.sleep(2)
        # 添加类型
        access_web[12]. zh_xtsz_zcgl_lxbj_01()
        # 点击保存
        access_web[12]. zh_xtsz_zcgl_lxbj_04()
        assert access_web[12]. zh_xtsz_zcgl_lxbj_tsy()=="请输入类型ID"



    def test_zh_stsz_dtgl_lxbj_02(self, access_web):
        time.sleep(3)
        # 添加类型
        access_web[12].zh_xtsz_zcgl_lxbj_01()
        # 输入类型ID
        access_web[12].zh_xtsz_zcgl_lxbj_06("GSM_PC")
        # 点击保存
        access_web[12].zh_xtsz_zcgl_lxbj_04()
        assert access_web[12].zh_xtsz_zcgl_lxbj_tsy() == "请选择分组"




    # 输入分组ID 点击保存
    def test_zh_stsz_dtgl_lxbj_03(self, access_web):
        time.sleep(3)
        # 添加类型
        access_web[12].zh_xtsz_zcgl_lxbj_01()
        # 输入类型ID
        access_web[12].zh_xtsz_zcgl_lxbj_06("GSM_PC")
        # 选择分组ID
        access_web[12].zh_xtsz_zcgl_lxbj_07()
        # 点击保存
        access_web[12].zh_xtsz_zcgl_lxbj_04()
        assert access_web[12].zh_xtsz_zcgl_lxbj_tsy() == "请输入类型名称"


    # 输入类型名称 点击保存
    def test_zh_stsz_dtgl_lxbj_04(self, access_web):
        time.sleep(3)
        # 添加类型
        access_web[12].zh_xtsz_zcgl_lxbj_01()
        # 输入类型ID
        access_web[12].zh_xtsz_zcgl_lxbj_06("GSM_PC")
        # 选择分组ID
        access_web[12].zh_xtsz_zcgl_lxbj_07()
        # 输入类型名称
        access_web[12].zh_xtsz_zcgl_lxbj_08("测试自动化")
        # 点击保存
        access_web[12].zh_xtsz_zcgl_lxbj_04()
        assert access_web[12].zh_xtsz_zcgl_lxbj_tsy() == "变量名格式错误!"

    # 输入类型参数 点击保存---添加
    # @pytest.mark.usefixtures("refresh_page")
    def test_zh_stsz_dtgl_lxbj_05(self, access_web):
        time.sleep(4.5)
        # 添加类型
        access_web[12].zh_xtsz_zcgl_lxbj_01()
        # 输入类型ID
        access_web[12].zh_xtsz_zcgl_lxbj_06("GSM_PC")
        # 选择分组ID
        access_web[12].zh_xtsz_zcgl_lxbj_07()
        # 输入类型名称
        access_web[12].zh_xtsz_zcgl_lxbj_08("测试自动化")
        # 输入类型参数(变量名)
        access_web[12].zh_xtsz_zcgl_lxbj_09("102")
        # 点击保存
        access_web[12].zh_xtsz_zcgl_lxbj_04()
        assert access_web[12].zh_xtsz_zcgl_lxbj_tsy() == "添加成功!"

    # 输入类型id  分组id  类型名称  类型参数   点击保存
    def test_zh_stsz_dtgl_xlbj_06(self, access_web):
        time.sleep(3)
        # 添加类型
        access_web[12].zh_xtsz_zcgl_lxbj_01()
        # 输入类型ID
        access_web[12].zh_xtsz_zcgl_lxbj_06("GSM_PC")
        # 选择分组ID
        access_web[12].zh_xtsz_zcgl_lxbj_07()
        # 输入类型名称
        access_web[12].zh_xtsz_zcgl_lxbj_08("测试自动化")
        # 输入类型参数(变量名)
        access_web[12].zh_xtsz_zcgl_lxbj_09("102")
        # 点击保存
        access_web[12].zh_xtsz_zcgl_lxbj_04()
        assert access_web[12].zh_xtsz_zcgl_lxbj_tsy()=="类型已存在"



    # 点击列表中最后一个进行修改
    def test_zh_stsz_dtgl_lxbj_07(self, access_web):
        time.sleep(4)
        # 类型名称搜索框
        access_web[12].zh_xtsz_zcgl_lxbj_02("测试自动化")
        # 查询
        access_web[12].zh_xtsz_zcgl_lxbj_03()
        # 列表点击最后一个
        access_web[12].zh_xtsz_zcgl_lxbj_010()
        # 类型名称清除
        access_web[12].zh_xtsz_zcgl_lxbj_011()
        # 输入类型名称
        access_web[12].zh_xtsz_zcgl_lxbj_08("测试自动化123465")
        # 点击保存
        access_web[12].zh_xtsz_zcgl_lxbj_04()
        assert access_web[12].zh_xtsz_zcgl_lxbj_tsy()=="修改成功!"



    # 点击列表中最后一个进行删除
    def test_zh_stsz_dtgl_lxbj_08(self, access_web):
        time.sleep(5)
        # 列表点击最后一个
        access_web[12].zh_xtsz_zcgl_lxbj_010()
        # 删除
        access_web[12].zh_xtsz_zcgl_lxbj_05()
        assert access_web[12].zh_xtsz_zcgl_lxbj_tsy()== "删除成功"





