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
class  Test_dl_zcgl_sbkz_qpl:

    @pytest.mark.parametrize("data", LD.zcdl)
    @pytest.mark.usefixtures("sx")
    def test_dl_zhjk_sbjk_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(5)




    # #这个是查询棋盘梁双面车道指示器的版本为0的   远程正面通行    远程禁止  远程反面通行
    sql_qpl_smcdzsq0 = 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid  INNER JOIN remote a3 on a2.version=a3.version  and a1.type="ZSB_PT3" AND a1.region="7c7c3670-fb88-11e9-a81d-4348ba300ea2"  AND a2.version=0'
    get_name0(sql_qpl_smcdzsq0,"get_name_qpl_smzdzsqwenjian_0.yaml")
    yamlpath_qpl_smcdzsq0= get_name_wenjianmingcheng("get_name_qpl_smzdzsqwenjian_0.yaml")
    @allure.feature("棋盘梁双面车道指示器   远程正面通行指令模块")
    @allure.story("test_dl_zcgl_sbbx_01_1   棋盘梁双面车道指示器---远程正面通行----story")
    @pytest.mark.parametrize("data1",yamlpath_qpl_smcdzsq0)
    @allure.title("test_dl_zcgl_sbbx_01_1   棋盘梁双面车道指示器---远程正面通行{data1}")


    # @allure.description("这个用例是对棋盘梁双面车道指示器    进行远程正面通行下发指令   他具体设备名称是{data1}")
    def test_dl_zcgl_sbbx_01_1(self, access_web, sx,data1):


        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(15)
        access_web[38].dl_zhjk_sbjk_qpl()

        #点击棋盘梁隧道
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        #左侧搜索框
        time.sleep(13)
        B2=access_web[38].dl_zhjk_sbjk_qpl_02(data1["name"])
        '''他的值是{}'''.format(B2)

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_04()
        # 判断是否是  下面这个三种状态
        time.sleep(7)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() in ["远程正面通行" ,"远程禁止" ,"远程反面通行"]

        #获取初始状态的值
        time.sleep(3)
        a1=access_web[38].dl_zhjk_sbjk_qpl_09()
        print("获取他的值是：{}".format(a1))

        # 点击双面车道指示器状态---远程正面通行
        time.sleep(6)
        access_web[38].dl_zhjk_sbjk_qpl_05()
        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy()=="指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"
        time.sleep(5)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程正面通行"
        time.sleep(7)
        # 他是进行还原最初状态的
        access_web[38].dl_zhjk_sbjk_qpl_029(a1,access_web)



    @allure.feature("棋盘梁双面车道指示器    远程禁止指令模块")
    @allure.story("test_dl_zcgl_sbbx_02   棋盘梁双面车道指示器---远程禁止----story")
    @allure.title("test_dl_zcgl_sbbx_02   棋盘梁双面车道指示器---远程禁止：{data1}")
    @pytest.mark.parametrize("data1",yamlpath_qpl_smcdzsq0)
    @allure.description("这个用例是对棋盘梁双面车道指示器   进行远程禁止下发指令")
    def test_dl_zcgl_sbbx_02(self,access_web,sx,data1):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(15)
        access_web[38].dl_zhjk_sbjk_qpl()


        # 点击棋盘梁隧道
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        # 左侧搜索框
        time.sleep(15)
        access_web[38].dl_zhjk_sbjk_qpl_02(data1["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        access_web[38].dl_zhjk_sbjk_qpl_04()

        # 判断是否是  下面这个三种状态
        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() in ["远程正面通行" ,"远程禁止" ,"远程反面通行"]

        time.sleep(7)
        # 获取初始状态的值
        a1 = access_web[38].dl_zhjk_sbjk_qpl_09()

        # 点击双面车道指示器状态---远程禁止.
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_06()

        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"

        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程禁止"

        time.sleep(7)
        # 他是进行还原最初状态的
        access_web[38].dl_zhjk_sbjk_qpl_029(a1, access_web)



    @allure.feature("棋盘梁双面车道指示器    远程反面通行指令模块")
    @allure.story("test_dl_zcgl_sbbx_03   棋盘梁双面车道指示器---远程反面通行----story")
    @allure.title("test_dl_zcgl_sbbx_03   棋盘梁双面车道指示器---远程反面通行:{data1}")
    @allure.description("这个用例是对棋盘梁双面车道指示器   进行远程反面通行下发指令")
    @pytest.mark.parametrize("data1",yamlpath_qpl_smcdzsq0)
    def test_dl_zcgl_sbbx_03(self,access_web,sx,data1):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl()


        # 点击棋盘梁隧道
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl_02(data1["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_04()

        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() in ["远程正面通行" ,"远程禁止" ,"远程反面通行"]

        # 获取初始状态的值
        time.sleep(3)
        a1 = access_web[38].dl_zhjk_sbjk_qpl_09()

        # 点击双面车道指示器状态---远程反面通行
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_07()
        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"

        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程反面通行"
        time.sleep(7)
        # 他是进行还原最初状态的
        access_web[38].dl_zhjk_sbjk_qpl_029(a1, access_web)



    #这个是查询棋盘梁双面车道指示器的版本为1的   远程正面通行    远程禁止  远程反面通行  远程转向
    sql_qpl_smcdzsq1= 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid  INNER JOIN remote a3 on a2.version=a3.version  and a1.type="ZSB_PT3" AND a1.region="7c7c3670-fb88-11e9-a81d-4348ba300ea2"  AND a2.version=1'
    get_name1(sql_qpl_smcdzsq1,"get_name_qpl_smcdzsqwenjian_1.yaml")
    yamlpath_qlk_smcdzsq1= get_name_wenjianmingcheng("get_name_qpl_smcdzsqwenjian_1.yaml")


    @allure.feature("梁双面车道指示器的版本为1的 远程转向指令模块")
    @allure.story("test_dl_zcgl_sbbx_016     梁双面车道指示器的版本为1的---远程转向----story")
    @allure.title("test_dl_zcgl_sbbx_016     梁双面车道指示器的版本为1的---远程转向:{data14}")
    @allure.description("这个用例是对梁双面车道指示器的版本为1的    进行远程转向下发指令")
    @pytest.mark.parametrize("data14",yamlpath_qlk_smcdzsq1)
    def test_dl_zcgl_sbbx_016(self,access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(15)
        access_web[38].dl_zhjk_sbjk_qpl()


        # 点击棋盘梁隧道
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_01()


        # 左侧搜索框
        time.sleep(13)
        access_web[38].dl_zhjk_sbjk_qpl_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_04()

        assert access_web[38].dl_zhjk_sbjk_qpl_09() in ["远程正面通行" ,"远程禁止" ,"远程反面通行","远程转向"]
        # 获取初始状态的值
        a1 = access_web[38].dl_zhjk_sbjk_qpl_09()
        # assert a1=="1远程正面通行1"
        print("获取的值是{}".format(a1))


        # 点击双面车道指示器状态---远程转向
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_08()

        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"

        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程转向"

        # 他是进行还原最初状态的
        access_web[38].dl_zhjk_sbjk_qpl_029(a1, access_web)






    #这个是查询棋盘梁射流风机的  他的状态有    远程关  远程正转  远程反转
    sql_qpl_slfj_0= 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_PJF" AND a1.region="7c7c3670-fb88-11e9-a81d-4348ba300ea2"  AND a2.version=0'
    get_name0(sql_qpl_slfj_0,"get_name_qpl_slfjwenjian_0.yaml")
    yamlpath_qlk_slfj0= get_name_wenjianmingcheng("get_name_qpl_slfjwenjian_0.yaml")
    @allure.feature("棋盘梁射流风机 远程关 远程正转 远程反转 指令模块")
    @allure.story("test_dl_zcgl_sbbx_04     棋盘梁射流风机---远程关和远程正转操作----story")
    @allure.title("test_dl_zcgl_sbbx_04     棋盘梁射流风机---远程关和远程正转操作:{data14}")
    @allure.description("这个用例是对棋盘梁射流风机    进行远程关 和远程正转操作")
    @pytest.mark.parametrize("data14",yamlpath_qlk_slfj0)
    def test_dl_zcgl_sbbx_04(self,access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(70)
        access_web[38].dl_zhjk_sbjk_qpl()

        # 点击棋盘梁隧道
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        # 左侧搜索框
        time.sleep(15)
        access_web[38].dl_zhjk_sbjk_qpl_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl_04()

        #断言他是否等于其中某一个
        time.sleep(5)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() in["远程关","远程正转" ,"远程反转"]
        #获取他的值
        a2=access_web[38].dl_zhjk_sbjk_qpl_09()

        # 射流风机  远程关
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl_05()

        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程关"

        # 射流风机  远程正转
        time.sleep(70)
        access_web[38].dl_zhjk_sbjk_qpl_06()
        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程正转"
        # 射流风机--------他是进行还原最初状态的
        access_web[38].dl_zhjk_sbjk_qpl_030(a2, access_web)





    @allure.feature("棋盘梁射流风机   远程关 远程正转 远程反转 指令模块")
    @allure.story("test_dl_zcgl_sbbx_05     棋盘梁射流风机---远程关和远程反转操作----story")
    @allure.title("test_dl_zcgl_sbbx_05     棋盘梁射流风机---远程关和远程反转操作:{data14}")
    @allure.description("这个用例是对射流风机 进行远程关 和远程反转操作")
    @pytest.mark.parametrize("data14",yamlpath_qlk_slfj0)
    def test_dl_zcgl_sbbx_05(self,access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(70)
        access_web[38].dl_zhjk_sbjk_qpl()

        # 点击棋盘梁隧道
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        # 左侧搜索框
        time.sleep(15)
        access_web[38].dl_zhjk_sbjk_qpl_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl_04()

        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() in ["远程关", "远程正转", "远程反转"]
        # 获取他的值
        a2 = access_web[38].dl_zhjk_sbjk_qpl_09()

        # 射流风机  远程关
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl_05()

        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程关"

        # 射流风机  远程反转
        time.sleep(70)
        access_web[38].dl_zhjk_sbjk_qpl_07()
        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程反转"

        # 射流风机--------他是进行还原最初状态的
        access_web[38].dl_zhjk_sbjk_qpl_030(a2, access_web)







    #这个是查询棋盘梁洞口交通灯4控的  他的状态有    远程关  远程正转  远程反转
    sql_qpl_sk_0= 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_PH2" AND a1.region="7c7c3670-fb88-11e9-a81d-4348ba300ea2"  AND a2.version=0'
    get_name0(sql_qpl_sk_0,"get_name_qpl_sikongjiaotongwenjian_0.yaml")
    yamlpath_qlk_sk0= get_name_wenjianmingcheng("get_name_qpl_sikongjiaotongwenjian_0.yaml")
    @allure.feature("棋盘梁洞口交通灯4控  远程红 远程黄 远程绿  远程红+转向   指令模块")
    @allure.story("test_dl_zcgl_sbbx_08    棋盘梁洞口交通灯4控---远程红----story")
    @allure.title("test_dl_zcgl_sbbx_08    棋盘梁洞口交通灯4控---远程红:{data14}")
    @allure.description("这个用例是对棋盘梁洞口交通灯4控进行远程红 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14",yamlpath_qlk_sk0)
    def test_dl_zcgl_sbbx_08(self,access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl()

        # 点击棋盘梁隧道
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl_02(data14["name"])


        # 左侧搜索框到点击确定
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_04()

        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() in ["远程红","远程黄","远程绿","远程红+转向"]
        #获取初始状态
        a2=access_web[38].dl_zhjk_sbjk_qpl_09()

        #点击交通灯   远程红
        time.sleep(1)
        access_web[38].dl_zhjk_sbjk_qpl_05()
        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"
        # 显示状态
        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程红"

        #还原初始状态
        access_web[38].dl_zhjk_sbjk_qpl_031(a2,access_web)





    @allure.feature("棋盘梁洞口交通灯4控  远程红 远程黄 远程绿  远程红+转向   指令模块")
    @allure.story("test_dl_zcgl_sbbx_09    棋盘梁洞口交通灯4控---远程黄----story")
    @allure.title("test_dl_zcgl_sbbx_09    棋盘梁洞口交通灯4控---远程黄:{data14}")
    @allure.description("这个用例是对棋盘梁洞口交通灯4控进行远程黄 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14",yamlpath_qlk_sk0)
    def test_dl_zcgl_sbbx_09(self,access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl()


        # 点击棋盘梁隧道
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_04()

        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() in ["远程红","远程黄","远程绿","远程红+转向"]
        a2=access_web[38].dl_zhjk_sbjk_qpl_09()

        # 交通灯   远程黄
        time.sleep(1)
        access_web[38].dl_zhjk_sbjk_qpl_06()

        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程黄"
        # 还原初始状态
        access_web[38].dl_zhjk_sbjk_qpl_031(a2,access_web)




    @allure.feature("棋盘梁洞口交通灯4控  远程红 远程黄 远程绿  远程红+转向   指令模块")
    @allure.story("test_dl_zcgl_sbbx_010    棋盘梁洞口交通灯4控---远程绿----story")
    @allure.title("test_dl_zcgl_sbbx_010   棋盘梁洞口交通灯4控---远程绿:{data14}")
    @allure.description("这个用例是对棋盘梁洞口交通灯4控进行远程绿 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_qlk_sk0)
    def test_dl_zcgl_sbbx_010(self, access_web, sx,data14):
        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl()

        # 点击棋盘梁隧道
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_04()

        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() in ["远程红", "远程黄", "远程绿", "远程红+转向"]
        a2 = access_web[38].dl_zhjk_sbjk_qpl_09()

        # 交通灯   远程绿
        time.sleep(1)
        access_web[38].dl_zhjk_sbjk_qpl_07()

        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程绿"
        # 还原初始状态
        access_web[38].dl_zhjk_sbjk_qpl_031(a2, access_web)




    @allure.feature("棋盘梁洞口交通灯4控  远程红 远程黄 远程绿  远程红+转向   指令模块")
    @allure.story("test_dl_zcgl_sbbx_011    棋盘梁洞口交通灯4控---远程红+转向----story")
    @allure.title("test_dl_zcgl_sbbx_011   棋盘梁洞口交通灯4控---远程红+转向:{data14}")
    @allure.description("这个用例是对棋盘梁洞口交通灯4控进行远程红+转向 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_qlk_sk0)
    def test_dl_zcgl_sbbx_011(self, access_web, sx,data14):
        #鼠标悬浮到综合监控---点击设备监控
        time.sleep(5)
        access_web[38].dl_zhjk_sbjk_qpl()

        # 点击棋盘梁隧道
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_04()

        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() in ["远程红", "远程黄", "远程绿", "远程红+转向"]
        a2 = access_web[38].dl_zhjk_sbjk_qpl_09()

        # 交通灯   远程红+转向
        time.sleep(1)
        access_web[38].dl_zhjk_sbjk_08()

        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"
        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程红+转向"
        # 还原初始状态
        access_web[38].dl_zhjk_sbjk_qpl_031(a2, access_web)



    #这个是查询的棋盘梁可变限速标志  他的状态是正常
    sql_qpl_kbsbz_0= 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="SB_S" AND a1.region="7c7c3670-fb88-11e9-a81d-4348ba300ea2"  AND a2.version=0'
    get_name0(sql_qpl_kbsbz_0,"get_name_qpl_kbsbzwenjian_0.yaml")
    yamlpath_qlk_kbsbz0= get_name_wenjianmingcheng("get_name_qpl_kbsbzwenjian_0.yaml")
    @allure.feature("棋盘梁可变限速标志  指令模块")
    @allure.story("test_dl_zcgl_sbbx_012    棋盘梁可变限速标志----story")
    @allure.title("test_dl_zcgl_sbbx_012   棋盘梁可变限速标志；{data14}")
    @allure.description("这个用例是对棋盘梁可变限速标志 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14",yamlpath_qlk_kbsbz0)
    def test_dl_zcgl_sbbx_012(self, access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(8)
        access_web[38].dl_zhjk_sbjk_qpl()


        # 点击棋盘梁隧道
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_04()
        # # 可变速标志---点击速度设置
        # access_web[38].dl_zhjk_sbjk_011()


        # 可变速限速标志---点击数据报表
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_032()


        # 可变速限速标志---获取值(初始值)
        time.sleep(2)
        a1=access_web[38].dl_zhjk_sbjk_qpl_033()
        print("获取的值：{}".format(a1))


        #点击基本信息
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_034()

        #可变速标志---速度设置 清空
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_018()

        # 可变速标志---输入速度设置12
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_016(13)

        # 可变速标志---速度设置-----设置
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_017()

        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"

        # 可变速限速标志---点击数据报表
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_032()
        assert access_web[38].dl_zhjk_sbjk_qpl_033() == "13"

        # 点击基本信息
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_034()

        # 可变速标志---速度设置 清空
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_018()

        # 可变速标志---输入速度设置
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_016(a1)
        # 可变速标志---速度设置-----设置
        access_web[38].dl_zhjk_sbjk_qpl_017()

        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"

        # 可变速限速标志---点击数据报表
        time.sleep(2)
        access_web[38].dl_zhjk_sbjk_qpl_032()
        assert access_web[38].dl_zhjk_sbjk_qpl_033() == a1







    # 这个是查询的棋盘梁加强照明  他的状态是远程关  远程开
    sql_qpl_jqzm_0 = 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_LJQ" AND a1.region="7c7c3670-fb88-11e9-a81d-4348ba300ea2"  AND a2.version=0'
    get_name0(sql_qpl_jqzm_0, "get_name_qpl_jqzmwenjian_0.yaml")
    yamlpath_qlk_jqzm_0 = get_name_wenjianmingcheng("get_name_qpl_jqzmwenjian_0.yaml")
    @allure.feature("棋盘梁加强照明  远程关 远程开   指令模块")
    @allure.story("test_dl_zcgl_sbbx_013    棋盘梁加强照明---远程关----story")
    @allure.title("test_dl_zcgl_sbbx_013    棋盘梁加强照明---远程关:{data14}")
    @allure.description("这个用例是对棋盘梁加强照明进行远程关 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_qlk_jqzm_0)
    def test_dl_zcgl_sbbx_013(self, access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl()

        # 点击棋盘梁隧道
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_04()

        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() in ["远程开","远程关"]
        #获取他的初始值
        a1=access_web[38].dl_zhjk_sbjk_qpl_09()

        # 交通灯   远程关
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_08()

        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"

        # 交通灯   远程关
        time.sleep(5)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程关"
        #进行初始还原
        access_web[38].dl_zhjk_sbjk_qpl_035(a1,access_web)




    @allure.feature("棋盘梁加强照明  远程关 远程开   指令模块")
    @allure.story("test_dl_zcgl_sbbx_014    棋盘梁加强照明---远程开----story")
    @allure.title("test_dl_zcgl_sbbx_014    棋盘梁加强照明---远程开:{data14}")
    @allure.description("这个用例是对棋盘梁加强照明进行远程开 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_qlk_jqzm_0)
    def test_dl_zcgl_sbbx_014(self, access_web,sx,data14):
        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl()

        # 点击棋盘梁隧道
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_04()

        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() in ["远程开", "远程关"]
        # 获取他的初始值
        a1 = access_web[38].dl_zhjk_sbjk_qpl_09()

        # 交通灯   远程开
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_05()

        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"

        # 交通灯   远程关
        time.sleep(5)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程开"

        # 进行初始还原
        access_web[38].dl_zhjk_sbjk_qpl_035(a1, access_web)





    # 这个是查询的棋盘梁基本照明  他的状态是远程关  远程开
    sql_qpl_jbzm_0 = 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_LJB" AND a1.region="7c7c3670-fb88-11e9-a81d-4348ba300ea2" AND a2.version=0'
    get_name0(sql_qpl_jbzm_0, "get_name_qpl_jbzmwenjian_0.yaml")
    yamlpath_qpl_jbzm_0 = get_name_wenjianmingcheng("get_name_qpl_jbzmwenjian_0.yaml")
    @allure.feature("棋盘梁基本照明  远程关 远程开   指令模块")
    @allure.story("test_dl_zcgl_sbbx_015    棋盘梁基本照明 ---远程关----story")
    @allure.title("test_dl_zcgl_sbbx_015    棋盘梁基本照明 ---远程关:{data14}")
    @allure.description("这个用例是对棋盘梁基本照明 进行远程关 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_qpl_jbzm_0)
    def test_dl_zcgl_sbbx_015(self, access_web,sx,data14):

        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl()


        # 点击棋盘梁隧道
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_04()

        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() in ["远程开","远程关"]
        #获取他的初始值
        a1=access_web[38].dl_zhjk_sbjk_qpl_09()

        # 棋盘梁基本照明   远程关
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_08()

        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"

        # 交通灯   远程关
        time.sleep(5)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程关"
        #进行初始还原
        access_web[38].dl_zhjk_sbjk_qpl_035(a1,access_web)




    @allure.feature("棋盘梁基本照明  远程关 远程开   指令模块")
    @allure.story("test_dl_zcgl_sbbx_016    棋盘梁基本照明---远程开----story")
    @allure.title("test_dl_zcgl_sbbx_016    棋盘梁基本照明---远程开:{data14}")
    @allure.description("这个用例是对棋盘梁基本照明进行远程开 以及恢复初次状态 操作")
    @pytest.mark.parametrize("data14", yamlpath_qpl_jbzm_0)
    def test_dl_zcgl_sbbx_016(self, access_web,sx,data14):
        # 鼠标悬浮到综合监控---点击设备监控
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl()

        # 点击棋盘梁隧道
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_01()

        # 左侧搜索框
        time.sleep(10)
        access_web[38].dl_zhjk_sbjk_qpl_02(data14["name"])

        # 左侧搜索框到点击确定
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_03()

        # 左侧列表点击第一个
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_04()

        time.sleep(3)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() in ["远程开", "远程关"]
        # 获取他的初始值
        a1 = access_web[38].dl_zhjk_sbjk_qpl_09()

        # 交通灯   远程开
        time.sleep(3)
        access_web[38].dl_zhjk_sbjk_qpl_05()

        time.sleep(2)
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy() == "指令下发成功"
        assert access_web[38].dl_zhjk_sbjk_qpl_tsy1() == "设备控制成功"

        # 棋盘梁基本照明   远程关
        time.sleep(5)
        assert access_web[38].dl_zhjk_sbjk_qpl_09() == "远程开"

        # 进行初始还原
        access_web[38].dl_zhjk_sbjk_qpl_035(a1, access_web)





    # # 这个是查询的枪形摄像机     他的状态是正常
    # sql_qpl_qxsxj_0 = 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid INNER JOIN remote a3 on a2.version=a3.version and a1.type="ZSB_TVG" AND a1.region="7c7c3670-fb88-11e9-a81d-4348ba300ea2"  AND a2.version=0'
    # get_name0(sql_qpl_qxsxj_0, "get_name_qpl_qxsxj_0.yaml")
    # yamlpath_qlk_qxsxj_0= get_name_wenjianmingcheng("get_name_qpl_qxsxj_0.yaml")
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
    #     access_web[38].dl_zhjk_sbjk()
    #
    #
    #     # 点击棋盘梁隧道.
    #     time.sleep(2)
    #     access_web[38].dl_zhjk_sbjk_01()
    #
    #
    #     # 左侧搜索框
    #     time.sleep(10)
    #     access_web[38].dl_zhjk_sbjk_02(data14["name"])
    #
    #     # 左侧搜索框到点击确定
    #     time.sleep(2)
    #     access_web[38].dl_zhjk_sbjk_03()
    #
    #     # 左侧列表点击第一个
    #     time.sleep(2)
    #     access_web[38].dl_zhjk_sbjk_04()
    #
    #     # 获取状态
    #     time.sleep(5)
    #     assert access_web[38].dl_zhjk_sbjk_09() == "正常"
    #





    #
    # def test_dl_zcgl_sbbx_017(self, access_web):
    #     time.sleep(15)
    #     # 鼠标悬浮到综合监控---点击设备监控
    #     access_web[38].dl_zhjk_sbjk()
    #     time.sleep(2)
    #     # # 点击棋盘梁隧道
    #     # time.sleep(1)
    #     # access_web[38].dl_zhjk_sbjk_01()
    #
    #     time.sleep(10)
    #     # 左侧搜索框
    #     access_web[38].dl_zhjk_sbjk_02("延崇高速左线门架情报板ZXCMS10")
    #     # 左侧搜索框到点击确定
    #     time.sleep(3)
    #     access_web[38].dl_zhjk_sbjk_03()
    #     # 左侧列表点击第一个
    #     time.sleep(2)
    #     access_web[38].dl_zhjk_sbjk_04()
    #     # 左下侧设备名称
    #     time.sleep(5)
    #     assert access_web[38].dl_zhjk_sbjk_025() == "延崇高速左线门架情报板ZXCMS10"
    #
    #     # 左侧搜索框清除
    #     time.sleep(3)
    #     access_web[38].dl_zhjk_sbjk_010()
    #     time.sleep(10)
    #     # 左侧搜索框
    #     access_web[38].dl_zhjk_sbjk_02("延崇高速右线门架情报板YXCMS03")
    #     # 点击键盘上的回车键
    #     time.sleep(3)
    #     access_web[38].dl_zhjk_sbjk_027()
    #     # 左侧列表点击第一个
    #     time.sleep(5)
    #     access_web[38].dl_zhjk_sbjk_04()
    #     # 左下侧设备名称
    #     time.sleep(5)
    #     assert access_web[38].dl_zhjk_sbjk_025() == "延崇高速右线门架情报板YXCMS03"
    #


