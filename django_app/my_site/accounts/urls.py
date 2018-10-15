from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$',  views.index, name='index'),
    url(r'^list/$', views.list_accounts, name='list'),
    url(r'^add/$', views.create_account, name='create')
]