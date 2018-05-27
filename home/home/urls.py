"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from . import views
from . import auth_views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^matrices', views.matrices, name='matrices'),
    url(r'^matrix', views.matrix, name='matrix'),
    url(r'^arvores', views.arvores, name='arvores'),
    url(r'^adjacentMatrix', views.adjacentMatrix, name='adjacentMatrix'),
    url(r'^admin/', admin.site.urls),

    url(r'^tablesnames/$',views.getTablesNames),
    url(r'^tables/(?P<name>[a-zA-Z0-9]+)/names/$',views.tNames),
    url(r'^tables/(?P<name>[a-zA-Z0-9]+)/table/$',views.tTables),
    url(r'^tables/(?P<name>[a-zA-Z0-9]+)/csv/$',views.tCSV),
    url(r'^accounts/login/$', auth_views.loginView),
    url(r'^accounts/login_verify/$', auth_views.loginVerify, name='login'),

    url(r'^accounts/create_table/$', login_required(auth_views.createTable), name='create_table'),
    url(r'^accounts/table_validate/$', login_required(auth_views.table_validate), name='table_validate'),
    url(r'^accounts/login_error/$', auth_views.LoginError.as_view(), name='login_error')
]

