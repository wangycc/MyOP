from django.contrib import admin
import models
import auth_admin
# Register your models here.

admin.site.register(models.UserProfile,auth_admin.UserProfileAdmin)
admin.site.register(models.HostGroup)
admin.site.register(models.IDC)
admin.site.register(models.Host)
admin.site.register(models.BindHostToUser)
admin.site.register(models.HostUser)