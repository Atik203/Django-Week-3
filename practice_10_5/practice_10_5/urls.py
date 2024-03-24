
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/', include('first_app.urls')),  
    path('',views.Home, name='home'),
    path("navigation/", include('navigation.urls')),    
]
