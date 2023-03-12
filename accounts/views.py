from django.contrib.auth import login
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User

from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


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


class LoginUserAPIView(generics.GenericAPIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
