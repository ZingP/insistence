import time

timestring = '2020-03-08 10:20:22'
tuple_time = time.strptime(timestring, '%Y-%m-%d %H:%M:%S')
print(tuple_time)
print(time.mktime(tuple_time))
# ime.struct_time(tm_year=2020, tm_mon=3, tm_mday=8, tm_hour=10, tm_min=20, tm_sec=22, tm_wday=6, tm_yday=68, tm_isdst=-1)
# 1583634022.0