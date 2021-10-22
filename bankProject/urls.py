from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import authtoken
from rest_framework.routers import DefaultRouter
from core import views
from django.conf.urls.static import static

router = DefaultRouter()
router.register('employee', views.UserViewSet, basename='employees')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns