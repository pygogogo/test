import  requests

headers={
    "user-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0"
}
res = requests.get("https://www.baidu.com/",headers=headers)

print(res.text)