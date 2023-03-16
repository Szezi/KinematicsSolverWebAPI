from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import robotOverview, ProjectListAPIView, ProjectUpdateAPIView, ProjectDestroyAPIView, ProjectDetailAPIView, ProjectCreateAPIView,RobotListAPIView, RobotCreateAPIView, RobotDestroyAPIView, RobotDetailAPIView, RobotUpdateAPIView, FkCreateAPIView, FkDetailAPIView, IkCreateAPIView, IkDetailAPIView

urlpatterns = [
    path('', robotOverview, name="robot-overview"),
    path('project-list/', ProjectListAPIView.as_view(), name='project-list'),
    path('project-create/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('project-detail/<int:pk>', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('project-update/<int:pk>', ProjectUpdateAPIView.as_view(), name='project-update'),
    path('project-delete/<int:pk>', ProjectDestroyAPIView.as_view(), name='project-delete'),

    path('robot-list/', RobotListAPIView.as_view(), name='robot-list'),
    path('robot-create/', RobotCreateAPIView.as_view(), name='robot-create'),
    path('robot-detail/<int:pk>', RobotDetailAPIView.as_view(), name='robot-detail'),
    path('robot-update/<int:pk>', RobotUpdateAPIView.as_view(), name='robot-update'),
    path('robot-delete/<int:pk>', RobotDestroyAPIView.as_view(), name='robot-delete'),

    path('fk-create/', FkCreateAPIView.as_view(), name='fk-create'),
    path('fk-detail/<int:pk>', FkDetailAPIView.as_view(), name='fk-detail'),

    path('ik-create/', IkCreateAPIView.as_view(), name='ik-create'),
    path('ik-detail/<int:pk>', IkDetailAPIView.as_view(), name='ik-detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)