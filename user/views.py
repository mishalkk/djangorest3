from rest_framework.viewsets import ModelViewSet
from user.serializers import CustomUserSerializer, UserProfile, CustomUser, UserProfileSerializer


class CustomUserView(ModelViewSet):
    serializer_class = CustomUserSerializer
    # reverse relation
    queryset = CustomUser.objects.prefetch_related("user_profile", "user_profile__address_info")


class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    # forward relation
    queryset = UserProfile.objects.select_related("user", "address_info")

