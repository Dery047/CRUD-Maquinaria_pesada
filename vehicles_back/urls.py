from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("vehicles_app.urls")),  
]


print('Cargando rutas del proyecto...')
