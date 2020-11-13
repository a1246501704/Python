
\WEB框架本质： https://www.cnblogs.com/wupeiqi/articles/4938499.html
	1. 自己开发Web框架 
		- socket（TCP）
		- http协议
		- HTML知识
		- 数据库（pymysql，SQLAlchemy）

	HTTP: 建立在TCP之上
		无状态（如果服务端不给客户端一个凭证，下次再连过来腹端不知道你是谁）、短连接
	TCP：
		长连接、三次握手
		
	WEB应用（网站）：
		浏览器（socket客户端）
			2. www.cnblogs.com（42.121.252.58，80）
				sk.socket()
				sk.connect(（42.121.252.58，80）)
				sk.send('我想要xx')
			5. 接收
			6. 连接断开
			
		博客园（socket服务端）
			1. 监听ip和端口（42.121.252.58，80）
				while True:
					用户 = 等待用户连接
					3. 收到'我想要xx'
					4. 响应：“好”
					用户断开
		
		客户端：浏览器
		服务端：s1.py
		import socket
		sock = socket.socket()
		sock.bind(('127.0.0.1',8080))
		sock.listen(5)

		while True:
			conn,addr = sock.accept() # hang住
			# 有人来连接了
			# 获取用户发送的数据
			data = conn.recv(8096)
			conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
			conn.send(b'123123')
			conn.close()

		Http协议： 
			浏览器发送请求头：
			b'GET / HTTP/1.1\r\n Host: 127.0.0.1:8080\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en-CA;q=0.7,en-AU;q=0.6,en;q=0.5,en-GB;q=0.4\r\n\r\n'
				GET /index?p=123  HTTP/1.1  #（GET的请求体 /index?p=123） 
				Host: 127.0.0.1:8080
				Connection: keep-alive
				Cache-Control: max-age=0
				Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
				User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36
				HTTPS: 1
				Accept-Encoding: gzip, deflate, sdch
				Accept-Language: zh-CN,zh;q=0.8
				Cookie: csrftoken=hNmu2JOtntGMN0hSRSPmMQk2newEb3o8zb6pXW5Cc3m54IaA5VlTkUvqWsFezpni


				POST /index/?p=123  HTTP/1.1 # 在请求头中也可以有值
				Host: 127.0.0.1:8080
				Connection: keep-alive
				Cache-Control: max-age=0
				Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
				User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36
				HTTPS: 1
				Accept-Encoding: gzip, deflate, sdch
				Accept-Language: zh-CN,zh;q=0.8
				Cookie: csrftoken=hNmu2JOtntGMN0hSRSPmMQk2newEb3o8zb6pXW5Cc3m54IaA5VlTkUvqWsFezpni

				p=123 # 两个换行之后加内容（POST的请求体）
			

			服务端响应头：
				200 OK
				Cache-Control:public, max-age=15
				Connection:keep-alive
				Content-Encoding:gzip
				Content-Type:text/html; charset=utf-8
				Date:Wed, 14 Jun 2017 01:21:17 GMT
				Expires:Wed, 14 Jun 2017 01:21:33 GMT
				Last-Modified:Wed, 14 Jun 2017 01:21:03 GMT
				Transfer-Encoding:chunked
				Vary:Accept-Encoding
				X-Frame-Options:SAMEORIGIN
				X-UA-Compatible:IE=10
						
				服务端响应体：将网站源码做为“字符串”返回给用户到浏览器（看到页面效果，由浏览器解析并渲染）
			
			问题1：随便打什么url都返回同样的内容，看其他网站点不同的功能跳转不同的url
				  修改程序：寻找请求头中的\r\n\r\n 后面的就是请求体


		总结:
		1. Http，无状态，短连接
		2. 浏览器（socket客户端）网站（socket服务端）
			
		3. 自己写网站
			a. socket服务端
			b. 根据URL不同返回不同的内容
				路由系统：
					URL -> 函数
			c. 字符串返回给用户
				模板引擎渲染:
					HTML充当模板（特殊字符）
					自己创造任意数据
				字符串
				
		4. Web框架:
			框架种类:
				- a,b,c				   --> Tornado
				- [第三方a],b,c         --> wsgiref模块 -> Django 
				- [第三方a],b,[第三方c]  --> flask,
				
			分类:
				- Django框架（Web。。。。。。） # Python的WEB框架有Django、Tornado、Flask 等多种，Django相较与其他WEB框架其优势为：大而全，框架本身集成了ORM、模型绑定、模板引擎、缓存、Session等诸多功能。
				- 其他
	
