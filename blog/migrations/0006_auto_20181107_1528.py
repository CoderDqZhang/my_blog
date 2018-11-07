# Generated by Django 2.1.2 on 2018-11-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181107_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='abposition',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='职位'),
        ),
        migrations.AddField(
            model_name='account',
            name='abtext',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='image/list.png', max_length=200, null=True, upload_to='media/blog_list/%Y/%m', verbose_name='展示图片'),
        ),
    ]