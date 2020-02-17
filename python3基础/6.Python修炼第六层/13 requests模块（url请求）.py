

基本GET请求（headers参数 和 parmas参数）
\1. 最基本的GET请求可以直接用get方法
response = requests.get("http://www.baidu.com/")
# 也可以这么写
# response = requests.request("get", "http://www.baidu.com/")

\2. 添加 headers 和 查询参数
# 如果想添加 headers，可以传入headers参数来增加请求头中的headers信息。如果要将参数放在url中传递，可以利用 params 参数。
import requests
 
kw = {'wd':'长城'}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
 
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("http://www.baidu.com/s?", params = kw, headers = headers)
 
# 查看响应内容，response.text 返回的是Unicode格式的数据
print(response.text)
 
# 查看响应内容，response.content返回的字节流数据
print(respones.content)
 
# 查看完整url地址
print(response.url)
 
# 查看响应头部字符编码
print(response.encoding)
 
# 查看响应码
print(response.status_code)

\3. 私密代理验证（特定格式） 和 Web客户端验证（auth 参数）
urllib2 这里的做法比较复杂，requests只需要一步：

# 私密代理
# 如果代理需要使用HTTP Basic Auth，可以使用下面这种格式：
import requests
proxy = { "http": "mr_mao_hacker:sffqry9r@61.158.163.130:16816" }
response = requests.get("http://www.baidu.com", proxies = proxy)
print(response.text)

# web客户端验证
# 如果是Web客户端验证，需要添加 auth = (账户名, 密码)
import requests
auth=('test', '123456')
response = requests.get('http://192.168.199.107', auth = auth)
print(response.text)


\4. Cookies 和 Sission
\Cookies
如果一个响应中包含了cookie，那么我们可以利用 cookies参数拿到：

import requests
response = requests.get("http://www.baidu.com/")
# 7. 返回CookieJar对象:
cookiejar = response.cookies
# 8. 将CookieJar转为字典：
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
print(cookiejar)
print(cookiedict)

# Out:
<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
{'BDORZ': '27315'}

\Sission
在 requests 里，session对象是一个非常常用的对象，这个对象代表一次用户会话：从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开。
会话能让我们在跨请求时候保持某些参数，比如在同一个 Session 实例发出的所有请求之间保持 cookie 。

实现人人网登录
import requests
 
# 1. 创建session对象，可以保存Cookie值
ssion = requests.session()
 
# 2. 处理 headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
 
# 3. 需要登录的用户名和密码
data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}  
 
# 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
ssion.post("http://www.renren.com/PLogin.do", data = data)
 
# 5. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = ssion.get("http://www.renren.com/410043129/profile")
 
# 6. 打印响应内容
print(response.text)

\5. 处理HTTPS请求 SSL证书验证
Requests也可以为HTTPS请求验证SSL证书：

\要想检查某个主机的SSL证书，你可以使用 verify 参数（也可以不写）
import requests
response = requests.get("https://www.baidu.com/", verify=True)
 
# 也可以省略不写
# response = requests.get("https://www.baidu.com/")
print(r.text)

运行结果：
<!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge>百度一下，你就知道 ....

\如果SSL证书验证不通过，或者不信任服务器的安全证书，则会报出SSLError，据说 12306 证书是自己做的：
import requests
response = requests.get("https://www.12306.cn/mormhweb/")
print response.text
果然：
SSLError: ("bad handshake: Error([('SSL routines', 'ssl3_get_server_certificate', 'certificate verify failed')],)",)
如果我们想跳过 12306 的证书验证，把 verify 设置为 False 就可以正常请求了。

r = requests.get("https://www.12306.cn/mormhweb/", verify = False)



\6. 发送请求与传递参数
# 先来一个简单的例子吧！让你了解下其威力：
import requests
 
r = requests.get(url='http://www.itwhy.org')  # 最基本的GET请求
print(r.status_code) # 获取返回状态
r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'}) # 带参数的GET请求
print(r.url)
print(r.text) # 打印解码后的返回数据

