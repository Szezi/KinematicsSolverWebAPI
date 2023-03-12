from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Project, Robot, ForwardKinematics, InverseKinematics
from .serializers import ProjectSerializer, RobotSerializer, FkSerializer, IkSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Project List': reverse('project-list', request=request),
        'Project Detail': 'robot/project-detail/<str:pk>/',
        'Project Create': 'robot/project-create/',
        'Project Update': 'robot/project-update/<str:pk>/',
        'Project Delete': 'robot/project-delete/<str:pk>/',

        'Robot List': reverse('robot-list', request=request),
        'Robot Detail': 'robot/robot-detail/<str:pk>/',
        'Robot Create': 'robot/robot-create/',
        'Robot Update': 'robot/robot-update/<str:pk>/',
        'Robot Delete': 'robot/robot-delete/<str:pk>/',

        'Forward Kin Create': 'robot/fk-create/',
        'Forward Kin Detail&Update': 'robot/fk-detail/<str:pk>/',

        'Inverse Kin Create': 'robot/ik-create/',
        'Inverse Kin Detail&Update': 'robot/ik-detail/<str:pk>/',
    }

    return Response(api_urls)


class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreateAPIView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProjectDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


class RobotListAPIView(generics.ListAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class RobotCreateAPIView(generics.CreateAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class RobotDetailAPIView(generics.RetrieveAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class RobotUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class RobotDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


class FkCreateAPIView(generics.CreateAPIView):
    queryset = ForwardKinematics.objects.all()
    serializer_class = FkSerializer


class FkDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = ForwardKinematics.objects.all()
    serializer_class = FkSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class IkCreateAPIView(generics.CreateAPIView):
    queryset = InverseKinematics.objects.all()
    serializer_class = IkSerializer


class IkDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = InverseKinematics.objects.all()
    serializer_class = IkSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
