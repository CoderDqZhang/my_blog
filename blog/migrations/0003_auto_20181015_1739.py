# Generated by Django 2.0.5 on 2018-10-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181015_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='com_number',
            field=models.IntegerField(default=0, verbose_name='评论人数'),
        ),
        migrations.AddField(
            model_name='blog',
            name='read_number',
            field=models.IntegerField(default=0, verbose_name='阅读人数'),
        ),
    ]
