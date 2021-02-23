# import pytest
#
# from selenium import webdriver
#
# from TestDatas import Common_Datas  as CD                                         #地址
#
# from TestDatas import login_datas   as  LD                                        #登录数据
#
# from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
# import time
#
#
#
#
#
# @pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数
# @pytest.mark.usefixtures("refresh_page")
#
# class  Test_jkxt_xtpz:
#
#      #输入正确账号跟密码   鼠标悬浮个人账号——点击系统设置---系统配置 进行文本框填写数据
#     @pytest.mark.parametrize("data", LD.zcdl)
#     def test_dl(self,access_web,data):
#         access_web[1].login(data["text"], data["password"])
#         time.sleep(2)
#         # 鼠标悬浮账户
#         access_web[29].zh_02()
#         time.sleep(2)
#         # 点击系统设置
#         access_web[29].zh_xtsz()
#         time.sleep(2)
#         #鼠标进行悬浮，点击系统配置
#         access_web[3].zh_xtsz_xtpz()
#         time.sleep(2)
#         access_web[3].zh_xtsz_xtpz_sr("延崇高速",16,32,32,15,15)
#         assert access_web[3].zh_xtsz_xtpz_tsy()=="修改成功"
#
#
#
