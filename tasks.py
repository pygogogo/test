from celery import Celery
import requests
from lxml import etree

app = Celery(__name__, broker='amqp://guest:guest@192.168.2.216:5672//', backend='amqp://guest:guest@192.168.2.216:5672//')

@app.task
def spider(word):
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
    res.encoding = "utf-8"
    html = etree.HTML(res.text)
    divs = html.xpath("//div[@id='content_left']/div[@class='result c-container ']")
    lists = []
    for div in divs:
        dict = {}
        title = div.xpath("./h3[@class='t']/a//text()")
        title = "".join(title)
        detail_url = div.xpath("./h3[@class='t']/a/@href")
        if detail_url:
            detail_url=detail_url[0]
        dict["title"] = title
        dict["url"] = url
        lists.append(dict)
    return lists



if __name__ == '__main__':
    pass