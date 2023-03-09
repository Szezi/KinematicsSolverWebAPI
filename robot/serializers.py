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
