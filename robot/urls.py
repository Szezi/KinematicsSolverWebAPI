from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectListAPIView

urlpatterns = [
    path('project-list/', ProjectListAPIView.as_view(), name='project-list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)