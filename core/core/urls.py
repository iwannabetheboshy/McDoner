from django.contrib import admin
from django.urls import path, include
#from .sitemaps import StaticViewSitemap, DynamicViewSitemap
#from django.contrib.sitemaps.views import sitemap


#sitemaps = {
#    'static': StaticViewSitemap,
#    'dynamic': DynamicViewSitemap
#}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    #path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="django.contrib.sitemaps.views.main"),
]
