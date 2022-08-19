from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gateway/', include("gateway.urls")),
    path('user-main/', include("user.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static is used to make use of statc file like image

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
