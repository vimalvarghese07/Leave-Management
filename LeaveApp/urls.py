from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('register/',views.signup,name="signup"),
    path('login/',views.loginuser,name="loginuser"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('postleave/',views.postleave,name="postleave"),
    # path('viewmessage/',views.viewmessage,name="message"),
     path('approvemessage/',views.Approvemessage,name="approvemessage"),
     path('disapprovemessage/',views.Disapprovemessage,name="disapprovemessage"),
    
]
