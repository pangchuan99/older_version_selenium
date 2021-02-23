import pytest
import  os
from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time
import allure
from TestDatas.get_name import get_name0,get_name1,get_name_wenjianmingcheng   #这个文件写了 数据库 写入数据到文件
import json
import yaml

# @pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数
class  Test_dl_zcgl_sbbx_gjy:

    @pytest.mark.parametrize("data", LD.zcdl)
    @pytest.mark.usefixtures("sx")
    def test_dl_zhjk_sbjk_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(5)




    # #这个是查询郭家窑双面车道指示器的版本为0的   远程正面通行    远程禁止  远程反面通行
    sql_gjy_smcdzsq0 = 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid  INNER JOIN remote a3 on a2.version=a3.version  and a1.type="ZSB_PT3" AND a1.region="d4f0b6a0-fb88-11e9-bda2-af263eb7555a"  AND a2.version=0'

    get_name0(sql_gjy_smcdzsq0,"get_name_gjy_smzdzsqwenjian_0.yaml")
    yamlpath_gjy_smcdzsq0= get_name_wenjianmingcheng("get_name_gjy_smzdzsqwenjian_0.yaml")
    @allure.feature("郭家窑双面车道指示器的版本为0的   远程正面通行指令模块")
    @allure.story("test_dl_zcgl_sbbx_01_1   郭家窑双面车道指示器的版本为0的---远程正面通行----story")
    @pytest.mark.parametrize("data1",yamlpath_gjy_smcdzsq0)
    @allure.title("test_dl_zcgl_sbbx_01_1   郭家窑双面车道指示器的版本为0的---远程正面通行{data1}")


    @allure.description("这个用例是对郭家窑双面车道指示器的版本为0的   进行远程正面通行下发指令")
    def test_dl_zcgl_sbbx_01_1(self, access_web, sx,data1):


        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(15)
        access_web[35].dl_zhjk_sbjk_gjy()

        #点击郭家窑堡隧道
        time.sleep(5)
        access_web[35].dl_zhjk_sbjk_gjy_01()

        #左侧搜索框
        time.sleep(13)
        access_web[35].dl_zhjk_sbjk_gjy_02(data1["name"])


        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_04()
        # 判断是否是  下面这个三种状态
        time.sleep(7)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() in ["远程正面通行" ,"远程禁止" ,"远程反面通行"]

        #获取初始状态的值
        time.sleep(3)
        a1=access_web[35].dl_zhjk_sbjk_gjy_09()
        print("获取他的值是：{}".format(a1))

        # 点击双面车道指示器状态---远程正面通行
        time.sleep(6)
        access_web[35].dl_zhjk_sbjk_gjy_05()
        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy()=="指令下发成功"
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"
        time.sleep(5)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程正面通行"
        time.sleep(7)
        # 他是进行还原最初状态的
        access_web[35].dl_zhjk_sbjk_gjy_029(a1,access_web)



    @allure.feature("郭家窑双面车道指示器的版本为0的   远程禁止指令模块")
    @allure.story("test_dl_zcgl_sbbx_02   郭家窑双面车道指示器的版本为0的---远程禁止----story")
    @allure.title("test_dl_zcgl_sbbx_02   郭家窑双面车道指示器的版本为0的---远程禁止")
    @pytest.mark.parametrize("data1",yamlpath_gjy_smcdzsq0)
    @allure.description("这个用例是对郭家窑双面车道指示器的版本为0的   进行远程禁止下发指令")
    def test_dl_zcgl_sbbx_02(self,access_web,sx,data1):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(15)
        access_web[35].dl_zhjk_sbjk_gjy()


        # 点击郭家窑隧道
        time.sleep(5)
        access_web[35].dl_zhjk_sbjk_gjy_01()

        # 左侧搜索框
        time.sleep(15)
        access_web[35].dl_zhjk_sbjk_gjy_02(data1["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_03()

        # 左侧列表点击第一个
        access_web[35].dl_zhjk_sbjk_gjy_04()

        # 判断是否是  下面这个三种状态
        time.sleep(3)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() in ["远程正面通行" ,"远程禁止" ,"远程反面通行"]

        time.sleep(7)
        # 获取初始状态的值
        a1 = access_web[35].dl_zhjk_sbjk_gjy_09()

        # 点击双面车道指示器状态---远程禁止.
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_06()

        time.sleep(3)
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"

        time.sleep(3)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程禁止"
        time.sleep(7)
        # 他是进行还原最初状态的
        access_web[35].dl_zhjk_sbjk_gjy_029(a1, access_web)



    @allure.feature("郭家窑双面车道指示器的版本为0的    远程反面通行指令模块")
    @allure.story("test_dl_zcgl_sbbx_03    郭家窑双面车道指示器的版本为0的---远程反面通行----story")
    @allure.title("test_dl_zcgl_sbbx_03    郭家窑双面车道指示器的版本为0的---远程反面通行")
    @allure.description("这个用例是对郭家窑双面车道指示器的版本为0的    进行远程反面通行下发指令")
    @pytest.mark.parametrize("data1",yamlpath_gjy_smcdzsq0)
    def test_dl_zcgl_sbbx_03(self,access_web,sx,data1):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy()


        # 点击郭家窑隧道
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy_02(data1["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_04()

        time.sleep(3)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() in ["远程正面通行" ,"远程禁止" ,"远程反面通行"]

        # 获取初始状态的值
        time.sleep(3)
        a1 = access_web[35].dl_zhjk_sbjk_gjy_09()

        # 点击双面车道指示器状态---远程反面通行
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_07()
        time.sleep(3)
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"

        time.sleep(3)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程反面通行"
        time.sleep(7)
        # 他是进行还原最初状态的
        access_web[35].dl_zhjk_sbjk_gjy_029(a1, access_web)








    #这个是查询郭家窑洞口交通灯4控的  他的状态有    远程关  远程正转  远程反转
    sql_gjy_sk_0= 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_PH2" AND a1.region="d4f0b6a0-fb88-11e9-bda2-af263eb7555a"  AND a2.version=0'
    get_name0(sql_gjy_sk_0,"get_name_gjy_sikongjiaotongwenjian_0.yaml")
    yamlpath_gjy_sk0= get_name_wenjianmingcheng("get_name_gjy_sikongjiaotongwenjian_0.yaml")
    @allure.feature("郭家窑洞口交通灯4控  远程红 远程黄 远程绿  远程红+转向   指令模块")
    @allure.story("郭家窑洞口交通灯4控    洞口交通灯4控---远程红----story")
    @allure.title("郭家窑洞口交通灯4控    洞口交通灯4控---远程红{data14}")
    @allure.description("这个用例是对郭家窑洞口交通灯4控进行远程红 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14",yamlpath_gjy_sk0)
    def test_dl_zcgl_sbbx_08(self,access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(5)
        access_web[35].dl_zhjk_sbjk_gjy()

        # 点击郭家窑隧道
        time.sleep(2)
        access_web[35].dl_zhjk_sbjk_gjy_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy_02(data14["name"])


        # 左侧搜索框到点击确定
        time.sleep(2)
        access_web[35].dl_zhjk_sbjk_gjy_03()

        # 左侧列表点击第一个
        time.sleep(2)
        access_web[35].dl_zhjk_sbjk_gjy_04()

        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() in ["远程红","远程黄","远程绿","远程红+转向"]
        #获取初始状态
        a2=access_web[35].dl_zhjk_sbjk_gjy_09()

        #点击交通灯   远程红
        time.sleep(1)
        access_web[35].dl_zhjk_sbjk_gjy_05()
        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"
        # 显示状态
        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程红"

        #还原初始状态
        access_web[35].dl_zhjk_sbjk_gjy_031(a2,access_web)




    @allure.feature("郭家窑洞口交通灯4控  远程红 远程黄 远程绿  远程红+转向   指令模块")
    @allure.story("test_dl_zcgl_sbbx_09    郭家窑洞口交通灯4控--远程黄----story")
    @allure.title("test_dl_zcgl_sbbx_09    郭家窑洞口交通灯4控--远程黄{data14}")
    @allure.description("这个用例是对郭家窑洞口交通灯4控进行远程黄 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14",yamlpath_gjy_sk0)
    def test_dl_zcgl_sbbx_09(self,access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(5)
        access_web[35].dl_zhjk_sbjk_gjy()


        # 点击郭家窑隧道
        time.sleep(2)
        access_web[35].dl_zhjk_sbjk_gjy_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(2)
        access_web[35].dl_zhjk_sbjk_gjy_03()

        # 左侧列表点击第一个
        time.sleep(2)
        access_web[35].dl_zhjk_sbjk_gjy_04()

        time.sleep(3)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() in ["远程红","远程黄","远程绿","远程红+转向"]
        a2=access_web[35].dl_zhjk_sbjk_gjy_09()

        # 交通灯   远程黄
        time.sleep(1)
        access_web[35].dl_zhjk_sbjk_gjy_06()

        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程黄"
        # 还原初始状态
        access_web[35].dl_zhjk_sbjk_gjy_031(a2,access_web)




    @allure.feature("郭家窑洞口交通灯4控  远程红 远程黄 远程绿  远程红+转向   指令模块")
    @allure.story("test_dl_zcgl_sbbx_010    郭家窑洞口交通灯4控---远程绿----story")
    @allure.title("test_dl_zcgl_sbbx_010   郭家窑洞口交通灯4控---远程绿{data14}")
    @allure.description("这个用例是对郭家窑洞口交通灯4控进行远程绿 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_gjy_sk0)
    def test_dl_zcgl_sbbx_010(self, access_web, sx,data14):
        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(5)
        access_web[35].dl_zhjk_sbjk_gjy()

        # 点击郭家窑隧道
        time.sleep(2)
        access_web[35].dl_zhjk_sbjk_gjy_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(2)
        access_web[35].dl_zhjk_sbjk_gjy_03()

        # 左侧列表点击第一个
        time.sleep(2)
        access_web[35].dl_zhjk_sbjk_gjy_04()

        time.sleep(3)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() in ["远程红", "远程黄", "远程绿", "远程红+转向"]
        a2 = access_web[35].dl_zhjk_sbjk_gjy_09()

        # 交通灯   远程绿
        time.sleep(1)
        access_web[35].dl_zhjk_sbjk_gjy_07()

        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程绿"
        # 还原初始状态
        access_web[35].dl_zhjk_sbjk_gjy_031(a2, access_web)




    @allure.feature("郭家窑洞口交通灯4控  远程红 远程黄 远程绿  远程红+转向   指令模块")
    @allure.story("test_dl_zcgl_sbbx_011    郭家窑洞口交通灯4控---远程红+转向----story")
    @allure.title("test_dl_zcgl_sbbx_011   郭家窑洞口交通灯4控---远程红+转向{data14}")
    @allure.description("这个用例是对郭家窑洞口交通灯4控进行远程红+转向 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_gjy_sk0)
    def test_dl_zcgl_sbbx_011(self, access_web, sx,data14):
        #鼠标悬浮到综合监控---点击设备监控
        time.sleep(5)
        access_web[35].dl_zhjk_sbjk_gjy()

        # 点击郭家窑隧道
        time.sleep(2)
        access_web[35].dl_zhjk_sbjk_gjy_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(2)
        access_web[35].dl_zhjk_sbjk_gjy_03()

        # 左侧列表点击第一个
        time.sleep(2)
        access_web[35].dl_zhjk_sbjk_gjy_04()

        time.sleep(3)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() in ["远程红", "远程黄", "远程绿", "远程红+转向"]
        a2 = access_web[35].dl_zhjk_sbjk_gjy_09()

        # 交通灯   远程红+转向
        time.sleep(1)
        access_web[35].dl_zhjk_sbjk_gjy_08()

        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程红+转向"
        # 还原初始状态
        access_web[35].dl_zhjk_sbjk_gjy_031(a2, access_web)








    # 这个是查询的郭家窑基本照明  他的状态是远程关  远程开
    sql_gjy_jbzm_0 = 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_LJB" AND a1.region="d4f0b6a0-fb88-11e9-bda2-af263eb7555a" AND a2.version=0'
    get_name0(sql_gjy_jbzm_0, "get_name_gjy_jbzmwenjian_0.yaml")
    yamlpath_gjy_jbzm_0 = get_name_wenjianmingcheng("get_name_gjy_jbzmwenjian_0.yaml")
    @allure.feature("郭家窑基本照明  远程关 远程开   指令模块")
    @allure.story("test_dl_zcgl_sbbx_013    郭家窑基本照明 ---远程关----story")
    @allure.title("test_dl_zcgl_sbbx_013    郭家窑基本照明 ---远程关:{data14}")
    @allure.description("这个用例是对郭家窑基本照明 进行远程关 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_gjy_jbzm_0)
    def test_dl_zcgl_sbbx_013(self, access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy()

        # 点击郭家窑隧道
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_04()

        time.sleep(3)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() in ["远程开","远程关"]
        #获取他的初始值
        a1=access_web[35].dl_zhjk_sbjk_gjy_09()

        # 基本照明   远程关
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_08()

        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"

        # 交通灯   远程关
        time.sleep(5)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程关"
        #进行初始还原
        access_web[35].dl_zhjk_sbjk_gjy_035(a1,access_web)




    @allure.feature("郭家窑基本照明  远程关 远程开   指令模块")
    @allure.story("test_dl_zcgl_sbbx_014    郭家窑基本照明---远程开----story")
    @allure.title("test_dl_zcgl_sbbx_014    郭家窑基本照明---远程开")
    @allure.description("这个用例是对郭家窑基本照明进行远程开 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_gjy_jbzm_0)
    def test_dl_zcgl_sbbx_014(self, access_web,sx,data14):
        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy()

        # 点击郭家窑隧道
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_04()

        time.sleep(3)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() in ["远程开", "远程关"]
        # 获取他的初始值
        a1 = access_web[35].dl_zhjk_sbjk_gjy_09()

        # 郭家窑基本照明   远程开
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_05()

        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"

        # 基本照明   远程关
        time.sleep(5)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程开"

        # 进行初始还原
        access_web[35].dl_zhjk_sbjk_gjy_035(a1, access_web)







    # 这个是查询郭家窑加强照明  他的状态是远程关  远程开
    sql_gjy_jqzm_0 = 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_LJQ" AND a1.region="d4f0b6a0-fb88-11e9-bda2-af263eb7555a"  AND a2.version=0'
    get_name0(sql_gjy_jqzm_0, "get_name_gjy_jqzmwenjian_0.yaml")
    yamlpath_gjy_jqzm_0 = get_name_wenjianmingcheng("get_name_gjy_jqzmwenjian_0.yaml")
    @allure.feature("郭家窑加强照明  远程关 远程开   指令模块")
    @allure.story("test_dl_zcgl_sbbx_015    郭家窑加强照明---远程关----story")
    @allure.title("test_dl_zcgl_sbbx_015    郭家窑加强照明---远程关")
    @allure.description("这个用例是对郭家窑加强照明进行远程关 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_gjy_jqzm_0)
    def test_dl_zcgl_sbbx_015(self, access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy()

        # 点击郭家窑隧道
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_04()

        time.sleep(3)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() in ["远程开","远程关"]
        #获取他的初始值
        a1=access_web[35].dl_zhjk_sbjk_gjy_09()

        # 交通灯   远程关
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_08()

        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"

        # 交通灯   远程关
        time.sleep(5)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程关"
        #进行初始还原
        access_web[35].dl_zhjk_sbjk_gjy_035(a1,access_web)




    @allure.feature("郭家窑加强照明  远程关 远程开   指令模块")
    @allure.story("test_dl_zcgl_sbbx_016    郭家窑加强照明---远程开----story")
    @allure.title("test_dl_zcgl_sbbx_016    郭家窑加强照明---远程开")
    @allure.description("这个用例是对郭家窑加强照明进行远程开 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_gjy_jqzm_0)
    def test_dl_zcgl_sbbx_016(self, access_web,sx,data14):
        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy()

        # 点击郭家窑隧道
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[35].dl_zhjk_sbjk_gjy_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_04()

        time.sleep(3)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() in ["远程开", "远程关"]
        # 获取他的初始值
        a1 = access_web[35].dl_zhjk_sbjk_gjy_09()

        # 交通灯   远程开
        time.sleep(3)
        access_web[35].dl_zhjk_sbjk_gjy_05()

        time.sleep(2)
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy() == "指令下发成功"
        assert access_web[35].dl_zhjk_sbjk_gjy_tsy1() == "设备控制成功"

        # 交通灯   远程关
        time.sleep(5)
        assert access_web[35].dl_zhjk_sbjk_gjy_09() == "远程开"

        # 进行初始还原
        access_web[35].dl_zhjk_sbjk_gjy_035(a1, access_web)




    # # 这个是查询的枪形摄像机     他的状态是正常
    # sql_lqk_qxsxj_0 = 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_TVG" AND a1.region="01eaa630-fb88-11e9-9dda-eb6203b0a61e"  AND a2.version=0'
    # get_name0(sql_lqk_qxsxj_0, "get_name_lqk_qxsxj_0.yaml")
    # yamlpath_qlk_qxsxj_0= get_name_wenjianmingcheng("get_name_lqk_qxsxj_0.yaml")
    # @allure.feature("检查是否正常   指令模块")
    # @allure.story("test_dl_zcgl_sbbx_015   枪形摄像机----story")
    # @allure.title("test_dl_zcgl_sbbx_015   枪形摄像机")
    # @allure.description("这个用例是对枪形摄像机 操作")
    # @pytest.mark.parametrize("data14", yamlpath_qlk_qxsxj_0)
    #
    # def test_dl_zcgl_sbbx_015(self, access_web,sx,data14):
    #
    #     # 鼠标悬浮到综合监控---点击设备监控
    #     time.sleep(15)
    #     access_web[35].dl_zhjk_sbjk_gjy()
    #
    #
    #     # 点击郭家窑隧道.
    #     time.sleep(2)
    #     access_web[35].dl_zhjk_sbjk_gjy_01()
    #
    #
    #     # 左侧搜索框
    #     time.sleep(10)
    #     access_web[35].dl_zhjk_sbjk_gjy_02(data14["name"])
    #
    #     # 左侧搜索框到点击确定
    #     time.sleep(2)
    #     access_web[35].dl_zhjk_sbjk_gjy_03()
    #
    #     # 左侧列表点击第一个
    #     time.sleep(2)
    #     access_web[35].dl_zhjk_sbjk_gjy_04()
    #
    #     # 获取状态
    #     time.sleep(5)
    #     assert access_web[35].dl_zhjk_sbjk_gjy_09() == "正常"
    #





    #
    # def test_dl_zcgl_sbbx_017(self, access_web):
    #     time.sleep(15)
    #     # 鼠标悬浮到综合监控---点击设备监控
    #     access_web[35].dl_zhjk_sbjk_gjy()
    #     time.sleep(2)
    #     # # 点击郭家窑隧道
    #     # time.sleep(1)
    #     # access_web[35].dl_zhjk_sbjk_gjy_01()
    #
    #     time.sleep(10)
    #     # 左侧搜索框
    #     access_web[35].dl_zhjk_sbjk_gjy_02("延崇高速左线门架情报板ZXCMS10")
    #     # 左侧搜索框到点击确定
    #     time.sleep(3)
    #     access_web[35].dl_zhjk_sbjk_gjy_03()
    #     # 左侧列表点击第一个
    #     time.sleep(2)
    #     access_web[35].dl_zhjk_sbjk_gjy_04()
    #     # 左下侧设备名称
    #     time.sleep(5)
    #     assert access_web[35].dl_zhjk_sbjk_gjy_025() == "延崇高速左线门架情报板ZXCMS10"
    #
    #     # 左侧搜索框清除
    #     time.sleep(3)
    #     access_web[35].dl_zhjk_sbjk_gjy_010()
    #     time.sleep(10)
    #     # 左侧搜索框
    #     access_web[35].dl_zhjk_sbjk_gjy_02("延崇高速右线门架情报板YXCMS03")
    #     # 点击键盘上的回车键
    #     time.sleep(3)
    #     access_web[35].dl_zhjk_sbjk_gjy_027()
    #     # 左侧列表点击第一个
    #     time.sleep(5)
    #     access_web[35].dl_zhjk_sbjk_gjy_04()
    #     # 左下侧设备名称
    #     time.sleep(5)
    #     assert access_web[35].dl_zhjk_sbjk_gjy_025() == "延崇高速右线门架情报板YXCMS03"
    #


