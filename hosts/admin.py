#coding:utf-8
from django.contrib import admin
import models
import auth_admin
# Register your models here.

class HostAdmin(admin.ModelAdmin):
    list_display = ('hostname','ip_addr','port','idc','system_type','date','enabled')
    search_fields = ('hostname','ip_addr')
    list_filter = ('idc','system_type','port')
    list_editable = ('enabled','port')
    fieldsets = (('可管理的主机',{'fields':('hostname','ip_addr','port','idc','system_type')}),
                 ('Permissions', {'fields': ('enabled','memo')}),
                 )


class HostUserAdmin(admin.ModelAdmin):
    list_display = ('username','auth_type')

class BindHostToUserAdmin(admin.ModelAdmin):
    list_display = ('host','host_user','get_groups',)

admin.site.register(models.UserProfile,auth_admin.UserProfileAdmin)
admin.site.register(models.HostGroup)
admin.site.register(models.IDC)
admin.site.register(models.Host,HostAdmin)
admin.site.register(models.BindHostToUser,BindHostToUserAdmin)
admin.site.register(models.HostUser,HostUserAdmin)