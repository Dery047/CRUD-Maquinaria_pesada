from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehiculoViewSet

router = DefaultRouter()
router.register(r"vehiculos", VehiculoViewSet) #main route for the api endpoint

urlpatterns = [
    path("", include(router.urls)),
]

