import requests
from bs4 import BeautifulSoup
import xlwt

# 请求headers 模拟谷歌浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}


def get_data():
    response = requests.get('http://172.16.101.241:53595/index.html#suites', headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')

    # 标题处理
    title = bs.find_all('th')
    data_list_title = []  # 定义一个空列表
    for data in title:
        data_list_title.append(data.text.strip())  # 获取标签的内容去掉两边空格并添加到列表里

    # 内容处理
    content = bs.find_all('td')
    data_list_content = []  # 定义一个空列表
    for data in content:
        data_list_content.append(data.text.strip())  # 获取标签的内容去掉两边空格并添加到列表里
    # 语句featList = [example[i] for example in dataSet]作用为： 将dataSet中的数据按行依次放入example中，然后取得example中的example[i]元素，放入列表featList中
    new_list = [data_list_content[i:i + 16] for i in range(0, len(data_list_content), 16)]

    # 存入excel表格
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)

    # 标题存入
    heads = data_list_title[:]  # 将data_list_title第一位到最后一位赋值给heads
    ii = 0
    for head in heads:
        sheet1.write(0, ii, head)
        ii += 1

    # 内容录入
    i = 1
    for list in new_list:
        j = 0
        for data in list:
            sheet1.write(i, j, data)
            j += 1
        i += 1
    # 文件保存
    book.save('./data.xls')


print("全部完成")

# 调用

get_data()