"""koi1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""



from data.views import DataView
from gallary.views import GallaryView
from myJob.views import MyJobView
from notice.views import NoticeView
from qna.views import QnaView
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index', name="index"),
    url(r'^data/$', DataView.as_view()), 
    url(r'^gallary/$', GallaryView.as_view()), 
    url(r'^myJob/$', MyJobView.as_view()), 
    url(r'^notice/$', NoticeView.as_view()), 
    url(r'^qna/$', QnaView.as_view()), 

# 
#     url(r'^/data/write/$', 'data.views.write', name="write"),
#     url(r'^/gallary/write/$', 'gallary.views.write', name="write"),
#     url(r'^/myjob/write/$', 'myjob.views.write', name="write"),
#     url(r'^/notice/$', 'notice.views.write', name="write"),
#     url(r'^/qna/write/$', 'qna.views.write', name="write"),
# 
#     url(r'^/data/(?P<data_id>\d+)$', 'data.views.view', name="data_view"),
#     url(r'^/gallary/(?P<gallary_id>\d+)$', 'gallary.views.view', name="gallary_view"),
#     url(r'^/myjob/(?P<myjob_id>\d+)$', 'myjob.views.view', name="myjob_view"),
#     url(r'^/notice/(?P<notice_id>\d+)$', 'notice.views.view', name="notice_view"),
#     url(r'^/qna/(?P<qna_id>\d+)$', 'qna.views.view', name="qna_view"),
# 
#     url(r'^/data/delete/(?P<data_id>\d+)$', 'data.views.delete', name="data_delete"),
#     url(r'^/gallary/delete/(?P<gallary_id>\d+)$', 'gallary.views.delete', name="gallary_delete"),
#     url(r'^/myjob/delete/(?P<myjob_id>\d+)$', 'myjob.views.delete', name="myjob_delete"),
#     url(r'^/notice/delete/(?P<notice_id>\d+)$', 'notice.views.delete', name="notice_delete"),
#     url(r'^/qna/delete/(?P<qna_id>\d+)$', 'qna.views.delete', name="qna_delete"),
]
