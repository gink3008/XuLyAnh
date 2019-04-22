from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('profile', views.profile, name = 'profile'), 
    path('mysite', views.index, name = 'mysite' ),
    path('success', views.success, name = 'success'), 
    path('index2', views.index2, name= 'index2')
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
