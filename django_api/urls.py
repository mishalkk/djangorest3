from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gateway/', include("gateway.urls")),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns