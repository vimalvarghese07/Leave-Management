# Generated by Django 4.2.9 on 2024-02-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeaveApp', '0004_userprofile_delete_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course', models.CharField(max_length=100, null=True)),
                ('semester', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
