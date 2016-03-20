#_*_coding:utf-8_*_
__author__ = 'YiChen Wang'
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):

 #   return HttpResponse('ok')
    return render(request,'index.html')

@login_required
def cmdb_index(request):
    return render(request,'cmdb/index.html')

@login_required
def release_index(request):
    return render(request,'release/index.html')

@login_required
def monitor_index(request):
    return render(request,'monitor/index.html')

@login_required
def dashboard_index(request):
    return render(request,'dashboard/index.html')

@login_required
def hosts_index(request):
    return render(request,'hosts/index.html')


def access_login(request):
    login_err = ''
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)  ##登陆信息认证
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            login_err = "账户名和密码不匹配,请重新输入"

    return render(request,'login.html',{'login_err':login_err})

def access_logout(request):
    logout(request)

    return HttpResponseRedirect('/')


