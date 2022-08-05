from django.contrib import admin
from django.urls import path, include
from test_app.views import Simple
from rest_framework.routers import DefaultRouter
from django.conf import settings

router = DefaultRouter()
router.register("simple-viewset", Simple)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns