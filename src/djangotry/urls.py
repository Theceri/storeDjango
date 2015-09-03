"""djangotry URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .views import PSitemap

sitemaps = {
    'static': PSitemap,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', 'products.views.home', name='home'),
    url(r'^contact/', 'sitepages.views.contact', name='contact'),
    url(r'^services/', 'sitepages.views.services', name='services'),
    url(r'^about/', 'sitepages.views.about', name='about'),
    url(r'^update/(\w+)/', 'products.views.productEdit', name='update'),
    url(r'^view/(?P<name>[\w|\W]+)/(?P<id>\d+)/$', 'products.views.productView', name='view'),
    url(r'^$', 'products.views.products',  name='products'),
    url(r'^search2/', include('haystack.urls')),
    url(r'^search/', 'products.views.search',  name='search'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    	name='django.contrib.sitemaps.views.sitemap')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
