# Generated by Django 2.1.2 on 2018-11-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181107_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='image/list.png', max_length=200, null=True, upload_to='blog_list/%Y/%m', verbose_name='展示图片'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=255, verbose_name='标题'),
        ),
    ]
