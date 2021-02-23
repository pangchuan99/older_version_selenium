import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数

class  Test_dl_zbgl_dfgl:

    #点击添加新纪录----点击保存
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_dl_zbgl_dfgl_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        #鼠标悬浮值班管理--点击到访管理
        access_web[27].dl_zbgl_dfgl()
        time.sleep(2)
        #点击添加新纪录
        access_web[27].dl_zbgl_dfgl_01()
        #点击保存
        access_web[27].dl_zbgl_dfgl_02()
        assert access_web[27].dl_zbgl_dfgl_tsy()=="请输入姓名"


    #点击添加新纪录--输入姓名--点击保存
    def test_dl_zbgl_dfgl_02(self, access_web):
        time.sleep(4)
        # 点击添加新纪录
        access_web[27].dl_zbgl_dfgl_01()
        # 姓名
        access_web[27].dl_zbgl_dfgl_03("自动化添加的")
        # 点击保存
        access_web[27].dl_zbgl_dfgl_02()
        assert access_web[27].dl_zbgl_dfgl_tsy()== "请选择性别"



    # 点击添加新纪录--输入姓名---性别--点击保存
    def test_dl_zbgl_dfgl_03(self, access_web):
        time.sleep(4)
        # 点击添加新纪录
        access_web[27].dl_zbgl_dfgl_01()
        # 姓名
        access_web[27].dl_zbgl_dfgl_03("自动化添加的")
        # 性别---性别下拉内容选择
        access_web[27].dl_zbgl_dfgl_04()
        # 点击保存
        access_web[27].dl_zbgl_dfgl_02()
        assert access_web[27].dl_zbgl_dfgl_tsy() == "请输入正确的手机号"



    # 点击添加新纪录--输入姓名---性别---联系电话--点击保存
    def test_dl_zbgl_dfgl_04(self, access_web):
        time.sleep(4)
        # 点击添加新纪录
        access_web[27].dl_zbgl_dfgl_01()
        # 姓名
        access_web[27].dl_zbgl_dfgl_03("自动化添加的")
        # 性别---性别下拉内容选择
        access_web[27].dl_zbgl_dfgl_04()
        # 联系电话
        access_web[27].dl_zbgl_dfgl_05("13547324646")
        # 点击保存
        access_web[27].dl_zbgl_dfgl_02()
        assert access_web[27].dl_zbgl_dfgl_tsy() == "请输入正确的证件号"




    # 点击添加新纪录--输入姓名---性别---联系电话---证件号码--点击保存
    def test_dl_zbgl_dfgl_05(self, access_web):
        time.sleep(4)
        # 点击添加新纪录
        access_web[27].dl_zbgl_dfgl_01()
        # 姓名
        access_web[27].dl_zbgl_dfgl_03("自动化添加的")
        # 性别---性别下拉内容选择
        access_web[27].dl_zbgl_dfgl_04()
        # 联系电话
        access_web[27].dl_zbgl_dfgl_05("13547324646")
        #证件号码
        access_web[27].dl_zbgl_dfgl_06("147258369")
        # 点击保存
        access_web[27].dl_zbgl_dfgl_02()
        assert access_web[27].dl_zbgl_dfgl_tsy() == "请选择到访时间"




    # 点击添加新纪录--输入姓名---性别---联系电话---证件号码--点击保存
    def test_dl_zbgl_dfgl_06(self, access_web):
        time.sleep(4)
        # 点击添加新纪录
        access_web[27].dl_zbgl_dfgl_01()
        # 姓名
        access_web[27].dl_zbgl_dfgl_03("自动化添加的")
        # 性别---性别下拉内容选择
        access_web[27].dl_zbgl_dfgl_04()
        # 联系电话
        access_web[27].dl_zbgl_dfgl_05("13547324646")
        # 证件号码
        access_web[27].dl_zbgl_dfgl_06("147258369")
        # 到访时间
        access_web[27].dl_zbgl_dfgl_07("2020/03/28 08:09:10")
        # 点击保存
        access_web[27].dl_zbgl_dfgl_02()
        assert access_web[27].dl_zbgl_dfgl_tsy() == "添加成功"




    #姓名输入框 ---------点击查询-----------列表点击最后一个---------输入离开时间
    def test_dl_zbgl_dfgl_07(self, access_web):
        time.sleep(4)
        # 姓名搜索框
        access_web[27].dl_zbgl_dfgl_08("自动化添加的")
        #查询
        access_web[27].dl_zbgl_dfgl_09()
        # 列表取最后一个
        access_web[27].dl_zbgl_dfgl_010()
        # 离开时间
        access_web[27].dl_zbgl_dfgl_011("2020/04/02 10:10:15")
        # 点击保存
        access_web[27].dl_zbgl_dfgl_02()
        assert access_web[27].dl_zbgl_dfgl_tsy() == "修改成功"



    # 姓名输入框 ---------点击查询-----------列表点击最后一个---------输入离开时间
    def test_dl_zbgl_dfgl_08(self, access_web):
        time.sleep(5)
        # 列表取最后一个
        access_web[27].dl_zbgl_dfgl_010()
        # 点击保存
        access_web[27].dl_zbgl_dfgl_012()
        assert access_web[27].dl_zbgl_dfgl_tsy() == "删除成功"

