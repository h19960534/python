"""定义learning_logs的url模式"""

from django.conf.urls import urls
from . import views

urlpatterns = [
    #主页
    url(r'^$', views.index, name='index'),
]