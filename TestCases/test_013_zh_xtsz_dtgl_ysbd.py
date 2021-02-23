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
#
#
# class  Test_zh_stsz_dtgl_hmlb:
#
#      #进行验证提示语---必须包含画面名称
#      #点击添加新画面-点击保存提示语
#     @pytest.mark.parametrize("data", LD.zcdl)
#     def test_zh_stsz_dtgl_hmlb_01(self,access_web,data):
#         access_web[1].login(data["text"], data["password"])
#         time.sleep(1)
#         # 鼠标悬浮账户
#         access_web[29].zh_02()
#         time.sleep(2)
#         # 点击系统设置
#         access_web[29].zh_xtsz()
#         time.sleep(2)
#         access_web[6].zh_xtsz_dtgl_ysbd()
#         time.sleep(2)
#         access_web[25]. zh_xtsz_dtgl_ysbd_01()
#         # assert access_web[7].zh_xtsz_dtgl_hmlb_tsy01_1()=="必须包含画面名称"
#
#