\再讲Web框架本质: https://www.cnblogs.com/Dominic-Ji/articles/10982272.html
我们可以这样理解：所有的Web应用本质上就是一个socket服务端，而用户的浏览器就是一个socket客户端。 这样我们就可以自己实现Web框架了。

# 半成品自定义web框架
import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 80))
sk.listen()

while True:
    conn, addr = sk.accept()
    data = conn.recv(8096)
    conn.send(b"OK")
    conn.close()
	
可以说Web服务本质上都是在这十几行代码基础上扩展出来的。这段代码就是它们的祖宗。
用户的浏览器一输入网址，会给服务端发送数据，那浏览器会发送什么数据？怎么发？这个谁来定？ 你这个网站是这个规定，他那个网站按照他那个规定，这互联网还能玩？
所以，必须有一个统一的规则，让大家发送消息、接收消息的时候有个格式依据，不能随便写。
这个规则就是HTTP协议，以后浏览器发送请求信息也好，服务器回复响应信息也罢，都要按照这个规则来。
HTTP协议主要规定了客户端和服务器之间的通信格式，那HTTP协议是怎么规定消息格式的呢？
让我们首先打印下我们在服务端接收到的消息是什么。

import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 80))
sk.listen()

while True:
    conn, addr = sk.accept()
    data = conn.recv(8096)
    print(data)  # 将浏览器发来的消息打印出来
    conn.send(b"OK")
    conn.close()

输出: 回车+换行(\r\n) 
b'GET / HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nDNT: 1\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\nCookie: csrftoken=RKBXh1d3M97iz03Rpbojx1bR6mhHudhyX5PszUxxG3bOEwh1lxFpGOgWN93ZH3zv\r\n\r\n'
# 回车和换行的历史:
机械打字机有回车和换行两个键作用分别是:
　　换行就是把滚筒卷一格，不改变水平位置。即移到下一行，但不是行首，而是和上一行水平位置一样）
　　回车就是把水平位置复位，不卷动滚筒。（即将光标移到行首，但是不会移到下一行，如果继续输入的话会覆盖掉前面的内容）
　　Enter = 回车+换行(\r\n) 


然后我们再看一下我们访问博客园官网时浏览器收到的响应信息是什么。响应相关信息可以在浏览器调试窗口的network标签页中看到。
Network - Headers - Response HHeaders - 点击view source查看 原始响应数据（HTTP/1.1 200 OK），每个HTTP请求和响应都遵循相同的格式，一个HTTP包含Header和Body两部分，其中Body是可选的。 HTTP响应的Header中有一个 Content-Type表明响应的内容格式。如 text/html表示HTML网页。


\1.处女版自定义web框架
经过上面的补充学习，我们知道了要想让我们自己写的web server端正经起来，必须要让我们的Web server在给客户端回复消息的时候按照HTTP协议的规则加上响应状态行，这样我们就实现了一个正经的Web框架了。
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8000))
sock.listen()

while True:
    conn, addr = sock.accept()
    data = conn.recv(8096)
    # 给回复的消息加上响应状态行
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"OK")
    conn.close()


\2.根据不同的路径返回不同的内容
这样就结束了吗？ 如何让我们的Web服务根据用户请求的URL不同而返回不同的内容呢？
小事一桩，我们可以从请求相关数据里面拿到请求URL的路径，然后拿路径做一个判断...
"""
根据URL中不同的路径返回不同的内容
"""
import socket
sk = socket.socket()
sk.bind(("127.0.0.1", 8080))  # 绑定IP和端口
sk.listen()  # 监听

