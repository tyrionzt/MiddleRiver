from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^list/$', ListView.as_view(), name='item_list'),

    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item_detail'),

    url(r'^photo/(?P<pk>\d+)/$', PhotoDetailView.as_view(), name='photo_detail')
]