from django.db import models

class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100) 
    age = models.IntegerField()
    
class TeacherModel(models.Model):
    id=models.CharField(max_length=10,null=False,primary_key=True)
    subject=models.CharField(max_length=100,null=True)
    department=models.CharField(max_length=100,null=True)
    
    
class StudentModel(models.Model):
    id=models.CharField(max_length=10,null=False,primary_key=True)
    course=models.CharField(max_length=100,null=True)
    semester=models.CharField(max_length=100,null=True)

    
class LeaveModel(models.Model):
    student=models.CharField(max_length=50,null=True)
    teacher=models.CharField(max_length=50,null=True)
    message=models.CharField(max_length=300,null=True)
    verifystatus=models.CharField(max_length=50,null=True)
    