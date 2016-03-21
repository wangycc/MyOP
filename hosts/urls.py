#Author: Wang YiChen
#coding=utf-8
from django.conf.urls import patterns,include,url
from hosts import views

urlpatterns = patterns('',
    url(r'^$',views.hosts_index,name='hosts'),
    url(r'^hosts_mgr/',views.hosts_mgr,name='hosts_mgr'),
    url(r'^multi_cmd/',views.multi_cmd,name='multi_cmd'),
)
