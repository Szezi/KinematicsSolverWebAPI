from rest_framework import generics, request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Project, Robot, ForwardKinematics, InverseKinematics
from .serializers import ProjectRobotsSerializer, ProjectSerializer, RobotSerializer, FkSerializer, IkSerializer, RobotsCalculationsSerializer


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
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    def get_queryset(self):
        """
        This view should return a list of all the projects
        for the currently authenticated user.
        """
        user = self.request.user
        queryset = Project.objects.filter(members=user)
        return queryset


class ProjectCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = ProjectRobotsSerializer

    def get_queryset(self):
        """
        This view should return a list of all the projects
        for the currently authenticated user.
        """
        user = self.request.user
        queryset = Project.objects.all()
        return queryset


class ProjectUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProjectDestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


class RobotListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RobotSerializer

    def get_queryset(self):
        """
        This view should return a list of all the projects
        for the currently authenticated user.
        """
        user = self.request.user
        queryset = Robot.objects.filter(owner=user)
        return queryset


class RobotCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class RobotDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Robot.objects.all()
    serializer_class = RobotsCalculationsSerializer


class RobotUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class RobotDestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


class FkCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = ForwardKinematics.objects.all()
    serializer_class = FkSerializer


class FkDetailAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = ForwardKinematics.objects.all()
    serializer_class = FkSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class IkCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = InverseKinematics.objects.all()
    serializer_class = IkSerializer


class IkDetailAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = InverseKinematics.objects.all()
    serializer_class = IkSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
