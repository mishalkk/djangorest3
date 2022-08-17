from django.db import models
from user.models import CustomUser


class Jwt(models.Model):
    # When user can login multiple times while keeping old token
    # user = models.ForeignKey(CustomUser, related_name="login_user", on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, related_name="login_user", on_delete=models.CASCADE)
    access = models.TextField()
    refresh = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



