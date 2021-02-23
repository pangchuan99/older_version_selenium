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
# class  Test_jkxt_yppz:
#
#      #点击添加新配置---点击保存
#     @pytest.mark.parametrize("data", LD.zcdl)
#     def test_jkxt_yppz_01(self,access_web,data):
#         access_web[1].login(data["text"], data["password"])
#         access_web[2].zh()
#         time.sleep(1)
#         access_web[2].jkxt()
#         time.sleep(2)
#         access_web[17].zh_xtsz_yppz()
#         time.sleep(1)
#         access_web[17].zh_xtsz_yppz_01()
#         time.sleep(1)
#         assert  access_web[17].zh_xtsz_yppz_01_1()=="音频ID、版本号和名字为必填"
#
#
#
#     # 输入音频ID  点击保存
#     def test_jkxt_yppz_02(self, access_web):
#          time.sleep(3)
#          access_web[17].zh_xtsz_yppz_02(999999)
#          assert access_web[17].zh_xtsz_yppz_02_2() == "音频ID、版本号和名字为必填"
#
#
#
#
#     # 输入音频名称  点击保存
#     def test_jkxt_yppz_03(self, access_web):
#          time.sleep(3)
#          access_web[17].zh_xtsz_yppz_03(999999)
#          assert access_web[17].zh_xtsz_yppz_03_3() == "音频ID、版本号和名字为必填"
#
#
#
#
#     # 输入版本号  点击保存
#     def test_jkxt_yppz_04(self, access_web):
#          time.sleep(3)
#          access_web[17].zh_xtsz_yppz_04(999999)
#          assert access_web[17].zh_xtsz_yppz_04_4() == "添加成功"
#
#
#
#      # 修改版本号  点击保存
#     def test_jkxt_yppz_05(self, access_web):
#          time.sleep(3)
#          access_web[17].zh_xtsz_yppz_05(888888)
#          assert access_web[17].zh_xtsz_yppz_05_5() == "修改成功"
#
#
#
#
#     # 修改版本号  点击保存
#     def test_jkxt_yppz_06(self, access_web):
#         time.sleep(3)
#         access_web[17].zh_xtsz_yppz_06()
#         assert access_web[17].zh_xtsz_yppz_06_6() == "删除成功！"
#
#
#
#
#
#
#
#
#
#
#
#
