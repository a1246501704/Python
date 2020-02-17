# 需要回调函数的场景：进程池中任何一个任务一旦处理完了，就立即告知主进程：我好了额，你可以处理我的结果了。主进程则调用一个函数去处理该结果，该函数即回调函数。
# 我们可以把耗时间（阻塞）的任务放到进程池中，然后指定回调函数（主进程负责执行），这样主进程在执行回调函数时就省去了I/O的过程，直接拿到的是任务的结果。


# 方法一
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import requests
import os
import time

# 模拟爬网页
def get(url):
    print('%s GET %s' %(os.getpid(),url))
    response=requests.get(url)
    if response.status_code == 200:
        return {'url':url,'text':response.text}

# 模拟解析爬下来的数据
def parse(res):
    res=res.result()
    url=res['url']
    text=res['text']
    print('%s parse %s res:%s' %(os.getpid(),url,len(text)))

if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.cnblogs.com',
        'https://www.hao123.com',
        'https://www.jd.com/',
        'http://www.sina.com.cn/'
    ]

    p=ProcessPoolExecutor() # 造一个进程池，让get操作并发起来,进程池大小为默认cpu核数。
    start=time.time()
    l=[] 
    for url in urls:
        furture=p.submit(get,url) # 异步提交任务
        l.append(furture) # 把结果存入列表
    p.shutdown(wait=True)
    
    for furture in l: # 等进程池都执行完再拿着结果去做解析
        res=furture.result()
        parse(furture)
    
    print(time.time()-start) # 耗时0.5483059883117676,根据自己的网速会有些网络延迟。

# 执行结果
43703 GET https://www.cnblogs.com
43705 GET https://www.hao123.com
43704 GET https://www.jd.com/
43702 GET https://www.baidu.com
43702 GET http://www.sina.com.cn/
43700 parse https://www.baidu.com res:2443
43700 parse https://www.cnblogs.com res:42347
43700 parse https://www.hao123.com res:497497
43700 parse https://www.jd.com/ res:109287
43700 parse http://www.sina.com.cn/ res:571664
0.5483059883117676

# 执行效果: 程序启动后并发爬取，然后一个一个解析，等到所有的结果都解析完一起把解析结果返回。
# 这样做不合理，当第一个爬取任务执行结束后结果无法及时去解析。整个解析过程耗时过长。如果爬100个网页需要开200个进程才能完成。



# 使用回调机制实现
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import requests
import os
import time

def get(url):
    print('%s GET %s' %(os.getpid(),url))
    response=requests.get(url)
    if response.status_code == 200:
        return {'url':url,'text':response.text}

def parse(res):
    res=res.result() # 取结果
    url=res['url']
    text=res['text']
    print('%s parse %s res:%s' %(os.getpid(),url,len(text)))

if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.cnblogs.com',
        'https://www.hao123.com',
        'https://www.jd.com/',
        'http://www.sina.com.cn/'
    ]

    p=ProcessPoolExecutor()
    start=time.time()
    for url in urls:
        future=p.submit(get, url) # 向进程池异步提交任务
        future.add_done_callback(parse) # 回调
# 相当于给future也就是p.submit绑定了一个回调函数，当p.submit的执行有返回值了就会触发add_done_callback中指定的parse函数。
# PS: 给每个任务发了一个遥控器，干完活就按遥控器进行下一步。

    p.shutdown(wait=True)# 关闭进程池
    print(time.time()-start) # 0.3529038715362549
    print(os.getpid()) # 可以看到是主进程去做的回调

# 执行结果
43706 GET https://www.baidu.com
43707 GET https://www.cnblogs.com
43708 GET https://www.hao123.com
43700 parse https://www.baidu.com res:2443 # 在其他url还在爬的时候，第一个已经有返回了。
43709 GET https://www.jd.com/
43706 GET http://www.sina.com.cn/
43700 parse https://www.jd.com/ res:109287
43700 parse http://www.sina.com.cn/ res:571664
43700 parse https://www.cnblogs.com res:42347
43700 parse https://www.hao123.com res:497497
0.3529038715362549
43700
# 执行效果: 批量爬取，谁先爬完就去做解析。节省时间和资源，如果爬100个网页只需要开启101个进程。