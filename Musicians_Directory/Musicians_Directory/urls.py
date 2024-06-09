
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('album/', include('album.urls')),
    path('musician/', include('musician.urls')),
    path('', views.home, name="home"),   
]
