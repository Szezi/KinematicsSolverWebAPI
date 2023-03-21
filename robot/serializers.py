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


class InverseRobotsSerializer(serializers.ModelSerializer):
    Robot = RobotSerializer(read_only=False)

    class Meta:
        model = InverseKinematics
        fields = ['name', 'notes', 'created', 'modified', 'modified_by', 'x', 'y', 'z', 'alpha', 'theta1', 'theta11', 'theta2', 'theta22', 'theta3', 'theta33', 'theta4', 'theta44', 'Robot']

    def update(self, instance, validated_data):
        # CHANGE "userprofile" here to match your one-to-one field name
        if 'Robot' in validated_data:
            nested_serializer = self.fields['Robot']
            nested_instance = instance.Robot
            nested_data = validated_data.pop('Robot')

            # Runs the update on whatever serializer the nested data belongs to
            nested_serializer.update(nested_instance, nested_data)

        # Runs the original parent update(), since the nested fields were
        # "popped" out of the data
        return super(InverseRobotsSerializer, self).update(instance, validated_data)