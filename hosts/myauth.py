#_*_coding:utf-8_*_
__author__ = 'YiChen Wang'
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import django


class UserManager(BaseUserManager):
    """基于django的自定义认证系统
    createsuperuser 调用的这个基类,这里我们自定义如何创建用户

    Attributes:
        user:创建用户时必要信息
    """

    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        自己写创建用户方法
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            #token=token,
            #department=department,
            #tel=tel,
            #memo=memo,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name ,password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        创建超级用户
        """
        user = self.create_user(email,
            password=password,
            name=name,
            #token=token,
            #department=department,
            #tel=tel,
            #memo=memo,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    name = models.CharField(u'名字:', max_length=32)
    token = models.CharField(u'token', max_length=128,default=None,blank=True,null=True)
    department = models.CharField(u'部门', max_length=32,default=None,blank=True,null=True)
    #business_unit = models.ManyToManyField(BusinessUnit)
    tel = models.CharField(u'座机', max_length=32,default=None,blank=True,null=True)
    mobile = models.CharField(u'手机', max_length=32,default=None,blank=True,null=True)

    memo = models.TextField(u'备注', blank=True,null=True,default=None)
    date_joined = models.DateTimeField(blank=True, auto_now_add=True)
    #valid_begin = models.DateTimeField(blank=True, auto_now=True)
    valid_begin_time = models.DateTimeField(default=django.utils.timezone.now)
    valid_end_time = models.DateTimeField(null=True)

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['name','token','department','tel','mobile','memo']
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_perms(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = u"用户信息"
    def __unicode__(self):
        return self.name

    objects = UserManager()
    """实例化我们自定义的认证类,方便createsuperuser 调用我们的自定义认证系统"""