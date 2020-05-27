from celery import Celery
broker = 'redis://localhost:6379/1'
backend = 'redis://localhost:6379/2'
# c1是实例化产生的celery的名字，因为会存在多个celery
app = Celery('c1', broker=broker, backend=backend,
             # 包含一些2个任务文件，去相应的py文件找任务，对多个任务进行分类
             include=[
                 'ceshi.task1',
                 'ceshi.task2',
             ])