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
from django.conf.urls import url
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
    4. 每个正则表达式前面的'r' 是可选的但是建议加上。


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
上面的示例使用简单的正则表达式分组匹配（通过圆括号）来捕获URL中的值并以 位置参数形式传递给视图函数。
在更高级的用法中，可以使用 分组命名 匹配的正则表达式组来捕获URL中的值并以 关键字参数形式传递给视图函数。
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
这个实现与前面的示例完全相同，只有一个细微的差别：捕获的值作为关键字参数而不是位置参数传递给视图函数。
例如，针对url /articles/2017/12/相当于按以下方式调用视图函数:
views.month_archive(request, year="2017", month="12")

在实际应用中，使用分组命名匹配的方式可以让你的URLconf 更加明晰且不容易产生参数顺序问题的错误，但是有些开发人员则认为分组命名组语法太丑陋、繁琐。
至于究竟应该使用哪一种，你可以根据自己的喜好来决定。

\URLconf匹配的位置
URLconf 在请求的URL 上查找，将它当做一个普通的Python 字符串。不包括GET和POST参数以及域名。
例如，http://www.example.com/myapp/ 请求中，URLconf 将查找myapp/。
在http://www.example.com/myapp/?page=3 请求中，URLconf 仍将查找myapp/。
URLconf 不检查请求的方法。换句话讲，所有的请求方法 —— 同一个URL的POST、GET、HEAD等等 —— 都将路由到相同的函数。

\捕获的参数永远都是字符串
每个在URLconf中捕获的参数都作为一个普通的Python字符串传递给视图，无论正则表达式使用的是什么匹配方式。例如，下面这行URLconf 中：
url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
传递到视图函数views.year_archive() 中的year 参数永远是一个字符串类型。