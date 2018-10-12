"""为应用程序users定义URL模式"""
from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^', include('django.contrib.auth.urls')),
    # # 登陆页面
    # url(r'^login/$',LoginView.as_view(),
    #     name='login'),
    # url(r'^logout/$', views.logout_view, name='logout'),
    # # 注册页面
    url(r'^register/$', views.register, name='register')
]

app_name = 'registration'
