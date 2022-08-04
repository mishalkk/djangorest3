from django.contrib import admin
from django.urls import path, include
from test_app.views import Simple
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("simple-viewset", Simple)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
