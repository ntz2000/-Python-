import requests
import time
url = "http://www.oncewzh.com:8080/chaoxing3/sign?name=18186402662&pwd=ntz000212&address=%E4%B8%9C%E5%8D%8E%E5%A4%A7%E5%AD%A6%E6%9D%BE%E6%B1%9F%E6%A0%A1%E5%8C%BA%E5%9B%BE%E4%B9%A6%E9%A6%86&code=dqv1s6rb979593679&enc=&longitude=121.220435&latitude=31.062593"
sum=0
while True:
    res = requests.get(url)
    sum=sum+1
    print("共执行了%d次"%sum)
    print(res.text)
    time.sleep(31)