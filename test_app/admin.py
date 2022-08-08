from django.contrib import admin
from test_app.models import Blog, Car

admin.site.register((Blog, Car, ))