while 1:
    # 等待连接
    conn, add = sk.accept()
    data = conn.recv(8096)  # 接收客户端发来的消息
    # 从data中取到路径
    data = str(data, encoding="utf8")  # 把收到的字节类型的数据转换成字符串
    # 按\r\n分割
    data1 = data.split("\r\n")[0]
    url = data1.split()[1]  # url是我们从浏览器发过来的消息中分离出的访问路径
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')  # 因为要遵循HTTP协议，所以回复的消息也要加状态行
    # 根据不同的路径返回不同内容
    if url == "/index/":
        response = b"index"
    elif url == "/home/":
        response = b"home"
    else:
        response = b"404 not found!"

    conn.send(response)
    conn.close()

\3.根据不同的路径返回不同的内容--函数版
上面的代码解决了不同URL路径返回不同内容的需求。
但是问题又来了，如果有很多很多路径要判断怎么办？难道要挨个写if判断？ 当然不用，我们有更聪明的办法。
"""
根据URL中不同的路径返回不同的内容--函数版
"""

import socket
sk = socket.socket()
sk.bind(("127.0.0.1", 8080))  # 绑定IP和端口
sk.listen()  # 监听

# 将返回不同的内容部分封装成函数
def index(url):
    s = "这是{}页面！".format(url)
    return bytes(s, encoding="utf8")

def home(url):
    s = "这是{}页面！".format(url)
    return bytes(s, encoding="utf8")

while True:
    # 等待连接
    conn, add = sk.accept()
    data = conn.recv(8096)  # 接收客户端发来的消息
    # 从data中取到路径
    data = str(data, encoding="utf8")  # 把收到的字节类型的数据转换成字符串
    # 按\r\n分割
    data1 = data.split("\r\n")[0]
    url = data1.split()[1]  # url是我们从浏览器发过来的消息中分离出的访问路径
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')  # 因为要遵循HTTP协议，所以回复的消息也要加状态行
    # 根据不同的路径返回不同内容，response是具体的响应体
    if url == "/index/":
        response = index(url)
    elif url == "/home/":
        response = home(url)
    else:
        response = b"404 not found!"

    conn.send(response)
    conn.close()

\4.根据不同的路径返回不同的内容--函数进阶版
看起来上面的代码还是要挨个写if判断，怎么办？我们还是有办法！（只要思想不滑坡，方法总比问题多！）
"""
根据URL中不同的路径返回不同的内容--函数进阶版
"""
import socket
sk = socket.socket()
sk.bind(("127.0.0.1", 8080))  # 绑定IP和端口
sk.listen()  # 监听

# 将返回不同的内容部分封装成函数
def index(url):
    s = "这是{}页面！".format(url)
    return bytes(s, encoding="utf8")

def home(url):
    s = "这是{}页面！".format(url)
    return bytes(s, encoding="utf8")

# 定义一个url和实际要执行的函数的对应关系
list1 = [
    ("/index/", index),
    ("/home/", home),
]

while 1:
    # 等待连接
    conn, add = sk.accept()
    data = conn.recv(8096)  # 接收客户端发来的消息
    # 从data中取到路径
    data = str(data, encoding="utf8")  # 把收到的字节类型的数据转换成字符串
    # 按\r\n分割
    data1 = data.split("\r\n")[0]
    url = data1.split()[1]  # url是我们从浏览器发过来的消息中分离出的访问路径
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')  # 因为要遵循HTTP协议，所以回复的消息也要加状态行
    # 根据不同的路径返回不同内容
    func = None  # 定义一个保存将要执行的函数名的变量
    for i in list1:
        if i[0] == url:
            func = i[1]
            break
    if func:
        response = func(url)
    else:
        response = b"404 not found!"

    # 返回具体的响应消息
    conn.send(response)
    conn.close()


