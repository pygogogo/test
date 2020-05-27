from ceshi.celeryapp import app

@app.task
def add2(x, y):
    import time
    time.sleep(1)
    return x * y