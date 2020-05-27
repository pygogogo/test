import requests
from lxml import etree
from ezpymysql import Connection
from celery import Celery



app = Celery(__name__, broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/1')
@app.task
def spider(word):
    db = Connection(
        'localhost',
        'baiduspider',
        'root',
        '123456'
    )
    url = "https://www.baidu.com/s"
    parmas = {
        'tn': "baidu",
        "wd": word
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
        # "X-Requested-With": "XMLHttpRequest"
    }
    res = requests.get(url, headers=headers, params=parmas)
    #print(res.text)
    res.encoding = "utf-8"
    html = etree.HTML(res.text)

    divs = html.xpath("//div[@id='content_left']/div[@class='result c-container ']")
    for div in divs:
        result={}
        title = div.xpath("./h3[@class='t']/a//text()")
        title = "".join(title)
        detail_url = div.xpath("./h3[@class='t']/a/@href")
        if detail_url:
            detail_url=detail_url[0]
        else:
            detail_url=""
        result["title"]=title
        result["url"] = detail_url
        db.table_insert('baidu', result)



if __name__ == '__main__':
    spider("yingyu")