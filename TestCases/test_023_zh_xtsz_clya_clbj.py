import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_zh_stsz_clya_clbj:



    @pytest.mark.parametrize("data", LD.zcdl)
    def test_zh_stsz_clya_clbj_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(5)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        # 鼠标悬浮到策略预案  点击策略编辑
        access_web[21].zh_xtsz_clya_clbj()
        time.sleep(15)
        # 添加新策略
        access_web[21].zh_xtsz_clya_clbj_01()
        time.sleep(1)
        # 保存
        access_web[21].zh_xtsz_clya_clbj_02()
        # 取消
        access_web[21].zh_xtsz_clya_clbj_03()
        assert access_web[21].zh_xtsz_clya_clbj_tsy()=="请输入名称"





    def test_zh_stsz_clya_clbj_02(self,access_web):
        time.sleep(4)
        # 添加新策略
        access_web[21].zh_xtsz_clya_clbj_01()
        time.sleep(1)
        # 输入名称
        access_web[21].zh_xtsz_clya_clbj_04("自动策略")
        time.sleep(1)
        # 保存
        access_web[21].zh_xtsz_clya_clbj_02()
        # 取消
        access_web[21].zh_xtsz_clya_clbj_03()
        assert access_web[21].zh_xtsz_clya_clbj_tsy()=="请选择类型"






    def test_zh_stsz_clya_clbj_03(self, access_web):
        time.sleep(4)
        # 添加新策略
        access_web[21].zh_xtsz_clya_clbj_01()
        # 输入名称
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_04("自动策略")
        # 类型
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_05()
        # 类型下拉---选择程序自动策略
        access_web[21].zh_xtsz_clya_clbj_06()
        time.sleep(1)
        # 保存
        access_web[21].zh_xtsz_clya_clbj_02()
        # 取消
        access_web[21].zh_xtsz_clya_clbj_03()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "请选择分组"



    def test_zh_stsz_clya_clbj_04(self, access_web):
        time.sleep(4)
        # 添加新策略
        access_web[21].zh_xtsz_clya_clbj_01()
        # 输入名称
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_04("自动策略")
        # 类型
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_05()
        # 类型下拉---选择程序自动策略
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_06()
        # 分组
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_07()
        # 保存
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_02()
        # 取消
        access_web[21].zh_xtsz_clya_clbj_03()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "请选择区域"





    def test_zh_stsz_clya_clbj_05(self, access_web):
        time.sleep(4)
        # 添加新策略
        access_web[21].zh_xtsz_clya_clbj_01()
        # 输入名称
        time.sleep(2)
        access_web[21].zh_xtsz_clya_clbj_04("自动策略")
        # 类型
        time.sleep(2)
        access_web[21].zh_xtsz_clya_clbj_05()
        # 类型下拉---选择程序自动策略
        time.sleep(2)
        access_web[21].zh_xtsz_clya_clbj_06()
        # 分组
        time.sleep(2)
        access_web[21].zh_xtsz_clya_clbj_07()
        # 二级分类
        time.sleep(2)
        access_web[21].zh_xtsz_clya_clbj_028()

        # 影响区域
        time.sleep(2)
        access_web[21].zh_xtsz_clya_clbj_08()
        # 保存
        access_web[21].zh_xtsz_clya_clbj_02()
        access_web[21].zh_xtsz_clya_clbj_02()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "添加成功"






    def test_zh_stsz_clya_clbj_06(self, access_web):
        time.sleep(4)
        # 搜索框清除
        access_web[21].zh_xtsz_clya_clbj_010()
        # 搜索框输入
        access_web[21].zh_xtsz_clya_clbj_09("自动策略")
        # 搜索框确定
        access_web[21].zh_xtsz_clya_clbj_011()
        # 列表最后一个
        access_web[21].zh_xtsz_clya_clbj_012()
        # 点击关预案
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_013()
        # 关联预案最后一个
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_014()
        # 点击确定
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_015()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "修改成功"



    def test_zh_stsz_clya_clbj_07(self, access_web):
        time.sleep(4)
        # 搜索框清除
        access_web[21].zh_xtsz_clya_clbj_010()
        # 搜索框输入
        access_web[21].zh_xtsz_clya_clbj_09("自动策略")
        # 搜索框确定
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_011()
        # 列表最后一个
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_012()
        # 编辑
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_016()
        # 名称清除
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_024()
        # 输入名称
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_04("修改自动策略")
        # 保存
        access_web[21].zh_xtsz_clya_clbj_02()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "修改成功"




    def test_zh_stsz_clya_clbj_08(self, access_web):
        time.sleep(4)
        # 搜索框清除
        access_web[21].zh_xtsz_clya_clbj_010()
        # 搜索框输入
        access_web[21].zh_xtsz_clya_clbj_09("修改自动策略")
        # 搜索框确定
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_011()
        # 删除
        access_web[21].zh_xtsz_clya_clbj_017()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "删除成功"




    def test_zh_stsz_clya_clbj_09(self, access_web):
        time.sleep(4)
        # 添加新策略
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_01()
        # 输入名称
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_04("时间策略")
        # 类型
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_05()
        # 类型下拉---选择时间自动策略
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_018()
        # 分组
        time.sleep(2)
        access_web[21].zh_xtsz_clya_clbj_07()
        # 二级分类
        time.sleep(2)
        access_web[21].zh_xtsz_clya_clbj_028()
        # 影响区域
        time.sleep(2)
        access_web[21].zh_xtsz_clya_clbj_08()
        # 保存
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_02()
        access_web[21].zh_xtsz_clya_clbj_02()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "添加成功"




    def test_zh_stsz_clya_clbj_010(self, access_web):
        time.sleep(4)
        # 搜索框清除
        access_web[21].zh_xtsz_clya_clbj_010()
        # 搜索框输入
        access_web[21].zh_xtsz_clya_clbj_09("时间策略")
        # 搜索框确定
        access_web[21].zh_xtsz_clya_clbj_011()
        time.sleep(1)
        # 列表最后一个
        access_web[21].zh_xtsz_clya_clbj_012()
        time.sleep(1)
        # 时间保存
        access_web[21].zh_xtsz_clya_clbj_019()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "请选择周期"



    # 触发周期-----时间里面的周期
    def test_zh_stsz_clya_clbj_011(self, access_web):
        time.sleep(3)
        # 搜索框清除
        access_web[21].zh_xtsz_clya_clbj_010()
        # 搜索框输入
        access_web[21].zh_xtsz_clya_clbj_09("时间策略")
        # 搜索框确定
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_011()
        # 列表最后一个
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_012()
        # 触发周期
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_020()
        # 时间保存
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_019()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "请选择时间"




    def test_zh_stsz_clya_clbj_012(self, access_web):
        time.sleep(4)
        # 搜索框清除
        access_web[21].zh_xtsz_clya_clbj_010()
        # 搜索框输入
        access_web[21].zh_xtsz_clya_clbj_09("时间策略")
        # 搜索框确定
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_011()
        # 列表最后一个
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_012()
        # 触发周期
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_020()
        # 触发时间
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_021("08分09秒")
        # 选择时间范围  ---开始----删除
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_025()
        # 时间保存
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_019()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "请选择时间范围"




    def test_zh_stsz_clya_clbj_013(self, access_web):
        time.sleep(4)
        # 搜索框清除
        access_web[21].zh_xtsz_clya_clbj_010()
        # 搜索框输入
        access_web[21].zh_xtsz_clya_clbj_09("时间策略")
        # 搜索框确定
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_011()
        # 列表最后一个
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_012()
        # 触发周期
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_020()
        # 触发时间
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_021("08分09秒")
        # 选择时间范围  ---开始----删除
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_025()
        # 选择时间范围  ---开始
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_022("2020.01.22 00:00:03")
        # 选择时间范围  ---结束----删除
        access_web[21].zh_xtsz_clya_clbj_026()
        time.sleep(1)
        # 时间保存
        access_web[21].zh_xtsz_clya_clbj_019()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "请选择时间范围"




    def test_zh_stsz_clya_clbj_014(self, access_web):
        time.sleep(4)
        # 搜索框清除
        access_web[21].zh_xtsz_clya_clbj_010()
        # 搜索框输入
        access_web[21].zh_xtsz_clya_clbj_09("时间策略")
        # 搜索框确定
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_011()
        # 列表最后一个
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_012()
        # 触发周期
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_020()
        # 触发时间
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_021("08分10秒")
        # 选择时间范围  ---开始----删除
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_025()
        # 选择时间范围  ---开始
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_022("2020.01.22 00:00:03")
        # 选择时间范围  ---结束----删除
        access_web[21].zh_xtsz_clya_clbj_026()
        # 选择时间范围  --结束
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_023("2022.05.33 00:00:09")
        # 时间保存
        access_web[21].zh_xtsz_clya_clbj_019()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "修改成功"




    def test_zh_stsz_clya_clbj_015(self, access_web):
        time.sleep(4)
        # 搜索框清除
        access_web[21].zh_xtsz_clya_clbj_010()
        # 搜索框输入
        access_web[21].zh_xtsz_clya_clbj_09("时间策略")
        # 搜索框确定
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_011()
        # 列表最后一个
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_012()
        # 点击关预案
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_013()
        # 关联预案最后一个
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_014()
        # 点击确定
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_015()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "修改成功"





    # 列表最后一个进行点击---点击删除
    def test_zh_stsz_clya_clbj_016(self, access_web):
        time.sleep(3)
        # 搜索框清除
        access_web[21].zh_xtsz_clya_clbj_010()
        # 搜索框输入
        access_web[21].zh_xtsz_clya_clbj_09("时间策略")
        # 搜索框确定
        time.sleep(1)
        access_web[21].zh_xtsz_clya_clbj_011()
        # 删除
        access_web[21].zh_xtsz_clya_clbj_017()
        assert access_web[21].zh_xtsz_clya_clbj_tsy() == "删除成功"


