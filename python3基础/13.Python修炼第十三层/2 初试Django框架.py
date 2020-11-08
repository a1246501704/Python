\Django框架 : https://www.cnblogs.com/Dominic-Ji/p/10881214.html

\1. Django介绍
# MVC框架
MVC，全名是Model View Controller，是软件工程中的一种软件架构模式
把软件系统分为三个基本部分：模型(Model)、视图(View)和控制器(Controller)，具有耦合性低、重用性高、生命周期成本低等优点。
见 MVC框架图

Django框架的设计模式借鉴了MVC框架的思想，也是分成三部分，来降低各个部分之间的耦合性。
Django框架的不同之处在于它拆分的三部分为：Model（模型）、Template（模板）和View（视图），也就是MTV框架。

# MTV框架
Model(模型)：负责业务对象与数据库的对象(ORM)
Template(模版)：负责如何把页面展示给用户
View(视图)：负责业务逻辑，并在适当的时候调用Model和Template

此外，Django还有一个urls分发器，它的作用是将一个个URL的页面请求分发给不同的view处理，view再调用相应的Model和Template


\2. Django安装
下载:https://www.djangoproject.com/download/
pip3 install django
pip3 install django==3.0.8
pip3 list | grep Django
\3. 运行Django
# 命令运行
    django-admin startproject mysite # 创建Django项目
    cd mysite # 进入程序目录(在哪执行的命令就在哪生成文件夹)
    # 启动socket服务端，等待用户发送请求,如果不加 127.0.0.1:8080 即监听8000端口。
    python3 manage.py runserver
    或
    python3 manage.py runserver 127.0.0.1:8080  
    或
    python3 manage.py runserver 0.0.0.0:8080
    # 在浏览器输入：http://127.0.0.1:8000 会看到Django的欢迎页面。
    # 其他常用命令
　　 python manage.py runserver 0.0.0.0
　　 python manage.py startapp appname
　　 python manage.py syncdb
　　 python manage.py makemigrations
　　 python manage.py migrate
　　 python manage.py createsuperuser

# pycharm运行
File - New Project - Django （指定目录位置、指定python版本、指定模版语言、指定模版目录）
			
\4. Django程序目录介绍（见图2.1）
mysite/
├── manage.py  # 管理文件(启动文件)，对当前Django程序所有操作可以基于 python3 manage.py runserver
└── mysite     # 项目目录
    ├── __init__.py
    |—— asgi.py      # 异步服务网关接口
    ├── settings.py  # Django配置文件
    ├── urls.py  # 路由系统：url->函数 的对应关系(路径与视图函数的映射关系)
    └── wsgi.py  # 用于定义Django用socket, wsgiref（本地测试用，性能低）,uwsgi（生产用）。WSGI（Web Server Gateway Interface）是一种规范，它定义了使用python编写的web app与web server之间接口格式，实现web app与web server间的解耦。runserver命令就使用wsgiref模块做简单的web server

\5. Django的MTV分别代表
Model(模型): 和数据库相关的，负责业务对象与数据库的对象（ORM）。一个抽象层，用来构建和操作你的web应用中的数据，模型是你的数据的唯一的、权威的信息源。它包含你所储存数据的必要字段和行为。通常，每个模型对应数据库中唯一的一张表。
Template(模板): 放所有的html文件，模板层提供了设计友好的语法来展示信息给用户。使用模板方法可以动态地生成HTML。模板包含所需HTML 输出的静态部分，以及一些特殊的语法，描述如何将动态内容插入。
　　　　　　　　　模板语法:目的是将白变量（数据库的内容）如何巧妙的嵌入到html页面中
View(视图): 负责业务逻辑，并在适当的时候调用Model和Template。用于封装负责处理用户请求及返回响应的逻辑。视图可以看作是前端与数据库的中间人，他会将前端想要的数据从数据库中读出来给前端。他也会将用户要想保存的数据写到数据库。
此外，Django还有一个URL分发器。它的作用是将一个个URL的页面请求分别发给不同的Views处理，Views再调用相应的Model和Template。

\6. Django - urls路由系统
url(path) 对应关系
    GET请求  -> 只有request.GET有值，值在请求头的url中。
    POST请求 -> request.GET 和 request.POST都可能有值。在url中可以有值，在请求体中也可以有值。
    
    from django.shortcuts import HttpResponse
    def login(request):
        # request.method -> 获取提交方式
        # request.POST   -> 请求体
        # request.GET    -> 请求头中的url中

        return HttpResponse("Hello World")       # HttpResponse中只能加字符串，里面写什么页面就显示什么。
        return render(request,'login.html',{...})# 自动找到模板路径下的login.html文件，读取内容并返回给用户，如果template目录改了名字settings.py中会自动读取到。
        return redirect('要跳转的网址')

    修改urls.py
    path('login/',login), # 逗号一定要加  from django.urls import path
    或者
    url('^login/',login), # 逗号一定要加  from django.conf.urls import url

\7. Django - 模版文件配置
- 模板路径
	template目录
