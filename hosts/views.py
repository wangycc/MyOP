#_*_coding:utf-8_*_
__author__ = 'YiChen Wang'
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import models
# Create your views here.

@login_required
def index(request):

 #   return HttpResponse('ok')
    return render(request,'index.html')
    #return render_to_response("index.html", locals(),context_instance=RequestContext(request))

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

def hosts_mgr(request):
    select_id = request.GET.get('select_id')
    if select_id:
        host_list = models.BindHostToUser.objects.filter(host_groups__id=select_id)
    else:
        host_list = request.user.bind_hosts.select_related()
    print(host_list)
    print('hahah')
    return render(request,"hosts/host_mgr.html",{'host_list':host_list})

def multi_cmd(request):

    return render(request,"hosts/multi_cmd.html")
