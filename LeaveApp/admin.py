from django.contrib import admin
from .models import UserProfile,TeacherModel,StudentModel
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(TeacherModel)
admin.site.register(StudentModel)