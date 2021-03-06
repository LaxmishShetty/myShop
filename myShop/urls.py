"""myShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from myShopSales import views as myShopSales_views
from register import views as regViews
from myShop import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', myShopSales_views.index, name='index'),
    url(r'^register$',regViews.register,name='register'),
    url(r'^dashboard$',myShopSales_views.dashboard,name='dashboard'),
    url(r'^login$',regViews.login_page,name='login'),
    url(r'^logout$', regViews.logout_page, name='logout'),

    url(r'^secret/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]