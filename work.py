from spider import spider
res  = ["饼干","芝麻","面条","肉","新浪"]
for i in res:
    print(i)
    #spider.delay(i)
    spider.apply_async(args=(i,))