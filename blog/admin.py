from django.contrib import admin
from blog.blog_model.account import Account
from blog.blog_model.blog import Blog,Category,Tag,Comment


# Register your models here.

admin.site.register(Account)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
