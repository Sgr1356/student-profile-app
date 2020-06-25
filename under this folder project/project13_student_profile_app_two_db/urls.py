"""project13_student_profile_app_two_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app13 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/',views.showstudent),
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('forgetpassword',views.forgetpassword,name="forgetpassword"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),

    path('adminhome/',views.adminhome,name="adminhome"),
    path('allstudentdetails',views.allstudentdetails,name="allstudentdetails"),

    path('studenthome/',views.studenthome,name="studenthome"),
    path('studenviewprofile/',views.studentviewprofile,name="studentviewprofile"),
    path('studentupdateprofile/',views.studentupdateprofile,name="studentupdateprofile"),

    path('register_save/',views.register_save,name="register_save"),
    path('studentlogincheck/',views.studentlogincheck,name="studentlogincheck"),
    path('studentupdate_save/',views.studentupdate_save,name="studentupdate_save"),
    path('forget_showpass/',views.forget_show,name="forget_show"),


    path('logout/',views.logout,name="logout"),
    path('logout_admin/',views.logout_admin,name="logout_admin"),
    path('allstudentdetails_delete/',views.allstudentdetails_delete,name="allstudentdetails_delete"),
    path('adminlogin_check',views.adminlogin_check,name="adminlogin_check")
   ]
