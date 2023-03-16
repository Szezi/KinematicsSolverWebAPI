from rest_framework import serializers
from .models import Project, Robot, ForwardKinematics, InverseKinematics


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = '__all__'


class FkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForwardKinematics
        fields = '__all__'


class IkSerializer(serializers.ModelSerializer):
    class Meta:
        model = InverseKinematics
        fields = '__all__'


class ProjectRobotsSerializer(serializers.ModelSerializer):
    robots = RobotSerializer(many=True)

    class Meta:
        model = Project
        fields = ['name', 'admin', 'description', 'members', 'created', 'robots']


class RobotsCalculationsSerializer(serializers.ModelSerializer):
    fk_calc = FkSerializer()
    ik_calc = IkSerializer()

    class Meta:
        model = Robot
        fields = ['name', 'owner', 'description', 'notes', 'created', 'fk_calc', 'ik_calc']
