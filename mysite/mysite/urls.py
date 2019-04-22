from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #path('mysite', views.index, name = 'mysite' ),
    #path('success', views.success, name = 'success'), 
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)