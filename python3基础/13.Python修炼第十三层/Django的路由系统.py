Django 1.11版本 URLConf官方文档: https://docs.djangoproject.com/en/1.11/topics/http/urls/#specifying-defaults-for-view-arguments
URL配置(URLconf)就像Django 所支撑网站的目录。它的本质是URL与要为该URL调用的视图函数之间的映射表。
你就是以这种方式告诉Django，对于这个URL调用这段代码，对于那个URL调用那段代码。

\URLconf配置
\1、基本格式：
from django.conf.urls import url
urlpatterns = [
     url(正则表达式, views视图函数，参数，别名),
]
# 注意：Django 2.0版本中的路由系统已经替换成下面的写法（官方文档）:
from django.urls import path

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]

# 参数说明：
    正则表达式: 一个正则表达式字符串
    views视图函数: 一个可调用对象，通常为一个视图函数或一个指定视图函数路径的字符串
    参数: 可选的要传递给视图函数的默认参数（字典形式）
    别名: 一个可选的name参数


\2、基本配置
from django.conf.urls import url # url 是django 2.0兼容django 1.0的写法
from . import views

urlpatterns = [
    url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/([0-9]{4})/$', views.year_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
]

# 注意事项
    1. urlpatterns中的元素按照书写顺序从上往下逐一匹配正则表达式，一旦匹配成功则不再继续。
    2. 若要从URL中捕获一个值，只需要在它周围放置一对圆括号（分组匹配）。
    3. 不需要添加一个前导的反斜杠，因为每个URL 都有。例如，应该是^articles 而不是 ^/articles。
    4. 每个正则表达式前面的'r' 是可选的但是建议加上。原生字符串
    5. 尖号(^)和美元符号($)，都是正则表达式符号，分别表示字符串的开头和结尾。


\补充说明
# 是否开启URL访问地址后面不为/跳转至带有/的路径的配置项
APPEND_SLASH=True
Django settings.py配置文件中默认没有 APPEND_SLASH 这个参数，但 Django 默认这个参数为 APPEND_SLASH = True。 其作用就是自动在网址结尾加'/'。

其效果就是：
我们定义了urls.py：
from django.conf.urls import url
from app01 import views

urlpatterns = [
        url(r'^blog/$', views.blog),
]
访问 http://www.example.com/blog 时，默认将网址自动转换为 http://www.example/com/blog/。
如果在settings.py中设置了 APPEND_SLASH=False，此时我们再请求 http://www.example.com/blog 时就会提示找不到页面。

\分组命名匹配
上面的示例使用简单的正则表达式分组匹配（通过圆括号）来捕获URL中的值并以 位置参数形式传递给视图函数(简单用法位置参数)。
在更高级的用法中，可以使用 分组命名 匹配的正则表达式组来捕获URL中的值并以 关键字参数形式传递给视图函数(高级用法关键字参数)。
在Python的正则表达式中，分组命名正则表达式组的语法是(?P<name>pattern)，其中name是组的名称，pattern是要匹配的模式。
下面是以上URLconf 使用命名组的重写: 
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
]
分组实现与前面的示例完全相同，只有一个细微的差别：捕获的值(year 和 month)作为关键字参数而不是位置参数传递给视图函数。
例如，针对url /articles/2017/12/相当于按以下方式调用视图函数:
views.month_archive(request, year="2017", month="12")

在实际应用中，使用分组命名匹配的方式可以让你的URLconf 更加明晰且不容易产生参数顺序问题的错误，但是有些开发人员则认为分组命名组语法太丑陋、繁琐。
至于究竟应该使用哪一种，你可以根据自己的喜好来决定。

\URLconf匹配的位置
URLconf 在请求的URL上查找，将它当做一个普通的Python字符串。不包括GET和POST参数 以及 域名。
例如: http://www.example.com/myapp/ 请求中，URLconf将查找myapp/。
     在http://www.example.com/myapp/?page=3 请求中，URLconf仍将查找myapp/。
URLconf 不检查请求的方法。换句话讲，所有的请求方法 ——------ 同一个URL的POST、GET、HEAD等等 ——------ 都将路由到相同的函数。

\捕获的参数永远都是字符串
每个在URLconf中捕获的参数都作为一个普通的Python字符串传递给视图，无论正则表达式使用的是什么匹配方式。例如，下面这行URLconf中：
url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
传递到视图函数views.year_archive() 中的 year 参数永远是一个字符串类型。

\视图函数中指定默认值
# urls.py中
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', views.page),
    url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
]

# views.py中，可以为num指定默认值
def page(request, num="1"):
    pass

在上面的例子中，两个URL模式指向相同的 view - views.page - 但是第一个模式并没有从URL中捕获任何东西。
如果第一个模式匹配上了，page()函数将使用其默认参数num=“1”,如果第二个模式匹配，page()将使用正则表达式捕获到的num值。

\include其他的URLconfs
from django.conf.urls import include, url

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^blog/', include('blog.urls')),  # 可以包含其他的URLconfs文件
]

