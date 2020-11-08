"""s4day65 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views  # 导入app01

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 为了方便 路由、模版、视图尽量都使用相同的名称
    url(r'^classes/', views.classes),
    url(r'^add_class/', views.add_class),
    url(r'^del_class/', views.del_class),
    url(r'^edit_class/', views.edit_class),
]
