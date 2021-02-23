import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_jkxt_yppz:

     #点击添加新配置---点击保存
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_jkxt_yppz_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(1)
        # 账户进行鼠标悬浮---系统设置,点击音频配置
        access_web[17].zh_xtsz_yppz()
        time.sleep(1)
        # 点击添加新配置
        access_web[17].zh_xtsz_yppz_01()
        time.sleep(1)
        # 点击保存
        access_web[17].zh_xtsz_yppz_02()
        assert  access_web[17].zh_xtsz_yppz_03()=="音频ID、版本号和名字为必填"



    # 输入音频ID  点击保存
    def test_jkxt_yppz_02(self, access_web):
         time.sleep(3)
         # 点击添加新配置
         access_web[17].zh_xtsz_yppz_01()
         time.sleep(1)
         # 输入音频ID
         access_web[17].zh_xtsz_yppz_04(99999999)
         # 点击保存
         access_web[17].zh_xtsz_yppz_02()
         assert access_web[17].zh_xtsz_yppz_03() == "音频ID、版本号和名字为必填"




    # 输入音频名称  点击保存
    def test_jkxt_yppz_03(self, access_web):
         time.sleep(3)
         # 点击添加新配置
         access_web[17].zh_xtsz_yppz_01()
         time.sleep(1)
         # 输入音频ID
         access_web[17].zh_xtsz_yppz_04(99999999)
         # 输入音频名称
         access_web[17].zh_xtsz_yppz_05(99999999)
         # 点击保存
         access_web[17].zh_xtsz_yppz_02()
         assert access_web[17].zh_xtsz_yppz_03() == "音频ID、版本号和名字为必填"




    # 输入版本号  点击保存
    def test_jkxt_yppz_04(self, access_web):
         time.sleep(3)
         # 点击添加新配置
         access_web[17].zh_xtsz_yppz_01()
         time.sleep(1)
         # 输入音频ID
         access_web[17].zh_xtsz_yppz_04(99999999)
         # 输入音频名称
         access_web[17].zh_xtsz_yppz_05(99999999)
         # 输入版本号
         access_web[17].zh_xtsz_yppz_06(99999999)
         # 点击保存
         access_web[17].zh_xtsz_yppz_02()
         assert access_web[17].zh_xtsz_yppz_03() == "添加成功"



     # 修改版本号  点击保存
    def test_jkxt_yppz_05(self, access_web):
         time.sleep(3)
         # 音频ID搜索框
         access_web[17].zh_xtsz_yppz_07(99999999)
         # 查询
         access_web[17].zh_xtsz_yppz_08()
         # 列表点击最后一个
         access_web[17].zh_xtsz_yppz_09()
         # 修改版本号
         access_web[17].zh_xtsz_yppz_010(88888888)
         # 点击保存
         access_web[17].zh_xtsz_yppz_02()
         assert access_web[17].zh_xtsz_yppz_03() == "修改成功"




    # 修改版本号  点击保存
    def test_jkxt_yppz_06(self, access_web):

        # 列表点击最后一个
        # 音频ID搜索框
        # access_web[17].zh_xtsz_yppz_07(99999999)
        time.sleep(3)
        access_web[17].zh_xtsz_yppz_09()

        #删除
        access_web[17].zh_xtsz_yppz_011()
        assert access_web[17].zh_xtsz_yppz_03() == "删除成功！"












