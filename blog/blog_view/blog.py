from django.forms.models import model_to_dict
from django.db.models import Q
from django.http import JsonResponse
from blog.blog_model.blog import Blog,Category,Comment,Tag


def test_object_filter(request):

    #__contains查询方式
    #select * from xx where title like BINARY 'ios%';
    contains = Blog.objects.filter(title__contains='io')

    # __icontains查询方式 忽略大小写
    # select * from xx where title like 'ios%';
    icontains = Blog.objects.filter(title__icontains='io')

    #__in查询方式 包含在内
    # select * from xx where title in ('ios','i');
    in_blogs = Blog.objects.get(Q(title__in=['i','ios']))

    iexact_blog = Blog.objects.filter(title__iexact='ios')

    iexact_blog = Blog.objects.exclude(title__iexact='ios').\
        filter(title='ios').aggregate()

    Blog.objects.filter(id__gt='1')

    for blog in iexact_blog:
        print(""+blog.title+":"+str(blog.pub))
    return JsonResponse({'success':0})