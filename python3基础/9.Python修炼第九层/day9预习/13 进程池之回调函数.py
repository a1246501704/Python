import requests #pip3 install requests
import os,time
from multiprocessing import Pool
def get_page(url):
    print('<%s> get :%s' %(os.getpid(),url))
    respone = requests.get(url)
    if respone.status_code == 200:
        return {'url':url,'text':respone.text}

def parse_page(dic):
    print('<%s> parse :%s' %(os.getpid(),dic['url']))
    time.sleep(0.5)
    res='url:%s size:%s\n' %(dic['url'],len(dic['text'])) #模拟解析网页内容
    with open('db.txt','a') as f:
        f.write(res)


if __name__ == '__main__':
    p=Pool(4)
    urls = [
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
    ]


    for url in urls:
        # 把 get_page,args=(url,) 的future对象参数 给 callback=parse_page(通知主进程干解析的事)
        # 耗时长的任务交给进程池，耗时短的任务交给主进程
        p.apply_async(get_page,args=(url,),callback=parse_page)


    p.close()
    p.join()
    print('主进程pid:',os.getpid())

