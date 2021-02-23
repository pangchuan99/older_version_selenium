import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_zh_stsz_yhgl_jsgl:



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
        # 鼠标悬浮到用户管理---点击角色管理
        access_web[23].zh_xtsz_jsgl()
        time.sleep(2)
        # 添加新角色
        access_web[23].zh_xtsz_yhgl_jsgl_01()
        # 保存
        access_web[23].zh_xtsz_yhgl_jsgl_02()
        assert access_web[23].zh_xtsz_yhgl_jsgl_tsy()=="请输入角色名(50个字符以内)"





    def test_zh_stsz_yhgl_jsgl_02(self,access_web):
        time.sleep(3)
        # 添加新角色
        access_web[23].zh_xtsz_yhgl_jsgl_01()
        # 输入角色名
        access_web[23].zh_xtsz_yhgl_jsgl_03("自动测试")
        # 类型
        access_web[23].zh_xtsz_yhgl_jsgl_05()
        # 保存
        access_web[23].zh_xtsz_yhgl_jsgl_02()
        assert access_web[23].zh_xtsz_yhgl_jsgl_tsy() == "请选择权限"





    def test_zh_stsz_yhgl_jsgl_03(self,access_web):
        time.sleep(3)
        # 添加新角色
        access_web[23].zh_xtsz_yhgl_jsgl_01()
        # 输入角色名
        access_web[23].zh_xtsz_yhgl_jsgl_03("自动测试")
        # 类型
        access_web[23].zh_xtsz_yhgl_jsgl_05()
        # 权限
        access_web[23].zh_xtsz_yhgl_jsgl_06()
        # 保存
        access_web[23].zh_xtsz_yhgl_jsgl_02()

        assert access_web[23].zh_xtsz_yhgl_jsgl_tsy() == "添加成功"


    def test_zh_stsz_yhgl_jsgl_04(self,access_web):
        time.sleep(3)
        # 添加新角色
        access_web[23].zh_xtsz_yhgl_jsgl_01()
        # 输入角色名
        access_web[23].zh_xtsz_yhgl_jsgl_03("自动测试")
        # 类型
        access_web[23].zh_xtsz_yhgl_jsgl_05()
        # 权限
        access_web[23].zh_xtsz_yhgl_jsgl_06()
        # 保存
        access_web[23].zh_xtsz_yhgl_jsgl_02()
        assert access_web[23].zh_xtsz_yhgl_jsgl_tsy() == "角色已存在"






    def test_zh_stsz_yhgl_jsgl_05(self,access_web):
        time.sleep(3)
        # 列表最后一个
        access_web[23].zh_xtsz_yhgl_jsgl_07()
        # 角色名清除
        access_web[23].zh_xtsz_yhgl_jsgl_04()
        # 输入角色名
        access_web[23].zh_xtsz_yhgl_jsgl_03("自动测试123")
        # 保存
        access_web[23].zh_xtsz_yhgl_jsgl_02()
        assert access_web[23].zh_xtsz_yhgl_jsgl_tsy() == "修改成功"



    def test_zh_stsz_yhgl_jsgl_06(self, access_web):
        time.sleep(3)
        # 列表最后一个
        access_web[23].zh_xtsz_yhgl_jsgl_07()
        # 点击删除
        access_web[23].zh_xtsz_yhgl_jsgl_08()
        assert access_web[23].zh_xtsz_yhgl_jsgl_tsy() == "删除成功"




