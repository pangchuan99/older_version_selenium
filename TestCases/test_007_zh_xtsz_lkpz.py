import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_jkxt_lkpz:

     #点击添加配置--点击保存
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_lkpz_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        # 账户进行鼠标悬浮---系统设置,点击路况配置
        access_web[5].zh_xtsz_lkpz()
        time.sleep(1)
        # 点击添加配置-
        access_web[5].zh_xtsz_lkpz_01()
        time.sleep(1)
        # 点击保存
        access_web[5].zh_xtsz_lkpz_02()
        assert access_web[5].zh_xtsz_lkpz_03()=="请选择图标类型"


    # 图标类型
    def test_lkpz_02(self, access_web):
         time.sleep(3)
         # 点击添加配置-
         access_web[5].zh_xtsz_lkpz_01()
         time.sleep(1)
         # 选择图标类型
         access_web[5].zh_xtsz_lkpz_04()
         time.sleep(1)
         # 点击保存
         access_web[5].zh_xtsz_lkpz_02()
         assert access_web[5].zh_xtsz_lkpz_03() == "请选择事件类型"

     # 事件类型
    def test_lkpz_03(self,access_web):
        time.sleep(3)
        # 点击添加配置-
        access_web[5].zh_xtsz_lkpz_01()
        time.sleep(1)
        # 选择图标类型
        access_web[5].zh_xtsz_lkpz_04()
        time.sleep(1)
        # 事件类型
        access_web[5].zh_xtsz_lkpz_05()
        time.sleep(1)
        # 点击保存
        access_web[5].zh_xtsz_lkpz_02()
        assert access_web[5].zh_xtsz_lkpz_03() == "请选择事件等级"


     #事件等级
    def test_lkpz_04(self,access_web):
        time.sleep(3)
        # 点击添加配置-
        access_web[5].zh_xtsz_lkpz_01()
        time.sleep(1)
        # 选择图标类型
        access_web[5].zh_xtsz_lkpz_04()
        time.sleep(1)
        # 事件类型
        access_web[5].zh_xtsz_lkpz_05()
        time.sleep(1)
        # 事件等级
        access_web[5].zh_xtsz_lkpz_06()
        # 点击保存
        access_web[5].zh_xtsz_lkpz_02()
        assert access_web[5].zh_xtsz_lkpz_03()=="路况配置已存在！"












