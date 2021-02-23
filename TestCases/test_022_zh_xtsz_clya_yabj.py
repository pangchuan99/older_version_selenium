import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_zh_stsz_clya_yabj:


    # 添加+  点击保存
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_zh_stsz_clya_yabj_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        # 输入悬浮到策略预案---点击预案编辑
        access_web[20].zh_xtsz_clya_yabj()
        time.sleep(10)
        # 点击 +
        access_web[20].zh_xtsz_clya_yabj_01()
        # 点击保存
        access_web[20].zh_xtsz_clya_yabj_02()
        # 取消
        access_web[20].zh_xtsz_clya_yabj_023()
        assert access_web[20].zh_xtsz_clya_yabj_tsy()=="请输入名称"




    # 输入名称  --点击保存
    def test_zh_stsz_clya_yabj_02(self, access_web):
        time.sleep(3)
        # 点击 +
        access_web[20].zh_xtsz_clya_yabj_01()
        # 输入名称
        access_web[20].zh_xtsz_clya_yabj_03("脚本添加")
        # 点击保存
        access_web[20].zh_xtsz_clya_yabj_02()
        # 取消
        access_web[20].zh_xtsz_clya_yabj_023()
        assert access_web[20].zh_xtsz_clya_yabj_tsy()== "请选择类型"



    # 类型  --点击保存
    def test_zh_stsz_clya_yabj_03(self, access_web):

        time.sleep(3)
        # 点击 +
        access_web[20].zh_xtsz_clya_yabj_01()
        # 输入名称
        access_web[20].zh_xtsz_clya_yabj_03("脚本添加")
        # 类型
        access_web[20].zh_xtsz_clya_yabj_04()
        # 点击保存
        access_web[20].zh_xtsz_clya_yabj_02()
        # 取消
        access_web[20].zh_xtsz_clya_yabj_023()
        assert access_web[20].zh_xtsz_clya_yabj_tsy()== "请选择区域"




    def test_zh_stsz_clya_yabj_04(self, access_web):
        time.sleep(3)
        # 点击 +
        access_web[20].zh_xtsz_clya_yabj_01()
        # 输入名称
        access_web[20].zh_xtsz_clya_yabj_03("脚本添加")
        # 类型
        access_web[20].zh_xtsz_clya_yabj_04()
        # 影响区域
        access_web[20].zh_xtsz_clya_yabj_05()
        # 点击保存
        access_web[20].zh_xtsz_clya_yabj_02()
        assert access_web[20].zh_xtsz_clya_yabj_tsy()== "添加成功"





    def test_zh_stsz_clya_yabj_05(self, access_web):
        time.sleep(4)
        # 搜索框
        access_web[20].zh_xtsz_clya_yabj_027("脚本添加")
        # 搜索框确定
        access_web[20].zh_xtsz_clya_yabj_030()
        # 列表最后一个
        access_web[20].zh_xtsz_clya_yabj_06()
        # 点击下侧+
        access_web[20].zh_xtsz_clya_yabj_07()
        # 下侧 选择类型(双面车道指示器)
        access_web[20].zh_xtsz_clya_yabj_08()
        # 下侧弹出框点击全选
        access_web[20].zh_xtsz_clya_yabj_09()
        # 点击绑定
        access_web[20].zh_xtsz_clya_yabj_010()
        # 下侧保存
        access_web[20].zh_xtsz_clya_yabj_018()
        assert access_web[20].zh_xtsz_clya_yabj_tsy()== "修改成功"



    def test_zh_stsz_clya_yabj_06(self, access_web):
        time.sleep(3)
        # 点击下侧全选
        access_web[20].zh_xtsz_clya_yabj_011()
        # 优先级清除
        access_web[20].zh_xtsz_clya_yabj_012()
        # 优先级输入
        access_web[20].zh_xtsz_clya_yabj_013(3)
        # 间隔清除
        access_web[20].zh_xtsz_clya_yabj_014()
        # 间隔输入
        access_web[20].zh_xtsz_clya_yabj_015(4)
        # 是否确认
        access_web[20].zh_xtsz_clya_yabj_016()
        # 选择双面车道指示器
        access_web[20].zh_xtsz_clya_yabj_017()
        # 下侧保存
        access_web[20].zh_xtsz_clya_yabj_018()
        assert access_web[20].zh_xtsz_clya_yabj_tsy()== "修改成功"



    def test_zh_stsz_clya_yabj_07(self, access_web):
        time.sleep(3)
        # 下侧列表点击最后一个
        access_web[20].zh_xtsz_clya_yabj_019()
        # 下侧  （—）
        access_web[20].zh_xtsz_clya_yabj_020()
        # 删除弹出框
        access_web[20].zh_xtsz_clya_yabj_022()

        assert access_web[20].zh_xtsz_clya_yabj_tsy()== "删除成功"


    def test_zh_stsz_clya_yabj_08(self, access_web):
        time.sleep(3)

        # 列表最后一个
        access_web[20].zh_xtsz_clya_yabj_06()
        # 修改
        access_web[20].zh_xtsz_clya_yabj_026()
        # 名称清除
        access_web[20].zh_xtsz_clya_yabj_025()
        # 输入名称
        access_web[20].zh_xtsz_clya_yabj_03("修改的脚本添加")
        # 点击保存
        access_web[20].zh_xtsz_clya_yabj_02()
        assert access_web[20].zh_xtsz_clya_yabj_tsy() == "修改成功"







  #列表最后一个-------点击（-）
    def test_zh_stsz_clya_yabj_09(self, access_web):
        time.sleep(5)
        # 搜索框清除
        access_web[20].zh_xtsz_clya_yabj_028()
        # 搜索框
        access_web[20].zh_xtsz_clya_yabj_027("修改的脚本添加")
        # 搜索框确定
        access_web[20].zh_xtsz_clya_yabj_029()
        #列表最后一个
        access_web[20].zh_xtsz_clya_yabj_06()
        # 删除
        access_web[20].zh_xtsz_clya_yabj_024()
        # 删除弹出框
        access_web[20].zh_xtsz_clya_yabj_022()
        assert access_web[20].zh_xtsz_clya_yabj_tsy()== "删除成功"






