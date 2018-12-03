#coding=utf-8
from __future__ import unicode_literals
from django.db import models

class ResumeModel(models.Model):
    title = models.CharField(verbose_name='个人简历',max_length=255)
    resume = models.FileField(verbose_name='简历',upload_to='resume')


    class Meta:
        verbose_name="简历"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.title