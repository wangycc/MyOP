from django.conf.urls import patterns, include, url
from django.contrib import admin
from hosts import urls as host_url
from hosts import views


urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^$',views.index,name='index'),
        url(r'^login/',views.access_login,name='login'),
        url(r'^logout/',views.access_logout,name='logout'),

        url(r'^hosts/',include(host_url)),
        url(r'^cmdb/',views.cmdb_index,name="cmdb"),
        url(r'^release/',views.release_index,name="release"),
        url(r'^monitor/',views.monitor_index,name="monitor"),
        url(r'^dashboard/',views.dashboard_index,name='dashboard'),
    #url(r'^hosts/',views.hosts_index,name='hosts'),
  ]