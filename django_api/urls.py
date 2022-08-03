from django.contrib import admin
from django.urls import path, include
from test_app.views import SimpleGenerics, SimpleGenericsUpdate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/', SimpleGenerics.as_view()),
    path('simple/<int:id>', SimpleGenericsUpdate.as_view()),
]
