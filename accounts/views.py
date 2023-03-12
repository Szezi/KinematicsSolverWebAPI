from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, RegisterSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Register': 'accounts/register/',
        'Login': 'accounts/login/',
        'Logout': 'accounts/logout/',
        'User Detail': 'accounts/user-detail/<str:pk>/',
        'User Update': 'accounts/user-update/<str:pk>/',
    }

    return Response(api_urls)


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
