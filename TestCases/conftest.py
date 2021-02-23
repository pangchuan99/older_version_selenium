import pytest
from selenium import webdriver
import time
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "D:\PYcharm\python16")))


from PageObjects.zh_001 import dl_denglushouye_yuansu #元素定位页面___登录首页

from TestDatas import Common_Datas  as CD    #地址

from PageObjects.zh_002_grzh import Test_grzh                                             #元素定位页面___个人中心

from PageObjects.zh_003_xtsz import Test_xtsz                                             #元素定位页面___系统设置

from PageObjects.zh_004_zx import Test_zx                                                 #元素定位页面___注销

from PageObjects.zh_005_xtsz_xtpz import Test_zh_xtsz_xtpz                                 #元素定位页面————系统配置

from PageObjects.zh_006_xtsz_qbbpz import Test_zh_xtsz_qbbpz                               #元素定位---系统设置---情报板配置

from PageObjects.zh_007_xtsz_lkpz import Test_zh_xtsz_lkpz                                 #元素定位----系统设置---路况配置

from PageObjects.zh_012_xtsz_dtgl_hmlb import Test_zh_xtsz_dtgl_hmlb                       #---系统设置---地图管理---画面列表

from PageObjects.zh_014_xtsz_dtgl_qybj import Test_zh_xtsz_dtgl_qybj                       #---系统设置---地图管理---区域编辑

from  PageObjects.zh_015_xtsz_zcgl_tjzc import Test_zh_xtsz_zcgl_tjzc                      #---系统设置---资产管理---添加资产

from PageObjects.zh_016_xtsz_zcgl_zclb import Test_zh_xtsz_zcgl_zclb                       #---系统设置---资产管理---资产列表

from PageObjects.zh_017_xtsz_zcgl_lxbj import Test_zh_xtsz_zcgl_lxbj                       #---系统设置---资产管理---类型编辑

from PageObjects.zh_018_xtsz_zcgl_ztbds import Test_zh_xtsz_zcgl_ztbds                     #---系统设置---资产管理---状态表达式

from PageObjects.zh_019_xtsz_zcgl_ykpz import Test_zh_xtsz_zcgl_ykpz                       #---系统设置---资产管理---遥控配置

from PageObjects.zh_020_xtsz_zcgl_jczpz import Test_zh_xtsz_zcgl_jczpz                     #---系统设置---资产管理---检测值配置

from  PageObjects.zh_021_xtsz_zcgl_cjpz import Test_zh_xtsz_zcgl_cjpz                      #---系统设置---资产管理---厂家配置

from PageObjects.zh_008_xtsz_yppz import Test_zh_xtsz_yppz                                 #元素定位----系统设置---音频配置

from PageObjects.zh_010_xtsz_lxrpz import Test_zh_xtsz_lxrpz                               #元素定位----系统设置---联系人配置

from PageObjects.zh_011_xtsz_cjqfd import Test_zh_xtsz_cjqfd                               #元素定位----系统设置---车检器分段

from PageObjects.zh_022_xtsz_clya_yabj import Test_zh_xtsz_clya_yabj                        #系统设置---策略预案---预案编辑

from PageObjects.zh_023_xtsz_clya_clbj import Test_zh_xtsz_clya_clbj                        #系统设置---策略预案---策略编辑

from PageObjects.zh_024_xtsz_yhgl_yhgl import Test_zh_xtsz_yhgl_yhgl                        #系统设置---用户管理---用户管理

from PageObjects.zh_025_xtsz_yhgl_jsgl import Test_zh_xtsz_yhgl_jsgl                        #系统设置---用户管理---角色管理

from PageObjects.zh_026_xtsz_yhgl_qxgl import Test_zh_xtsz_yhgl_qxgl                        #系统设置---用户管理---权限管理

from PageObjects.zh_013_xtsz_dtgl_ysbd import Test_zh_xtsz_dtgl_ysbd                        #系统设置---用户管理---元素绑定

from PageObjects.zh_027_dl_zbgl_pbgl import Test_zbgl_pbgl                                   #值班管理--排班管理

from PageObjects.zh_028_dl_zbgl_dfgl import Test_zbgl_dfgl                                   #值班管理--到访管理

from  PageObjects.zh_029_dl_zbgl_jjgl import Test_zbgl_jjgl                                  #值班管理--接警管理

from PageObjects.zh_030_dl_zcgl_sbbx import Test_zcgl_sbbx                                   #资产管理---设备报修

from PageObjects.zh_031_dl_zhjk_sbjk_qlk import Test_zhjk_sbjk_lqk                            #综合监控---设备监控  龙泉口隧道

from  PageObjects.zh_032_dl_zhjk_sbjk_jlb import Test_zhjk_sbjk_jlb                           #综合监控---设备监控  吉林堡隧道

from  PageObjects.zh_033_dl_zhjk_sbjk_tb import Test_zhjk_sbjk_tb                             #综合监控---设备监控  头孢堡隧道

