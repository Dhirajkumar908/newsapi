from django.urls import path
from news import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home' ),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('News_post', views.News_post, name='News_post'),
    path('add_post',views.add_post,name='add_post'),
    path('show/<str:title>', views.show, name='show')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 
