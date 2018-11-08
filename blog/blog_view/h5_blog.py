from django.http import JsonResponse
from django.shortcuts import render
import json
from blog.blog_model.blog import Blog, Category, Tag, Comment, DataGroup
from blog.blog_model.account import Account
import markdown
#导入Paginator,EmptyPage和PageNotAnInteger模块
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def about(request, *args, **kwargs):
    return render(request, 'blog_temp/about.html',{'user': get_user_info(),
                                                   'categary_list': get_categary_data(),})

def homeView(request, page = 1, categary=0, data_group= "", tag_id = 0, *args, **kwargs):

    if request.GET.get('categary') != None:
        blog_list = Blog.objects.filter(category__id =request.GET.get('categary')).order_by('pub')
        categary = int(request.GET.get('categary'))
    #TO Do
    elif request.GET.get('data_group') != None:
        blog_list = Blog.objects.filter(id=request.GET.get('data_group')).order_by('pub')
        data_group = str(request.GET.get('data_group'))
    elif request.GET.get('tag_id') != None:
        tag_id = int(request.GET.get('tag_id'))
        blog_list = Blog.objects.filter(tag__id=request.GET.get('tag_id')).order_by('pub')
    else:
        blog_list = Blog.objects.all().order_by('pub')

    click_blog_list = Blog.objects.all().order_by('read_number')#点击数排行
    recommond_list = Blog.objects.all().filter(recommend=True)#站长推荐文章列表

    for blog in blog_list:
        print(blog.image)

    paginator = Paginator(blog_list, 2)
    #分页控制

    if request.GET.get('page') != None:
        page = int(request.GET.get('page'))
    #当前分页
    try:
        blog_list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        blog_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    if blog_list.__len__() == 0:
        page = 0

    return render(request, 'blog_temp/home.html', {'blog_list': blog_list,
                                              'categary_id': int(categary),
                                              'tag_id': int(tag_id),
                                              'page':int(page),
                                              'paginator':paginator,
                                              'data_group': str(data_group),
                                              'categary_list': get_categary_data(),
                                              'data_group_list': get_data_group_data(),
                                              'tag_list': get_tag_data(),
                                              'user': get_user_info(),
                                              'click_blog_list':click_blog_list,
                                              'recommond_list':recommond_list})


def detailView(request, blog_id = 0, *args, **kwargs):
    print(request.GET.get('blog_id'))
    blog = Blog.objects.get(id=request.GET.get('blog_id'))
    #增加阅读数量
    blog.increate_readnum()
    blog.content = markdown.markdown(blog.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    blog_nex_pre_data = has_nex_pre(request.GET.get('blog_id'))
    return render(request, 'blog/../../templates/blog_temp/detail.html', {'blog': blog, 'blog_nex_pre_data': blog_nex_pre_data,
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
    return render(request, 'blog_temp/index.html', {'blog': blog, 'blog_content': blog_content})


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