\传递额外的参数给视图函数（了解）
URLconfs 具有一个钩子，让你传递一个Python 字典作为额外的参数传递给视图函数。
django.conf.urls.url() 函数可以接收一个可选的第三个参数，它是一个字典，表示想要传递给视图函数的额外关键字参数。

# 例如
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/(?P<year>[0-9]{4})/$', views.year_archive, {'foo': 'bar'}),
]
在这个例子中，对于/blog/2005/请求，Django 将调用views.year_archive(request, year='2005', foo='bar')。

\命名URL和URL反向解析(别名)
# 可以给我们的URL匹配规则起个名字，这样我们以后就不需要写死URL代码了，只需要通过名字来调用当前的URL。

# 1. 命名 URL
# test.html:
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>测试页面</title>
        </head>
    <body>
        <p>测试页面</p>
        <form action="/test/" method="post">
            <input type="text" name="username" value="">
            <input type="submit" name="提交">
        </form>
        <a href="/json_test/" rel="external nofollow" >json 数据</a> 
    </body>
</html>

# urls.py:
from django.conf.urls import url
from app01 import views
urlpatterns = [
    url(r'^test/', views.test),
    url(r'^json_test/', views.json_test),
]
如果 urls.py 中的 json_test/ 路径发生改变，test.html 中的地址也要改。
可以使用反向 url 解析，给 json_test/ 起一个别名

# urls.py:
from django.conf.urls import url
from app01 import views
urlpatterns = [
    url(r'^test/', views.test),
    url(r'^json_test/', views.json_test, name="json"), # 给该 url 定义别名为 json
]

# test.html:
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>测试页面</title>
    </head>
    <body> 
        <p>测试页面</p> 
        <form action="/test/" method="post">
            <input type="text" name="username" value="">
            <input type="submit" name="提交">
        </form> 
        <a href="{% url 'json' %}" rel="external nofollow" >json 数据</a> 
    </body>
</html>

这时候如果修改 urls.py 中的 json_test/ 路径，就不需要再去修改 test.html


# 2. 反向解析 URL
# 如果需要重定向这样的路径的话，可以在 views.py 中这样写:
from django.shortcuts import render, redirect
from django.urls import reverse 

# json 测试
def json_test(request):
    hobby = ["Music", "Movie", "Basketball", "Reading"]
    from django.http import HttpResponse, JsonResponse
    return JsonResponse(hobby, safe=False) 

def test(request):
    return redirect(reverse("json",args=("xxxx",))) # 通过 json 反向得到路径 json_test/
因为在/test/的函数中重定向到了 json别名，所以当访问：http://127.0.0.1:8000/test/ 就变成访问：http://127.0.0.1:8000/json_test/

# 3. 如果 url 需要传参数的话
# urls.py
from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^test/', views.test),
    url(r'^json_test/(?P<id>[0-9]{2,4})/(?P<title>[a-zA-Z]+)/', views.json_test, name="json"),
]

# test.html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>测试页面</title>
    </head>
    <body>
        <p>测试页面</p>
        <form action="/test/" method="post">
            <input type="text" name="username" value="">
            <input type="submit" name="提交">
        </form>
        <a href="{% url 'json' 12 'abcd' %}" rel="external nofollow" >json 数据</a>
    </body>
</html>

访问：http://127.0.0.1:8000/test/   # 点击 “json数据” 会往后台提交 id：12  title：abcd


# 4. 反向解析需要传参数
# urls.py
from django.conf.urls import url,include
from app01 import views
urlpatterns = [
    url(r'^test/', views.test),
    url(r'^json_test/(?P<id>[0-9]{2,4})/(?P<title>[a-zA-Z]+)/', views.json_test, name="json"),
]

# views.py
from django.shortcuts import HttpResponse, redirect
from django.urls import reverse 

def json_test(request, id, title):
    print("id: ", id)
    print("title: ", title)
    return HttpResponse(id+"----"+title) 

def test(request):
    return redirect(reverse("json", kwargs={"id": 23, "title": "aaaa"}))

访问：http://127.0.0.1:8000/test/  跳转到了：http://127.0.0.1:8000/json_test/23/aaaa/


\命名空间模式
# 即使不同的APP使用相同的URL别名名称，URL的命名空间模式也可以让你唯一反转命名的URL。

# 举个例子：
# project中的urls.py
from django.conf.urls import url, include
urlpatterns = [
    url(r'^app01/', include('app01.urls', namespace='app01')),
    url(r'^app02/', include('app02.urls', namespace='app02')),
]

# app01中的urls.py
from django.conf.urls import url
from app01 import views
 
app_name = 'app01'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail')
]

# app02中的urls.py
from django.conf.urls import url
from app02 import views
 
app_name = 'app02'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail')
]

现在，我的两个app中 url名称重复了，我反转URL的时候就可以通过命名空间的名称得到我当前的URL。
语法: '命名空间名称:URL名称'
# 模板中使用:
{% url 'app01:detail' pk=12 pp=99 %}

# views中的函数中使用
v = reverse('app01:detail', kwargs={'pk':11})
这样即使app中URL的别名命名相同，我也可以反转得到正确的URL了。

