import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_jkxt_qbbpz:

     # 输入正确账号跟密码   鼠标悬浮个人账号——点击系统设置---情报板配置 添加数据
     # 添加

    @pytest.mark.parametrize("data", LD.zcdl)
    def test_qbbpz_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(5)
        #鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        #鼠标悬浮系统设置点击情报板配置
        access_web[4].zh_xtsz_qbbpz()
        time.sleep(2)
        #点击添加类型
        access_web[4].zh_xtsz_qbbpz_01()
        time.sleep(2)
        #点击保存
        access_web[4].zh_xtsz_qbbpz_02()
        assert access_web[4].zh_xtsz_qbbpz_03()=="请选择厂家"


    def test_qbbpz_02(self, access_web):
         time.sleep(3)
         # 点击添加类型
         access_web[4].zh_xtsz_qbbpz_01()
         time.sleep(2)
         # 点击厂家
         access_web[4].zh_xtsz_qbbpz_04()
         time.sleep(2)
         # 字体大小
         access_web[4].zh_xtsz_qbbpz_06()
         # 点击保存
         access_web[4].zh_xtsz_qbbpz_02()
         assert access_web[4].zh_xtsz_qbbpz_03() == "添加成功"




    #修改
    def test_updata(self,access_web):
        time.sleep(3)
        # 列表点击最后一个
        access_web[4].zh_xtsz_qbbpz_07()
        time.sleep(2)
        # 尺寸
        access_web[4].zh_xtsz_qbbpz_05("1150")
        access_web[4].zh_xtsz_qbbpz_02()
        assert access_web[4].zh_xtsz_qbbpz_03()=="修改成功"



    #删除
    def test_delete(self,access_web):
         time.sleep(3)
         # 列表点击最后一个
         access_web[4].zh_xtsz_qbbpz_07()
         time.sleep(2)
         # 点击删除
         access_web[4].zh_xtsz_qbbpz_09()
         assert access_web[4].zh_xtsz_qbbpz_03()=="删除成功"









