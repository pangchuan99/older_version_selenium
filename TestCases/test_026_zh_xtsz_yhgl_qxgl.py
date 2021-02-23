import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数

class  Test_zh_stsz_yhgl_qxgl:


    @pytest.mark.parametrize("data", LD.zcdl)
    def test_zh_stsz_yhgl_jsgl_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        # 输入悬浮到用户管理---点击权限管理
        access_web[24].zh_xtsz_qxgl()
        time.sleep(2)
        # 添加新权限
        access_web[24].zh_xtsz_yhgl_qxgl_01()
        # 点击保存
        access_web[24].zh_xtsz_yhgl_qxgl_02()
        assert access_web[24].zh_xtsz_yhgl_qxgl_tsy()=="请输入权限代码"





    def test_zh_stsz_yhgl_jsgl_02(self, access_web):
        time.sleep(3)
        # 添加新权限
        access_web[24].zh_xtsz_yhgl_qxgl_01()
        # 输入权限代码
        access_web[24].zh_xtsz_yhgl_qxgl_04("menu.pc")
        # 点击保存
        access_web[24].zh_xtsz_yhgl_qxgl_02()
        assert access_web[24].zh_xtsz_yhgl_qxgl_tsy() == "请输入权限名称"




    def test_zh_stsz_yhgl_jsgl_03(self, access_web):
        time.sleep(3)
        # 添加新权限
        access_web[24].zh_xtsz_yhgl_qxgl_01()
        # 输入权限代码
        access_web[24].zh_xtsz_yhgl_qxgl_04("menu.pc")
        # 输入权限名称
        access_web[24].zh_xtsz_yhgl_qxgl_06("自动测试")
        # 点击保存
        access_web[24].zh_xtsz_yhgl_qxgl_02()
        assert access_web[24].zh_xtsz_yhgl_qxgl_tsy() == "添加成功"




    def test_zh_stsz_yhgl_jsgl_04(self, access_web):
        time.sleep(4)
        # 添加新权限
        access_web[24].zh_xtsz_yhgl_qxgl_01()
        # 输入权限代码
        access_web[24].zh_xtsz_yhgl_qxgl_04("menu.pc")
        # 输入权限名称
        access_web[24].zh_xtsz_yhgl_qxgl_06("自动测试")
        # 点击保存
        access_web[24].zh_xtsz_yhgl_qxgl_02()
        assert access_web[24].zh_xtsz_yhgl_qxgl_tsy() == "已存在"




    def test_zh_stsz_yhgl_jsgl_05(self, access_web):
        time.sleep(3)
        # 列表最后一个
        access_web[24].zh_xtsz_yhgl_qxgl_08()
        # 清除权限名称
        access_web[24].zh_xtsz_yhgl_qxgl_07()
        # 输入权限名称
        access_web[24].zh_xtsz_yhgl_qxgl_06("自动测试123456")
        # 点击保存
        access_web[24].zh_xtsz_yhgl_qxgl_02()
        assert access_web[24].zh_xtsz_yhgl_qxgl_tsy() == "修改成功"




    def test_zh_stsz_yhgl_jsgl_06(self, access_web):
        time.sleep(3)
        # 列表最后一个
        access_web[24].zh_xtsz_yhgl_qxgl_08()
        # 删除
        time.sleep(1.5)
        access_web[24].zh_xtsz_yhgl_qxgl_03()
        assert access_web[24].zh_xtsz_yhgl_qxgl_tsy() == "删除成功"





