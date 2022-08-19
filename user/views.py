from rest_framework.viewsets import ModelViewSet
from user.serializers import CustomUserSerializer, UserProfile, CustomUser, UserProfileSerializer


class CustomUserView(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