\5.返回具体的HTML文件
完美解决了不同URL返回不同内容的问题。 但是我不想仅仅返回几个字符串，我想给浏览器返回完整的HTML内容，这又该怎么办呢？
没问题，不管是什么内容，最后都是转换成字节数据发送出去的。 我们可以打开HTML文件，读取出它内部的二进制数据，然后再发送给浏览器。
"""
根据URL中不同的路径返回不同的内容--函数进阶版
返回独立的HTML页面
"""

import socket
sk = socket.socket()
sk.bind(("127.0.0.1", 8080))  # 绑定IP和端口
sk.listen()  # 监听

# 将返回不同的内容部分封装成函数
def index(url):
    # 读取index.html页面的内容
    with open("index.html", "r", encoding="utf8") as f:
        s = f.read()
    # 返回字节数据
    return bytes(s, encoding="utf8")

def home(url):
    with open("home.html", "r", encoding="utf8") as f:
        s = f.read()
    return bytes(s, encoding="utf8")

# 定义一个url和实际要执行的函数的对应关系
list1 = [
    ("/index/", index),
    ("/home/", home),
]

while True:
    # 等待连接
    conn, add = sk.accept()
    data = conn.recv(8096)  # 接收客户端发来的消息
    # 从data中取到路径
    data = str(data, encoding="utf8")  # 把收到的字节类型的数据转换成字符串
    # 按\r\n分割
    data1 = data.split("\r\n")[0]
    url = data1.split()[1]  # url是我们从浏览器发过来的消息中分离出的访问路径
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')  # 因为要遵循HTTP协议，所以回复的消息也要加状态行
    # 根据不同的路径返回不同内容
    func = None  # 定义一个保存将要执行的函数名的变量
    for i in list1:
        if i[0] == url:
            func = i[1]
            break
    if func:
        response = func(url)
    else:
        response = b"404 not found!"

    # 返回具体的响应消息
    conn.send(response)
    conn.close()

\6.让网页动态起来
这网页能够显示出来了，但是都是静态的啊。页面的内容都不会变化的，我想要的是动态网站。
没问题，我也有办法解决。我选择使用字符串替换来实现这个需求。（这里使用时间戳来模拟动态的数据）
"""
根据URL中不同的路径返回不同的内容--函数进阶版
返回HTML页面
让网页动态起来
"""

import socket
import time

sk = socket.socket()
sk.bind(("127.0.0.1", 8080))  # 绑定IP和端口
sk.listen()  # 监听

# 将返回不同的内容部分封装成函数
def index(url):
    with open("index.html", "r", encoding="utf8") as f:
        s = f.read()
        now = str(time.time())
        s = s.replace("@@oo@@", now)  # 在网页中定义好特殊符号，用动态的数据去替换提前定义好的特殊符号
    return bytes(s, encoding="utf8")

def home(url):
    with open("home.html", "r", encoding="utf8") as f:
        s = f.read()
    return bytes(s, encoding="utf8")

# 定义一个url和实际要执行的函数的对应关系
list1 = [
    ("/index/", index),
    ("/home/", home),
]

while 1:
    # 等待连接
    conn, add = sk.accept()
    data = conn.recv(8096)  # 接收客户端发来的消息
    # 从data中取到路径
    data = str(data, encoding="utf8")  # 把收到的字节类型的数据转换成字符串
    # 按\r\n分割
    data1 = data.split("\r\n")[0]
    url = data1.split()[1]  # url是我们从浏览器发过来的消息中分离出的访问路径
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')  # 因为要遵循HTTP协议，所以回复的消息也要加状态行
    # 根据不同的路径返回不同内容
    func = None  # 定义一个保存将要执行的函数名的变量
    for i in list1:
        if i[0] == url:
            func = i[1]
            break
    if func:
        response = func(url)
    else:
        response = b"404 not found!"

    # 返回具体的响应消息
    conn.send(response)
    conn.close()




