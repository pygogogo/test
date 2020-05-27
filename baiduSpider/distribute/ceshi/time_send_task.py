from ceshi.task1 import add1
from ceshi.task2 import add2
# 执行定时任务，3s以后执行add1、add2任务
from datetime import datetime
# 设置任务执行时间2019年7月12日21点45分12秒
v1 = datetime(2019, 7, 12, 21, 48, 12)
print(v1)  # 2019-07-12 21:45:12
# 将v1时间转成utc时间
v2 = datetime.utcfromtimestamp(v1.timestamp())
print(v2)  # 2019-07-12 13:45:12
# 取出要执行任务的时间对象，调用apply_async方法，args是任务函数传的参数，eta是执行的时间
result1 = add1.apply_async(args=[3, 8], eta=v2)
result2 = add2.apply_async(args=[4, 9], eta=v2)
print(result1.id)
print(result2.id)