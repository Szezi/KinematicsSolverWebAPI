from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Project, Robot, ForwardKinematics, InverseKinematics


class ProjectSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='project-detail',
        lookup_field='pk',
        read_only=True)

    edit_url = serializers.HyperlinkedIdentityField(
        view_name='project-update',
        lookup_field='pk',
        read_only=True)

    delete_url = serializers.HyperlinkedIdentityField(
        view_name='project-delete',
        lookup_field='pk',
        read_only=True)

    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['name', 'description', 'admin', 'members', 'created', 'detail_url', 'edit_url', 'delete_url']


class RobotSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='robot-detail',
        lookup_field='pk',
        read_only=True)

    edit_url = serializers.HyperlinkedIdentityField(
        view_name='robot-update',
        lookup_field='pk',
        read_only=True)

    delete_url = serializers.HyperlinkedIdentityField(
        view_name='robot-delete',
        lookup_field='pk',
        read_only=True)

    class Meta:
        model = Robot
        # fields = '__all__'
        fields = [
            'project',
            'name',
            'description',
            'notes',
            'created',
            'owner',
            'link1',
            'link2',
            'link3',
            'link4',
            'link5',
            'link1_min',
            'link2_min',
            'link3_min',
            'link4_min',
            'link5_min',
            'link1_max',
            'link2_max',
            'link3_max',
            'link4_max',
            'link5_max',
            'detail_url',
            'edit_url',
            'delete_url']


class FkSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='fk-detail',
        lookup_field='pk',
        read_only=True)

    class Meta:
        model = ForwardKinematics
        fields = ['detail_url', 'name', 'notes', 'created', 'modified', 'modified_by', 'x', 'y', 'z', 'alpha', 'theta1', 'theta2',
                  'theta3', 'theta4', 'Robot']


class IkSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='ik-detail',
        lookup_field='pk',
        read_only=True)

    class Meta:
        model = InverseKinematics
        fields = ['detail_url', 'name', 'notes', 'created', 'modified', 'modified_by', 'x', 'y', 'z', 'alpha', 'theta1', 'theta11',
                  'theta2', 'theta22', 'theta3', 'theta33', 'theta4', 'theta44', 'Robot']


class ProjectRobotsSerializer(serializers.ModelSerializer):
    robots = RobotSerializer(many=True)
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='project-detail',
        lookup_field='pk',
        read_only=True)

    edit_url = serializers.HyperlinkedIdentityField(
        view_name='project-update',
        lookup_field='pk',
        read_only=True)

    delete_url = serializers.HyperlinkedIdentityField(
        view_name='project-delete',
        lookup_field='pk',
        read_only=True)

    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['name', 'description', 'admin', 'members', 'created', 'detail_url', 'edit_url', 'delete_url', 'robots']


class RobotsCalculationsSerializer(serializers.ModelSerializer):
    fk_calc = FkSerializer()
    ik_calc = IkSerializer()

    detail_url = serializers.HyperlinkedIdentityField(
        view_name='robot-detail',
        lookup_field='pk',
        read_only=True)

    edit_url = serializers.HyperlinkedIdentityField(
        view_name='robot-update',
        lookup_field='pk',
        read_only=True)

    delete_url = serializers.HyperlinkedIdentityField(
        view_name='robot-delete',
        lookup_field='pk',
        read_only=True)

    class Meta:
        model = Robot
        fields = ['name', 'owner', 'description', 'notes', 'created', 'detail_url', 'edit_url', 'delete_url', 'fk_calc', 'ik_calc']


class InverseRobotsSerializer(serializers.ModelSerializer):
    Robot = RobotSerializer(read_only=False)

    class Meta:
        model = InverseKinematics
        fields = ['name', 'notes', 'created', 'modified', 'modified_by', 'x', 'y', 'z', 'alpha', 'theta1', 'theta11',
                  'theta2', 'theta22', 'theta3', 'theta33', 'theta4', 'theta44', 'Robot']

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


class ForwardRobotsSerializer(serializers.ModelSerializer):
    Robot = RobotSerializer(read_only=False)

    class Meta:
        model = ForwardKinematics
        fields = ['name', 'notes', 'created', 'modified', 'modified_by', 'x', 'y', 'z', 'alpha', 'theta1', 'theta2',
                  'theta3', 'theta4', 'Robot']

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
        return super(ForwardRobotsSerializer, self).update(instance, validated_data)


class DashboardSerializer(serializers.ModelSerializer):
    num_robots = serializers.IntegerField(read_only=True)
    num_projects = serializers.IntegerField(read_only=True)
    num_fk = serializers.IntegerField(read_only=True)
    num_ik = serializers.IntegerField(read_only=True)
    last_robot = serializers.ModelSerializer

    class Meta:
        model = Robot
        fields = ['name', 'num_robots', 'num_projects', 'num_fk', 'num_ik', 'last_robot']