在配置文件settings.py中修改模版引擎
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', #指定DTL模板引擎,也可以改为jinja2，下载的包中有源码（根据包含的路径去找）
        'DIRS': [os.path.join(BASE_DIR, "template")],  # template文件夹位置,模板文件所在根目录。不支持中文,BASE_DIR 指的是当前项目的根目录
        'APP_DIRS': True, # #先DIRS找，再 APP_DIRS找
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
在这个字典中，我们只需要连接前三个ksy值：‘BACKEND’,‘DIRS’,‘APP_DIRS’
如果APP_URLS项设置为True，表示可以到应用下的名字固定为templaets目录下查找模板文件
前提：必须将该应用app添加到配置文件中指定列表中settings.py中的INSTALLED_APPS
如何添加？
    1.直接将应用名称添加到应用列表
    2.将应用下app.py配置添加到应用中
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'book',		# 第一种方式
    'book.apps.BookConfig',	#第二种方式
]

\8. Django - 静态文件配置
- 静态文件路径
	static目录（见图2.2）
在配置文件settings.py中修改静态文件位置
STATIC_URL = '/static/'  # HTML中使用的静态文件夹前缀，可以起其它的名字。通常都和真实静态文件目录名称一致。
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # 静态文件真实存放位置
]



\9. 额外配置
刚开始学习时可在配置文件中暂时禁用csrf中间件，方便表单提交测试。
在配置文件settings.py中修改
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        #'django.middleware.csrf.CsrfViewMiddleware', # 功能：防止跨站请求伪造的功能,CSRF 表示django全局发送post请求均需要字符串验证 https://www.cnblogs.com/dushangguzhousuoli/p/10649756.html
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
				

\10. Django基础必备三件套
from django.urls import path
from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect

# 1.HttpResponse
内部传入一个字符串参数，返回给浏览器。
例如：
def index(request):
    # 业务逻辑代码
    return HttpResponse("OK")

# 2.render
除request参数外 还可以接收 一个待渲染的模板文件 和 一个保存具体数据的字典参数。
将数据填充进模板文件，最后把结果返回给浏览器。（类似于我们上面用到的jinja2）
例如：结合一个给定的模板和一个给定的上下文字典, 并返回一个html渲染后的HttpResponse对象。
参数讲解:
    request: 是一个固定参数, 没什么好讲的。
    template_name: templates 中定义的文件, 要注意路径名. 比如'templates\polls\index.html', 参数就要写‘polls\index.html’
    context: 要传入文件中用于渲染呈现的数据, 默认是字典格式
    content_type: 生成的文档要使用的MIME 类型。默认为DEFAULT_CONTENT_TYPE 设置的值。
    status: http的响应代码,默认是200.
    using: 用于加载模板使用的模板引擎的名称。
def index(request):
    # 业务逻辑代码
    return render(request, "index.html", {"name": "alex", "hobby": ["烫头", "泡吧"]})

# 3.redirect
参数可以是:
    一个模型: 将调用模型的get_absolute_url()函数
    一个视图, 可以带有函数:　可以使用urlresolvers.reverse来反向解析名称
    一个绝对的或相对的URL, 将原封不动的作为重定向的位置.
默认返回一个临时的重定向, 传递permanent=True可以返回一个永久的重定向.
接受一个URL参数，表示跳转到指定的URL。

示例:
你可以用多种方式使用redirect()函数.
传递一个具体的ORM对象(了解即可).
将调用具体ORM对象的get_absolute_url()方法来获取重定向的URL.
from django.shortcuts import redirect
def my_view(request):
    ...
    object = MyModel.objects.get(...)
    return redirect(object)

传递一个视图的名称
def my_view(request):
    ...
    return redirect("some-view-name", foo="bar")　

传递要重定向到的一个具体的路径
def my_view(request):
    ...
    return redirect("/some/url/")

当然也可以是一个完整的网址
def my_view(request):
    ...
    return redirect("www.baidu.com")

默认情况下, redirect()返回一个临时重定向. 以上所有的形式都接收一个permanent参数; 如果设置为True, 将返回一个永久的重定向:
def my_view(request):
    ...
    object = MyModel.objects.get(...)
    return redirect(object, permanent=True)


\11. 实操案例: 查看 mysite工程和 s4day64mysite工程








\12. Django模版语言引擎中的特殊标记（一）
    login.html
        {{name}}

    def login(request):
        return render(request,'login.html',{'name': 'alex'})

def index(request):
    # return HttpResponse('Index')
    return render(
        request,
        'index.html',
        {
            'name': 'alex',
            'users':['李志','李杰'],
            'user_dict':{'k1': 'v1','k2':'v2'},
            'user_list_dict': [
                {'id':1, 'name': 'alex', 'email': 'alex3714@163.com'},
                {'id':2, 'name': 'alex2', 'email': 'alex3714@1632.com'},
                {'id':3, 'name': 'alex3', 'email': 'alex3713@1632.com'},
            ]
        }
    )
'''
<body>
    <h1>模板标记学习</h1>
    <p>{{ name }}</p>
    <p>{{ users.0 }}</p>
    <p>{{ users.1 }}</p>
    <p>{{ user_dict.k1 }}</p>
    <p>{{ user_dict.k2 }}</p>
    <h3>循环</h3>
    <ul>
        {% for item in users %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
    <h3>循环</h3>
    <table border="1">
        {% for row in user_list_dict %}
            <tr>
                <td>{{ row.id }}</td>
                <td>{{ row.name }}</td>
                <td>{{ row.email }}</td>
                <td>
                    <a>编辑</a> | <a href="/del/?nid={{ row.id }}">删除</a>
                </td>
            </tr>
        {% endfor %}
    </table>
</body>
'''


\13. 作业
    django + pymysql实现
        - 用户登陆
        - 查看用户列表