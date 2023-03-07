from rest_framework import generics

from .models import Project, Robot, ForwardKinematics, InverseKinematics
from .serializers import ProjectSerializer


class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
