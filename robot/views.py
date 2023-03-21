from rest_framework import generics, request, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny, IsAuthenticated
from robot.utils import calculate_ik
from .models import Project, Robot, ForwardKinematics, InverseKinematics
from .serializers import ProjectRobotsSerializer, ProjectSerializer, RobotSerializer, FkSerializer, IkSerializer, \
    RobotsCalculationsSerializer, InverseRobotsSerializer


@api_view(['GET'])
def robotOverview(request):
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


class IkCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = InverseKinematics.objects.all()
    serializer_class = IkSerializer


class IkDetailAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = InverseKinematics.objects.all()
    serializer_class = InverseRobotsSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        self.x = int(request.data.get("x"))
        self.y = int(request.data.get("y"))
        self.z = int(request.data.get("z"))
        self.alpha = int(request.data.get("alpha"))
        link1 = int(request.data.get("Robot.link1"))
        link2 = int(request.data.get("Robot.link2"))
        link3 = int(request.data.get("Robot.link3"))
        link4 = int(request.data.get("Robot.link4"))
        link5 = int(request.data.get("Robot.link5"))
        link1_min = int(request.data.get("Robot.link1_min"))
        link2_min = int(request.data.get("Robot.link2_min"))
        link3_min = int(request.data.get("Robot.link3_min"))
        link4_min = int(request.data.get("Robot.link4_min"))
        link5_min = int(request.data.get("Robot.link5_min"))
        link1_max = int(request.data.get("Robot.link1_max"))
        link2_max = int(request.data.get("Robot.link2_max"))
        link3_max = int(request.data.get("Robot.link3_max"))
        link4_max = int(request.data.get("Robot.link4_max"))
        link5_max = int(request.data.get("Robot.link5_max"))
        self.links = {
            "link1": [link1, link1_min, link1_max],
            "link2": [link2, link2_min, link2_max],
            "link3": [link3, link3_min, link3_max],
            "link4": [link4, link4_min, link4_max],
            "link5": [link5, link5_min, link5_max],
        }
        # print(self.links, self.x, self.y, self.y, self.alpha)

        result = calculate_ik(self.links, self.x, self.y, self.z, self.alpha)
        # print(result)

        request.data._mutable = True
        request.data['theta1'] = result[0][0][0]
        request.data['theta2'] = result[0][0][1]
        request.data['theta3'] = result[0][0][2]
        request.data['theta4'] = result[0][0][3]
        request.data['theta11'] = result[1][0][0]
        request.data['theta22'] = result[1][0][1]
        request.data['theta33'] = result[1][0][2]
        request.data['theta44'] = result[1][0][3]
        request.data._mutable = False

        return super(IkDetailAPIView, self).update(request, *args, **kwargs)

