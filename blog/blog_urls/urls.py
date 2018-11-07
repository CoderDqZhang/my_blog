from django.conf.urls import url, include
from rest_framework import routers
from blog.blog_view import account,blog,h5_blog

router = routers.DefaultRouter()
router.register(r'users', account.UserViewSet)
router.register(r'groups', account.GroupViewSet)

urlpatterns = [
    url(r'^list/$', h5_blog.homeView),
    url(r'^detail/$',h5_blog.detailView),
    url(r'^about/$',h5_blog.about),

    url(r'^onetest/',h5_blog.testView),

    # url('test',h5_blog.test),
]