import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_zh_stsz_dtgl_qybj:

     #点击添加新区域---提示---请选择区域类型
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_zh_stsz_dtgl_qybj_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)

        # 鼠标悬浮到地图管理 点击区域编辑
        access_web[8].zh_xtsz_dtgl_qybj()
        time.sleep(25)
        # 点击查询
        access_web[8]. zh_xtsz_dtgl_qybj_02()

        # 点击添加新区域
        access_web[8].zh_xtsz_dtgl_qybj_01()
        # 点击保存
        access_web[8].zh_xtsz_dtgl_qybj_03()
        assert access_web[8]. zh_xtsz_dtgl_qybj_tsy()=="请选择区域类型"



    def test_zh_stsz_dtgl_qybj_02(self,access_web):
        time.sleep(5)
        # 点击添加新区域
        access_web[8].zh_xtsz_dtgl_qybj_01()
        # 点击区域类型
        access_web[8].zh_xtsz_dtgl_qybj_04()
        # 点击保存
        access_web[8].zh_xtsz_dtgl_qybj_03()
        assert access_web[8]. zh_xtsz_dtgl_qybj_tsy()=="请输入区域名称"



     # 输入名称   对应结构物  点击保存
    def test_zh_stsz_dtgl_qybj_03(self,access_web):
        time.sleep(3)
        # 点击添加新区域
        access_web[8].zh_xtsz_dtgl_qybj_01()
        # 点击区域类型
        access_web[8].zh_xtsz_dtgl_qybj_04()
        # 输入名称名称
        access_web[8].zh_xtsz_dtgl_qybj_05("自动测试添加")
        #  对应结构物
        access_web[8].zh_xtsz_dtgl_qybj_07()
        # 点击保存
        access_web[8].zh_xtsz_dtgl_qybj_03()
        assert access_web[8]. zh_xtsz_dtgl_qybj_tsy()=="添加成功"

    # # 输入名称   对应结构物  点击保存
    # def test_zh_stsz_dtgl_qybj_04(self, access_web):
    #     time.sleep(2)
    #     access_web[8].zh_xtsz_dtgl_qybj_tsy01()
    #     time.sleep(3)
    #     access_web[8].zh_xtsz_dtgl_qybj_tsy02()
    #     time.sleep(3)
    #     access_web[8].zh_xtsz_dtgl_qybj_tsy03("添加的名称")
    #     time.sleep(3)
    #     access_web[8].zh_xtsz_dtgl_qybj_tsy04()
    #     assert access_web[8].zh_xtsz_dtgl_qybj_tsy04_4() == "添加成功"




    def test_zh_stsz_dtgl_qybj_07(self, access_web):
        time.sleep(2)
        # 点击添加新区域
        access_web[8].zh_xtsz_dtgl_qybj_01()
        # 点击区域类型
        access_web[8].zh_xtsz_dtgl_qybj_04()
        # 输入名称名称
        access_web[8].zh_xtsz_dtgl_qybj_05("自动测试添加")
        #  对应结构物
        access_web[8].zh_xtsz_dtgl_qybj_07()
        # 点击保存
        access_web[8].zh_xtsz_dtgl_qybj_03()
        assert access_web[8].zh_xtsz_dtgl_qybj_tsy() == "已存在"




    # 修改名称名称   点击保存
    def test_zh_stsz_dtgl_qybj_05(self, access_web):
         time.sleep(2)
         # 点击列表最后一个
         access_web[8].zh_xtsz_dtgl_qybj_08()
         # 名称清除
         access_web[8].zh_xtsz_dtgl_qybj_06()
         # 输入名称名称
         access_web[8].zh_xtsz_dtgl_qybj_05("修改后的名称")
         # 点击保存
         access_web[8].zh_xtsz_dtgl_qybj_03()
         assert access_web[8].zh_xtsz_dtgl_qybj_tsy() == "修改成功"




    #删除
    def test_zh_stsz_dtgl_qybj_06(self, access_web):
         time.sleep(2)
         # 点击列表最后一个
         access_web[8].zh_xtsz_dtgl_qybj_08()
         # 进行删除
         access_web[8].zh_xtsz_dtgl_qybj_09()

         assert access_web[8].zh_xtsz_dtgl_qybj_tsy() == "删除成功"