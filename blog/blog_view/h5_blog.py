from django.http import JsonResponse
from django.shortcuts import render
import json
from blog.blog_model.blog import Blog, Category, Tag, Comment, DataGroup
from blog.blog_model.account import Account
import markdown


def homeView(request, categary=0, data_group="", tag_id = 0, *args, **kwargs):
    print(request.GET.get('tag_id'))
    print(request.GET.get('categary'))
    print(request.GET.get('data_group'))
    print(request.GET.get('tag_id'))
    if request.GET.get('categary') != None:
        blog_list = Blog.objects.filter(id=request.GET.get('categary'))
        categary = int(request.GET.get('categary'))
    elif request.GET.get('data_group') != None:
        blog_list = Blog.objects.filter(id=request.GET.get('data_group'))
        data_group = str(request.GET.get('data_group'))
    elif request.GET.get('tag_id') != None:
        tag_id = int(request.GET.get('tag_id'))
        blog_list = Blog.objects.filter(tag__id=request.GET.get('tag_id'))
    else:
        blog_list = Blog.objects.all()
    return render(request, 'blog/home.html', {'blog_list': blog_list,
                                              'categary_id': int(categary),
                                              'tag_id': int(tag_id),
                                              'data_group': str(data_group),
                                              'categary_list': get_categary_data(),
                                              'data_group_list': get_data_group_data(),
                                              'tag_list': get_tag_data(),
                                              'user': get_user_info()})


def detailView(request, blog_id):
    blog = Blog.objects.get(id=request.GET.get('blog_id'))
    blog.content = markdown.markdown(blog.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    blog_nex_pre_data = has_nex_pre(blog_id)
    return render(request, 'blog/detail.html', {'blog': blog, 'blog_nex_pre_data': blog_nex_pre_data,
                                                'categary_id': 0,
                                                'categary_list': get_categary_data(),
                                                'data_group_list': get_data_group_data(),
                                                'tag_list': get_tag_data(),
                                                'user': get_user_info()
                                                })


def testView(request):
    blog = Blog.objects.get(id=2)
    blog_content = markdown.markdown(blog.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.extra'
    ])
    blog.content = blog_content
    return render(request, 'blog/test.html', {'blog': blog, 'blog_content': blog_content})


def test(request):
    return JsonResponse({'success': 'success'})


def get_categary_data():
    return Category.objects.all()


def get_data_group_data():
    return DataGroup.objects.all()


def get_user_info():
    return Account.objects.all().first()


def get_tag_data():
    return Tag.objects.all()


def has_nex_pre(blog_id):
    has_prev = False
    has_next = False
    id_prev = id_next = int(blog_id)
    blog_id_max = Blog.objects.all().order_by('-id').first()
    id_max = blog_id_max.id
    while not has_prev and id_prev >= 1:
        blog_prev = Blog.objects.filter(id=id_prev - 1).first()
        if not blog_prev:
            id_prev -= 1
        else:
            has_prev = True
    while not has_next and id_next <= id_max:
        blog_next = Blog.objects.filter(id=id_next + 1).first()
        if not blog_next:
            id_next += 1
        else:
            has_next = True
    data = {}
    data['blog_prev'] = blog_prev
    data['blog_next'] = blog_next
    data['has_next'] = has_next
    data['has_prev'] = has_prev
    # 将状态码与上下博客传递给前端页面
    return data