# 很简单,不但GET方法简单，其他方法都是统一的接口样式！
requests.get(‘https://github.com/timeline.json’) #GET请求
requests.post(“http://httpbin.org/post”) #POST请求
requests.put(“http://httpbin.org/put”) #PUT请求
requests.delete(“http://httpbin.org/delete”) #DELETE请求
requests.head(“http://httpbin.org/get”) #HEAD请求
requests.options(“http://httpbin.org/get”) #OPTIONS请求

PS：以上的HTTP方法，对于WEB系统一般只支持 GET 和 POST，有一些还支持 HEAD 方法。
带参数的请求实例：
import requests
requests.get('http://www.dict.baidu.com/s', params={'wd': 'python'})    #GET参数实例
requests.post('http://www.itwhy.org/wp-comments-post.php', data={'comment': '测试POST'})    #POST参数实例

\POST发送JSON数据
import requests
import json
 
r = requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))
print(r.json())

\定制header
import requests
import json
 
data = {'some': 'data'}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
 
r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers)
print(r.text)

\6. Response对象
# 使用requests方法后，会返回一个response对象，其存储了服务器响应的内容，如上实例中已经提到的 r.text、r.status_code……
# 获取文本方式的响应体实例：当你访问 r.text 之时，会使用其响应的文本编码进行解码，并且你可以修改其编码让 r.text 使用自定义的编码进行解码.

r = requests.get('http://www.itwhy.org')
print(r.text, '\n{}\n'.format('*'*79), r.encoding)
r.encoding = 'GBK'
print(r.text, '\n{}\n'.format('*'*79), r.encoding)

其他响应：
r.status_code #响应状态码
r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
#*特殊方法*#
r.json() #Requests中内置的JSON解码器
r.raise_for_status() #失败请求(非200响应)抛出异常

案例之一:
import requests
 
URL = 'http://ip.taobao.com/service/getIpInfo.php'  # 淘宝IP地址库API
try:
    r = requests.get(URL, params={'ip': '8.8.8.8'}, timeout=1)
    r.raise_for_status()    # 如果响应状态码不是 200，就主动抛出异常
except requests.RequestException as e:
    print(e)
else:
    result = r.json()
    print(type(result), result, sep='\n')

\7. 上传文件
# 使用 Requests 模块，上传文件也是如此简单的，文件的类型会自动进行处理：
import requests
 
url = 'http://127.0.0.1:5000/upload'
files = {'file': open('/home/lyb/sjzl.mpg', 'rb')}
#files = {'file': ('report.jpg', open('/home/lyb/sjzl.mpg', 'rb'))}     #显式的设置文件名
 
r = requests.post(url, files=files)
print(r.text)
# 更加方便的是，你可以把字符串当着文件进行上传：
import requests
 
url = 'http://127.0.0.1:5000/upload'
files = {'file': ('test.txt', b'Hello Requests.')}     #必需显式的设置文件名
 
r = requests.post(url, files=files)
print(r.text)

\8. 身份验证
# 基本身份认证(HTTP Basic Auth):
import requests
from requests.auth import HTTPBasicAuth
 
r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=HTTPBasicAuth('user', 'passwd'))
# r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=('user', 'passwd'))    # 简写
print(r.json())

# 另一种非常流行的HTTP身份认证形式是摘要式身份认证，Requests对它的支持也是开箱即可用的:
requests.get(URL, auth=HTTPDigestAuth('user', 'pass'))

\9. Cookies与会话对象
# 如果某个响应中包含一些Cookie，你可以快速访问它们：
import requests
 
r = requests.get('http://www.google.com.hk/')
print(r.cookies['NID'])
print(tuple(r.cookies))

# 要想发送你的cookies到服务器，可以使用 cookies 参数：
import requests
 
url = 'http://httpbin.org/cookies'
cookies = {'testCookies_1': 'Hello_Python3', 'testCookies_2': 'Hello_Requests'}
# 在Cookie Version 0中规定空格、方括号、圆括号、等于号、逗号、双引号、斜杠、问号、@，冒号，分号等特殊符号都不能作为Cookie的内容。
r = requests.get(url, cookies=cookies)
print(r.json())
# 会话对象让你能够跨请求保持某些参数，最方便的是在同一个Session实例发出的所有请求之间保持cookies，且这些都是自动处理的，甚是方便。
# 下面就来一个真正的实例，如下是快盘签到脚本：

import requests
 
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
 
s = requests.Session()
s.headers.update(headers)
# s.auth = ('superuser', '123')
s.get('https://www.kuaipan.cn/account_login.htm')
 
_URL = 'http://www.kuaipan.cn/index.php'
s.post(_URL, params={'ac':'account', 'op':'login'},
       data={'username':'****@foxmail.com', 'userpwd':'********', 'isajax':'yes'})
r = s.get(_URL, params={'ac':'zone', 'op':'taskdetail'})
print(r.json())
s.get(_URL, params={'ac':'common', 'op':'usersign'})


\10. 快速指南
\10.1 发送请求
# 发送请求很简单的，首先要导入requests模块：
>>>import requests
# 接下来让我们获取一个网页，例如我个人博客的首页：
>>>r = requests.get('http://www.zhidaow.com')
# 接下来，我们就可以使用这个r的各种方法和函数了。
# 另外，HTTP请求还有很多类型，比如POST,PUT,DELETE,HEAD,OPTIONS。也都可以用同样的方式实现：
>>> r = requests.post("http://httpbin.org/post")
>>> r = requests.put("http://httpbin.org/put")
>>> r = requests.delete("http://httpbin.org/delete")
>>> r = requests.head("http://httpbin.org/get")
>>> r = requests.options("http://httpbin.org/get")
# 因为目前我还没用到这些，所以没有深入研究。

\10.2 在URLs中传递参数
# 有时候我们需要在URL中传递参数，比如在采集百度搜索结果时，我们wd参数（搜索词）和rn参数（搜素结果数量），你可以手工组成URL，requests也提供了一种看起来很NB的方法：
>>> payload = {'wd': '张亚楠', 'rn': '100'}
>>> r = requests.get("http://www.baidu.com/s", params=payload)
>>> print r.url
u'http://www.baidu.com/s?rn=100&wd=%E5%BC%A0%E4%BA%9A%E6%A5%A0'
# 上面wd=的乱码就是“张亚楠”的转码形式。（好像参数按照首字母进行了排序。）

\10.3 获取响应内容
# 可以通过r.text来获取网页的内容。
>>> r = requests.get('https://www.zhidaow.com')
>>> r.text
u'<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml"...'
# 文档里说，requests会自动将内容转码。大多数unicode字体都会无缝转码。但我在cygwin下使用时老是出现UnicodeEncodeError错误，郁闷。倒是在python的IDLE中完全正常。
# 另外，还可以通过r.content来获取页面内容。
>>> r = requests.get('https://www.zhidaow.com')
>>> r.content
b'<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml"...'
# 文档中说r.content是以字节的方式去显示，所以在IDLE中以b开头。但我在cygwin中用起来并没有，下载网页正好。所以就替代了urllib2的urllib2.urlopen(url).read()功能。（基本上是我用的最多的一个功能。）

\10.4 获取网页编码
# 可以使用r.encoding来获取网页编码。
>>> r = requests.get('http://www.zhidaow.com')
>>> r.encoding
'utf-8'
# 当你发送请求时，requests会根据HTTP头部来猜测网页编码，当你使用r.text时，requests就会使用这个编码。当然你还可以修改requests的编码形式。
>>> r = requests.get('http://www.zhidaow.com')
>>> r.encoding
'utf-8'
>>>r.encoding = 'ISO-8859-1'
# 像上面的例子，对encoding修改后就直接会用修改后的编码去获取网页内容。

\10.5 json
# 像urllib和urllib2，如果用到json，就要引入新模块，如json和simplejson，但在requests中已经有了内置的函数，r.json()。就拿查询IP的API来说：
>>>r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=122.88.60.28')
>>>r.json()['data']['country']
'中国'

\10.6 网页状态码
# 我们可以用r.status_code来检查网页的状态码。
>>>r = requests.get('http://www.mengtiankong.com')
>>>r.status_code
200
>>>r = requests.get('http://www.mengtiankong.com/123123/')
>>>r.status_code
404
>>>r = requests.get('http://www.baidu.com/link?url=QeTRFOS7TuUQRppa0wlTJJr6FfIYI1DJprJukx4Qy0XnsDO_s9baoO8u1wvjxgqN')
>>>r.url
u'http://www.zhidaow.com/
>>>r.status_code
200
# 前两个例子很正常，能正常打开的返回200，不能正常打开的返回404。但第三个就有点奇怪了，那个是百度搜索结果中的302跳转地址，但状态码显示是200，接下来我用了一招让他原形毕露：
>>>r.history
(<Response [302]>,)
# 这里能看出他是使用了302跳转。也许有人认为这样可以通过判断和正则来获取跳转的状态码了，其实还有个更简单的方法：
>>>r = requests.get('http://www.baidu.com/link?url=QeTRFOS7TuUQRppa0wlTJJr6FfIYI1DJprJukx4Qy0XnsDO_s9baoO8u1wvjxgqN', allow_redirects = False)
>>>r.status_code
302
# 只要加上一个参数allow_redirects，禁止了跳转，就直接出现跳转的状态码了，好用吧？我也利用这个在最后一掌做了个简单的获取网页状态码的小应用，原理就是这个。

\10.7 响应头内容
# 可以通过r.headers来获取响应头内容。
>>>r = requests.get('http://www.zhidaow.com')
>>> r.headers
{
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'content-type': 'text/html; charset=utf-8';
    ...
}
# 可以看到是以字典的形式返回了全部内容，我们也可以访问部分内容。
>>> r.headers['Content-Type']
'text/html; charset=utf-8'
>>> r.headers.get('content-type')
'text/html; charset=utf-8'

\10.8 设置超时时间
# 我们可以通过timeout属性设置超时时间，一旦超过这个时间还没获得响应内容，就会提示错误。
>>> requests.get('http://github.com', timeout=0.001)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)

\10.9 代理访问
# 采集时为避免被封IP，经常会使用代理。requests也有相应的proxies属性。

import requests
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}
requests.get("http://www.zhidaow.com", proxies=proxies)
# 如果代理需要账户和密码，则需这样：
proxies = {
    "http": "http://user:pass@10.10.1.10:3128/",
}

