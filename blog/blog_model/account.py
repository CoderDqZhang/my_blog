#coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from blog.until import define

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField('用户名', max_length=200)  # 用户名
    openid = models.CharField(max_length=200, primary_key=True)
    avatar = models.ImageField('头像', upload_to="avatar/%Y/%m", default=u"image/default.png", max_length=200, null=True)
    createTime = models.DateField(auto_created=True, auto_now_add=True)
    gender = models.IntegerField('性别', choices=define.GENDER, default=0, null=True)
    phone = models.CharField('电话', max_length=11, default='', null=True)

    class Meta:
        verbose_name="用户"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.nickname