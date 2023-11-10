
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from asosiy.views import *

router = DefaultRouter()
router.register("albomlar", AlbomModelViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Spotify API",
      default_version='v1',
      description="Dars davomida o'rganish uchun yozilgan API'lar to'plami",
      contact=openapi.Contact("Rakhmatullayev Azamjon, gmail= raxmatullayevazamjon025@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qoshiqlar/', QoshiqAPI.as_view()),
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0)),
    path('redoc/', schema_view.with_ui("redoc", cache_timeout=0)),

]
