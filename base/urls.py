
from django.conf.urls import url

from . import views


app_name = 'base'

urlpatterns = [

    url(r'^$', views.ListViewBase.as_view(), name='base'),


 ]





