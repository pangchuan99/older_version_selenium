# 引入time模块
import time
import datetime


ticks = time.time()
print ("当前时间戳为:{}".format(ticks))

#获取当前时间
localtime = time.localtime(time.time())
print ("本地时间为 {}:".format(localtime))



# 格式化成2016-03-20 11:45:39形式
#%Y   Y是年的意思
#%m   M是月的意思
#%d   D是日的意思
#%H   H是小时的意思
#%M   M是分钟的意思
#%s   S是秒的意思

a1="2020-05-08 16:36:44"
# print("未进行转换前的时间：{}".format(a1))
st1=datetime.datetime.strptime(a1,"%Y-%m-%d %H:%M:%S")
st1=str(st1)
print("他的类型是：",type(st1))
print("指定时间进行格式转换:{}".format(st1))


st2= (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("他的类型是：",type(st2))

print("当前时间：{}".format(st2))


# st3=st2-sr
# print("减的结果：{}".format(st3))
#
#
