# import pytest
#
# from selenium import webdriver
#
# from TestDatas import Common_Datas  as CD                                         #地址
#
# from TestDatas import login_datas   as  LD                                        #登录数据
#
# from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
#
#
#
#
#
# @pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数
# @pytest.mark.usefixtures("refresh_page")
#
# class  Test_zx:
#
#      #输入正确账号跟密码   鼠标悬浮个人账号——点击注销
#     @pytest.mark.parametrize("data", LD.zcdl)
#     def test_dl(self,access_web,data):
#         access_web[1].login(data["text"], data["password"])
#         access_web[30].zh_03()
#         access_web[30].zh_zx()
#
#
#
#
#
#
