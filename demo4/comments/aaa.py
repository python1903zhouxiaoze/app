import time,calendar
# a=time.localtime()
# print(list(a))
# print(time.asctime())
# print(time.process_time())
# print(time.ctime())

#闰年，能被4整除，但是不能被100整除---》小闰年
#能被400整除，大闰年

# a=filter(lambda x:not calendar.isleap(x),[x for x in range(1900,2021)])
# print(len(list(a)))
#
# print(calendar.leapdays(1990,2020))

print(calendar.month(theyear=2019,themonth=6,w=2,l=1))