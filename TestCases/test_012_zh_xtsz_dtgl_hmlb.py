import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_zh_stsz_dtgl_hmlb:


    @pytest.mark.parametrize("data", LD.zcdl)
    def test_zh_stsz_dtgl_hmlb_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        #  鼠标悬浮地图管理--------点击画面列表
        access_web[7].zh_xtsz_dtgl_hmlb()
        time.sleep(10)
        # 点击查询
        access_web[7].zh_xtsz_dtgl_hmlb_03()
        # 点击添加新画面
        access_web[7]. zh_xtsz_dtgl_hmlb_01()
        # 保存
        access_web[7].zh_xtsz_dtgl_hmlb_04()
        assert access_web[7].zh_xtsz_dtgl_hmlb_06()=="必须包含画面名称"





    def test_zh_stsz_dtgl_hmlb_02(self, access_web):
        time.sleep(3.5)
        # 点击添加新画面
        access_web[7].zh_xtsz_dtgl_hmlb_01()
        # 名称
        time.sleep(0.5)
        access_web[7].zh_xtsz_dtgl_hmlb_07("测试自动化001")
        # 保存
        time.sleep(0.5)
        access_web[7].zh_xtsz_dtgl_hmlb_04()
        assert access_web[7].zh_xtsz_dtgl_hmlb_06() == "必须选择结构物"




    def test_zh_stsz_dtgl_hmlb_03(self, access_web):
        time.sleep(3.5)
        # 点击添加新画面
        access_web[7].zh_xtsz_dtgl_hmlb_01()
        # 名称
        time.sleep(0.5)
        access_web[7].zh_xtsz_dtgl_hmlb_07("测试自动化001")
        # 选择结构物
        time.sleep(0.5)
        access_web[7].zh_xtsz_dtgl_hmlb_09()
        # 保存
        time.sleep(0.5)
        access_web[7].zh_xtsz_dtgl_hmlb_04()
        assert access_web[7].zh_xtsz_dtgl_hmlb_06() == "必须上传切片压缩包"




    def test_zh_stsz_dtgl_hmlb_04(self, access_web):
        time.sleep(5)
        # 点击添加新画面
        access_web[7].zh_xtsz_dtgl_hmlb_01()
        time.sleep(0.5)
        # 名称
        access_web[7].zh_xtsz_dtgl_hmlb_07("测试自动化001")
        time.sleep(0.5)
        # 选择结构物
        access_web[7].zh_xtsz_dtgl_hmlb_09()
        time.sleep(1)
        # 矢量底图
        access_web[7].zh_xtsz_dtgl_hmlb_010("23465789")
        time.sleep(1)
        # 保存
        access_web[7].zh_xtsz_dtgl_hmlb_04()
        time.sleep(1.5)
        assert access_web[7].zh_xtsz_dtgl_hmlb_06() == "添加成功"




    def test_zh_stsz_dtgl_hmlb_05(self, access_web):
        time.sleep(6)

        # 名称搜索框
        access_web[7].zh_xtsz_dtgl_hmlb_02("测试自动化001")
        time.sleep(0.5)
        # 点击查询
        access_web[7].zh_xtsz_dtgl_hmlb_03()
        time.sleep(0.5)
        # 列表最后一个
        access_web[7].zh_xtsz_dtgl_hmlb_011()
        time.sleep(0.5)
        # 名称--------进行清除
        access_web[7].zh_xtsz_dtgl_hmlb_012()
        time.sleep(0.5)
        # 名称
        access_web[7].zh_xtsz_dtgl_hmlb_07("测试自动化002")
        # 保存
        access_web[7].zh_xtsz_dtgl_hmlb_04()
        assert access_web[7].zh_xtsz_dtgl_hmlb_06() == "更新成功"




    def test_zh_stsz_dtgl_hmlb_06(self, access_web):
        time.sleep(4)
        # 名称搜索框----进行清除
        access_web[7].zh_xtsz_dtgl_hmlb_013()
        # 名称搜索框
        access_web[7].zh_xtsz_dtgl_hmlb_02("测试自动化002")
        # 点击查询
        access_web[7].zh_xtsz_dtgl_hmlb_03()
        # 列表最后一个
        access_web[7].zh_xtsz_dtgl_hmlb_011()
        #删除
        access_web[7].zh_xtsz_dtgl_hmlb_05()
        assert access_web[7].zh_xtsz_dtgl_hmlb_06() == "删除成功!"







    def test_zh_stsz_dtgl_hmlb_07(self, access_web):
        time.sleep(4)
        # 点击添加新画面
        access_web[7].zh_xtsz_dtgl_hmlb_01()
        # 画面列表--隧道
        access_web[7].zh_xtsz_dtgl_hmlb_08()
        # 保存
        access_web[7].zh_xtsz_dtgl_hmlb_04()
        assert access_web[7].zh_xtsz_dtgl_hmlb_06() == "必须包含画面名称"



    def test_zh_stsz_dtgl_hmlb_08(self, access_web):
        time.sleep(4)
        # 点击添加新画面
        access_web[7].zh_xtsz_dtgl_hmlb_01()
        # 画面列表--隧道
        access_web[7].zh_xtsz_dtgl_hmlb_08()
        # 名称
        access_web[7].zh_xtsz_dtgl_hmlb_07("测试自动化003")
        # 保存
        access_web[7].zh_xtsz_dtgl_hmlb_04()

        assert access_web[7].zh_xtsz_dtgl_hmlb_06() == "必须选择结构物"




    def test_zh_stsz_dtgl_hmlb_09(self, access_web):
        time.sleep(4)
        # 点击添加新画面
        access_web[7].zh_xtsz_dtgl_hmlb_01()
        # 画面列表--隧道
        access_web[7].zh_xtsz_dtgl_hmlb_08()
        # 名称
        access_web[7].zh_xtsz_dtgl_hmlb_07("测试自动化003")
        # 选择结构物
        access_web[7].zh_xtsz_dtgl_hmlb_09()
        # 保存
        access_web[7].zh_xtsz_dtgl_hmlb_04()
        assert access_web[7].zh_xtsz_dtgl_hmlb_06() == "添加成功"




    def test_zh_stsz_dtgl_hmlb_010(self, access_web):
        time.sleep(4)
        # 名称搜索框----进行清除
        access_web[7].zh_xtsz_dtgl_hmlb_013()
        # 名称搜索框
        access_web[7].zh_xtsz_dtgl_hmlb_02("测试自动化003")
        # 点击查询
        access_web[7].zh_xtsz_dtgl_hmlb_03()
        # 列表最后一个
        access_web[7].zh_xtsz_dtgl_hmlb_011()
        # 名称--------进行清除
        access_web[7].zh_xtsz_dtgl_hmlb_012()
        # 名称
        access_web[7].zh_xtsz_dtgl_hmlb_07("测试自动化004")
        # 保存
        access_web[7].zh_xtsz_dtgl_hmlb_04()
        assert access_web[7].zh_xtsz_dtgl_hmlb_06() == "更新成功"




    def test_zh_stsz_dtgl_hmlb_011(self, access_web):
        time.sleep(5)
        # 名称搜索框----进行清除
        access_web[7].zh_xtsz_dtgl_hmlb_013()
        # 名称搜索框
        access_web[7].zh_xtsz_dtgl_hmlb_02("测试自动化004")
        # 点击查询
        access_web[7].zh_xtsz_dtgl_hmlb_03()
        # 列表最后一个
        access_web[7].zh_xtsz_dtgl_hmlb_011()
        # 删除
        access_web[7].zh_xtsz_dtgl_hmlb_05()
        assert access_web[7].zh_xtsz_dtgl_hmlb_06() == "删除成功!"










