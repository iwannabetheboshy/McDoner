from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main, name='main'),
    path('feedback', views.sendFeedBack, name='fb'),
    #path("robots.txt", views.robots_txt),
    
] #+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
