

from  selenium.webdriver.common.by import By


class LoginPageLocator:

    # 元素定位
    '''登陆模块定位'''
    # 用户名输入框
    name_text = (By.XPATH, '//input[@type="text"]')
    # 密码输入框
    pwd_text = (By.XPATH, '//input[@type="password"]')
    # 点击登录
    login_but = (By.XPATH, '//button[@type="button"]')
    #输入错误账号和密码就弹出提示框
    tishicuowu=(By.XPATH,'//*[contains(text(),"账户或密码错误")]')
    #登陆成功后进行预期结果和实际结果
    suidaojiesoujiance=(By.XPATH,'//*[contains(text(),"隧道结构检测")]')
    sdjc='隧道结构检测'
    '''登陆模块定位'''



    '''登陆账户模块定位'''
    #定位账号---显示信息下拉框----鼠标悬浮
    zh=(By.XPATH,'//*[@id="user-profile"]')
    #账号中的个人中心，监控系统，注销
    zh_xllb=(By.XPATH,'//*[@class="user-handle"]//div')

    # #个人中心
    # grzx=(By.XPATH,'//*[text()="个人中心"]')
    # #系统设置
    # xtsz=(By.XPATH,'//*[text()="系统设置"]')
    # #注销
    # zx=(By.XPATH,'//*[text()="注销"]')
    # '''登陆账户模块定位'''
    #
    #
    #

    '''账户里面的 系统设置'''
    #账号里面的——系统设置
    zh_xtsz=(By.XPATH,'//*[contains(text(),"系统设置")]')

    '''账户里面的 系统设置---系统配置'''
    #进行定位系统配置
    zh_xtsz_xtpz=(By.XPATH,'//*[contains(text(),"系统配置")]')
    #进行定位系统名称
    zh_xtsz_xtpz_xtmc=(By.XPATH,'//*[@class="ivu-input"]')
    #进行定位字体大小
    zh_xtsz_xtpz_ztdx=(By.XPATH,'//div[3]//div[@class="item"]//*[@class="ivu-input-number-input"]')
    #进行定位图片宽度
    zh_xtsz_xtpz_tpkd=(By.XPATH,'//div[@class="item extra"]//*[@class="ivu-input-number-input"]')
    #进行定位图片高度
    zh_xtsz_xtpz_tpgd=(By.XPATH,'//div[@class="item extra1"]//*[@class="ivu-input-number-input"]')
    #进行定位居左距离
    zh_xtsz_xtpz_jzjl=(By.XPATH,'//div[5]//div[@class="item"]//*[@class="ivu-input-number-input"]')

    # 进行定位居右距离
    zh_xtsz_xtpz_jyjl=(By.XPATH,'//div[6]//div[@class="item"]//*[@class="ivu-input-number-input"]')
    #进行点击保存
    zh_xtsz_xtpz_bc=(By.XPATH,'//*[contains(text(),"保")]')
    #点击保存 提示 修改成功
    zh_xtsz_xtpz_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    '''账户里面的 系统设置---系统配置'''




    '''账户里面的 系统设置---情报板配置'''
    #进行定位情报板配置
    zh_xtsz_qbbpz=(By.XPATH,'//*[contains(text(),"情报板配置")]')
    #点击  添加新类型
    zh_xtsz_qbbpz_tjxlx=(By.XPATH,'//*[text()="添加新类型"]')
    #厂家
    zh_xtsz_qbbpz_cj1=(By.XPATH,'//*[text()="请选择"]')
    #厂家下拉框里面的内容
    zh_xtsz_qbbpz_xlnr=(By.XPATH,'//*[@class="ivu-select-dropdown-list"]//li')
    #尺寸
    zh_xtsz_qbbpz_cc=(By.XPATH,'//*[@class="inbg ivu-form-item"]//*[@class="ivu-input-number-input"]')
    #字体大小---
    zh_xtsz_qbbpz_ztdx=(By.XPATH,'//div[5][@class="div-click"]//*[@class="div-click-item"]//div')
    #字体类型
    zh_xtsz_qbbpz_ztlx=(By.XPATH,'//div[6][@class="div-click"]//*[@class="div-click-item"]//div')
    #点击保存
    zh_xtsz_qbbpz_bc=(By.XPATH,'//*[contains(text(),"保存")]')
    #提示语
    zh_xtsz_qbbpz_tsy = (By.XPATH, '//*[@class="ivu-notice-title"]')
    # #提示  请选择厂家
    # zh_xtsz_qbbpz_cj = (By.XPATH, '//*[contains(text(),"请选择厂家")]')
    # #提示添加成功
    # zh_xtsz_qbbpz_tjcg=(By.XPATH,'//*[contains(text(),"添加成功")]')
    # #提示修改成功
    # zh_xtsz_qbbpz_xgcg=(By.XPATH,'//*[contains(text(),"修改成功")]')
    #点击删除
    zh_xtsz_qbbpz_sc=(By.XPATH,'//*[text()="删除"]')
    #弹出框点击确定
    zh_xtsz_qbbpz_qd=(By.XPATH,'//*[@class="ivu-modal-confirm-footer"]//*[text()="确定"]')
    # #提示删除成功
    # zh_xtsz_qbbpz_sccg=(By.XPATH,'//*[contains(text(),"删除成功")]')

    #列表最后一个
    zh_xtsz_qbbpz_lb=(By.XPATH,'//*[@class="ivu-table-tbody"]//tr')

    '''账户里面的 系统设置---情报板配置'''






    '''账户里面的 系统设置---路况配置'''
    #进行定位路况配置
    zh_xtsz_lkpz = (By.XPATH, '//*[contains(text(),"路况配置")]')
    #点击 添加配置
    zh_xtsz_lkpz_tjpz=(By.XPATH,'//*[text()="添加配置"]')
    #图标类型
    zh_xtsz_lkpz_tb=(By.XPATH,'//*[contains(@class,"ivu-form-item")]//*[@class="ivu-select-placeholder"]')
    #正确的---图标类型
    zh_xtsz_lkpz_zqtb= (By.XPATH, '//div[1][@class="ivu-form-item"]//*[@class="ivu-select-placeholder"]')
    #图标类型下拉框内容
    zh_xtsz_lkpz_tbxl=(By.XPATH,'//*[@class="ivu-select-dropdown-list"]//li[1][contains(text(),"路况")]')

    #事件类型
    zh_xtsz_lkpz_sj=(By.XPATH,'//*[contains(@class,"ivu-form-item")]//*[@class="ivu-select-placeholder"]')
    #事件类型下拉框内容
    zh_xtsz_lkpz_sjxlxl=(By.XPATH,'//*[@class="row fill"]//div[2][contains(@class,"ivu-form-item")]//*[@class="ivu-select-dropdown-list"]//li')

    #事件等级
    zh_xtsz_lkpz_sjdj=(By.XPATH,'//*[contains(@class,"ivu-form-item")]//*[@class="ivu-select-placeholder"]')
    #事件等级下拉框内容
    zh_xtsz_lkpz_sjdjxl=(By.XPATH,'//*[@class="row fill"]//div[3][contains(@class,"ivu-form-item")]//*[@class="ivu-select-dropdown-list"]//li')
    #点击保存
    zh_xtsz_lkpz_bc=(By.XPATH,'//*[text()="保存"]')
    #点击保存后提示语---请选择图标类型
    zh_xtsz_lkpz_tsy=(By.XPATH,'//*[@class="ivu-notice-title"]')
    '''账户里面的 系统设置---路况配置'''




    '''账户里面的 系统设置--音频配置'''
    #进行定位音频配置
    zh_xtsz_yppz= (By.XPATH, '//*[contains(text(),"音频配置")]')
    # 添加新配置
    zh_xtsz_yppz_tjxpz= (By.XPATH, '//*[text()="添加新配置"]')
    # 保存
    zh_xtsz_yppz_bc= (By.XPATH, '//*[text()="保存"]')
    # 删除
    zh_xtsz_yppz_sc= (By.XPATH, '//*[text()="删除"]')
    # 删除弹出框---点击确定
    zh_xtsz_yppz_sctck= (By.XPATH, '//*[@class="ivu-btn ivu-btn-primary"]//*[text()="确定"]')
    # 提示语---音频ID、版本号和名字为必填-----修改成功---删除成功！
    zh_xtsz_yppz_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    # 音频ID
    zh_xtsz_yppz_ypid= (By.XPATH,'//div[2][@class="inbg require-star ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 音频名称
    zh_xtsz_yppz_ypmc= (By.XPATH, '//div[3][@class="inbg require-star ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 版本号
    zh_xtsz_yppz_bbh= (By.XPATH, '//div[4][@class="inbg require-star ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 分页
    zh_xtsz_yppz_fy= (By.XPATH, '//*[@class="ivu-page"]//li')
    # 音频ID搜索框
    zh_xtsz_yppz_ypidssk= (By.XPATH, '//div[1][@class="ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 查询
    zh_xtsz_yppz_cx= (By.XPATH, '//*[@class="ivu-btn ivu-btn-primary ivu-btn-circle"]')

    # 列表
    zh_xtsz_yppz_lb= (By.XPATH, '//*[@class="ivu-table-tbody"]//tr')
    '''账户里面的 系统设置--音频配置'''




    #进行定位视频配置
    zh_xtsz_sppz = (By.XPATH, '//*[contains(text(),"视频配置")]')

    '''账户里面的 系统设置--联系人配置'''
    #进行定位联系人配置
    zh_xtsz_lxrpz = (By.XPATH, '//*[contains(text(),"联系人配置")]')
    # 添加新成员
    zh_xtsz_lxrpz_tjxcy= (By.XPATH, '//*[text()="添加新成员"]')
    # 姓名
    zh_xtsz_lxrpz_xm= (By.XPATH, '//div[2][@class="inbg ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')


    # 性别
    zh_xtsz_lxrpz_xb= (By.XPATH, '//div[3][@class="inbg ivu-form-item"]//*[@class="ivu-select-placeholder"]')
    # 性别下拉
    zh_xtsz_lxrpz_xbxl= (By.XPATH, '//div[3][@class="inbg ivu-form-item"]//*[@class="ivu-select-dropdown-list"]//li')
    # 电话
    zh_xtsz_lxrpz_dh= (By.XPATH, '//div[4][@class="inbg ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 公司
    zh_xtsz_lxrpz_gs= (By.XPATH, '//div[5][@class="inbg ivu-form-item"]//*[@class="ivu-select-placeholder"]')
    # 公司下拉
    zh_xtsz_lxrpz_gsxl= (By.XPATH, '//div[5][@class="inbg ivu-form-item"]//*[@class="ivu-select-dropdown-list"]//li')
    # 部门
    zh_xtsz_lxrpz_bm= (By.XPATH, '//div[6][@class="inbg ivu-form-item"]//*[@class="ivu-select-placeholder"]')
    # 部门下拉
    zh_xtsz_lxrpz_bmxl= (By.XPATH, '//div[6][@class="inbg ivu-form-item"]//*[@class="ivu-select-dropdown-list"]//li')
    # 职位
    zh_xtsz_lxrpz_zw= (By.XPATH, '//div[7][@class="inbg ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 删除
    zh_xtsz_lxrpz_sc= (By.XPATH, '//*[@class="form-btns"]//*[text()="删除"]')
    # 删除弹出框---点击确定
    zh_xtsz_lxrpz_sctck= (By.XPATH, '//*[text()="确定"]')
    # 保存
    zh_xtsz_lxrpz_bc= (By.XPATH, '//*[@class="form-btns"]//*[text()="保存"]')
    # 提示语
    zh_xtsz_lxrpz_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    # 提示语----删除成功
    zh_xtsz_lxrpz_tsysccg= (By.XPATH, '//*[text()="删除成功"]')
    # 列表最后一个
    zh_xtsz_lxrpz_lbzhyg= (By.XPATH, '//*[@class="row fill"]//*[@class="ivu-table-tbody"]//tr')
    # 姓名搜索框
    zh_xtsz_lxrpz_xmssk= (By.XPATH, '//*[@class="ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 查询
    zh_xtsz_lxrpz_cx= (By.XPATH, '//*[@class="ivu-btn ivu-btn-primary ivu-btn-circle"]')


    #进行左侧列表操作
    #左侧---添加
    zh_xtsz_lxrpz_zctj= (By.XPATH, '//*[text()="添加"]')
    #左侧---删除
    zh_xtsz_lxrpz_zcsc= (By.XPATH, '//*[@class="leftremovebtn leftbtn ivu-btn ivu-btn-default"]//*[text()="删除"]')
    # 左侧---删除弹出框---点击确定
    zh_xtsz_lxrpz_zcsctck= (By.XPATH, '//*[text()="确定"]')

    # 左侧---类型
    zh_xtsz_lxrpz_zclx= (By.XPATH, '//*[@class="bounced"]//*[@class="ivu-select-selected-value"]')
    # 左侧---类型下拉选择部门
    zh_xtsz_lxrpz_zclxxl= (By.XPATH, '//*[@class="bounced"]//*[@class="ivu-select-dropdown-list"]//li')
    # 左侧---公司
    zh_xtsz_lxrpz_zcgs = (By.XPATH,'//*[@class="bounced"]//*[@class="ivu-select-placeholder"]')
    # 左侧---（公司 列表）取某一个
    zh_xtsz_lxrpz_zcgsxl= (By.XPATH, '//*[@class="light ivu-form ivu-form-label-right"]/div[2]//*[@class="ivu-select-dropdown-list"]//li')
    #左侧---名称
    zh_xtsz_lxrpz_zcmc= (By.XPATH, '//*[@class="light ivu-form ivu-form-label-right"]//*[@class="ivu-input ivu-input-default"]')
    # 左侧---保存
    zh_xtsz_lxrpz_zcbc= (By.XPATH, '//*[text()="保存"]')
    # 左侧---列表最后一个
    zh_xtsz_lxrpz_zclbzhyg= (By.XPATH, '//*[@class="ivu-tree"]//ul')
    '''账户里面的 系统设置--联系人配置'''





    '''账户里面的 系统设置--车检器分段'''
    #进行定位车检器分段
    zh_xtsz_cjqfd = (By.XPATH, '//*[contains(text(),"车检器分段")]')
    # 添加新配置
    zh_xtsz_cjqfd_tjxpz= (By.XPATH, '//*[text()="添加新配置"]')
    #保存
    zh_xtsz_cjqfd_bc= (By.XPATH, '//*[text()="保存"]')
    # 删除
    zh_xtsz_cjqfd_sc= (By.XPATH, '//*[text()="删除"]')
    # 删除弹出框---点击确定
    zh_xtsz_cjqfd_sctck= (By.XPATH, '//*[text()="确定"]')
    #方向
    zh_xtsz_cjqfd_fx= (By.XPATH, '//*[@class="ivu-select-selected-value"]')
    # 方向下拉内容
    zh_xtsz_cjqfd_fxxlnr= (By.XPATH, '//*[@class="inbg dir ivu-form-item"]//*[@class="ivu-select-dropdown-list"]//li')

    # 起始设备
    zh_xtsz_cjqfd_qssb= (By.XPATH, '//div[2][@class="inbg dir require-star ivu-form-item"]//*[@class="ivu-select-input"]')
    # 起始设备下拉
    zh_xtsz_cjqfd_qssbxl= (By.XPATH, '//div[2][@class="inbg dir require-star ivu-form-item"]//*[@class="ivu-select-dropdown-list"]//li')
    # 结束设备
    zh_xtsz_cjqfd_jssb= (By.XPATH, '//div[3][@class="inbg dir require-star ivu-form-item"]//*[@class="ivu-select-input"]')
    # 结束设备下拉
    zh_xtsz_cjqfd_jssbxl= (By.XPATH, '//div[3][@class="inbg dir require-star ivu-form-item"]//*[@class="ivu-select-dropdown-list"]//li')
    # 车道数
    zh_xtsz_cjqfd_cds= (By.XPATH, '//*[contains(@class,"inbg require-star ivu-form-item")]//*[@class="ivu-input ivu-input-default"]')
    # 提示语-------起始设备、结束设备和车道数为必填项
    zh_xtsz_cjqfd_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    # 列表
    zh_xtsz_cjqfd_lb= (By.XPATH, '//*[@class="ivu-table-tbody"]//tr')

    '''账户里面的 系统设置--车检器分段'''






    #地图管理
    zh_xtsz_dtgl=(By.XPATH,'//*[contains(text(),"地图管理")]')

    '''系统设置-----地图管理---画面列表'''
    #画面列表
    zh_xtsz_dtgl_hmlb=(By.XPATH,'//*[contains(text(),"画面列表")]')
    #添加新画面
    zh_xtsz_dtgl_hmlb_tjxhm=(By.XPATH,'//*[@class="addnewbtn ivu-btn ivu-btn-primary"]')
    # 名称搜索框
    zh_xtsz_dtgl_hmlb_mcssk = (By.XPATH, '//*[@class="light ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 查询
    zh_xtsz_dtgl_hmlb_cx= (By.XPATH, '//*[text()="查询"]')
    #点击保存
    zh_xtsz_dtgl_hmlb_bc = (By.XPATH, '//*[@class="form-btns"]//*[@class="savebtn ivu-btn ivu-btn-primary"]')
    #点击删除
    zh_xtsz_dtgl_hmlb_sc=(By.XPATH,'//*[@class="form-btns"]//*[@class="ivu-btn ivu-btn-default"]')
    #点击删除弹框-点击确定
    zh_xtsz_dtgl_hmlb_sctck=(By.XPATH,'//*[@class="ivu-modal-confirm-footer"]//*[contains(text(),"确定")]')
    #点击保存提示语
    zh_xtsz_dtgl_hmlb_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    #名称
    zh_xtsz_dtgl_hmlb_mc=(By.XPATH,'//*[contains(@class,"require-star ivu-form-item")]//*[@class="ivu-input ivu-input-default"]')
    # 画面类别
    zh_xtsz_dtgl_hmlb_hmlb= (By.XPATH, '//*[@class="require-star ivu-form-item"]//*[@class="ivu-select-selected-value"]')
    # 画面类别---下拉内容
    zh_xtsz_dtgl_hmlb_hmlbxl= (By.XPATH, '//*[@class="require-star ivu-form-item"]//*[@class="ivu-select-dropdown-list"]/li')
    #结构物
    zh_xtsz_dtgl_hmlb_jgw=(By.XPATH,'//*[contains(@class,"require-star ivu-form-item")]//*[@class="ivu-select-placeholder"]')
    #结构物下拉内容
    zh_xtsz_dtgl_hmlb_jgwxl=(By.XPATH,'//div[4][@class="ivu-row"]//*[@class="ivu-select-dropdown-list"]//li')
    #矢量底图
    zh_xtsz_dtgl_hmlb_zldt=(By.XPATH,'//*[contains(@class,"require-star tile-url1")]//*[@class="ivu-input ivu-input-default"]')
    #列表最后一个
    zh_xtsz_dtgl_hmlb_lb=(By.XPATH,'//*[@class="ivu-table-tbody"]//tr')
    '''系统设置----地图管理---画面列表'''




    '''系统设置----地图管理---元素绑定'''
    #元素绑定
    zh_xtsz_dtgl_ysbd=(By.XPATH,'//*[contains(text(),"元素绑定")]')
    #设备
    zh_xtsz_dtgl_ysbd_sb= (By.XPATH, '//*[@class="dragbox"]//div')
    # 另一个div元素
    zh_xtsz_dtgl_ysbd_div= (By.XPATH, '//*[@class="leaflet-marker-icon leaflet-zoom-animated leaflet-interactive selected leaflet-marker-draggable"]')
    '''系统设置----地图管理---元素绑定'''




    #区域编辑
    '''地图管理中的-画面列表--元素绑定---区域编辑'''
    zh_xtsz_dtgl_qybj=(By.XPATH,'//*[contains(text(),"区域编辑")]')
    #添加新区域
    zh_xtsz_dtgl_qybj_tjxqy=(By.XPATH,'//*[@class="addnewbtn ivu-btn ivu-btn-primary"]')
    #查询
    zh_xtsz_dtgl_qybj_cx=(By.XPATH,'//*[@class="ivu-btn ivu-btn-primary ivu-btn-circle"]')

    #保存
    zh_xtsz_dtgl_qybj_bc=(By.XPATH,'//*[@class="savebtn ivu-btn ivu-btn-primary"]')
    #删除
    zh_xtsz_dtgl_qybj_sc=(By.XPATH,'//*[@class="ivu-btn ivu-btn-default"]')
    #删除弹出框
    zh_xtsz_dtgl_qybj_sctck=(By.XPATH,'//*[text()="确定"]')
    #提示语---
    zh_xtsz_dtgl_qybj_tsy=(By.XPATH,'//*[@class="ivu-notice-title"]')

    # 区域类型
    zh_xtsz_dtgl_qybj_qylx= (By.XPATH,'//*[contains(@class,"region-property require-star ivu-form-item")]//*[@class="ivu-select-placeholder"]')
    #区域类型下拉框内容
    zh_xtsz_dtgl_qybj_qylxxl = (By.XPATH, '//*[contains(@class,"region-property require-star ivu-form-item")]//*[@class="ivu-select-dropdown-list"]//li')
    #名称
    zh_xtsz_dtgl_qybj_mc=(By.XPATH,'//*[contains(@class,"editarea panel grey ivu-form")]//*[@class="ivu-input ivu-input-default"]')
    #对应结构物
    zh_xtsz_dtgl_qybj_dyjgw=(By.XPATH,'//div[3][@class="region-property ivu-form-item"]//*[@class="ivu-select-placeholder"]')
    #对应结构物下拉框内容
    zh_xtsz_dtgl_qybj_dyjgwxl=(By.XPATH,'//div[3][@class="region-property ivu-form-item"]//*[@class="ivu-select-dropdown-list"]//li')
    #列表最后一个
    zh_xtsz_dtgl_qybj_lb=(By.XPATH,'//*[@class="ivu-table-tbody"]//tr')
    '''地图管理中的-画面列表--元素绑定---区域编辑'''





    '''系统设置---资产管理'''
    #资产管理
    zh_xtsz_zcgl=(By.XPATH,'//*[contains(text(),"资产管理")]')
    '''系统设置---资产管理---资产添加'''
    #资产添加
    zh_xtsz_zcgl_tjzc=(By.XPATH,'//*[text()="添加资产"]')
    #类型
    zh_xtsz_zcgl_tjzc_lx=(By.XPATH,'//div[1][@class="property-row ivu-row"]//*[@class="ivu-select-input"]')
    # 类型下拉火灾手报
    zh_xtsz_zcgl_tjzc_lxxl = (By.XPATH, '//div[1][@class="property-row ivu-row"]//*[@class="ivu-select-dropdown-list"]//*[text()="火灾手报"]')
    #名称
    #zh_xtsz_zcgl_tjzc_mc=(By.XPATH,'//div[2][@class="property-col ivu-col ivu-col-span-6"]//*[@class="ivu-input-wrapper ivu-input-wrapper-default ivu-input-type"]')
    zh_xtsz_zcgl_tjzc_mc=(By.XPATH,'//*[2][@class="property-col ivu-col ivu-col-span-6"]//*[@class="require-star ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')

    #桩号
    zh_xtsz_zcgl_tjzc_zh=(By.XPATH,'//*[1][@class="property-col ivu-col ivu-col-span-6"]//*[@class="require-star ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    #区域
    zh_xtsz_zcgl_tjzc_qy=(By.XPATH,'//*[@class="property-row ivu-row"]//div[2][@class="property-col ivu-col ivu-col-span-6"]//*[@class="ivu-select-input"]')
    #区域下拉---金家庄隧道
    zh_xtsz_zcgl_tjzc_qyxl=(By.XPATH,'//div[4][@class="property-row ivu-row"]//div[2][@class="property-col ivu-col ivu-col-span-6"]//*[@class="ivu-select-dropdown-list"]//li')
    #额定功率
    zh_xtsz_zcgl_tjzc_edgl= (By.XPATH, '//*[@class="test-common common-property"]//*[@class="ivu-input ivu-input-default"]')
    #保存
    zh_xtsz_zcgl_tjzc_bc=(By.XPATH,'//*[@class="item-component edit testedit"]//*[@class="save-btn ivu-btn ivu-btn-primary"]')
    # 提示语
    zh_xtsz_zcgl_tjzc_tsy = (By.XPATH, '//*[@class="ivu-notice-title"]')

    '''系统设置---资产管理---资产添加'''








    '''系统设置---资产管理---资产列表'''
    #资产列表
    zh_xtsz_zcgl_zclb=(By.XPATH,'//*[text()="资产列表"]')
    #设备名称搜索框
    zh_xtsz_zcgl_zclb_sbmc=(By.XPATH,'//div[1][@class="ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 名称
    zh_xtsz_zcgl_zclb_mc = (By.XPATH, '//div[1][@class="property-row ivu-row"]//*[@class="ivu-input ivu-input-default"]')
    #查询
    zh_xtsz_zcgl_zclb_cx=(By.XPATH,'//*[text()="查询"]')
    # 列表最后一个
    zh_xtsz_zcgl_zclb_lb= (By.XPATH, '//*[@class="ivu-table ivu-table-default ivu-table-border"]//div[2]//tr')
    # 详细编辑
    zh_xtsz_zcgl_zclb_xxbj = (By.XPATH, '//*[text()="详细编辑"]')
    # 详细编辑里面的保存
    zh_xtsz_zcgl_zclb_bc = (By.XPATH, '//*[contains(text(),"保存")]')
    # 提示语
    zh_xtsz_zcgl_zclb_tsy = (By.XPATH, '//*[@class="ivu-notice-title"]')
    # 详细编辑里面的资产列表
    zh_xtsz_zcgl_zclb_xxbjzclb= (By.XPATH, '//*[@class="ivu-breadcrumb"]//*[contains(text(),"资产列表")]')
    # 删除
    zh_xtsz_zcgl_zclb_sc = (By.XPATH, '//*[contains(text(),"删除")]')
    # 删除弹出框点击确定
    zh_xtsz_zcgl_zclb_sctck = (By.XPATH, '//*[text()="确定"]')

    '''系统设置---资产管理---资产列表'''









    '''系统设置---资产管理---类型编辑'''
    #类型编辑
    zh_xtsz_zcgl_lxbj=(By.XPATH,'//*[text()="类型编辑"]')
    # 添加类型
    zh_xtsz_zcgl_lxbj_tjlx= (By.XPATH, '//*[text()="添加类型"]')
    # 类型名称搜索框
    zh_xtsz_zcgl_lxbj_lxmcssk= (By.XPATH, '//*[@class="name ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 查询
    zh_xtsz_zcgl_lxbj_cx= (By.XPATH, '//*[text()="查询"]')

    # 类型ID
    zh_xtsz_zcgl_lxbj_lxid = (By.XPATH, '//*[@class="formcon"]/div[1]/div/div[2]/input')
    # 分组ID
    zh_xtsz_zcgl_lxbj_fzid= (By.XPATH, '//*[text()="请选择"]')
    # 分组ID下拉内容
    zh_xtsz_zcgl_lxbj_fzidxl= (By.XPATH, '//*[@class="formcon"]/div[2]//*[@class="ivu-select-dropdown-list"]//li')
    # 类型名称
    zh_xtsz_zcgl_lxbj_lxmc= (By.XPATH, '//*[@class="formcon"]/div[3]/div/div[2]/input')
    #类型参数---变量名
    zh_xtsz_zcgl_lxbj_lxcsblm= (By.XPATH, '//*[@class="formcon"]/div[8]/div/div[2]/span[1]/div/input')
    #删除
    zh_xtsz_zcgl_lxbj_sc= (By.XPATH, '//*[text()="删除"]')
    # 删除之后弹出框---点击确定
    zh_xtsz_zcgl_lxbj_sctck = (By.XPATH, '//*[text()="确定"]')
    # 保存
    zh_xtsz_zcgl_lxbj_bc= (By.XPATH, '//*[text()="保存"]')
    # 提示语---请输入类型ID---请选择分组---请输入类型名称---变量名格式错误!---删除成功---已存在
    zh_xtsz_zcgl_lxbj_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    #类型分组
    zh_xtsz_zcgl_lxbj_lxfz=(By.XPATH,'//*[@class="ivu-select-selection"]//*[text()="全部"]')
    #类型分组下拉框---其他对象
    zh_xtsz_zcgl_lxbj_lxfzxl=(By.XPATH,'//*[@class="ivu-select-dropdown-list"]//*[text()="其他对象"]')
    # 列表最后一个
    zh_xtsz_zcgl_lxbj_lb= (By.XPATH, '//*[@class="ivu-table-tbody"]//tr')

    '''系统设置---资产管理---类型编辑'''





    '''系统设置---资产管理---状态表达式'''

    #状态表达式
    zh_xtsz_zcgl_ztbds=(By.XPATH,'//*[text()="状态表达式"]')
    # 添加表达式
    zh_xtsz_zcgl_ztbds_tjbds= (By.XPATH, '//*[text()="添加表达式"]')
    # 设备类型
    zh_xtsz_zcgl_ztbds_sblx= (By.XPATH, '//*[@class="ivu-select-selection"]//input[@placeholder="请选择"]')
    # 设备类型下拉内容
    zh_xtsz_zcgl_ztbds_sblxxl=(By.XPATH, '//*[@class="editarea panel grey ivu-form ivu-form-label-right"]//*[@class="ivu-select-dropdown-list"]//li')
    # 状态
    zh_xtsz_zcgl_ztbds_zt=(By.XPATH, '//*[@class="ivu-select-selection"]//*[text()="请选择"]')
    # 状态下拉
    zh_xtsz_zcgl_ztbds_ztxl=(By.XPATH, '//*[@class="ivu-select-dropdown"]//*[text()="网络故障"]')
    # 版本
    zh_xtsz_zcgl_ztbds_bb=(By.XPATH, '//*[@class="ivu-input-number-input"]')
    # 表达式
    zh_xtsz_zcgl_ztbds_bds= (By.XPATH, '//*[@class="inbg textareaclass require-star ivu-form-item"]//*[@class="ivu-input"]')
    # 保存
    zh_xtsz_zcgl_ztbds_bc= (By.XPATH, '//*[text()="保存"]')
    # 删除
    zh_xtsz_zcgl_ztbds_sc= (By.XPATH, '//*[text()="删除"]')
    # 删除弹出框---点击确定
    zh_xtsz_zcgl_ztbds_sctck= (By.XPATH, '//*[text()="确定"]')
    # 提示语----参数错误，请检查输入!
    zh_xtsz_zcgl_ztbds_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    # 分页
    zh_xtsz_zcgl_ztbds_fy= (By.XPATH, '//*[@class="ivu-page"]//li')
    # 列表
    zh_xtsz_zcgl_ztbds_lb= (By.XPATH, '//*[@class="ivu-table-tbody"]//tr')
    '''系统设置---资产管理---类型编辑'''



    '''系统设置---资产管理---遥控配置'''
    #遥控配置
    zh_xtsz_zcgl_ykpz=(By.XPATH,'//*[text()="遥控配置"]')
    # 添加表达式
    zh_xtsz_zcgl_ykpz_tjbds= (By.XPATH, '//*[text()="添加表达式"]')
    # 设备类型
    zh_xtsz_zcgl_ykpz_sblx= (By.XPATH, '//*[contains(@class,"inbg ivu-form-item")]//*[@class="ivu-select-input"]')
    # 设备类型下拉
    zh_xtsz_zcgl_ykpz_sblxxl= (By.XPATH, '//div[1][contains(@class,"inbg ivu-form-item")]//*[@class="ivu-select-dropdown-list"]//li')
    #状态
    zh_xtsz_zcgl_ykpz_zt= (By.XPATH, '//*[@class="ivu-select ivu-select-single ivu-select-default"]//*[@class="ivu-select-placeholder"]')
    # 状态下拉
    zh_xtsz_zcgl_ykpz_ztxl= (By.XPATH, '//div[2][contains(@class,"inbg ivu-form-item")]//*[@class="ivu-select-dropdown-list"]//li')
    #版本
    zh_xtsz_zcgl_ykpz_bb= (By.XPATH, '//*[@class="ivu-input-number-input"]')
    # 值
    zh_xtsz_zcgl_ykpz_z= (By.XPATH, '//*[@class="ivu-input ivu-input-default"]')
    # 保存
    zh_xtsz_zcgl_ykpz_bc= (By.XPATH, '//*[text()="保存"]')
    # 删除
    zh_xtsz_zcgl_ykpz_sc= (By.XPATH, '//*[text()="删除"]')
    # 删除弹出框--点击确定
    zh_xtsz_zcgl_ykpz_sctck= (By.XPATH, '//*[text()="确定"]')
    # 提示语
    zh_xtsz_zcgl_ykpz_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    # 列表最后一个
    zh_xtsz_zcgl_ykpz_lbzhyg= (By.XPATH, '//*[@class="ivu-table-tbody"]//tr')
    # 上测----设备类型
    zh_xtsz_zcgl_ykpz_sblxxz= (By.XPATH, '//*[@class="ivu-select-input"]')
    # 上测---设备类型下拉内容
    zh_xtsz_zcgl_ykpz_sblxxzxl= (By.XPATH, '//*[@class="ivu-select-dropdown-list"]//li')
    #查询
    zh_xtsz_zcgl_ykpz_cx= (By.XPATH,'//*[@class="ivu-btn ivu-btn-primary ivu-btn-circle"]')
    '''系统设置---资产管理---遥控配置'''













    '''系统设置---资产管理---检测值配置'''
    #检测值配置
    zh_xtsz_zcgl_jczpz=(By.XPATH,'//*[text()="检测值配置"]')
    # 添加配置
    zh_xtsz_zcgl_jczpz_tjpz= (By.XPATH, '//*[text()="添加配置"]')
    # 保存
    zh_xtsz_zcgl_jczpz_bc= (By.XPATH, '//*[text()="保存"]')
    # 删除
    zh_xtsz_zcgl_jczpz_sc= (By.XPATH, '//*[text()="删除"]')
    # 删除弹出框---点击确定
    zh_xtsz_zcgl_jczpz_sctck= (By.XPATH, '//*[text()="确定"]')
    # 设备类型
    zh_xtsz_zcgl_jczpz_sblx= (By.XPATH, '//*[contains(@class,"inbg ivu-form-item")]//*[@class="ivu-select-input"]')
    # 设备类型下拉
    zh_xtsz_zcgl_jczpz_sblxxl= (By.XPATH, '//*[contains(@class,"inbg ivu-form-item")]//*[@class="ivu-select-dropdown-list"]//li')
    # 版本
    zh_xtsz_zcgl_jczpz_bb= (By.XPATH, '//*[@class="ivu-input-number-input"]')
    # 表达式
    zh_xtsz_zcgl_jczpz_bds= (By.XPATH, '//div[3][contains(@class,"inbg textareaclass ivu-form-item")]//*[@class="ivu-input"]')
    # 提示语---请选择设备类型---请输入版本---请输入表达式--添加成功！----已存在--添加成功！-修改成功！---删除成功！
    zh_xtsz_zcgl_jczpz_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    # 列表最后一个
    zh_xtsz_zcgl_jczpz_lbzhyg= (By.XPATH, '//*[@class="ivu-table-tbody"]//tr[last()]')
    '''系统设置---资产管理---检测值配置'''




    '''系统设置---资产管理---检测值配置'''

    #厂家配置
    zh_xtsz_zcgl_cjpz=(By.XPATH,'//*[text()="厂家配置"]')
    # 厂家配置
    zh_xtsz_zcgl_cjpz_tjcj= (By.XPATH, '//*[text()="添加厂家"]')
    # 保存
    zh_xtsz_zcgl_cjpz_bc= (By.XPATH, '//*[text()="保存"]')
    # 删除
    zh_xtsz_zcgl_cjpz_sc= (By.XPATH, '//*[text()="删除"]')
    # 删除弹出框---点击确定
    zh_xtsz_zcgl_cjpz_sctck= (By.XPATH, '//*[text()="确定"]')
    #设备类型
    zh_xtsz_zcgl_cjpz_sblx= (By.XPATH, '//*[@class="ivu-select-input"]')
    # 设备类型下拉
    zh_xtsz_zcgl_cjpz_sblxxl= (By.XPATH, '//*[@class="ivu-select-dropdown-list"]//li')
    # 厂家名称
    zh_xtsz_zcgl_cjpz_cjmc= (By.XPATH, '//div[2][contains(@class,"ivu-form-item")]//*[@class="ivu-input ivu-input-default"]')
    # 版本
    zh_xtsz_zcgl_cjpz_bb= (By.XPATH, '//*[@class="ivu-form-item-content"]//*[@class="ivu-input-number-input"]')
    # 通讯方式
    zh_xtsz_zcgl_cjpz_txfs= (By.XPATH, '//div[4][contains(@class,"ivu-form-item")]//*[@class="ivu-input ivu-input-default"]')
    # 脚本名称
    zh_xtsz_zcgl_cjpz_jbmc= (By.XPATH, '//div[5][contains(@class,"ivu-form-item")]//*[@class="ivu-input ivu-input-default"]')
    # 提示语---请选择设备类型---请选择设备类型
    zh_xtsz_zcgl_cjpz_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    # 列表最后一个
    zh_xtsz_zcgl_cjpz_lb= (By.XPATH, '//*[@class="ivu-table-tbody"]//tr')
    '''系统设置---资产管理---检测值配置'''
    '''系统设置---资产管理'''






    '''系统设置---测略预案'''
    # 策略预案
    zh_xtsz_clya= (By.XPATH, '//*[@class="ivu-menu-submenu-title"]//*[@class="ivu-icon ivu-icon-celveyuan1"]')



    '''系统设置---测略预案---预案编辑'''
    # 预案编辑
    zh_xtsz_clya_yabj= (By.XPATH, '//*[@class="ivu-select-dropdown"]//*[text()="预案编辑"]')
    #搜索框
    zh_xtsz_clya_yabj_ssk= (By.XPATH, '//*[@class="input-search"]//*[@class="ivu-input ivu-input-default"]')
    # 搜索框点击确定
    zh_xtsz_clya_yabj_sskqd= (By.XPATH, '//*[@class="ivu-icon ivu-icon-sousuo1 ivu-input-icon ivu-input-icon-normal"]')
    # +   号
    zh_xtsz_clya_yabj_tj= (By.XPATH, '//*[@class="plan-list"]//*[@class="ivu-icon ivu-icon-zengjia"]')
    # -   号
    zh_xtsz_clya_yabj_sc= (By.XPATH, '//*[@class="plan-list"]//*[@class="ivu-icon ivu-icon-shanchu1"]')
    # -   号点击确定
    zh_xtsz_clya_yabj_sctck= (By.XPATH, '//*[@class="ivu-btn ivu-btn-primary ivu-btn-large"]')
    # 修改   号
    zh_xtsz_clya_yabj_xg= (By.XPATH, '//*[@class="plan-list"]//*[@class="ivu-icon ivu-icon-shuaxin"]')
    #取消
    zh_xtsz_clya_yabj_qx= (By.XPATH, '//*[@class="editbtn ivu-btn ivu-btn-default"]')
    #名称
    zh_xtsz_clya_yabj_mc= (By.XPATH, '//div[2][contains(@class,"ivu-form-item")]//*[@class="ivu-input ivu-input-default"]')
    # 类型
    zh_xtsz_clya_yabj_lx= (By.XPATH, '//*[contains(@class,"ivu-form-item")]//*[@class="ivu-select-placeholder"]')
    # 类型下拉
    zh_xtsz_clya_yabj_lxxl = (By.XPATH, '//*[contains(@class,"ivu-form-item")]//*[@class="ivu-select-dropdown-list"]//li')
    # 影响区域
    zh_xtsz_clya_yabj_ysqy= (By.XPATH, '//*[contains(@class,"nopadding ivu-form-item")]//*[@class="ivu-icon ivu-icon-tianjia"]')
    # 影响区域下拉
    zh_xtsz_clya_yabj_ysqyxl= (By.XPATH, '//*[@class="ivu-select-dropdown"]//*[@class="ivu-dropdown-menu"]//li')
    #保存
    zh_xtsz_clya_yabj_bc= (By.XPATH, '//div[7][@class="form-btns"]//*[text()="保存"]')
    #提示语
    zh_xtsz_clya_yabj_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    # 列表最后一个
    zh_xtsz_clya_yabj_lbzhyg= (By.XPATH, '//div[2][@class="ivu-table-wrapper"]//*[@class="ivu-table-tbody"]//tr')
    #下侧  + 号
    zh_xtsz_clya_yabj_xctj= (By.XPATH, '//*[@class="bottom-area wrapper-panel"]//*[@class="ivu-icon ivu-icon-zengjia"]')
    # 下侧  -  号
    zh_xtsz_clya_yabj_xcsc=(By.XPATH, '//*[@class="bottom-area wrapper-panel"]//*[@class="ivu-icon ivu-icon-shanchu1"]')
    # 下侧  保存
    zh_xtsz_clya_yabj_xcbc= (By.XPATH, '//*[@class="bottom-area wrapper-panel"]//*[@class="ivu-icon ivu-icon-baocun"]')
    #下侧 选择类型
    zh_xtsz_clya_yabj_xcxzlx= (By.XPATH, '//*[@class="ivu-select-input"]')
    # 下侧 选择类型下拉内容
    zh_xtsz_clya_yabj_xcxzlxxl= (By.XPATH, ' //*[@class="ivu-select ivu-select-visible ivu-select-single ivu-select-default"]//*[@class="ivu-select-dropdown-list"]//*[text()="双面车道指示器"]')
    # 下侧弹出框点击全选
    zh_xtsz_clya_yabj_xctckqx= (By.XPATH, '//*[@class="ivu-table ivu-table-small ivu-table-border ivu-table-with-fixed-top"]//th[1][@class="ivu-table-column-center"]')
    # 下侧绑定
    zh_xtsz_clya_yabj_xcbd= (By.XPATH, '//*[text()="绑定"]')
    #下侧全选
    zh_xtsz_clya_yabj_xcqx= (By.XPATH, '//*[@class="inline-row header"]//*[@class="inline-col checkbox"]')
    # 下侧点击是否确认
    zh_xtsz_clya_yabj_xcqr= (By.XPATH, '//*[@class="inline-row header"]//*[@class="ivu-checkbox-input"]')
    #下侧 屏号
    zh_xtsz_clya_yabj_xcph= (By.XPATH, '//*[@class="item-edit-item ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    #下侧列表最后一个
    zh_xtsz_clya_yabj_xclbzhyg=(By.XPATH, '//div[last()][@class="inline-row"]//*[@class="inline-col checkbox"]')
    # 下侧--门架情报板--优先级
    zh_xtsz_clya_yabj_xcyxj= (By.XPATH, '//div[2][@class="item-edit-item input-list-fixed ivu-form-item"]//*[@class="ivu-input-number-input"]')
    # 下侧--门架情报板--间隔
    zh_xtsz_clya_yabj_xcjg= (By.XPATH, '//div[3][@class="item-edit-item input-list-fixed ivu-form-item"]//*[@class="ivu-input-number-input"]')
    # 下侧--门架情报板---是否确认
    zh_xtsz_clya_yabj_xcsfqr= (By.XPATH, '//*[@class="ivu-switch ivu-switch-default"]')
    #下侧---双面车道指示器
    zh_xtsz_clya_yabj_xcsmcdzsq= (By.XPATH, '//*[@class="item-edit-item lll ivu-form-item"]//*[@class="ivu-select-placeholder"]')
    #下侧---双面车道指示器--下拉内容
    zh_xtsz_clya_yabj_xcsmcdzsqxl= (By.XPATH, '//*[@class="item-edit-item lll ivu-form-item"]//*[@class="ivu-select-dropdown-list"]//li')
    # 下侧--字号
    zh_xtsz_clya_yabj_xczh= (By.XPATH, '//*[@class="ivu-table-row"]//td[2]//*[@class="ivu-select-placeholder"]')
    # 下侧--字号下拉
    zh_xtsz_clya_yabj_xczhxl= (By.XPATH, '//*[@class="ivu-select ivu-select-visible ivu-select-single ivu-select-default"]//*[@class="ivu-select-dropdown-list"]//li[1]')
    # 下侧--字体
    zh_xtsz_clya_yabj_xczt= (By.XPATH, '//*[@class="ivu-table-row"]//td[3]//*[@class="ivu-select-placeholder"]')
    # 下侧--字体下拉
    zh_xtsz_clya_yabj_xcztxl= (By.XPATH, '//*[@class="ivu-select ivu-select-visible ivu-select-single ivu-select-default"]//*[@class="ivu-select-dropdown-list"]//li[1]')
    # 下侧--颜色
    zh_xtsz_clya_yabj_xcys= (By.XPATH, '//*[@class="ivu-table-row"]//td[4]//*[@class="ivu-select-placeholder"]')
    # 下侧--颜色下拉
    zh_xtsz_clya_yabj_xcysxl= (By.XPATH, '//*[@class="ivu-select ivu-select-visible ivu-select-single ivu-select-default"]//*[@class="ivu-select-dropdown-list"]//li[1]')
    # 下侧--左侧--   +  ---
    zh_xtsz_clya_yabj_xczctj= (By.XPATH,'//*[@class="item-edit-item input-list-fixed ivu-form-item"]//*[@class="ivu-icon ivu-icon-zengjia"]')
    # 下侧--左侧--   -  ---
    zh_xtsz_clya_yabj_xczcsc= (By.XPATH, '//*[@class="btns"]//*[@class="ivu-icon ivu-icon-shanchu1"]')
    # 下侧--左侧列表
    zh_xtsz_clya_yabj_xczclbzhyg= (By.XPATH,'//*[@class="ivu-table ivu-table-default ivu-table-border"]//div[@class="ivu-table-body"]//tr[last()]//label')
    '''系统设置---测略预案---预案编辑'''




    '''系统设置---测略预案---策略编辑'''
    # 策略编辑
    zh_xtsz_clya_clbj= (By.XPATH, '//*[@class="ivu-select-dropdown"]//*[text()="策略编辑"]')
    # 搜索框
    zh_xtsz_clya_clbj_ssk= (By.XPATH, '//*[@class="input-search"]//*[@class="ivu-input ivu-input-default"]')
    # 搜索框确定
    zh_xtsz_clya_clbj_sskqd= (By.XPATH, '//*[@class="ivu-icon ivu-icon-sousuo1 ivu-input-icon ivu-input-icon-normal"]')
    # 添加新策略
    zh_xtsz_clya_clbj_tjclbj= (By.XPATH, '//*[text()="添加新策略"]')
    # 名称
    zh_xtsz_clya_clbj_mc= (By.XPATH, '//*[@class="ivu-modal-wrap"]//div[2]/div/div[1]/input')
    # 类型
    zh_xtsz_clya_clbj_lx=(By.XPATH, '//*[@class="ivu-modal-wrap"]//div[3]/div/div[1]/div[1]/div/span')
    # 类型下拉-
    zh_xtsz_clya_clbj_lxxl= (By.XPATH, '//*[@class="strategy-modal v-transfer-dom"]//form//div[3]//*[@class="ivu-select-dropdown-list"]//li')
    #分组
    zh_xtsz_clya_clbj_fz= (By.XPATH, '//*[@class="ivu-modal-wrap"]//div[4]/div/div[1]/div[1]/div/span')
    # 分组下拉
    zh_xtsz_clya_clbj_fzxl= (By.XPATH, '//div[4][contains(@class,"ivu-form-item")]//*[@class="ivu-select-dropdown-list"]//li')
    #二类分级
    zh_xtsz_clya_clbj_ejfl= (By.XPATH, '//*[@class="strategy-modal-body"]//div[5]//*[@class="ivu-form-item-content"]//*[@class="ivu-select-placeholder"]')
    #二类分级下拉
    zh_xtsz_clya_clbj_ejflxl= (By.XPATH, '//*[@class="ivu-modal-wrap"]//div[5]//*[@class="ivu-select-dropdown-list"]//li')
    # 影响区域
    zh_xtsz_clya_clbj_ysqy= (By.XPATH, '//*[contains(@class,"nopadding ivu-form-item")]//*[@class="ivu-select-placeholder"]')
    # 影响区域下拉
    zh_xtsz_clya_clbj_ysqyxl= (By.XPATH, '//*[@class="ivu-modal-wrap"]//div[6]//*[@class="ivu-select-dropdown-list"]//li')
    # 保存
    zh_xtsz_clya_clbj_bc= (By.XPATH, '//*[@class="strategy-modal v-transfer-dom"]//*[@class="savebtn ivu-btn ivu-btn-primary"]')
    # 取消
    zh_xtsz_clya_clbj_qx= (By.XPATH, '//div[10][@class="form-btns"]//*[@class="editbtn ivu-btn ivu-btn-default"]')


    # 触发周期
    zh_xtsz_clya_clbj_cfzq= (By.XPATH, '//*[@class="ivu-row"]//*[@class="ivu-select-placeholder"]')
    # 触发周期下拉--选择小时
    zh_xtsz_clya_clbj_cfzqxl= (By.XPATH, '//*[@class="ivu-row"]//*[@class="ivu-select-dropdown-list"]//li[1]')
    # 触发时间
    zh_xtsz_clya_clbj_cfsj= (By.XPATH, '//*[@class="time-config ivu-col ivu-col-span-24"]//*[@class="ivu-input ivu-input-default ivu-input-with-suffix"]')
    # 选择时间范围---开始
    zh_xtsz_clya_clbj_xzsjfwks= (By.XPATH,'//*[@class="ivu-col ivu-col-span-24"]//div[1][@class="ivu-date-picker"]//*[@class="ivu-input ivu-input-default ivu-input-with-suffix"]')
    #选择时间范围---开始--删除时间
    zh_xtsz_clya_clbj_xzsjfwks_sc= (By.XPATH,'//*[@class="ivu-col ivu-col-span-24"]//div[1][@class="ivu-date-picker"]//*[@class="ivu-icon ivu-icon-ios-calendar-outline"]')
    # 选择时间范围---结束
    zh_xtsz_clya_clbj_xzsjfwjs= (By.XPATH,'//div[2][@class="ivu-date-picker"]//*[@class="ivu-input ivu-input-default ivu-input-with-suffix"]')
    # 选择时间范围---结束---删除时间
    zh_xtsz_clya_clbj_xzsjfwjs_sc= (By.XPATH, '//div[2][@class="ivu-date-picker"]//*[@class="ivu-icon ivu-icon-ios-calendar-outline"]')
    # 选择时间里面的---保存
    zh_xtsz_clya_clbj_sjbc= (By.XPATH, '//*[@class="time-save-btn ivu-btn ivu-btn-primary"]//*[text()="保存"]')



    # 列表
    zh_xtsz_clya_clbj_lbzhyg= (By.XPATH, '//*[@class="ivu-table ivu-table-default ivu-table-border"]//*[@class="ivu-table-tbody"]//tr')

    # 关联预案
    zh_xtsz_clya_clbj_glya= (By.XPATH, '//*[@class="relevant-plan ivu-btn ivu-btn-text"]')
    # 关联预案中的最后一个
    zh_xtsz_clya_clbj_glyazhyg= (By.XPATH, '//*[@class="ivu-modal-body"]//ul[last()]//*[@class="ivu-checkbox-wrapper ivu-checkbox-default"]')
    # 确定
    zh_xtsz_clya_clbj_qd= (By.XPATH, '//*[text()="确定"]')
    # 编辑
    zh_xtsz_clya_clbj_bj= (By.XPATH, '//*[text()="编辑"]')
    # 删除
    zh_xtsz_clya_clbj_sc= (By.XPATH, '//*[text()="删除"]')
    # 删除弹出框---点击确定
    zh_xtsz_clya_clbj_sctck= (By.XPATH, '//*[@class="ivu-btn ivu-btn-primary ivu-btn-large"]//*[text()="确定"]')
    # 提示语
    zh_xtsz_clya_clbj_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')


    '''系统设置---测略预案---策略编辑'''
    '''系统设置---测略预案'''




    '''系统设置---用户管理'''
    #用户管理
    zh_xtsz_yhgl=(By.XPATH,'//*[@class="ivu-icon ivu-icon-yonghuguanli1"]')
    '''系统设置---用户管理---用户管理'''
    #用户管理
    zh_xtsz_yhgl_yhgl=(By.XPATH,'//*[@class="ivu-menu-drop-list"]//*[text()="用户管理"]')
    # 添加新用户
    zh_xtsz_yhgl_yhgl_tjxyh= (By.XPATH, '//*[text()="添加新用户"]')
    #账号搜索框
    zh_xtsz_yhgl_yhgl_zhssk= (By.XPATH, '//div[1][@class="ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    #查询
    zh_xtsz_yhgl_yhgl_cx= (By.XPATH, '//*[@class="ivu-btn ivu-btn-primary ivu-btn-circle"]')
    # 保存
    zh_xtsz_yhgl_yhgl_bc= (By.XPATH, '//*[@class="form-btns"]//*[@class="savebtn ivu-btn ivu-btn-primary"]')
    # 删除
    zh_xtsz_yhgl_yhgl_sc= (By.XPATH, '//*[text()="删除"]')
    # 删除弹出框--点击确定
    zh_xtsz_yhgl_yhgl_sctck= (By.XPATH, '//*[text()="确定"]')

    # 账号
    zh_xtsz_yhgl_yhgl_zh= (By.XPATH, '//div[1][contains(@class,"inbg ivu-form-item")]//*[@class="ivu-input ivu-input-default"]')
    # 角色
    zh_xtsz_yhgl_yhgl_js= (By.XPATH, '//*[contains(@class,"inbg ivu-form-item")]//*[@class="ivu-select-placeholder"]')
    # 角色下拉
    zh_xtsz_yhgl_yhgl_jsxl= (By.XPATH, '//div[2][contains(@class,"inbg ivu-form-item")]//*[@class="ivu-select-dropdown-list"]//li')
    # 姓名
    zh_xtsz_yhgl_yhgl_xm= (By.XPATH, '//div[3][contains(@class,"inbg ivu-form-item")]//*[@class="ivu-input ivu-input-default"]')
    # 分页---li
    zh_xtsz_yhgl_yhgl_fy=(By.XPATH, '//*[@class="funAreas row top"]//*[@class="ivu-page"]//li')
    # 列表-------tr
    zh_xtsz_yhgl_yhgl_lb= (By.XPATH, '//*[@class="ivu-table ivu-table-default ivu-table-border"]//*[@class="ivu-table-tbody"]//tr')
    # 提示语
    zh_xtsz_yhgl_yhgl_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    '''系统设置---用户管理---用户管理'''



    '''系统设置---用户管理---角色管理'''
    # 角色管理
    zh_xtsz_yhgl_jsgl= (By.XPATH, '//*[@class="ivu-menu-drop-list"]//*[text()="角色管理"]')
    # 添加新角色
    zh_xtsz_yhgl_jsgl_tjxjs= (By.XPATH, '//*[text()="添加新角色"]')
    # 保存
    zh_xtsz_yhgl_jsgl_bc= (By.XPATH, '//*[text()="保存"]')
    # 删除
    zh_xtsz_yhgl_jsgl_sc= (By.XPATH, '//*[text()="删除"]')
    # 删除弹出框--点击确定
    zh_xtsz_yhgl_jsgl_sc_tck= (By.XPATH, '//*[text()="确定"]')
    # 角色名
    zh_xtsz_yhgl_jsgl_jsm= (By.XPATH, '//*[contains(@class,"inbg ivu-form-item")]//*[@class="ivu-input ivu-input-default"]')
    #类型
    zh_xtsz_yhgl_jsgl_lx= (By.XPATH, '//*[contains(@class,"inbg ivu-form-item")]//*[@class="ivu-select-selected-value"]')
    # 类型下拉内容
    zh_xtsz_yhgl_jsgl_lxxl=(By.XPATH, '//*[contains(@class,"inbg ivu-form-item")]//*[@class="ivu-select-dropdown-list"]//li')
    # 权限----复选框
    zh_xtsz_yhgl_jsgl_qx= (By.XPATH, '//*[@class="inbg treeheight ivu-form-item"]//*[@class="ivu-checkbox-wrapper ivu-checkbox-default"]')
    # 列表
    zh_xtsz_yhgl_jsgl_lb= (By.XPATH, '//*[@class="row fill"]//*[@class="ivu-table-tbody"]//tr')
    # 提示语
    zh_xtsz_yhgl_jsgl_tsy = (By.XPATH, '//*[@class="ivu-notice-title"]')
    '''系统设置---用户管理---角色管理'''




    '''系统设置---用户管理---权限管理'''

    # 权限管理
    zh_xtsz_yhgl_qxgl = (By.XPATH, '//*[@class="ivu-menu-drop-list"]//*[text()="权限管理"]')
    # 添加新权限
    zh_xtsz_yhgl_qxgl_tjxqx= (By.XPATH, '//*[text()="添加新权限"]')
    # 保存
    zh_xtsz_yhgl_qxgl_bc= (By.XPATH, '//*[@class="editarea panel grey ivu-form ivu-form-label-right"]//*[text()="保存"]')
    # 删除
    zh_xtsz_yhgl_qxgl_sc= (By.XPATH, '//*[text()="删除"]')
    # 删除弹出框
    zh_xtsz_yhgl_qxgl_sctck= (By.XPATH, '//*[text()="确定"]')
    # 权限代码
    zh_xtsz_yhgl_qxgl_qxdm= (By.XPATH, '//div[1][contains(@class,"inbg ivu-form-item")]//*[@class="ivu-input ivu-input-default"]')
    # 权限名称
    zh_xtsz_yhgl_qxgl_qxmc= (By.XPATH, '//div[3][contains(@class,"inbg ivu-form-item")]//*[@class="ivu-input ivu-input-default"]')
    # 列表
    zh_xtsz_yhgl_qxgl_lb= (By.XPATH, '//*[@class="panel ivu-table-wrapper"]//*[@class="ivu-table-tbody"]//tr')
    '''系统设置---用户管理---权限管理'''
    '''系统设置---用户管理'''



    '''值班管理----'''
    #值班管理
    dl_zbgl=(By.XPATH,'//*[contains(text(),"值班管理")]')

    '''值班管理----排班管理'''
    # 排版管理
    dl_zbgl_pbgl= (By.XPATH, '//*[contains(text(),"排班管理")]')
    # 班组-排版-交接班-历史记录
    dl_zbgl_pbgl_bpjl= (By.XPATH, '//*[@class="left-menu ivu-menu ivu-menu-light ivu-menu-vertical"]/a')
    # 班组-左侧增加
    dl_zbgl_pbgl_bz_zj= (By.XPATH, '//*[@class="add ivu-btn ivu-btn-default"]')
    # 班组-左侧删除
    dl_zbgl_pbgl_bz_zcsc= (By.XPATH, '//*[@class="dele ivu-btn ivu-btn-default"]')
    # 班组-左侧删除弹出框---点击确定
    dl_zbgl_pbgl_bz_zcsctck= (By.XPATH, '//*[@class="ivu-btn ivu-btn-primary ivu-btn-large"]')

    # 班组-请输入班组名称
    dl_zbgl_pbgl_bz_qsrbzmc= (By.XPATH, '//*[@class="ivu-input ivu-input-default"]')
    # 班组-确定
    dl_zbgl_pbgl_bz_qd= (By.XPATH, '//*[@class="addbtn ivu-btn ivu-btn-primary"]')
    # 班组-添加新组员
    dl_zbgl_pbgl_bz_tjxzy= (By.XPATH, '//*[@class="ivu-icon ivu-icon-tianjia"]')
    # 班组-保存
    dl_zbgl_pbgl_bz_bc= (By.XPATH, '//*[@class="savebtn ivu-btn ivu-btn-primary"]')
    # 班组-删除
    dl_zbgl_pbgl_bz_sc= (By.XPATH, '//*[@class="ivu-btn ivu-btn-default"]')
    # 班组-删除弹出框点击确定
    dl_zbgl_pbgl_bz_sctck= (By.XPATH, '//*[text()="确定"]')
    # 班组-班组
    dl_zbgl_pbgl_bz_bz= (By.XPATH, '//div[1][@class="teamRequ"]//*[@class="ivu-select-selection"]')
    # 班组-下拉内容
    dl_zbgl_pbgl_bz_bzxl= (By.XPATH, '//div[1][@class="teamRequ"]//*[@class="ivu-select-dropdown-list"]//li')
    # 班组-姓名
    dl_zbgl_pbgl_bz_xm= (By.XPATH, '//div[2][@class="teamRequ"]//*[@class="ivu-select-input"]')
    # 班组-姓名下拉内容
    # dl_zbgl_pbgl_bz_xmxl= (By.XPATH, '//div[2][@class="teamRequ"]//*[@class="ivu-select-dropdown-list"]//li')
    # dl_zbgl_pbgl_bz_xmxl= (By.XPATH, '//div[2][@class="teamRequ"]//*[@class="ivu-select-dropdown-list"]//*[text()="pc"]')
    # dl_zbgl_pbgl_bz_xmxl1= (By.XPATH, '//div[2][@class="teamRequ"]//*[@class="ivu-select-dropdown-list"]//*[text()="庞川"]')
    dl_zbgl_pbgl_bz_xmxl1= (By.XPATH, '//div[2][@class="teamRequ"]//*[@class="ivu-select-dropdown-list"]//*[text()="庞川" or text()="庞川1"]')
    # 班组-备注
    dl_zbgl_pbgl_bz_bzbz= (By.XPATH, '//div[5][@class="teamRequ"]//*[@class="ivu-input"]')
    # 班组-添加新组员列表
    dl_zbgl_pbgl_bz_tjxzylb= (By.XPATH, '//*[@class="ivu-table-tbody"]//tr')
    # 班组-左侧班组最后一个进行修改
    dl_zbgl_pbglbz_zcbzlbzhyg= (By.XPATH, '//li[last()][@class="ivu-menu-submenu"]//*[@class="ivu-input ivu-input-default ivu-input-disabled"]')
    # 班组-左侧班组最后一个进行删除
    dl_zbgl_pbgl_bz_zcxz= (By.XPATH, '//li[last()][@class="ivu-menu-submenu"]//*[@class="ivu-icon icon"]')
    # 提示语
    dl_zbgl_pbgl_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    # 排班------选择当前日历
    dl_zbgl_pbgl_pb_rl= (By.XPATH, '//*[@class="datespan nowdayclass"]')
    # 排班------班组
    dl_zbgl_pbgl_pb_bz= (By.XPATH, '//div[1][@class="ivu-tabs-tabpane"]//*[@class="ivu-select ivu-select-single ivu-select-default"]')
    # 排班------班组下拉内容
    dl_zbgl_pbgl_pb_bzxl= (By.XPATH, '//div[1][@class="ivu-tabs-tabpane"]//*[@class="ivu-select-dropdown-list"]//li')
    # 排班------确定
    dl_zbgl_pbgl_pb_qd= (By.XPATH, '//div[1][@class="ivu-tabs-tabpane"]//*[@class="ivu-btn ivu-btn-primary"]')
    # 交接班------提交
    dl_zbgl_pbgl_jjb_tj= (By.XPATH, '//*[@class="subbtn ivu-form-item"]//*[@class="ivu-btn ivu-btn-primary"]')
    # 交接班------今日完成工作
    dl_zbgl_pbgl_jjb_jrwcgz= (By.XPATH, '//div[1][contains(@class,"panel ivu-form-item")]//*[@class="ivu-input"]')
    # 交接班------+
    dl_zbgl_pbgl_jjb_jh= (By.XPATH, '//*[@class="ivu-form-item-content"]//*[@class="ivu-icon ivu-icon-chaodatianjia"]')
    # 交接班------点击（+）进行选择班组
    dl_zbgl_pbgl_jjb_bz= (By.XPATH, '//*[@class="grouplist ivu-radio-group ivu-radio-group-default ivu-radio-default"]//label')
    # 交接班------确定
    dl_zbgl_pbgl_jjb_qd= (By.XPATH, '//*[@class="ivu-btn ivu-btn-primary ivu-btn-long ivu-btn-large"]')







    '''值班管理----到访管理'''
    # 到访管理
    dl_zbgl_dfgl= (By.XPATH, '//*[contains(text(),"到访管理")]')
    #添加新记录
    dl_zbgl_dfgl_tjxjl= (By.XPATH, '//*[text()="添加新记录"]')
    # 姓名搜索框
    dl_zbgl_dfgl_xmssk = (By.XPATH, '//div[1][@class="ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 查询
    dl_zbgl_dfgl_cx = (By.XPATH, '//*[text()="查询"]')
    # 列表
    dl_zbgl_dfgl_lb = (By.XPATH, '//*[@class="row fill"]//*[@class="ivu-table-tbody"]//tr')
    #姓名
    dl_zbgl_dfgl_xm= (By.XPATH, '//div[1][@class="mandatory"]//*[@class="ivu-input ivu-input-default"]')
    # 性别
    dl_zbgl_dfgl_xb= (By.XPATH, '//*[@class="mandatory"]//*[@class="ivu-select-placeholder"]')
    # 性别下拉
    dl_zbgl_dfgl_xbxl= (By.XPATH, '//*[@class="mandatory"]//*[@class="ivu-select-dropdown-list"]//li')
    #联系电话
    dl_zbgl_dfgl_lxdh= (By.XPATH, '//div[3][@class="mandatory"]//*[@class="ivu-input ivu-input-default"]')
    #证件号码
    dl_zbgl_dfgl_zjhm= (By.XPATH, '//div[4][@class="mandatory"]//*[@class="ivu-input ivu-input-default"]')
    #到访时间
    dl_zbgl_dfgl_dfsj= (By.XPATH, '//div[5][@class="mandatory"]//*[@class="ivu-input ivu-input-default ivu-input-with-suffix"]')
    #到访时间---删除
    dl_zbgl_dfgl_dfsj_sc=(By.XPATH, '//div[5][@class="mandatory"]//*[@class="ivu-icon ivu-icon-ios-calendar-outline"]')
    #离开时间
    dl_zbgl_dfgl_lksj= (By.XPATH, '//div[6][@class="mandatory"]//*[@class="ivu-input ivu-input-default ivu-input-with-suffix"]')
    # 离开时间---清除
    dl_zbgl_dfgl_lksj_sc= (By.XPATH, '//div[6][@class="mandatory"]//*[@class="ivu-icon ivu-icon-ios-calendar-outline"]')
    #保存
    dl_zbgl_dfgl_bc= (By.XPATH, '//*[text()="保存"]')
    # 删除
    dl_zbgl_dfgl_sc= (By.XPATH, '//*[text()="删除"]')
    # 删除弹出框---点击确定
    dl_zbgl_dfgl_sctck= (By.XPATH, '//*[text()="确定"]')
    # 提示语
    dl_zbgl_dfgl_tsy = (By.XPATH, '//*[@class="ivu-notice-title"]')
    '''值班管理----到访管理'''




    '''值班管理----接警管理'''
    # 接警管理
    dl_zbgl_jjgl= (By.XPATH, '//*[contains(text(),"接警管理")]')
    #开始时间
    dl_zbgl_jjgl_kssj= (By.XPATH, '//*[@class="ivu-col ivu-col-span-10"]//*[@class="ivu-input ivu-input-default ivu-input-with-suffix"]')
    #事件类型
    dl_zbgl_jjgl_sjlb= (By.XPATH, '//div[1][@class="ivu-col ivu-col-span-10"]//*[@class="ivu-select-placeholder"]')
    # 事件类型下拉
    dl_zbgl_jjgl_sjlbxl= (By.XPATH, '//*[@class="ivu-col ivu-col-span-10"]//*[@class="ivu-select-dropdown-list"]//li')
    # 事件等级
    dl_zbgl_jjgl_sjdj= (By.XPATH, '//div[3][@class="ivu-col ivu-col-span-10"]//*[@class="ivu-select-placeholder"]')
    # 事件等级下拉
    dl_zbgl_jjgl_sjdjxl= (By.XPATH, '//div[3][@class="ivu-col ivu-col-span-10"]//*[@class="ivu-select-dropdown-list"]//li')
    #开始桩号
    dl_zbgl_jjgl_kszh= (By.XPATH, '//div[3][@class="ivu-row"]//div[1][@class="ivu-col ivu-col-span-10"]//*[@class="ivu-input ivu-input-default"]')
    #结束桩号
    dl_zbgl_jjgl_jszh= (By.XPATH, '//div[3][@class="ivu-col ivu-col-span-10"]//*[@class="ivu-input ivu-input-default"]')
    #提交
    dl_zbgl_jjgl_tj= (By.XPATH, '//*[text()="提交"]')
    # 提示语
    dl_zbgl_jjgl_tsy = (By.XPATH, '//*[@class="ivu-notice-title"]')
    '''值班管理----接警管理'''




    '''资产管理'''
    dl_zcgl= (By.XPATH, '//*[@class="ivu-icon ivu-icon-zichanguanli1"]')
    # 提示语
    dl_zcgl_tsy= (By.XPATH, '//*[@class="ivu-notice-title"]')
    '''资产管理---设备报修'''
    dl_zcgl_xbbx= (By.XPATH, '//*[text()="设备报修"]')
    #报修工单   报修记录  故障记录
    dl_zcgl_xbbx_gd_jl_sb= (By.XPATH, '//*[@class="left-menu ivu-menu ivu-menu-light ivu-menu-vertical"]//a')
    # 报修工单----添加报修
    dl_zcgl_xbbx_gd_tjbx= (By.XPATH, '//*[@class="addnewbtn ivu-btn ivu-btn-primary"]')
    # 报修工单----报修原因搜索框
    dl_zcgl_xbbx_gd_bxyyssk= (By.XPATH, '//*[@class="ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 报修工单----查询
    dl_zcgl_xbbx_gd_cx= (By.XPATH, '//*[text()="查询"]')
    # 报修工单----列表
    dl_zcgl_xbbx_gd_lb= (By.XPATH, '//*[@class="row fill"]//*[@class="ivu-table-tbody"]//tr')
    # 报修工单----删除
    dl_zcgl_xbbx_gd_sc= (By.XPATH, '//*[text()="删除"]')
    # 报修工单----删除弹出框点击确定
    dl_zcgl_xbbx_gd_sctck= (By.XPATH, '//*[text()="确定"]')
    # 报修工单----保存
    dl_zcgl_xbbx_gd_bc= (By.XPATH, '//*[@class="save-btn savebtn ivu-btn ivu-btn-default"]')
    # 报修工单----完成
    dl_zcgl_xbbx_gd_wc= (By.XPATH, '//*[text()="完成"]')
    # 报修工单----设备名称
    dl_zcgl_xbbx_gd_sbmc= (By.XPATH, '//*[@class="add-icon"]')
    # 报修工单----设备类型
    dl_zcgl_xbbx_gd_sblx = (By.XPATH, '//div[1][@class="inbg ivu-form-item"]//*[@class="ivu-select-input"]')
    # 报修工单----设备类型下拉
    dl_zcgl_xbbx_gd_sblx_xl= (By.XPATH, '//div[1][@class="inbg ivu-form-item"]//*[@class="ivu-select-dropdown-list"]//li')
    # 报修工单----设备名称----设备名称
    dl_zcgl_xbbx_gd_sbmcsbmc= (By.XPATH, '//div[2][@class="inbg ivu-form-item"]//*[@class="ivu-select-input"]')
    # 报修工单----设备名称----设备名称下拉
    dl_zcgl_xbbx_gd_sbmcsbmc_xl= (By.XPATH, '//div[2][@class="inbg ivu-form-item"]//*[@class="ivu-select-dropdown-list"]//li')
    # 报修工单----确定
    dl_zcgl_xbbx_gd_qd= (By.XPATH, '//*[text()="确 定"]')
    # 报修工单----报修原因
    dl_zcgl_xbbx_gd_bxyy= (By.XPATH, '//div[2][@class="inbg ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 报修工单----报修人员
    dl_zcgl_xbbx_gd_bxry= (By.XPATH, '//div[3][@class="inbg ivu-form-item"]//*[@class="ivu-input ivu-input-default"]')
    # 报修工单----报修时间
    dl_zcgl_xbbx_gd_bxsj= (By.XPATH, '//*[@class="ivu-input ivu-input-default ivu-input-disabled ivu-input-with-suffix"]')

    '''资产管理---设备报修'''





    '''资产管理---资产查询'''
    dl_zcgl_zccx= (By.XPATH, '//*[text()="资产查询"]')
    '''资产管理---资产查询'''
    '''资产管理'''


    '''综合监控'''
    #综合监控
    dl_zhjk=(By.XPATH, '//*[@class="ivu-icon ivu-icon-zonghejiankong1"]')

    '''设备监控'''
    #设备监控
    dl_zhjk_sbjk=(By.XPATH, '//*[text()="设备监控"]')
    # 延崇高速路段
    dl_zhjk_sbjk_ycgsld= (By.XPATH, '//*[text()="延崇高速路段"]')
    #松山隧道（河北段）
    dl_zhjk_sbjk_sssdhbd= (By.XPATH, '//*[@class="subnav-item sub-active"]//*[text()="松山隧道（河北段）"]')
    #龙泉口隧道
    dl_zhjk_sbjk_lqksd= (By.XPATH, '//*[@class="subnav-item sub-active"]//*[text()="龙泉口隧道"]')
    # 吉林堡隧道
    dl_zhjk_sbjk_jlbsd= (By.XPATH, '//*[@class="subnav-item"]//*[text()="杏林堡隧道"]')
    #头孢隧道
    dl_zhjk_sbjk_tbsd= (By.XPATH, '//*[@class="subnav-item"]//*[text()="头炮隧道"]')
    #郭家窑隧道
    dl_zhjk_sbjk_gjysd= (By.XPATH, '//*[@class="subnav-item"]//*[text()="郭家窑隧道"]')
    #冯家沟隧道
    dl_zhjk_sbjk_fjgsd= (By.XPATH, '//*[@class="subnav-item"]//*[text()="冯家沟隧道"]')
    #金家庄隧道
    dl_zhjk_sbjk_jjzsd = (By.XPATH, '//*[@class="subnav-item"]//*[text()="金家庄隧道"]')
    #棋盘梁隧道
    dl_zhjk_sbjk_qplsd= (By.XPATH, '//*[@class="subnav-item"]//*[text()="棋盘梁隧道"]')
    #怀来北收费站
    dl_zhjk_sbjk_hlbsfz= (By.XPATH, '//*[@class="subnav-item"]//*[text()="怀来北收费站"]')
    #大海陀收费站
    dl_zhjk_sbjk_dhtsfz= (By.XPATH, '//*[@class="subnav-item"]//*[text()="大海陀收费站"]')
    # 赤城南收费站
    dl_zhjk_sbjk_ccmsfz= (By.XPATH, '//*[@class="subnav-item"]//*[text()="赤城南收费站"]')
    # 太子城收费站
    dl_zhjk_sbjk_tzcsfz= (By.XPATH, '//*[@class="subnav-item"]//*[text()="太子城收费站"]')





    # 左侧搜索框
    dl_zhjk_sbjk_zcssk= (By.XPATH, '//*[@class="search-component search-bar"]//*[@class="ivu-input ivu-input-default"]')
    # 左侧搜索框点击确定--清除
    dl_zhjk_sbjk_zcssk_qd= (By.XPATH, '//*[@class="search-btn ivu-btn ivu-btn-default ivu-btn-icon-only"]')
    # 左侧列表
    dl_zhjk_sbjk_zclb= (By.XPATH, '//*[@class="list-item"]')
    #双面车道指示器进行点击  远程正面通行，远程禁止，远程反面通行
    dl_zhjk_sbjk_zcssk_zt= (By.XPATH, '//*[@class="controller-item" or @class="controller-item active-status"]')
    # 提示语
    dl_zhjk_sbjk_tsy = (By.XPATH, '//*[@class="ivu-notice-title"]')
    # 提示语1
    dl_zhjk_sbjk_tsy1= (By.XPATH, '//*[text()="设备控制成功"]')
    #设备状态
    dl_zhjk_sbjk_sbzt= (By.XPATH, '//*[@class="value"]')

    #情报板 信息下发
    dl_zhjk_sbjk_qbbxxxf= (By.XPATH, '//*[text()="信息下发"]')
    # 情报板信息清空
    dl_zhjk_sbjk_qbbxxqk= (By.XPATH, '//*[@class="send-tools"]//*[text()="清空"]')
    # 情报板信息下发----下发
    dl_zhjk_sbjk_qbbxxxf_xf= (By.XPATH, '//*[@class="tool-item btn ivu-btn ivu-btn-primary"]')
    #情报板信息下发---X   退出的意思
    dl_zhjk_sbjk_qbbxxxf_tc= (By.XPATH, '//*[@class="the-close-button ivu-btn ivu-btn-error ivu-btn-icon-only ivu-btn-ghost"]//*[@class="ivu-icon ivu-icon-guanbi"]')
    #取消
    dl_zhjk_sbjk_qbbxxxf_qx12= (By.XPATH, '//*[@class="ivu-modal-wrap cms-edit-modal"]//*[@class="tool-item btn ivu-btn ivu-btn-error ivu-btn-ghost"]')

    # 速度设置输入框
    dl_zhjk_sbjk_sdszssk= (By.XPATH, '//*[@class="ivu-tabs-tabpane"]//*[@class="ivu-input-number-input-wrap"]//*[@class="ivu-input-number-input"]')
    # 速度设置----设置
    dl_zhjk_sbjk_sdszssk_sz= (By.XPATH, '//*[text()="设置"]')
    # 限速标志----速度设置----取消
    dl_zhjk_sbjk_sdszssk_qx= (By.XPATH, '//*[@class="ivu-modal-wrap speed-modal"]//*[@class="ivu-btn ivu-btn-default"]//*[text()="取消"]')
    # 数据报表
    dl_zhjk_sbjk_kbsbz_sjbb= (By.XPATH,'//*[text()=" 数据报表 "]')
    # 数据报表-----获取列表第一个限速值
    dl_zhjk_sbjk_kbsbz_sjbb_xsz= (By.XPATH, '//*[@class="ivu-table-tbody"]//tr[1]//td[2]')
    #基本信息
    dl_zhjk_sbjk_kbsbz_jbxx= (By.XPATH, '//*[text()=" 基本信息 "]')
    #当前速速
    dl_zhjk_sbjk_sdszssk_sd= (By.XPATH, '//*[@class="base"]//*[contains(@class,"detail-line")]')
    #交通照明
    dl_zhjk_sbjk_zm= (By.XPATH, '//*[@class="item-detail"]//*[@class="line"]//span')
    #枪机  查看视频弹出框点击X
    dl_zhjk_sbjk_sp_sc= (By.XPATH, '//*[@class="close ivu-icon ivu-icon-guanbi"]')
    # 路段 点击某一个设备组
    dl_zhjk_sbjk_lusbz= (By.XPATH, '//*[@class="leaflet-pane leaflet-marker-pane"]//*[@class="leaflet-marker-icon leaflet-zoom-animated leaflet-interactive"]')
    '''设备监控'''
    '''综合监控'''
