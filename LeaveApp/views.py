from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm,TeacherDetails,StudentDetails,ReasonForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import UserProfile,TeacherModel,StudentModel,LeaveModel
import json
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request,"home.html") 

def about(request):
    return render(request,"about.html") 

def contact(request):
    return render(request,"contact.html") 


def signup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('loginuser')
    else:
        form=SignUpForm()
    return render(request,"register.html",{'form':form})



def loginuser(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            authuser = form.user
            request.session['user'] = authuser.id
            if authuser.user_type == 'teacher':
                return redirect('dashboard')  
            elif authuser.user_type== 'student':
                return redirect('dashboard')
                
                           
        return render(request,'login.html',{'form':form,'error':'some error occured'})
    else:
        form=LoginForm()
        return render(request,"login.html",{'form':form}) 
    
    
    
def dashboard(request):
    user_id = request.session.get('user')

    if user_id:
        try:
            authuser = UserProfile.objects.get(id=user_id)
            user_type = authuser.user_type

            if user_type == 'teacher':
                try:
                    teacherdetails = TeacherModel.objects.get(id=user_id)
                    messageslist = LeaveModel.objects.filter(teacher=user_id)

                    if request.method == 'POST':
                        form = TeacherDetails(request.POST, instance=teacherdetails)
                        if form.is_valid():
                            form.save()
                            return redirect('/dashboard')
                    else:
                        form = TeacherDetails(instance=teacherdetails)
                        return render(request, "teacher.html", {'authuser': authuser, 'form': form, 'teacherdetails': teacherdetails, 'messageslist': messageslist})
                except TeacherModel.DoesNotExist:
                    if request.method == 'POST':
                        form = TeacherDetails(request.POST)
                        if form.is_valid():
                            teacher = form.save(commit=False)
                            teacher.id = user_id
                            teacher.save()
                            return redirect('/dashboard')
                    else:
                        form = TeacherDetails()
                        return render(request, "teacher.html", {'authuser': authuser, 'form': form})

            elif user_type == 'student':
                try:
                    studentdetails = StudentModel.objects.get(id=user_id)
                    teacherslist = UserProfile.objects.filter(user_type='teacher')
                    messageslist = LeaveModel.objects.filter(student=authuser.name)

                    if request.method == 'POST':
                        form = StudentDetails(request.POST, instance=studentdetails)
                        if form.is_valid():
                            form.save()
                            return render(request, "student.html", {'authuser': authuser, 'form': form, 'studentdetails': studentdetails, 'teacherslist': teacherslist, 'messageslist': messageslist})
                    else:
                        form = StudentDetails(instance=studentdetails)
                        return render(request, "student.html", {'authuser': authuser, 'form': form, 'studentdetails': studentdetails, 'teacherslist': teacherslist, 'messageslist': messageslist})
                except StudentModel.DoesNotExist:
                    teacherslist = UserProfile.objects.filter(user_type='teacher')
                    if request.method == 'POST':
                        form = StudentDetails(request.POST)
                        if form.is_valid():
                            student = form.save(commit=False)
                            student.id = user_id
                            student.save()
                        return render(request, "student.html", {'authuser': authuser, 'form': form, 'teacherslist': teacherslist})
                    else:
                        form = StudentDetails()
                        return render(request, "student.html", {'authuser': authuser, 'form': form, 'teacherslist': teacherslist})

        except UserProfile.DoesNotExist as e:
            print(e)
            pass

    messages.error(request, 'Invalid user or not authenticated.')
    return redirect('loginuser')

def postleave(request):
    user_id = request.session.get('user')
    try:
        authuser = UserProfile.objects.get(id=user_id)
        
        if request.method == 'POST':
            form = ReasonForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                message = form.save(commit=False)
                message.student = authuser.name
                message.save()
                return redirect('dashboard')
            
            else:
                print(form.errors)
                return redirect('dashboard')
        else:
            return redirect('dashboard')
    except:
        return redirect("dashboard")
    
    


def Approvemessage(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            message = data.get('message')
            student = data.get('student')
            leave_instance = LeaveModel.objects.get(message=message, student=student)
            leave_instance.verifystatus = 'Approved'
            leave_instance.save()
            return redirect('dashboard')
        except:
            return redirect('dashboard')
    else:
        return redirect('dashboard')
    
def Disapprovemessage(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            message = data.get('message')
            student = data.get('student')
            leave_instance = LeaveModel.objects.get(message=message, student=student)
            leave_instance.verifystatus = 'Rejected'
            leave_instance.save()
            return redirect('dashboard')
        except:
            return redirect('dashboard')
    else:
        return redirect('dashboard')