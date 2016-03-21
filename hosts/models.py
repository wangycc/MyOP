from django.db import models
from myauth import UserProfile
# Create your models here.

class Host(models.Model):
    """Host Information"""
    hostname = models.CharField(max_length=64)
    ip_addr = models.GenericIPAddressField(unique=True)
    port = models.IntegerField(default=22)
    idc = models.ForeignKey('IDC')
    system_type_choice = (
        ('linux','Linux'),
        ('windows','Windows'),
    )
    system_type = models.CharField(choices=system_type_choice)
    enabled = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    memo = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return "%s(%s)"%(self.hostname,self.ip_addr)

class IDC(models.Model):
    """IDC"""
    name = models.CharField(max_length=64,unique=True)
    memo = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.name

class HostUser(models.Model):
    """Remote User
        account:
            username
            password
            authentication
    """
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=128,blank=True,null=True)
    auth_type_choice = (
        ('ssh-password','SSH/PASSWORD'),
        ('ssh-key','SSH-KEY'),
    )
    auth_type= models.CharField(max_length=64,choices=auth_type_choice)

    def __unicode__(self):
        return "(%s)%s"%(self.auth_type,self.username)

    class Meta:
        '''
            确保主机账号认证唯一性
        '''
        unique_together = ('auth_type','username','password')

class HostGroup(models.Model):
    """Host Group"""
    name = models.CharField(max_length=64,unique=True)
    memo = models.TextField(blank=True,null=True)

class BindHostToUser(models.Model):
    """绑定主机到用户"""
    host = models.Foreignkey(host)
    host_user = models.ForeignKey(host_user)
    host_groups = models.ManyToManyField(host_groups)

    class Meta:

        unique_together = ('host',)
