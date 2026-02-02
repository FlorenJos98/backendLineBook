from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, LibroViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet, basename='autor')
router.register(r'libros', LibroViewSet, basename= 'libro')

urlpatterns = [
path('', include(router.urls)),
]