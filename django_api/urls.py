from django.contrib import admin
from django.urls import path, include
from test_app.views import SimpleView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/', SimpleView.as_view())
]
