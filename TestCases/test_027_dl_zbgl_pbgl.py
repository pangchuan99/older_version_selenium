import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数

class  Test_dl_zbgl_pbgl:

    # 点击班组  ---添加--输入名称---点击确定
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_dl_zbgl_pbgl_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        access_web[26].dl_zbgl_pbgl()
        time.sleep(2)
        #左侧---班组
        access_web[26].dl_zbgl_pbgl_02()
        # 左侧--班组里面进行点击-----添加
        access_web[26].dl_zbgl_pbgl_03()
        time.sleep(0.5)
        # 左侧--班组里面进行点击添加后--弹出框--- 输入名称
        access_web[26].dl_zbgl_pbgl_04("监控七班")
        # 左侧--班组里面进行点击添加后--弹出框--- 输入名称--点击确定
        access_web[26].dl_zbgl_pbgl_05()
        assert access_web[26].dl_zbgl_pbgl_01()=="添加成功"


    #点击添加新组员--点击保存
    def test_dl_zbgl_pbgl_02(self, access_web):
        time.sleep(4)
        # 左侧---班组
        access_web[26].dl_zbgl_pbgl_02()
        # 点击添加新组员
        access_web[26].dl_zbgl_pbgl_06()
        # 点击保存
        access_web[26].dl_zbgl_pbgl_07()
        assert access_web[26].dl_zbgl_pbgl_01() == "请选择班组"

    #点击添加新组员---班组--班组下拉内容--点击保存
    def test_dl_zbgl_pbgl_03(self, access_web):
        time.sleep(4)
        # 左侧---班组
        access_web[26].dl_zbgl_pbgl_02()
        # 点击添加新组员
        access_web[26].dl_zbgl_pbgl_06()
        # 班组
        access_web[26].dl_zbgl_pbgl_08()
        # 班组下拉内容(取pc)
        access_web[26].dl_zbgl_pbgl_09()
        # 点击保存
        access_web[26].dl_zbgl_pbgl_07()
        assert access_web[26].dl_zbgl_pbgl_01() == "请输入姓名"



    # 点击添加新组员---班组--班组下拉内容--点击保存
    def test_dl_zbgl_pbgl_04(self, access_web):
        time.sleep(4)
        # 左侧---班组
        access_web[26].dl_zbgl_pbgl_02()
        # 点击添加新组员
        access_web[26].dl_zbgl_pbgl_06()
        # 班组
        access_web[26].dl_zbgl_pbgl_08()
        # 班组下拉内容(取最后一个)
        access_web[26].dl_zbgl_pbgl_09()
        # 姓名
        access_web[26].dl_zbgl_pbgl_010()
        # 姓名下拉内容取第一个
        access_web[26].dl_zbgl_pbgl_011()
        # 点击保存
        access_web[26].dl_zbgl_pbgl_07()
        assert access_web[26].dl_zbgl_pbgl_01() == "添加成功"


    # 左侧点击排班---点击当日日历，班组以及下拉内容--点击确定
    def test_dl_zbgl_pbgl_010(self, access_web):
        time.sleep(4)
        # 左侧--点击排班
        access_web[26].dl_zbgl_pbgl_018()
        #  点击今日日历
        time.sleep(1)
        access_web[26].dl_zbgl_pbgl_019()
        time.sleep(0.5)
        # 点击班组--下拉内容
        access_web[26].dl_zbgl_pbgl_020()
        time.sleep(0.5)
        # 确定
        access_web[26].dl_zbgl_pbgl_021()
        assert access_web[26].dl_zbgl_pbgl_01() == "修改保存成功"





    # 交接班---点击交接班--提交
    def test_dl_zbgl_pbgl_011(self, access_web):
        time.sleep(4)
        # 左侧--点击交接班
        access_web[26].dl_zbgl_pbgl_022()
        # 交接班---提交
        time.sleep(1)
        access_web[26].dl_zbgl_pbgl_023()
        assert access_web[26].dl_zbgl_pbgl_01() == "请填写今日完成工作"



    # 交接班---今日完成工作---提交
    def test_dl_zbgl_pbgl_012(self, access_web):
        time.sleep(4)
        # 左侧--点击交接班
        access_web[26].dl_zbgl_pbgl_022()
        # 交接班----今日完成工作
        access_web[26].dl_zbgl_pbgl_024("今日工作内容有：第一个 第二个  第三个")
        # 交接班---提交
        time.sleep(1)
        access_web[26].dl_zbgl_pbgl_023()
        assert access_web[26].dl_zbgl_pbgl_01() == "请选择交接班班组!"



    # 交接班---今日完成工作---提交
    def test_dl_zbgl_pbgl_013(self, access_web):
        time.sleep(4)
        # 左侧--点击交接班
        access_web[26].dl_zbgl_pbgl_022()
        # 交接班----今日完成工作(文本内容进行清空)
        access_web[26].dl_zbgl_pbgl_028()
        # 交接班----今日完成工作
        access_web[26].dl_zbgl_pbgl_024("今日工作内容有：第一个 第二个  第三个123456")
        # 交接班----点击+
        access_web[26].dl_zbgl_pbgl_025()
        # 交接班----点击+号后---选择最后一个
        access_web[26].dl_zbgl_pbgl_026()
        # 交接班----点击确定
        access_web[26].dl_zbgl_pbgl_027()

        # 交接班---提交
        time.sleep(1)
        access_web[26].dl_zbgl_pbgl_023()
        assert access_web[26].dl_zbgl_pbgl_01() == "交接班成功"




    # 添加新组员列表最后一个他 -------备注进行修改
    def test_dl_zbgl_pbgl_05(self, access_web):
        time.sleep(4)
        # 左侧---班组
        access_web[26].dl_zbgl_pbgl_02()
        #添加新组员列表取最后一个
        access_web[26].dl_zbgl_pbgl_012()
        #备注
        access_web[26].dl_zbgl_pbgl_013("修改的")
        # 点击保存
        access_web[26].dl_zbgl_pbgl_07()
        assert access_web[26].dl_zbgl_pbgl_01() == "修改成功"




    # 添加新组员列表最后一个------进行删除
    def test_dl_zbgl_pbgl_06(self, access_web):
        time.sleep(4)
        # 左侧---班组
        access_web[26].dl_zbgl_pbgl_02()
        # 添加新组员列表取最后一个
        access_web[26].dl_zbgl_pbgl_012()
        # 删除
        access_web[26].dl_zbgl_pbgl_014()
        assert access_web[26].dl_zbgl_pbgl_01() == "删除成功"



    #左侧列表取最后一个---进行双击点击
    def test_dl_zbgl_pbgl_07(self, access_web):
        time.sleep(4)
        # 左侧---班组
        access_web[26].dl_zbgl_pbgl_02()
        #左侧---班组
        access_web[26].dl_zbgl_pbgl_02()
        # 左侧--班组里面进行点击-----添加
        access_web[26].dl_zbgl_pbgl_03()
        time.sleep(0.5)
        # 左侧--班组里面进行点击添加后--弹出框--- 输入名称
        access_web[26].dl_zbgl_pbgl_04("监控七班")
        # 左侧--班组里面进行点击添加后--弹出框--- 输入名称--点击确定
        access_web[26].dl_zbgl_pbgl_05()
        assert access_web[26].dl_zbgl_pbgl_01() == "班组名称不能相同"


    # 左侧列表取最后一个---进行双击点击
    def test_dl_zbgl_pbgl_09(self, access_web):
        time.sleep(4)
        # 左侧---班组
        access_web[26].dl_zbgl_pbgl_02()
        # 点击最后一个进行选择
        access_web[26].dl_zbgl_pbgl_016()
        # 点击左侧这边的删除
        access_web[26].dl_zbgl_pbgl_017()
        assert access_web[26].dl_zbgl_pbgl_01() == "删除成功"


