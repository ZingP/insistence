import time

# 获取当前时间并转换成响应的格式
today = time.strftime("%Y%m%d", time.localtime())
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print(today)
print(now)
# 20200309
# 2020-03-09 21:46:36