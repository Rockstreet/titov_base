
from django.conf.urls import url

from . import views


app_name = 'base'

urlpatterns = [

    url(r'^$', views.ListViewBase.as_view(), name='base'),

    url(r'^base/(?P<pk>[-\w]+)/$', views.DetailView.as_view(), name='base_item'),

]





