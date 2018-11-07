#coding=utf-8
from __future__ import unicode_literals
from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.
class Category(models.Model):
    """
    博客分类
    """
    name=models.CharField('名称',max_length=30)
    class Meta:
        verbose_name="类别"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField('名称',max_length=16)

    class Meta:
        verbose_name="标签"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

"""

on_delete:详解

CASCADE:这就是默认的选项，级联删除，你无需显性指定它。
PROTECT: 保护模式，如果采用该选项，删除的时候，会抛出ProtectedError错误。
SET_NULL: 置空模式，删除的时候，外键字段被设置为空，前提就是blank=True, null=True,定义该字段的时候，允许为空。
SET_DEFAULT: 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。
SET(): 自定义一个值，该值当然只能是对应的实体了
"""
class Blog(models.Model):
    title=models.TextField('标题',max_length=266)
    author=models.CharField('作者',max_length=16)
    content=MDTextField()
    read_number = models.PositiveIntegerField('阅读人数',default=0)
    com_number = models.IntegerField('评论人数', default=0)
    pub=models.DateField('发布时间',auto_now_add=True)
    category=models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE)#多对一（博客--类别）
    tag=models.ManyToManyField(Tag,verbose_name='标签')#(多对多）
    class Meta:
        verbose_name="博客"
        verbose_name_plural=verbose_name

    #阅读数量增加
    def increate_readnum(self):
        self.read_number += 1
        self.save(update_fields=['read_number'])

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    blog=models.ForeignKey(Blog,verbose_name='博客',on_delete=models.CASCADE)#(博客--评论:一对多)
    name=models.CharField('称呼',max_length=16)
    email=models.EmailField('邮箱')
    content=models.CharField('内容',max_length=240)
    pub=models.DateField('发布时间',auto_now_add=True)

    class Meta:
        verbose_name="评论"
        verbose_name_plural="评论"
    def __unicode__(self):
        return self.content


class DataGroup(models.Model):
    date_str = models.CharField('年月',max_length=7)
    number = models.IntegerField(default=0)

    class Meta:
        verbose_name="时间分组"
        verbose_name_plural="时间分组"
    def __unicode__(self):
        return self.date_str