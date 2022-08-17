import random
import string
import jwt
from gateway.models import Jwt
from user.models import CustomUser
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework.views import APIView
from gateway.serializers import LoginSerializer, RegisterSerializer, RefreshSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status


def get_random(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def get_access_token(payload):
    return jwt.encode(
        {"exp": datetime.now() + timedelta(minutes=5), **payload},
        settings.SECRET_KEY,
        algorithm="HS256"
    )


def get_refresh_token():
    return jwt.encode(
        {"exp": datetime.now() + timedelta(days=7), "data": get_random(10)},
        settings.SECRET_KEY,
        algorithm="HS256"
    )


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response({"error": "invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

        # remove already existing token for a user
        Jwt.objects.filter(user_id=user.id).delete()

        access = get_access_token({"user_id": user.id})
        refresh = get_refresh_token()

        Jwt.objects.create(
            user_id=user.id,
            access=access,
            refresh=refresh,
        )

        return Response({"access": access, "refresh": refresh})


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        CustomUser.objects.create_user(**serializer.validated_data)

        return Response({"Success": "User created"})


def verify_token(token):
    # decode token
    try:
        decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
    except Exception:
        return None

    # check if token has expired
    exp = decoded_data['exp']

    if datetime.now().timestamp() > exp:
        return None

    return decoded_data


class RefreshView(APIView):
    serializer_class = RefreshSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            active_jwt = Jwt.objects.get(refresh=serializer.validated_data['refresh'])

        except Jwt.DoesNotExist:
            return Response({"error": "refresh token not found"}, status=status.HTTP_400_BAD_REQUEST)

        if not verify_token(serializer.validated_data['refresh']):
            return Response({"error": "Token is invalid or has expired"})

        access = get_access_token({"user_id": active_jwt.user.id})
        refresh = get_refresh_token()

        active_jwt.access = access
        active_jwt.refresh = refresh

        active_jwt.save()

        return Response({"access": access, "refresh": refresh})
