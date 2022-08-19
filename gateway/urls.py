from django.urls import path, include
from gateway import views

urlpatterns = [
    path('login', views.LoginView.as_view()),
    path('register', views.RegisterView.as_view()),
    path('refresh', views.RefreshView.as_view()),
    path('secure-info', views.GetSecuredInfo.as_view()),
    path('test-exception', views.TestExpection.as_view()),
]
