import pytest

from selenium import webdriver

from TestDatas import Common_Datas  as CD                                         #地址

from TestDatas import login_datas   as  LD                                        #登录数据

from Pagelocators.loginpage_locators import LoginPageLocator  as loc              #这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）

driver=webdriver.Chrome()




@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数
class  Test_dl_denglushouye:

    #输入错误账号跟密码  验证提示框
    # @pytest.mark.usefixtures("sx")
    @pytest.mark.parametrize("data", LD.cwdl)
    # test_data=[
    #     {"text":"13547324646","password":"a1234567"}
    #
    # ]

    # @pytest.mark.parametrize("test_input",test_data)
    def test_dl_cuowudenglu(self,access_web,data,sx):
        access_web[1].login(data["text"],data["password"])
        # assert access_web[1].get_errordengluxinxi() == data["check"]




    #输入正确账号跟密码   验证  隧道结构检测
    @pytest.mark.parametrize("data", LD.zcdl)
    def test_dl_zhengchengdenglu(self,access_web,data):

        access_web[1].login(data["text"], data["password"])

        # assert access_web[1].login_suidaojiance()==loc.sdjc






