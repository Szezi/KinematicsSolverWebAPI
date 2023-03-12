from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import apiOverview, UserDetailAPIView, UserUpdateAPIView, RegisterUserAPIView

urlpatterns = [
    path('', apiOverview, name="api-overview"),
    # path("login", .as_view(), name='login'),
    # path("logout", .as_view(), name='logout'),
    path('register', RegisterUserAPIView.as_view(), name='register'),
    path("detail/<int:pk>", UserDetailAPIView.as_view(), name='detail'),
    path("update/<int:pk>", UserUpdateAPIView.as_view(), name='update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)