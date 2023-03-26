from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import accountsOverview, UserDetailAPIView, UserUpdateAPIView, RegisterUserAPIView, LoginUserAPIView, ChangePasswordAPIView

urlpatterns = [
    path('', accountsOverview, name="accounts-overview"),
    path("login", LoginUserAPIView.as_view(), name='login'),
    path("logout", LogoutView.as_view(next_page='login'), name='logout'),
    path('register', RegisterUserAPIView.as_view(), name='register'),
    path('change-password', ChangePasswordAPIView.as_view(), name='change-password'),
    path("detail", UserDetailAPIView.as_view(), name='detail'),
    path("update", UserUpdateAPIView.as_view(), name='update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)