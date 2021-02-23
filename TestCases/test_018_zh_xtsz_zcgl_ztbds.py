import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_zh_stsz_dtgl_ztbds:


    @pytest.mark.parametrize("data", LD.zcdl)
    def test_zh_stsz_dtgl_ztbds_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        # 鼠标悬浮资产管理点击状态表达式
        access_web[13].zh_xtsz_zcgl_ztbds()
        time.sleep(2)
        # 添加表达式
        access_web[13].zh_xtsz_zcgl_ztbds_01()
        # 点击保存
        access_web[13].zh_xtsz_zcgl_ztbds_02()
        assert access_web[13].zh_xtsz_zcgl_ztbds_tsy()=="请选择设备类型"


    # 设备类型选择 点击保存
    def test_zh_stsz_dtgl_ztbds_02(self, access_web):
        time.sleep(3)
        # 添加表达式
        access_web[13].zh_xtsz_zcgl_ztbds_01()
        # 设备类型选择
        access_web[13].zh_xtsz_zcgl_ztbds_04()
        # 点击保存
        access_web[13].zh_xtsz_zcgl_ztbds_02()
        assert access_web[13].zh_xtsz_zcgl_ztbds_tsy()== "请选择状态"

    # 状态选择 点击保存
    def test_zh_stsz_dtgl_ztbds_03(self, access_web):
        time.sleep(3)
        # 添加表达式
        access_web[13].zh_xtsz_zcgl_ztbds_01()
        # 设备类型选择
        access_web[13].zh_xtsz_zcgl_ztbds_04()
        # 状态选择
        access_web[13].zh_xtsz_zcgl_ztbds_05()
        # 版本清空
        access_web[13].zh_xtsz_zcgl_ztbds_06()
        # 点击保存
        access_web[13].zh_xtsz_zcgl_ztbds_02()
        assert access_web[13].zh_xtsz_zcgl_ztbds_tsy()== "请输入版本"



     # 版本输入 点击保存
    def test_zh_stsz_dtgl_ztbds_04(self, access_web):
        time.sleep(4)
        # 添加表达式
        access_web[13].zh_xtsz_zcgl_ztbds_01()
        # 设备类型选择
        access_web[13].zh_xtsz_zcgl_ztbds_04()
        # 状态选择
        access_web[13].zh_xtsz_zcgl_ztbds_05()
        # 版本清空
        access_web[13].zh_xtsz_zcgl_ztbds_06()
        # 版本输入
        access_web[13].zh_xtsz_zcgl_ztbds_07("9")
        # 点击保存
        time.sleep(1)
        access_web[13].zh_xtsz_zcgl_ztbds_02()
        assert access_web[13].zh_xtsz_zcgl_ztbds_tsy()== "请输入表达式"

     # 表达式输入 点击保存
    def test_zh_stsz_dtgl_ztbds_05(self, access_web):
        # 添加表达式
        access_web[13].zh_xtsz_zcgl_ztbds_01()
        # 设备类型选择
        access_web[13].zh_xtsz_zcgl_ztbds_04()
        # 状态选择
        access_web[13].zh_xtsz_zcgl_ztbds_05()
        # 版本清空
        access_web[13].zh_xtsz_zcgl_ztbds_06()
        # 版本输入
        access_web[13].zh_xtsz_zcgl_ztbds_07(9)
        # 表达式输入
        access_web[13].zh_xtsz_zcgl_ztbds_08("1")
        # 点击保存
        access_web[13].zh_xtsz_zcgl_ztbds_02()
        assert access_web[13].zh_xtsz_zcgl_ztbds_tsy()== "添加成功！"





    def test_zh_stsz_dtgl_ztbds_06(self, access_web):
        time.sleep(5)
        # 分页
        access_web[13].zh_xtsz_zcgl_ztbds_09()
        # 列表最后一个
        access_web[13].zh_xtsz_zcgl_ztbds_010()
        # 版本清空
        access_web[13].zh_xtsz_zcgl_ztbds_06()
        # 版本输入
        access_web[13].zh_xtsz_zcgl_ztbds_07(88)
        # 点击保存
        access_web[13].zh_xtsz_zcgl_ztbds_02()
        assert access_web[13].zh_xtsz_zcgl_ztbds_tsy()== "修改成功！"





    def test_zh_stsz_dtgl_ztbds_07(self, access_web):
        time.sleep(5)
        # 分页
        access_web[13].zh_xtsz_zcgl_ztbds_09()
        # 列表最后一个
        access_web[13].zh_xtsz_zcgl_ztbds_010()
        # 点击删除
        access_web[13].zh_xtsz_zcgl_ztbds_011()
        assert access_web[13].zh_xtsz_zcgl_ztbds_tsy() == "删除成功!"

