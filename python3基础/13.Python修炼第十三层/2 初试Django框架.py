\Django框架 : https://www.cnblogs.com/Dominic-Ji/p/10881214.html

\Django介绍

\Django安装
pip3 install django
\运行Django
# 命令运行
    # 创建Django程序
    django-admin startproject mysite
    # 进入程序目录(在哪执行的命令就在哪生成文件夹)
    cd mysite
    # 启动socket服务端，等待用户发送请求,如果不加 127.0.0.1:8080 即监听8000端口。
    python3 manage.py runserver
    或
    python3 manage.py runserver 127.0.0.1:8080  
    或
    python3 manage.py runserver 0.0.0.0:8080

    # 其他常用命令
　　 python manage.py runserver 0.0.0.0
　　 python manage.py startapp appname
　　 python manage.py syncdb
　　 python manage.py makemigrations
　　 python manage.py migrate
　　 python manage.py createsuperuser

# pycharm运行
File - New Project - Django （指定目录位置、指定python版本、指定模版语言、指定模版目录）
			
\Django程序目录介绍
mysite/
├── manage.py  # 管理文件，对当前Django程序所有操作可以基于 python3 manage.py runserver
└── mysite     # 项目目录
    ├── __init__.py
    |—— asgi.py      # 异步服务网关接口
    ├── settings.py  # Django配置文件
    ├── urls.py  # 路由系统：url->函数 的对应关系
    └── wsgi.py  # 用于定义Django用socket, wsgiref（本地测试用，性能低）,uwsgi（生产用）。WSGI（Web Server Gateway Interface）是一种规范，它定义了使用python编写的web app与web server之间接口格式，实现web app与web server间的解耦。runserver命令就使用wsgiref模块做简单的web server
	
\Django - urls路由系统
url 对应关系
    GET请求  -> 只有request.GET有值
    POST请求 -> request.GET 和 request.POST都可能有值
    
    def login(request):
        request.method
        request.POST -> 请求体
        request.GET  -> 请求头中的url中

        return HttpResponse(..)
        return render(request,'login.html',{...})
        return redirect('要跳转的网址')

    修改urls.py
    path('login/',login)

\Django - 模版文件配置
- 模板路径
	template目录
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "template")],  # template文件夹位置
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
\Django - 静态文件配置
- 静态文件路径
	static目录
STATIC_URL = '/static/'  # HTML中使用的静态文件夹前缀
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # 静态文件存放位置
]



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
				

5. 模版引擎中的特殊标记
    login.html
        {{name}}

    def login(request):
        return render(request,'login.html',{'name': 'alex'})

6. 作业
    django + pymysql实现
        - 用户登陆
        - 查看用户列表