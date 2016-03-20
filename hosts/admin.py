from django.contrib import admin
import models
import auth_admin
# Register your models here.

admin.site.register(models.UserProfile,auth_admin.UserProfileAdmin)