import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_jkxt_lxrpz:

     #左侧点击添加--左侧类型-公司--左侧名称--左侧保存
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_jkxt_lxrpz_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(1)
        # 账户进行鼠标悬浮---系统设置,点击联系人配置
        access_web[18].zh_xtsz_lxrpz()
        time.sleep(3)
        # 左侧点击添加
        access_web[18].zh_xtsz_lxrpz_01()
        time.sleep(1)
        # 左侧类型-公司
        access_web[18].zh_xtsz_lxrpz_02()
        time.sleep(1)
        # 左侧名称
        access_web[18].zh_xtsz_lxrpz_03("自动化公司")
        time.sleep(1)
        # 左侧保存
        access_web[18].zh_xtsz_lxrpz_04()

        time.sleep(1)
        # assert  access_web[18].zh_xtsz_lxrpz_01_1()=="公司、部门、电话和名字为必填"

     # 左侧点击添加--左侧类型-部门---左侧公司-公司---左侧名称进行清空---左侧名称-- 左侧保存
    def test_jkxt_lxrpz_02(self, access_web):
        time.sleep(3)
        # 左侧点击添加
        access_web[18].zh_xtsz_lxrpz_01()
        time.sleep(1)
        # 左侧类型-部门
        access_web[18].zh_xtsz_lxrpz_05()
        time.sleep(1)
        # 左侧公司-公司
        access_web[18].zh_xtsz_lxrpz_06()
        # 左侧名称进行清空
        access_web[18].zh_xtsz_lxrpz_07()
        time.sleep(1)
        # 左侧名称
        access_web[18].zh_xtsz_lxrpz_03("测试部门")
        time.sleep(1)
        # 左侧保存
        access_web[18].zh_xtsz_lxrpz_04()
        time.sleep(1)



     # 点击添加新成员---点击保存
    def test_jkxt_lxrpz_03(self, access_web):
        time.sleep(3)
        # 点击添加新成员-
        access_web[18].zh_xtsz_lxrpz_011()
        # 点击保存
        access_web[18].zh_xtsz_lxrpz_012()
        time.sleep(1)
        assert access_web[18].zh_xtsz_lxrpz_013() == "公司、部门、电话和名字为必填"




   # 输入姓名---点击保存
    def test_jkxt_lxrpz_04(self, access_web):
        time.sleep(3)
        # 点击添加新成员-
        access_web[18].zh_xtsz_lxrpz_011()
        # 输入姓名 -
        access_web[18].zh_xtsz_lxrpz_014("测试部门1")
        # 点击保存
        access_web[18].zh_xtsz_lxrpz_012()

        time.sleep(1)
        assert access_web[18].zh_xtsz_lxrpz_013() == "公司、部门、电话和名字为必填"





    # 输入姓名---点击保存
    def test_jkxt_lxrpz_05(self, access_web):
        time.sleep(3)
        # 点击添加新成员-
        access_web[18].zh_xtsz_lxrpz_011()
        # 输入姓名 -
        access_web[18].zh_xtsz_lxrpz_014("测试部门1")
        # 性别---
        access_web[18].zh_xtsz_lxrpz_015()
        # 点击保存
        access_web[18].zh_xtsz_lxrpz_012()

        time.sleep(1)
        assert access_web[18].zh_xtsz_lxrpz_013() == "公司、部门、电话和名字为必填"


   # 输入姓名---点击保存
    def test_jkxt_lxrpz_06(self, access_web):
        time.sleep(3)
        # 点击添加新成员-
        access_web[18].zh_xtsz_lxrpz_011()
        # 输入姓名 -
        access_web[18].zh_xtsz_lxrpz_014("测试部门1")
        # 性别---
        access_web[18].zh_xtsz_lxrpz_015()
        # 电话
        access_web[18].zh_xtsz_lxrpz_016(123456)
        # 点击保存
        access_web[18].zh_xtsz_lxrpz_012()
        time.sleep(1)
        assert access_web[18].zh_xtsz_lxrpz_013() == "公司、部门、电话和名字为必填"



    # 输入姓名---点击保存
    def test_jkxt_lxrpz_07(self, access_web):
        time.sleep(3)
        # 点击添加新成员-
        access_web[18].zh_xtsz_lxrpz_011()
        # 输入姓名 -
        access_web[18].zh_xtsz_lxrpz_014("测试部门1")
        # 性别---
        access_web[18].zh_xtsz_lxrpz_015()
        # 电话
        access_web[18].zh_xtsz_lxrpz_016(123456)
        # 公司--
        access_web[18].zh_xtsz_lxrpz_017()
        # 点击保存
        access_web[18].zh_xtsz_lxrpz_012()

        assert access_web[18].zh_xtsz_lxrpz_013() == "公司、部门、电话和名字为必填"





    # 输入姓名---点击保存
    def test_jkxt_lxrpz_08(self, access_web):
        time.sleep(3)
        # 点击添加新成员-
        access_web[18].zh_xtsz_lxrpz_011()
        # 输入姓名 -
        access_web[18].zh_xtsz_lxrpz_014("测试姓名1")
        # 性别---
        access_web[18].zh_xtsz_lxrpz_015()
        # 电话
        access_web[18].zh_xtsz_lxrpz_016(123456)
        # 公司--
        access_web[18].zh_xtsz_lxrpz_017()
        # 部门-
        access_web[18].zh_xtsz_lxrpz_018()
        # 职位
        access_web[18].zh_xtsz_lxrpz_019("你猜")
        # 点击保存
        access_web[18].zh_xtsz_lxrpz_012()

        time.sleep(1)
        assert access_web[18].zh_xtsz_lxrpz_013() == "添加成功"








    def test_jkxt_lxrpz_09(self, access_web):
        time.sleep(2.5)

        # 姓名搜索框
        access_web[18].zh_xtsz_lxrpz_025("测试姓名1")
        # 查询
        access_web[18].zh_xtsz_lxrpz_026()
        # 列表点击最后一个
        access_web[18].zh_xtsz_lxrpz_020()
        # 修改姓名
        access_web[18].zh_xtsz_lxrpz_021("测试姓名2")
        # 点击保存
        access_web[18].zh_xtsz_lxrpz_012()
        assert access_web[18].zh_xtsz_lxrpz_013() == "修改成功"








    def test_jkxt_lxrpz_010(self, access_web):
        time.sleep(2.5)
        # 姓名搜索框清除
        access_web[18].zh_xtsz_lxrpz_027()
        # 姓名搜索框
        access_web[18].zh_xtsz_lxrpz_025("测试姓名2")
        # 查询
        access_web[18].zh_xtsz_lxrpz_026()
        # 列表点击最后一个
        access_web[18].zh_xtsz_lxrpz_020()
        # 删除
        access_web[18].zh_xtsz_lxrpz_022()

        assert access_web[18].zh_xtsz_lxrpz_028() == "删除成功"




    def test_jkxt_lxrpz_011(self, access_web):
         time.sleep(3)
         # 左侧列表点击最后一个
         access_web[18].zh_xtsz_lxrpz_023()
         # 左侧 删除
         access_web[18].zh_xtsz_lxrpz_024()

         assert access_web[18].zh_xtsz_lxrpz_028() == "删除成功"





