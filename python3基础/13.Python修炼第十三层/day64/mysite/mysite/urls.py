"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect

'''
使用 HttpResponse 返回字符串
'''

# def login(request):
#     """
#     处理用户请求，并返回内容
#     :param request: 用户请求相关的所有信息（对象）
#     :return:
#     """
#     return HttpResponse("Hello World")
#
#
# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('login/', login),  # 注意一定要写逗号
# ]


'''
使用 render 渲染的模板文件 并返回返给用户浏览器呈现

'''
# def login(request):
#     """
#     处理用户请求，并返回内容
#     :param request: 用户请求相关的所有信息（对象）
#     :return:
#     """
#     # 字符串
#     # return HttpResponse('<input type="text"/>')
#     # return HttpResponse('login.heml')
#     return render(request,'login.html')
#
# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('login/', login),  # 注意一定要写逗号
# ]

'''
使用 form 表单的 action 重定向
使用 redirect 重定向访问位置
使用 render  往模版中传入数据、渲染被替换完参数的模版 返回给用户
'''
def login(request):
    """
    处理用户请求，并返回内容
    :param request: 用户请求相关的所有信息（对象）
    :return:
    """
    # 字符串
    # return HttpResponse('<input type="text"/>')
    # return HttpResponse('login.heml')
    if request.method == "GET":  # 获取用户的提交方式
        return render(request,'login.html') # 当以GET提交时给用户返回登陆页
    else:
        print(request.POST)  # 当用户输入完用户名密码后提交时 form 表单中的action又让跳转到了 /login/ 此时是post请求
        # 获取用户以POST方式提交的数据（请求体）
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if u == 'root' and p == '123123':
            # 登陆成功
            return redirect('http://www.baidu.com')
        else:
            # 登陆失败
            return render(request,'login.html',{'msg':'用户名或密码输入错误，请重试！'})  # msg 将替换html中的 msg

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
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login ),
    url('^login/',login),
    path('index/',index),
]