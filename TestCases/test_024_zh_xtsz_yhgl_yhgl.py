import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）
import time





@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数


class  Test_zh_stsz_yhgl_yhgl:


    #点击添加新用户  --点击保存
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_zh_stsz_yhgl_yhgl_01(self,access_web,data):
        access_web[1].login(data["text"], data["password"])
        time.sleep(2)
        # 鼠标悬浮账户
        access_web[29].zh_02()
        time.sleep(2)
        # 点击系统设置
        access_web[29].zh_xtsz()
        time.sleep(2)
        # 鼠标悬浮到策略预案  点击策略编辑
        time.sleep(2)
        # 输入悬浮到用户管理---点击用户管理
        access_web[22].zh_xtsz_yhgl()
        time.sleep(2)
        # 点击添加新用户
        access_web[22].zh_xtsz_yhgl_yhgl_01()
        # 保存
        access_web[22].zh_xtsz_yhgl_yhgl_05()
        assert access_web[22].zh_xtsz_yhgl_yhgl_tsy()=="请输入正确的手机号码"





    # 账号进行边界值输入(输入10位)  --点击保存
    def test_zh_stsz_yhgl_yhgl_02(self,access_web):
        time.sleep(3)
        # 点击添加新用户
        access_web[22].zh_xtsz_yhgl_yhgl_01()
        # 账号
        access_web[22].zh_xtsz_yhgl_yhgl_07("1399999999")
        # 保存
        access_web[22].zh_xtsz_yhgl_yhgl_05()
        assert access_web[22].zh_xtsz_yhgl_yhgl_tsy() == "请输入正确的手机号码"




    # 账号进行边界值输入（输入12位）  --点击保存
    def test_zh_stsz_yhgl_yhgl_03(self,access_web):
        time.sleep(3)
        # 点击添加新用户
        access_web[22].zh_xtsz_yhgl_yhgl_01()
        # 账号
        access_web[22].zh_xtsz_yhgl_yhgl_07("139999999999")
        # 保存
        access_web[22].zh_xtsz_yhgl_yhgl_05()
        assert access_web[22].zh_xtsz_yhgl_yhgl_tsy() == "请输入正确的手机号码"




    # 账号进行边界值输入（输入11位）  --点击保存
    def test_zh_stsz_yhgl_yhgl_04(self, access_web):
        time.sleep(3)
        # 点击添加新用户
        access_web[22].zh_xtsz_yhgl_yhgl_01()
        # 账号
        access_web[22].zh_xtsz_yhgl_yhgl_07("13999999999")
        # 保存
        access_web[22].zh_xtsz_yhgl_yhgl_05()
        assert access_web[22].zh_xtsz_yhgl_yhgl_tsy() == "必须包含名称"




   # 角色--保存
    def test_zh_stsz_yhgl_yhgl_05(self, access_web):
        time.sleep(3)
        # 点击添加新用户
        access_web[22].zh_xtsz_yhgl_yhgl_01()
        # 账号
        access_web[22].zh_xtsz_yhgl_yhgl_07("13999999999")
        # 角色
        access_web[22].zh_xtsz_yhgl_yhgl_08()
        # 保存
        access_web[22].zh_xtsz_yhgl_yhgl_05()
        assert access_web[22].zh_xtsz_yhgl_yhgl_tsy() == "必须包含名称"




    # 输入姓名---点击保存
    def test_zh_stsz_yhgl_yhgl_06(self, access_web):
        time.sleep(3)
        # 点击添加新用户
        access_web[22].zh_xtsz_yhgl_yhgl_01()
        # 账号
        access_web[22].zh_xtsz_yhgl_yhgl_07("13999999999")
        # 角色
        access_web[22].zh_xtsz_yhgl_yhgl_08()
        # 输入姓名
        access_web[22].zh_xtsz_yhgl_yhgl_09("张三")
        # 保存
        access_web[22].zh_xtsz_yhgl_yhgl_05()
        assert access_web[22].zh_xtsz_yhgl_yhgl_tsy() == "添加成功"



    # 点击添加新用户----输入账号---角色---姓名---点击保存---提示已存在
    def test_zh_stsz_yhgl_yhgl_07(self, access_web):
        time.sleep(3)
        # 点击添加新用户
        access_web[22].zh_xtsz_yhgl_yhgl_01()
        # 账号
        access_web[22].zh_xtsz_yhgl_yhgl_07("13999999999")
        # 角色
        access_web[22].zh_xtsz_yhgl_yhgl_08()
        # 输入姓名
        access_web[22].zh_xtsz_yhgl_yhgl_09("张三")
        # 保存
        access_web[22].zh_xtsz_yhgl_yhgl_05()
        assert access_web[22].zh_xtsz_yhgl_yhgl_tsy() == "账号已存在"






    def test_zh_stsz_yhgl_yhgl_08(self, access_web):
        time.sleep(3)
        # 账号搜索框--清除
        access_web[22].zh_xtsz_yhgl_yhgl_03()
        # 账号搜索框--输入
        access_web[22].zh_xtsz_yhgl_yhgl_02("13999999999")
        # 查询
        access_web[22].zh_xtsz_yhgl_yhgl_04()
        # 列表最后一个
        access_web[22].zh_xtsz_yhgl_yhgl_010()
        # 姓名清除
        access_web[22].zh_xtsz_yhgl_yhgl_011()
        # 输入姓名
        access_web[22].zh_xtsz_yhgl_yhgl_09("张三123")
        # 保存
        access_web[22].zh_xtsz_yhgl_yhgl_05()
        assert access_web[22].zh_xtsz_yhgl_yhgl_tsy() == "修改成功"





    # 点击最后一个分页---点击列表最后一个  -点击删除
    def test_zh_stsz_yhgl_yhgl_09(self, access_web):
        time.sleep(3)
        # 账号搜索框--清除
        access_web[22].zh_xtsz_yhgl_yhgl_03()
        # 账号搜索框--输入
        access_web[22].zh_xtsz_yhgl_yhgl_02("13999999999")
        # 查询
        access_web[22].zh_xtsz_yhgl_yhgl_04()
        # 列表最后一个
        access_web[22].zh_xtsz_yhgl_yhgl_010()
        # 删除
        access_web[22].zh_xtsz_yhgl_yhgl_06()

        assert access_web[22].zh_xtsz_yhgl_yhgl_tsy() == "删除成功"






