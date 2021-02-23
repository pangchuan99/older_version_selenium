import os
from TestDatas.connect_mysql import select_sql  #数据库的
import pytest
import json
import yaml


#这个是读取数据库 写到文件里面
def get_name0(sql0,wenjian0):
    a = select_sql(sql0)

    # #   W 是重写
    with open(r"..\TestDatas\{}".format(wenjian0), "w",encoding="utf-8") as fp:
        fp.write("")
    # for i in a:
    #     c = (i["name"])
    #     # print("为1的{}".format(c))

    with open(r"..\TestDatas\{}".format(wenjian0), "a",encoding="utf-8") as fp1:
        fp1.write(str(a))

def get_name1(sql1,wenjian1):
    b= select_sql(sql1)

    # print(b)
    with open(r"..\TestDatas\{}".format(wenjian1), "w",encoding="utf-8") as fp2:
        fp2.write("")
    # for i in b:
    #     d = (i["name"])
    #     print("
    #     为0的{}".format(d))
    with open(r"..\TestDatas\{}".format(wenjian1), "a",encoding="utf-8") as fp3:
        fp3.write(str(b))



#这个是读取数据库写到文件后 进行读取
def get_yaml_data(yamlpath): 
    '''
    读取文件
    :param yamlpath:
    :return:
    '''
    f = open(yamlpath, "r", encoding='utf-8')
    yamldata = f.read()
    print(yamldata)
    # a = [i for i in yamldata.split("\n")]
    # # print(a)

    return yamldata

def get_name_wenjianmingcheng(mingcheng):
    # 获取当前文件的上一层路径,上一层路径
    curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(curpath)
    # 然后在获取某一个文件的绝对路径
    yamlpath = os.path.join(curpath, "TestDatas",mingcheng)
    a1=get_yaml_data(yamlpath)
    a3=yaml.load(a1,Loader=yaml.FullLoader)
    print(type(a3))

    return a3


if __name__ == '__main__':
    # get_name0()
    # get_name1()
    pc=get_name_wenjianmingcheng("get_name_tb_smzdzsqwenjian_0.yaml")
    print(pc)
    print(type(pc))
    # a3=yaml.load(pc)
    # print(type(a3))
    # print(pc["name"])