WSGI（Web Server Gateway Interface）就是一种规范，它定义了使用Python编写的web应用程序与web服务器程序之间的接口格式，实现web应用程序与web服务器程序间的解耦。
常用的WSGI服务器有uwsgi、Gunicorn。而Python标准库提供的独立WSGI服务器叫wsgiref，Django开发环境用的就是这个模块来做服务器。
\wsgiref
我们利用wsgiref模块来替换我们自己写的web框架的socket server部分：
"""
根据URL中不同的路径返回不同的内容--函数进阶版
返回HTML页面
让网页动态起来
wsgiref模块版
"""

import time
from wsgiref.simple_server import make_server

# 将返回不同的内容部分封装成函数
def index(url):
    with open("index.html", "r", encoding="utf8") as f:
        s = f.read()
        now = str(time.time())
        s = s.replace("@@oo@@", now)
    return bytes(s, encoding="utf8")

def home(url):
    with open("home.html", "r", encoding="utf8") as f:
        s = f.read()
    return bytes(s, encoding="utf8")

# 定义一个url和实际要执行的函数的对应关系
list1 = [
    ("/index/", index),
    ("/home/", home),
]

def run_server(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8'), ])  # 设置HTTP响应的状态码和头信息
    url = environ['PATH_INFO']  # 取到用户输入的url
    func = None
    for i in list1:
        if i[0] == url:
            func = i[1]
            break
    if func:
        response = func(url)
    else:
        response = b"404 not found!"
    return [response, ]

if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8090, run_server)
    print("我在8090等你哦...")
    httpd.serve_forever()


\jinja2
上面的代码实现了一个简单的动态，我完全可以从数据库中查询数据，然后去替换我html中的对应内容，然后再发送给浏览器完成渲染。 这个过程就相当于HTML模板渲染数据。 本质上就是HTML内容中利用一些特殊的符号来替换要展示的数据。 我这里用的特殊符号是我定义的，其实模板渲染有个现成的工具： jinja2

# 下载jinja2:
pip3 install jinja2

# index.html
<!DOCTYPE html>
<html lang="zh-CN">
	<head>
		<meta charset="UTF-8">
		<meta http-equiv="x-ua-compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Title</title>
	</head>
	<body>
		<h1>姓名：{{name}}</h1>
		<h1>爱好：</h1>
		<ul>
			{% for hobby in hobby_list %}
			<li>{{hobby}}</li>
			{% endfor %}
		</ul>
	</body>
</html>

# 使用jinja2渲染index.html文件：
from wsgiref.simple_server import make_server
from jinja2 import Template

def index():
    with open("index2.html", "r") as f:
        data = f.read()
    template = Template(data)  # 生成模板文件
    ret = template.render({"name": "Alex", "hobby_list": ["烫头", "泡吧"]})  # 把数据填充到模板里面
    return [bytes(ret, encoding="utf8"), ]

def home():
    with open("home.html", "rb") as f:
        data = f.read()
    return [data, ]

# 定义一个url和函数的对应关系
URL_LIST = [
    ("/index/", index),
    ("/home/", home),
]

def run_server(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8'), ])  # 设置HTTP响应的状态码和头信息
    url = environ['PATH_INFO']  # 取到用户输入的url
    func = None  # 将要执行的函数
    for i in URL_LIST:
        if i[0] == url:
            func = i[1]  # 去之前定义好的url列表里找url应该执行的函数
            break
    if func:  # 如果能找到要执行的函数
        return func()  # 返回函数的执行结果
    else:
        return [bytes("404没有该页面", encoding="utf8"), ]

if __name__ == '__main__':
    httpd = make_server('', 8000, run_server)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()

现在的数据是我们自己手写的，那可不可以从数据库中查询数据，来填充页面呢？
# 使用pymysql连接数据库：
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="xxx", db="xxx", charset="utf8")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("select name, age, department_id from userinfo")
user_list = cursor.fetchall()
cursor.close()
conn.close()
# 创建一个测试的user表：
CREATE TABLE user(
  id int auto_increment PRIMARY KEY,
  name CHAR(10) NOT NULL,
  hobby CHAR(20) NOT NULL
)engine=innodb DEFAULT charset=UTF8;