from  PageObjects.zh_034_dl_zhjk_sbjk_gjy import  Test_zhjk_sbjk_gjy                          #综合监控---设备监控  郭家窑隧道

from  PageObjects.zh_035_dl_zhjk_sbjk_fjg import Test_zhjk_sbjk_fjg                           #综合监控---设备监控  冯家沟隧道

from  PageObjects.zh_036_dl_zhjk_sbjk_jjz import Test_zhjk_sbjk_jjz                          #综合监控---设备监控  金家庄隧道

from  PageObjects.zh_037_dl_zhjk_sbjk_qpl import Test_zhjk_sbjk_qpl                            #综合监控---设备监控  棋盘梁隧道


driver=None



#声明他是一个fixture
@pytest.fixture(scope="class")
def access_web():
    global driver  #global声明一个全局变量
    #前置操作
    print("=--------------类开始----------------")

    #下面这三行是 设置无头模式
    # opt= webdriver.ChromeOptions()
    # opt.set_headless()
    # driver=webdriver.Chrome(options=opt)


    #下面这一行代码是启动浏览器进行执行
    driver=webdriver.Chrome()


    driver.get(CD.yanchongxiangmu42)

    dl=dl_denglushouye_yuansu(driver)
    grzh=Test_grzh(driver)
    xtsz=Test_xtsz(driver)
    zx=Test_zx(driver)
    xtpz=Test_zh_xtsz_xtpz(driver)
    qbbpz=Test_zh_xtsz_qbbpz(driver)
    lkpz=Test_zh_xtsz_lkpz(driver)
    hmlb=Test_zh_xtsz_dtgl_hmlb(driver)
    qybj=Test_zh_xtsz_dtgl_qybj(driver)
    tjzc=Test_zh_xtsz_zcgl_tjzc(driver)
    zclb=Test_zh_xtsz_zcgl_zclb(driver)
    lxbj=Test_zh_xtsz_zcgl_lxbj(driver)
    ztbds=Test_zh_xtsz_zcgl_ztbds(driver)
    ykpz=Test_zh_xtsz_zcgl_ykpz(driver)
    jczpz=Test_zh_xtsz_zcgl_jczpz(driver)
    cjpz=Test_zh_xtsz_zcgl_cjpz(driver)
    yppz=Test_zh_xtsz_yppz(driver)
    lxrpz=Test_zh_xtsz_lxrpz(driver)
    cjqfd=Test_zh_xtsz_cjqfd(driver)
    yabj=Test_zh_xtsz_clya_yabj(driver)
    clbj=Test_zh_xtsz_clya_clbj(driver)
    yhgl=Test_zh_xtsz_yhgl_yhgl(driver)
    jsgl=Test_zh_xtsz_yhgl_jsgl(driver)
    qxgl=Test_zh_xtsz_yhgl_qxgl(driver)
    ysbd=Test_zh_xtsz_dtgl_ysbd(driver)
    pbgl=Test_zbgl_pbgl(driver)
    dfgl=Test_zbgl_dfgl(driver)
    jjgl=Test_zbgl_jjgl(driver)
    sbbx=Test_zcgl_sbbx(driver)

    jksb_lqk=Test_zhjk_sbjk_lqk(driver)
    jksb_jlb=Test_zhjk_sbjk_jlb(driver)
    jksb_tb= Test_zhjk_sbjk_tb(driver)
    jksb_gjy= Test_zhjk_sbjk_gjy(driver)
    jksb_fjg=Test_zhjk_sbjk_fjg(driver)
    jksb_jjz= Test_zhjk_sbjk_jjz(driver)
    jksb_qpl= Test_zhjk_sbjk_qpl(driver)

    yield(driver,dl,grzh,xtpz,qbbpz,lkpz,123,hmlb,qybj,456,tjzc,zclb,lxbj,ztbds,ykpz,jczpz,cjpz,yppz,lxrpz,cjqfd,yabj,clbj,yhgl,jsgl,qxgl,ysbd,pbgl,dfgl,jjgl,xtsz,zx,sbbx,jksb_lqk,jksb_jlb,jksb_tb,jksb_gjy,jksb_fjg,jksb_jjz,jksb_qpl) #下标是从0开始的             这个关键字指的是分隔符  yield前面指的前置条件   yield后面是后置条件
    '       0     1   2    3    4    5    6   7    8    9   10   11   12   13    14   15    16   17   18     19   20   21   22   23   24   25   26   27   28   29  30  31     32        33        34      35     36         37       38'
                                                                             #代表分割线：#后面接返回值
    #后置操作
    print("---------------结束----------------")
    driver.quit()



@pytest.fixture()
def sx():
    global driver
    #前置操作
    yield
    time.sleep(2)
    driver.refresh()




    #后置操作



# @pytest.fixture(scope="session")
# def session_demon():
#     print("*************我是整个测试绘画期间的开始****************")
#     yield
#     print("**************我是整个测试绘画期间的结束***************")
#
