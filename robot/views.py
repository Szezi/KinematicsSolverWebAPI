import datetime
from django.db.models import Count
from rest_framework import generics, request, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny, IsAuthenticated
from robot.utils import calculate_ik, calculate_fk
from .models import Project, Robot, ForwardKinematics, InverseKinematics
from .serializers import ProjectRobotsSerializer, ProjectSerializer, RobotSerializer, FkSerializer, IkSerializer, \
    RobotsCalculationsSerializer, InverseRobotsSerializer, ForwardRobotsSerializer, DashboardSerializer


@api_view(['GET'])
def robotOverview(request):
    api_urls = {
        'Dashboard': reverse('dashboard', request=request),

        'Project List': reverse('project-list', request=request),
        'Project Detail': 'robot/project-detail/<str:pk>/',
        'Project Create': reverse('project-create', request=request),
        'Project Update': 'robot/project-update/<str:pk>/',
        'Project Delete': 'robot/project-delete/<str:pk>/',

        'Robot List': reverse('robot-list', request=request),
        'Robot Detail': 'robot/robot-detail/<str:pk>/',
        'Robot Create': reverse('robot-create', request=request),
        'Robot Update': 'robot/robot-update/<str:pk>/',
        'Robot Delete': 'robot/robot-delete/<str:pk>/',

        'Forward Kin Create': reverse('fk-create', request=request),
        'Forward Kin Detail&Update': 'robot/fk-detail/<str:pk>/',

        'Inverse Kin Create': reverse('ik-create', request=request),
        'Inverse Kin Detail&Update': 'robot/ik-detail/<str:pk>/',
    }

    return Response(api_urls)


class DashboardAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    # queryset = Robot.objects.all()
    serializer_class = DashboardSerializer

    def get(self, request, *args, **kwargs):
        num_projects = Project.objects.filter(members=self.request.user).count()
        fk_calc = ForwardKinematics.objects.filter(modified_by=self.request.user).count()
        ik_calc = InverseKinematics.objects.filter(modified_by=self.request.user).count()
        project_admin = Project.objects.filter(admin=self.request.user).count()
        last_robot = Robot.objects.all().filter(owner=self.request.user).order_by('-created')[0:1].values()

        data = {
            'num_projects': num_projects,
            'fk_calc': fk_calc,
            'ik_calc': ik_calc,
            'project_admin': project_admin,
            'last_robot': last_robot
        }
        print(data)

        return Response(data, status=status.HTTP_200_OK)


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
        This view should return details of the project
        if user is member of the project.
        """
        user = self.request.user
        queryset = Project.objects.filter(members=user)
        return queryset


class ProjectUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)

    # queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        """
        This view should return update view of the project
        if user is member of the project.
        """
        user = self.request.user
        queryset = Project.objects.filter(admin=user)
        return queryset


class ProjectDestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    # queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)

    def get_queryset(self):
        """
        This view should return delete view of the project
        if user is admin of the project.
        """
        user = self.request.user
        queryset = Project.objects.filter(admin=user)
        return queryset


class RobotListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RobotSerializer

    def get_queryset(self):
        """
        This view should return list of all the robots
        authenticated user if is owner of.
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

    # queryset = Robot.objects.all()
    serializer_class = RobotsCalculationsSerializer

    def get_queryset(self):
        """
        This view should return detail view of the robot
        for the currently authenticated user if is member of robots project.
        """
        user = self.request.user
        queryset = Robot.objects.filter(project__members=user)
        return queryset


class RobotUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)

    # queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        """
        This view should return update view of the robot
        for the currently authenticated user if is member of robots project.
        """
        user = self.request.user
        queryset = Robot.objects.filter(project__members=user)
        return queryset


class RobotDestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    # queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)

    def get_queryset(self):
        """
        This view should return delete view of the robot
        for the currently authenticated user if is owner of that robot.
        """
        user = self.request.user
        queryset = Robot.objects.filter(owner=user)
        return queryset


class FkCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = ForwardKinematics.objects.all()
    serializer_class = FkSerializer


class FkDetailAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)

    # queryset = ForwardKinematics.objects.all()
    serializer_class = FkSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        """
        This view should return detail view of the fk
        for the currently authenticated user IF is member of the fk robots project.
        """
        user = self.request.user
        queryset = ForwardKinematics.objects.filter(Robot__project__members=user)
        return queryset

    def put(self, request, *args, **kwargs):
        robot = Robot.objects.filter(id=request.data.get("Robot"))

        self.theta1 = float(request.data.get("theta1"))
        self.theta2 = float(request.data.get("theta2"))
        self.theta3 = float(request.data.get("theta3"))
        self.theta4 = float(request.data.get("theta4"))

        link1 = robot.values_list('link1', flat=True).get()
        link2 = robot.values_list('link2', flat=True).get()
        link3 = robot.values_list('link3', flat=True).get()
        link4 = robot.values_list('link4', flat=True).get()
        link5 = robot.values_list('link5', flat=True).get()
        link1_min = robot.values_list('link1_min', flat=True).get()
        link2_min = robot.values_list('link2_min', flat=True).get()
        link3_min = robot.values_list('link3_min', flat=True).get()
        link4_min = robot.values_list('link4_min', flat=True).get()
        link5_min = robot.values_list('link5_min', flat=True).get()
        link1_max = robot.values_list('link1_max', flat=True).get()
        link2_max = robot.values_list('link2_max', flat=True).get()
        link3_max = robot.values_list('link3_max', flat=True).get()
        link4_max = robot.values_list('link4_max', flat=True).get()
        link5_max = robot.values_list('link5_max', flat=True).get()
        self.links = {
            "link1": [link1, link1_min, link1_max],
            "link2": [link2, link2_min, link2_max],
            "link3": [link3, link3_min, link3_max],
            "link4": [link4, link4_min, link4_max],
            "link5": [link5, link5_min, link5_max],
        }

        result = calculate_fk(self.links, self.theta1, self.theta2, self.theta3, self.theta4)
        # print(result)
        request.data._mutable = True
        request.data['x'] = float(result[0][1][3][0])
        request.data['y'] = float(result[0][1][3][1])
        request.data['z'] = float(result[0][1][3][2])
        request.data['alpha'] = float(result[0][0])
        request.data['modified'] = datetime.datetime.now()
        request.data['modified_by'] = self.request.user.pk
        request.data._mutable = False

        return super(FkDetailAPIView, self).update(request, *args, **kwargs)


class IkCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = InverseKinematics.objects.all()
    serializer_class = IkSerializer


class IkDetailAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)

    # queryset = InverseKinematics.objects.all()
    serializer_class = IkSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        """
        This view should return detail view of the ik
        for the currently authenticated user IF is member of the ik robots project.
        """
        user = self.request.user
        queryset = InverseKinematics.objects.filter(Robot__project__members=user)
        return queryset

    def put(self, request, *args, **kwargs):
        robot = Robot.objects.filter(id=request.data.get("Robot"))
        self.x = int(request.data.get("x"))
        self.y = int(request.data.get("y"))
        self.z = int(request.data.get("z"))
        self.alpha = int(request.data.get("alpha"))
        link1 = robot.values_list('link1', flat=True).get()
        link2 = robot.values_list('link2', flat=True).get()
        link3 = robot.values_list('link3', flat=True).get()
        link4 = robot.values_list('link4', flat=True).get()
        link5 = robot.values_list('link5', flat=True).get()
        link1_min = robot.values_list('link1_min', flat=True).get()
        link2_min = robot.values_list('link2_min', flat=True).get()
        link3_min = robot.values_list('link3_min', flat=True).get()
        link4_min = robot.values_list('link4_min', flat=True).get()
        link5_min = robot.values_list('link5_min', flat=True).get()
        link1_max = robot.values_list('link1_max', flat=True).get()
        link2_max = robot.values_list('link2_max', flat=True).get()
        link3_max = robot.values_list('link3_max', flat=True).get()
        link4_max = robot.values_list('link4_max', flat=True).get()
        link5_max = robot.values_list('link5_max', flat=True).get()
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
        request.data['modified'] = datetime.datetime.now()
        request.data['modified_by'] = self.request.user.pk
        request.data._mutable = False

        return super(IkDetailAPIView, self).update(request, *args, **kwargs)