\10.10 请求头内容
# 请求头内容可以用r.request.headers来获取。
>>> r.request.headers
{'Accept-Encoding': 'identity, deflate, compress, gzip',
'Accept': '*/*', 'User-Agent': 'python-requests/1.2.3 CPython/2.7.3 Windows/XP'}

\10.11 自定义请求头部
# 伪装请求头部是采集时经常用的，我们可以用这个方法来隐藏：
r = requests.get('http://www.zhidaow.com')
print r.request.headers['User-Agent']
#python-requests/1.2.3 CPython/2.7.3 Windows/XP
 
headers = {'User-Agent': 'alexkh'}
r = requests.get('http://www.zhidaow.com', headers = headers)
print r.request.headers['User-Agent']
#alexkh
\10.12 持久连接keep-alive
# requests的keep-alive是基于urllib3，同一会话内的持久连接完全是自动的。同一会话内的所有请求都会自动使用恰当的连接。
# 也就是说，你无需任何设置，requests会自动实现keep-alive。

\11. 简单应用
\11.1 获取网页返回码
def get_status(url):
    r = requests.get(url, allow_redirects = False)
    return r.status_code
 
print get_status('http://www.zhidaow.com') 
#200
print get_status('http://www.zhidaow.com/hi404/')
#404
print get_status('http://mengtiankong.com')
#301
print get_status('http://www.baidu.com/link?url=QeTRFOS7TuUQRppa0wlTJJr6FfIYI1DJprJukx4Qy0XnsDO_s9baoO8u1wvjxgqN')
#302
print get_status('http://www.huiya56.com/com8.intre.asp?46981.html')
#500
