
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
			b'GET / HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en-CA;q=0.7,en-AU;q=0.6,en;q=0.5,en-GB;q=0.4\r\n\r\n'
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


				POST /index  HTTP/1.1
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
				
	


		
		
		1. Http，无状态，短连接
		2. 
			浏览器（socket客户端）
			网站（socket服务端）
			
		3. 自己写网站
			a. socket服务端
			b. 根据URL不同返回不同的内容
				路由系统：
					URL -> 函数
			c. 字符串返回给用户
				模板引擎渲染：
					HTML充当模板（特殊字符）
					自己创造任意数据
				字符串
				
		4. Web框架：
			框架种类：
				- a,b,c					 --> Tornado
				- [第三方a],b,c          --> wsgiref -> Django 
				- [第三方a],b,[第三方c]  --> flask,
				
			分类：
				- Django框架（Web。。。。。。）
				- 其他
		

		
	2. Django框架
		pip3 install django
		
		命令：
			# 创建Django程序
			django-admin startproject mysite
			# 进入程序目录
			cd mysite
			# 启动socket服务端，等待用户发送请求
			python manage.py runserver 127.0.0.1:8080
	
		pycharm：
			...
			
		Django程序目录：
			mysite
				mysite
					- settings.py  # Django配置文件
					- url.py       # 路由系统：url->函数
					- wsgi.py      # 用于定义Django用socket, wsgiref,uwsgi
			
				# 对当前Django程序所有操作可以基于 python manage.py runserver
				manage.py 
	
	
		1. 创建project
		2. 配置：
				- 模板路径
					template目录
					
					TEMPLATES = [
						{
							'BACKEND': 'django.template.backends.django.DjangoTemplates',
							'DIRS': [os.path.join(BASE_DIR, 'template')],
							'APP_DIRS': True,
							'OPTIONS': {
								'context_processors': [
									'django.template.context_processors.debug',
									'django.template.context_processors.request',
									'django.contrib.auth.context_processors.auth',
									'django.contrib.messages.context_processors.messages',
								],
							},
						},
					]
				- 静态文件路径
					static目录
					
					STATIC_URL = '/static/'
					STATICFILES_DIRS = (
						os.path.join(BASE_DIR,'static'),
					)

		3. 额外配置
			MIDDLEWARE = [
				'django.middleware.security.SecurityMiddleware',
				'django.contrib.sessions.middleware.SessionMiddleware',
				'django.middleware.common.CommonMiddleware',
				#'django.middleware.csrf.CsrfViewMiddleware',
				'django.contrib.auth.middleware.AuthenticationMiddleware',
				'django.contrib.messages.middleware.MessageMiddleware',
				'django.middleware.clickjacking.XFrameOptionsMiddleware',
			]
				
	
	
	        4. url 对应关系
		GET请求  -> 只有request.GET有值
		POST请求 -> request.GET 和 request.POST都可能有值

			/login/  login
			
			def login(request):
			    request.method
			    request.POST -> 请求体
			    request.GET  -> 请求头中的url中

			    return HttpResponse(..)
			    return render(request,'login.html',{...})
			    return redirect('要跳转的网址')


		5. 模版引擎中的特殊标记
			login.html
			    {{name}}

			def login(request):
				
			    return render(request,'login.html',{'name': 'alex'})
	

		6. 作业
			django + pymysql实现
				- 用户登陆
				- 查看用户列表
	
	
	
	
	
	
	
	
	
	