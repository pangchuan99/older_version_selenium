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
import csv


# @pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数
@allure.story("Test_dl_zcgl_sbkz_lqk  龙泉口隧道")
@allure.feature("Test_dl_zcgl_sbkz_lqk  龙泉口隧道feature")
class  Test_dl_zcgl_sbkz_lqk:

    @pytest.mark.parametrize("data", LD.zcdl)
    @pytest.mark.usefixtures("sx")
    def test_dl_zhjk_sbjk_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(5)


    #
    # # 1. 创建文件对象
    # f = open("龙泉口.csv", "w", encoding="utf8")
    # # 2. 基于文件对象构建 csv写入对象
    # csv_writer = csv.writer(f)
    # # 3. 构建列表头
    # csv_writer.writerow(["姓名", "年龄", "性别"])
    #
    # # 4. 写入csv文件内容
    # csv_writer.writerow(["{data1}", '{}', '男'])

    #这个是查询龙泉口双面车道指示器的版本为0的   远程正面通行    远程禁止  远程反面通行
    sql_lqk_smcdzsq0 = 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid  INNER JOIN remote a3 on a2.version=a3.version  and a1.type="ZSB_PT3" AND a1.region="01eaa630-fb88-11e9-9dda-eb6203b0a61e"  AND a2.version=0'
    get_name0(sql_lqk_smcdzsq0,"get_name_lqk_smzdzsqwenjian_0.yaml")


    yamlpath_lqk_smcdzsq0= get_name_wenjianmingcheng("get_name_lqk_smzdzsqwenjian_0.yaml")
    @allure.feature("指示器 远程正面通行指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_01_1   双面车道指示器---远程正面通行----story")
    @pytest.mark.parametrize("data1",yamlpath_lqk_smcdzsq0)
    @allure.title("test_dl_zcgl_sbkz_lqk_01_1   双面车道指示器---远程正面通行{data1}")
    @allure.description("这个用例是对双面车道指示器 进行远程正面通行下发指令   他具体设备名称是{data1}")
    def test_dl_zcgl_sbkz_lqk_01_1(self, access_web, sx,data1):
        try:
            # 鼠标悬浮到综合监控---点击设备监控
            time.sleep(15)
            access_web[32].dl_zhjk_sbjk_lqk()

            #点击龙泉口隧道
            time.sleep(5)
            access_web[32].dl_zhjk_sbjk_lqk_01()

            #左侧搜索框
            time.sleep(13)
            B2=access_web[32].dl_zhjk_sbjk_lqk_02(data1["name"])
            '''他的值是{}'''.format(B2)

            # 左侧搜索框到点击确定
            time.sleep(3)
            access_web[32].dl_zhjk_sbjk_lqk_03()

            # 左侧列表点击第一个
            time.sleep(3)
            access_web[32].dl_zhjk_sbjk_lqk_04()
            # 判断是否是  下面这个三种状态
            time.sleep(7)
            assert access_web[32].dl_zhjk_sbjk_lqk_09() in ["远程正面通行" ,"远程禁止" ,"远程反面通行"]

            #获取初始状态的值
            time.sleep(3)
            a1=access_web[32].dl_zhjk_sbjk_lqk_09()
            print("获取他的值是：{}".format(a1))

            # 点击双面车道指示器状态---远程正面通行
            time.sleep(6)
            access_web[32].dl_zhjk_sbjk_lqk_05()
            time.sleep(2)
            assert access_web[32].dl_zhjk_sbjk_lqk_tsy()=="指令下发成功"
            assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"
            time.sleep(5)
            assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程正面通行"
            time.sleep(7)
            # 他是进行还原最初状态的
            access_web[32].dl_zhjk_sbjk_lqk_029(a1,access_web)
        except :
            pass



    @allure.feature("指示器 远程禁止指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_02   双面车道指示器---远程禁止----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_02   双面车道指示器---远程禁止")
    @pytest.mark.parametrize("data1",yamlpath_lqk_smcdzsq0)
    @allure.description("这个用例是对双面车道指示器 进行远程禁止下发指令")
    def test_dl_zcgl_sbkz_lqk_02(self,access_web,sx,data1):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(15)
        access_web[32].dl_zhjk_sbjk_lqk()


        # 点击龙泉口隧道
        time.sleep(5)
        access_web[32].dl_zhjk_sbjk_lqk_01()

        # 左侧搜索框
        time.sleep(15)
        access_web[32].dl_zhjk_sbjk_lqk_02(data1["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        access_web[32].dl_zhjk_sbjk_lqk_04()

        # 判断是否是  下面这个三种状态
        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() in ["远程正面通行" ,"远程禁止" ,"远程反面通行"]

        time.sleep(7)
        # 获取初始状态的值
        a1 = access_web[32].dl_zhjk_sbjk_lqk_09()

        # 点击双面车道指示器状态---远程禁止.
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_06()

        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"

        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程禁止"
        time.sleep(7)
        # 他是进行还原最初状态的
        access_web[32].dl_zhjk_sbjk_lqk_029(a1, access_web)



    @allure.feature("指示器 远程反面通行指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_03   双面车道指示器---远程反面通行----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_03   双面车道指示器---远程反面通行")
    @allure.description("这个用例是对双面车道指示器 进行远程反面通行下发指令")
    @pytest.mark.parametrize("data1",yamlpath_lqk_smcdzsq0)
    def test_dl_zcgl_sbkz_lqk_03(self,access_web,sx,data1):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk()


        # 点击龙泉口隧道
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk_02(data1["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_04()

        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() in ["远程正面通行" ,"远程禁止" ,"远程反面通行"]

        # 获取初始状态的值
        time.sleep(3)
        a1 = access_web[32].dl_zhjk_sbjk_lqk_09()

        # 点击双面车道指示器状态---远程反面通行
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_07()
        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"

        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程反面通行"
        time.sleep(7)
        # 他是进行还原最初状态的
        access_web[32].dl_zhjk_sbjk_lqk_029(a1, access_web)





    #这个是查询龙泉口双面车道指示器的版本为1的   远程正面通行    远程禁止  远程反面通行  远程转向
    sql_lqk_smcdzsq1= 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid  INNER JOIN remote a3 on a2.version=a3.version  and a1.type="ZSB_PT3" AND a1.region="01eaa630-fb88-11e9-9dda-eb6203b0a61e"  AND a2.version=1'
    get_name1(sql_lqk_smcdzsq1,"get_name_lqk_smcdzsqwenjian_1.yaml")
    yamlpath_qlk_smcdzsq1= get_name_wenjianmingcheng("get_name_lqk_smcdzsqwenjian_1.yaml")


    @allure.feature("指示器 远程转向指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_016     双面车道指示器---远程转向----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_016   双面车道指示器---远程转向")
    @allure.description("这个用例是对双面车道指示器 进行远程转向下发指令")
    @pytest.mark.parametrize("data14",yamlpath_qlk_smcdzsq1)
    def test_dl_zcgl_sbkz_lqk_016(self,access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(15)
        access_web[32].dl_zhjk_sbjk_lqk()


        # 点击龙泉口隧道
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_01()


        # 左侧搜索框
        time.sleep(13)
        access_web[32].dl_zhjk_sbjk_lqk_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_04()

        assert access_web[32].dl_zhjk_sbjk_lqk_09() in ["远程正面通行" ,"远程禁止" ,"远程反面通行","远程转向"]
        # 获取初始状态的值
        a1 = access_web[32].dl_zhjk_sbjk_lqk_09()
        # assert a1=="1远程正面通行1"
        print("获取的值是{}".format(a1))


        # 点击双面车道指示器状态---远程转向
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_08()

        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"

        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程转向"

        # 他是进行还原最初状态的
        access_web[32].dl_zhjk_sbjk_lqk_029(a1, access_web)






    #这个是查询龙泉口射流风机的  他的状态有    远程关  远程正转  远程反转
    sql_lqk_slfj_0= 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_PJF" AND a1.region="01eaa630-fb88-11e9-9dda-eb6203b0a61e"  AND a2.version=0'
    get_name0(sql_lqk_slfj_0,"get_name_lqk_slfjwenjian_0.yaml")
    yamlpath_qlk_slfj0= get_name_wenjianmingcheng("get_name_lqk_slfjwenjian_0.yaml")
    @allure.feature("射流风机 远程关 远程正转 远程反转 指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_04     射流风机---远程关和远程正转操作----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_04     射流风机---远程关和远程正转操作")
    @allure.description("这个用例是对射流风机 进行远程关 和远程正转操作")
    @pytest.mark.parametrize("data14",yamlpath_qlk_slfj0)
    def test_dl_zcgl_sbkz_lqk_04(self,access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(70)
        access_web[32].dl_zhjk_sbjk_lqk()

        # 点击龙泉口隧道
        time.sleep(5)
        access_web[32].dl_zhjk_sbjk_lqk_01()

        # 左侧搜索框
        time.sleep(15)
        access_web[32].dl_zhjk_sbjk_lqk_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(5)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        time.sleep(5)
        access_web[32].dl_zhjk_sbjk_lqk_04()

        #断言他是否等于其中某一个
        time.sleep(5)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() in["远程关","远程正转" ,"远程反转"]
        #获取他的值
        a2=access_web[32].dl_zhjk_sbjk_lqk_09()

        # 射流风机  远程关
        time.sleep(5)
        access_web[32].dl_zhjk_sbjk_lqk_05()

        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程关"

        # 射流风机  远程正转
        time.sleep(70)
        access_web[32].dl_zhjk_sbjk_lqk_06()
        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程正转"
        # 射流风机--------他是进行还原最初状态的
        access_web[32].dl_zhjk_sbjk_lqk_030(a2, access_web)





    @allure.feature("射流风机 远程关 远程正转 远程反转 指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_05     射流风机---远程关和远程反转操作----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_05     射流风机---远程关和远程反转操作")
    @allure.description("这个用例是对射流风机 进行远程关 和远程反转操作")
    @pytest.mark.parametrize("data14",yamlpath_qlk_slfj0)
    def test_dl_zcgl_sbkz_lqk_05(self,access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(70)
        access_web[32].dl_zhjk_sbjk_lqk()

        # 点击龙泉口隧道
        time.sleep(5)
        access_web[32].dl_zhjk_sbjk_lqk_01()

        # 左侧搜索框
        time.sleep(15)
        access_web[32].dl_zhjk_sbjk_lqk_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(5)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        time.sleep(5)
        access_web[32].dl_zhjk_sbjk_lqk_04()

        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() in ["远程关", "远程正转", "远程反转"]
        # 获取他的值
        a2 = access_web[32].dl_zhjk_sbjk_lqk_09()

        # 射流风机  远程关
        time.sleep(5)
        access_web[32].dl_zhjk_sbjk_lqk_05()

        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程关"


        # 射流风机  远程反转
        time.sleep(70)
        access_web[32].dl_zhjk_sbjk_lqk_07()
        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程反转"

        # 射流风机--------他是进行还原最初状态的
        access_web[32].dl_zhjk_sbjk_lqk_030(a2, access_web)







    #这个是查询龙泉口洞口交通灯4控的  他的状态有    远程关  远程正转  远程反转
    sql_lqk_sk_0= 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_PH2" AND a1.region="01eaa630-fb88-11e9-9dda-eb6203b0a61e"  AND a2.version=0'
    get_name0(sql_lqk_sk_0,"get_name_lqk_sikongjiaotongwenjian_0.yaml")
    yamlpath_qlk_sk0= get_name_wenjianmingcheng("get_name_lqk_sikongjiaotongwenjian_0.yaml")
    @allure.feature("洞口交通灯4控  远程红 远程黄 远程绿  远程红+转向   指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_08    洞口交通灯4控---远程红----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_08    洞口交通灯4控---远程红")
    @allure.description("这个用例是对洞口交通灯4控进行远程红 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14",yamlpath_qlk_sk0)
    def test_dl_zcgl_sbkz_lqk_08(self,access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(5)
        access_web[32].dl_zhjk_sbjk_lqk()

        # 点击龙泉口隧道
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk_02(data14["name"])


        # 左侧搜索框到点击确定
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_04()

        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() in ["远程红","远程黄","远程绿","远程红+转向"]
        #获取初始状态
        a2=access_web[32].dl_zhjk_sbjk_lqk_09()

        #点击交通灯   远程红
        time.sleep(1)
        access_web[32].dl_zhjk_sbjk_lqk_05()
        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"
        # 显示状态
        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程红"

        #还原初始状态
        access_web[32].dl_zhjk_sbjk_lqk_031(a2,access_web)




    @allure.feature("洞口交通灯4控  远程红 远程黄 远程绿  远程红+转向   指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_09    洞口交通灯4控---远程黄----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_09    洞口交通灯4控---远程黄")
    @allure.description("这个用例是对洞口交通灯4控进行远程黄 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14",yamlpath_qlk_sk0)
    def test_dl_zcgl_sbkz_lqk_09(self,access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(5)
        access_web[32].dl_zhjk_sbjk_lqk()


        # 点击龙泉口隧道
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_04()

        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() in ["远程红","远程黄","远程绿","远程红+转向"]
        a2=access_web[32].dl_zhjk_sbjk_lqk_09()

        # 交通灯   远程黄
        time.sleep(1)
        access_web[32].dl_zhjk_sbjk_lqk_06()

        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程黄"
        # 还原初始状态
        access_web[32].dl_zhjk_sbjk_lqk_031(a2,access_web)




    @allure.feature("洞口交通灯4控  远程红 远程黄 远程绿  远程红+转向   指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_010    洞口交通灯4控---远程绿----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_010   洞口交通灯4控---远程绿")
    @allure.description("这个用例是对洞口交通灯4控进行远程绿 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_qlk_sk0)
    def test_dl_zcgl_sbkz_lqk_010(self, access_web, sx,data14):
        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(5)
        access_web[32].dl_zhjk_sbjk_lqk()

        # 点击龙泉口隧道
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_04()

        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() in ["远程红", "远程黄", "远程绿", "远程红+转向"]
        a2 = access_web[32].dl_zhjk_sbjk_lqk_09()

        # 交通灯   远程绿
        time.sleep(1)
        access_web[32].dl_zhjk_sbjk_lqk_07()

        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程绿"
        # 还原初始状态
        access_web[32].dl_zhjk_sbjk_lqk_031(a2, access_web)




    @allure.feature("洞口交通灯4控  远程红 远程黄 远程绿  远程红+转向   指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_011    洞口交通灯4控---远程红+转向----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_011   洞口交通灯4控---远程红+转向")
    @allure.description("这个用例是对洞口交通灯4控进行远程红+转向 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_qlk_sk0)
    def test_dl_zcgl_sbkz_lqk_011(self, access_web, sx,data14):
        #鼠标悬浮到综合监控---点击设备监控
        time.sleep(5)
        access_web[32].dl_zhjk_sbjk_lqk()

        # 点击龙泉口隧道
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_04()

        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() in ["远程红", "远程黄", "远程绿", "远程红+转向"]
        a2 = access_web[32].dl_zhjk_sbjk_lqk_09()

        # 交通灯   远程红+转向
        time.sleep(1)
        access_web[32].dl_zhjk_sbjk_08()

        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程红+转向"
        # 还原初始状态
        access_web[32].dl_zhjk_sbjk_lqk_031(a2, access_web)





    #这个是查询的可变限速标志  他的状态是正常
    sql_lqk_kbsbz_0= 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="SB_S" AND a1.region="01eaa630-fb88-11e9-9dda-eb6203b0a61e"  AND a2.version=0'
    get_name0(sql_lqk_kbsbz_0,"get_name_lqk_kbsbzwenjian_0.yaml")
    yamlpath_qlk_kbsbz0= get_name_wenjianmingcheng("get_name_lqk_kbsbzwenjian_0.yaml")
    @allure.feature("可变限速标志  输入值的   指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_012    可变限速标志----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_012   可变限速标志")
    @allure.description("这个用例是对可变限速标志 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14",yamlpath_qlk_kbsbz0)
    def test_dl_zcgl_sbkz_lqk_012(self, access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(8)
        access_web[32].dl_zhjk_sbjk_lqk()


        # 点击龙泉口隧道
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_04()
        # # 可变速标志---点击速度设置
        # access_web[32].dl_zhjk_sbjk_011()


        # 可变速限速标志---点击数据报表
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_032()


        # 可变速限速标志---获取值(初始值)
        time.sleep(2)
        a1=access_web[32].dl_zhjk_sbjk_lqk_033()
        print("获取的值：{}".format(a1))


        #点击基本信息
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_034()

        #可变速标志---速度设置 清空
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_018()

        # 可变速标志---输入速度设置12
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_016(13)

        # 可变速标志---速度设置-----设置
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_017()

        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"

        # 可变速限速标志---点击数据报表
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_032()
        assert access_web[32].dl_zhjk_sbjk_lqk_033() == "13"


        # 点击基本信息
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_034()

        # 可变速标志---速度设置 清空
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_018()

        # 可变速标志---输入速度设置
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_016(a1)
        # 可变速标志---速度设置-----设置
        access_web[32].dl_zhjk_sbjk_lqk_017()

        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"

        # 可变速限速标志---点击数据报表
        time.sleep(2)
        access_web[32].dl_zhjk_sbjk_lqk_032()

        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_033() == a1






    # 这个是查询的加强照明  他的状态是远程关  远程开
    sql_lqk_jqzm_0 = 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_LJQ" AND a1.region="01eaa630-fb88-11e9-9dda-eb6203b0a61e"  AND a2.version=0'
    get_name0(sql_lqk_jqzm_0, "get_name_lqk_jqzmwenjian_0.yaml")
    yamlpath_qlk_jqzm_0 = get_name_wenjianmingcheng("get_name_lqk_jqzmwenjian_0.yaml")
    @allure.feature("加强照明  远程关 远程开   指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_013    加强照明---远程关----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_013    加强照明---远程关")
    @allure.description("这个用例是对加强照明进行远程关 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_qlk_jqzm_0)
    def test_dl_zcgl_sbkz_lqk_013(self, access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk()

        # 点击龙泉口隧道
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_04()

        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() in ["远程开","远程关"]
        #获取他的初始值
        a1=access_web[32].dl_zhjk_sbjk_lqk_09()

        # 交通灯   远程关
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_08()

        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"

        # 交通灯   远程关
        time.sleep(5)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程关"
        #进行初始还原
        access_web[32].dl_zhjk_sbjk_lqk_035(a1,access_web)







    @allure.feature("加强照明  远程关 远程开   指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_013    加强照明---远程开----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_013    加强照明---远程开")
    @allure.description("这个用例是对加强照明进行远程开 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_qlk_jqzm_0)
    def test_dl_zcgl_sbkz_lqk_014(self, access_web,sx,data14):
        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk()

        # 点击龙泉口隧道
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_04()

        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() in ["远程开", "远程关"]
        # 获取他的初始值
        a1 = access_web[32].dl_zhjk_sbjk_lqk_09()

        # 交通灯   远程开
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_05()

        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"

        # 交通灯   远程关
        time.sleep(5)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程开"

        # 进行初始还原
        access_web[32].dl_zhjk_sbjk_lqk_035(a1, access_web)





    #这个是查询的基本照明  他的状态是远程关  远程开
    sql_lqk_jbzm_0 = 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_LJB" AND a1.region="01eaa630-fb88-11e9-9dda-eb6203b0a61e" AND a2.version=0'
    get_name0(sql_lqk_jbzm_0, "get_name_lqk_jbzmwenjian_0.yaml")
    yamlpath_lqk_jbzm_0 = get_name_wenjianmingcheng("get_name_lqk_jbzmwenjian_0.yaml")
    @allure.feature("基本照明  远程关 远程开   指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_015   基本照明 ---远程关----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_015    基本照明 ---远程关")
    @allure.description("这个用例是对基本照明 进行远程关 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_lqk_jbzm_0)
    def test_dl_zcgl_sbkz_lqk_015(self, access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk()


        # 点击龙泉口隧道
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_04()

        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() in ["远程开","远程关"]
        #获取他的初始值
        a1=access_web[32].dl_zhjk_sbjk_lqk_09()

        # 基本照明   远程关
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_08()

        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"

        # 交通灯   远程关
        time.sleep(5)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程关"
        #进行初始还原
        access_web[32].dl_zhjk_sbjk_lqk_035(a1,access_web)




    @allure.feature("基本照明  远程关 远程开   指令模块")
    @allure.story("test_dl_zcgl_sbkz_lqk_016    基本照明---远程开----story")
    @allure.title("test_dl_zcgl_sbkz_lqk_016    基本照明---远程开")
    @allure.description("这个用例是对基本照明 进行远程开 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_lqk_jbzm_0)
    def test_dl_zcgl_sbkz_lqk_016(self, access_web,sx,data14):
        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk()

        # 点击龙泉口隧道
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[32].dl_zhjk_sbjk_lqk_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_04()

        time.sleep(3)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() in ["远程开", "远程关"]
        # 获取他的初始值
        a1 = access_web[32].dl_zhjk_sbjk_lqk_09()

        # 交通灯   远程开
        time.sleep(3)
        access_web[32].dl_zhjk_sbjk_lqk_05()

        time.sleep(2)
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
        assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"

        # 基本照明   远程关
        time.sleep(5)
        assert access_web[32].dl_zhjk_sbjk_lqk_09() == "远程开"

        # 进行初始还原
        access_web[32].dl_zhjk_sbjk_lqk_035(a1, access_web)







    # # 这个是查询的情报板  他的状态是远程关  远程开
    # sql_lqk_jbzm_0 = 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_LJB" AND a1.region="01eaa630-fb88-11e9-9dda-eb6203b0a61e" AND a2.version=0'
    # get_name0(sql_lqk_jbzm_0, "get_name_lqk_jbzmwenjian_0.yaml")
    # yamlpath_lqk_jbzm_0 = get_name_wenjianmingcheng("get_name_lqk_jbzmwenjian_0.yaml")
    # @allure.feature("情报板  远程关 远程开   指令模块")
    # @allure.story("test_dl_zcgl_sbkz_lqk_017    情报板 ---远程关----story")
    # @allure.title("test_dl_zcgl_sbkz_lqk_017    情报板--远程关")
    # @allure.description("这个用例是对基本照明 进行远程关 以及恢复初次状态 操作")
    # @pytest.mark.parametrize("data14", yamlpath_lqk_jbzm_0)
    # def test_dl_zcgl_sbkz_lqk_017(self, access_web):
    #     time.sleep(15)
    #
    #     # 鼠标悬浮到综合监控---点击设备监控
    #     time.sleep(8)
    #     access_web[32].dl_zhjk_sbjk_lqk()
      #
      #   # 点击龙泉口隧道
      #   time.sleep(2)
      #   access_web[32].dl_zhjk_sbjk_lqk_01()
      #
      #   # 左侧搜索框
      #   time.sleep(10)
      #   access_web[32].dl_zhjk_sbjk_lqk_02("龙泉口隧道右线超车道全彩板Y02")
      #
      #   # 左侧搜索框到点击确定
      #   time.sleep(3)
      #   access_web[32].dl_zhjk_sbjk_lqk_03()
      #
      #   # 左侧列表点击第一个
      #   time.sleep(3)
      #   access_web[32].dl_zhjk_sbjk_lqk_04()
      #
      #   # 情报板信息下发-----退出
      #   time.sleep(2)
      #   access_web[32].dl_zhjk_sbjk_lqk_038()
      #
      #   # 可变速限速标志---点击数据报表
      #   time.sleep(2)
      #   access_web[32].dl_zhjk_sbjk_lqk_032()
      #
      #   # 情报板---获取值(初始值)
      #   time.sleep(2)
      #   a1 = access_web[32].dl_zhjk_sbjk_lqk_033()
      #   print("获取的值：{}".format(a1))
      #
      #   # 点击信息下发
      #   time.sleep(2)
      #   access_web[32].dl_zhjk_sbjk_lqk_011()
      #   # 情报板信息下发---清空
      #   time.sleep(2)
      #   access_web[32].dl_zhjk_sbjk_lqk_037()
      #
      #   # 情报板信息下发-----用JS输入内容
      #   time.sleep(2)
      #   access_web[32].dl_zhjk_sbjk_lqk_039()
      #   # 情报板信息下发-----下发
      #   time.sleep(2)
      #   access_web[32].dl_zhjk_sbjk_lqk_013()
      #   time.sleep(2)
      #   assert access_web[32].dl_zhjk_sbjk_lqk_tsy() == "指令下发成功"
      #   assert access_web[32].dl_zhjk_sbjk_lqk_tsy1() == "设备控制成功"
      #   # 情报板信息下发-----退出
      #   time.sleep(2)
      #   access_web[32].dl_zhjk_sbjk_lqk_038()
      #
      # # 情报板---获取自己下发后的值
      #   time.sleep(2)
      #   a1 = access_web[32].dl_zhjk_sbjk_lqk_033()
      #   print("获取的值：{}".format(a1))
      #   assert access_web[32].dl_zhjk_sbjk_lqk_033()=="测试"


