# Generated by Django 4.1.7 on 2023-03-07 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Project', max_length=50)),
                ('description', models.CharField(blank=True, default='Project description', max_length=250, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ManyToManyField(related_name='admin', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New robot', max_length=50)),
                ('description', models.CharField(blank=True, default='Robot description', max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('link1', models.IntegerField(blank=True, default=118, null=True)),
                ('link2', models.IntegerField(blank=True, default=150, null=True)),
                ('link3', models.IntegerField(blank=True, default=150, null=True)),
                ('link4', models.IntegerField(blank=True, default=0, null=True)),
                ('link5', models.IntegerField(blank=True, default=54, null=True)),
                ('link1_min', models.IntegerField(blank=True, default=-80, null=True)),
                ('link2_min', models.IntegerField(blank=True, default=5, null=True)),
                ('link3_min', models.IntegerField(blank=True, default=-115, null=True)),
                ('link4_min', models.IntegerField(blank=True, default=-85, null=True)),
                ('link5_min', models.IntegerField(blank=True, default=0, null=True)),
                ('link1_max', models.IntegerField(blank=True, default=80, null=True)),
                ('link2_max', models.IntegerField(blank=True, default=175, null=True)),
                ('link3_max', models.IntegerField(blank=True, default=55, null=True)),
                ('link4_max', models.IntegerField(blank=True, default=85, null=True)),
                ('link5_max', models.IntegerField(blank=True, default=0, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robot.project')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='InverseKinematics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='IK Calculation', max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(blank=True, default='2023-12-12 12:12', null=True)),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
                ('x', models.IntegerField(blank=True, default=0, null=True)),
                ('y', models.IntegerField(blank=True, default=0, null=True)),
                ('z', models.IntegerField(blank=True, default=0, null=True)),
                ('alpha', models.IntegerField(blank=True, default=0, null=True)),
                ('theta1', models.IntegerField(blank=True, default=0, null=True)),
                ('theta2', models.IntegerField(blank=True, default=0, null=True)),
                ('theta3', models.IntegerField(blank=True, default=0, null=True)),
                ('theta4', models.IntegerField(blank=True, default=0, null=True)),
                ('theta11', models.IntegerField(blank=True, default=0, null=True)),
                ('theta22', models.IntegerField(blank=True, default=0, null=True)),
                ('theta33', models.IntegerField(blank=True, default=0, null=True)),
                ('theta44', models.IntegerField(blank=True, default=0, null=True)),
                ('Robot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='robot.robot')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ForwardKinematics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='FK Calculation', max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(blank=True, default='2023-12-12 12:12', null=True)),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
                ('theta1', models.FloatField(blank=True, default=0.0, null=True)),
                ('theta2', models.FloatField(blank=True, default=0.0, null=True)),
                ('theta3', models.FloatField(blank=True, default=0.0, null=True)),
                ('theta4', models.FloatField(blank=True, default=0.0, null=True)),
                ('x', models.FloatField(blank=True, default=0.0, null=True)),
                ('y', models.FloatField(blank=True, default=0.0, null=True)),
                ('z', models.FloatField(blank=True, default=0.0, null=True)),
                ('alpha', models.FloatField(blank=True, default=0.0, null=True)),
                ('Robot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='robot.robot')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
