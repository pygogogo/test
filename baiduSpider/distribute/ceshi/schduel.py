# 计划任务
from datetime import timedelta
from celery.schedules import crontab
from ceshi.celeryapp import app

app.conf.beat_schedule = {
    'submit_every_2_seconds': {
        # 计划的任务执行函数
        'task': 'ceshi.task1.add1',
        # 每个2秒执行一次
        'schedule': timedelta(seconds=2),
        # 传递的任务函数参数
        'args': (3, 9)
    },
    'submit_every_3_seconds': {
        # 计划的任务执行函数
        'task': 'ceshi.task2.add2',
        # 每个3秒执行一次
        'schedule': timedelta(seconds=3),
        # 传递的任务函数参数
        'args': (4, 7)
    },
    # 'submit_in_fix_datetime': {
    #     'task': 'celery_task.task_3.add3',
    #     # 比如每年的7月13日10点53分执行
    #     # 注意：默认使用utc时间，当前的时间中的小时必须要-8个小时才会到点提交
    #     'schedule': crontab(minute=53, hour=2, day_of_month=13, month_of_year=7),
    #
    #     '''
    #     # 如果不想-8，可以先设置时区，再按正常时间设置
    #     app.conf.timezone = "Asia/Shanghai"
    #     app.conf.enable_utc = True
    #     '''
    #     'args': ('Hello World',)
    # }

}

# 上面写完后，需要起一个进程，启动计划任务
# celery beat -A celery_task -l info

# 启动worker：
# celery worker -A celery_task -l info -P eventlet