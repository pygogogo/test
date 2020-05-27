# task_1.py
from ceshi.celeryapp import app

@app.task
def add1(x, y):
    import time
    time.sleep(0.5)
    return x + y
