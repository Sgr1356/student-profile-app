from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from app13.models import studentmodel
from app13.models import loginmodel

def showstudent(request):
    return render(request,"homecommon.html")


def home(request):
    return render(request,"home.html")


def login(request):
    return render(request,"studentloginpage.html")


def register(request):
    return render(request,"register.html")


def forgetpassword(request):
    return render(request,"forgetpassword.html")





def adminlogin(request):
    return render(request, "adminlogin.html")


def adminhome(request):
    return render(request,"adminhome.html")






def studenthome(request):
    #reading data from hyperlinks
    uname=request.GET.get("unm")
    return render(request,"studenthome.html",{"name":uname})


def studentviewprofile(request):
    #reading data from hyperlinks
    uname=request.GET.get("unm")
    stu=studentmodel.objects.get(username=uname)
    return render(request,"studentviewprofile.html",{"name":uname,"data":stu})


def studentupdateprofile(request):
    #reading data from hyperlinks
    uname=request.GET.get("unm")
    stu=studentmodel.objects.get(username=uname)
    return render(request,"studentupdateprofile.html",{"name":uname,"data":stu})






def register_save(request):
   n= request.POST.get("name")
   ag=request.POST.get("ag")
   cnumber = request.POST.get("cno")
   gender = request.POST.get("g")
   un = request.POST.get("u_name")
   password = request.POST.get("u_pass")
   type='student'
   print(password,n,ag,cnumber,gender,un)

   student=studentmodel(name=n,age=ag,contact=cnumber,gender=gender,username=un)
   student.save()
   login=loginmodel(username=un,password=password,type=type)
   login.save()

   messages.success(request,"Successfully Registered")
   return redirect("register")


def studentlogincheck(request):
    usern=request.POST.get("uname")
    passwd=request.POST.get("password")
    ty='student'
    try:
        a = loginmodel.objects.get(username=usern,password=passwd,type=ty)
        return render(request,"studenthome.html",{"name":usern})
    except loginmodel.DoesNotExist:
        messages.error(request,"not valid")
        return redirect("login")


def logout(request):
    return render(request,"studentloginpage.html")


def studentupdate_save(request):
    n=request.POST.get("t1")
    ag=request.POST.get("t2")
    cn=request.POST.get("t3")
    gen=request.POST.get("t4")
    un=request.POST.get("t5")
    try:
        studentmodel.objects.filter(username=un).update(name=n,age=ag,contact=cn,gender=gen)
        stu=loginmodel.objects.get(username=un)
        return render(request, "studenthome.html", {"name": un, "data": stu})
#print messages
    except studentmodel.DoesNotExist:
        return redirect('studentviewprofile')


def forget_show(request):
    name_f1=request.POST.get("f1")
    cno_f2=request.POST.get("f2")
    try:
        studentmodel.objects.get(username=name_f1,contact=cno_f2)

        stu=loginmodel.objects.get(username=name_f1)
        return render(request,"forgetpassword.html",{"data":stu.password})
    except studentmodel.DoesNotExist:
        messages.error(request, "not valid")
        return redirect('forgetpassword')

# =======================================================================================================


def adminlogin_check(request):
    usern = request.POST.get("uname")
    passwd = request.POST.get("password")
    ty = 'admin'
    print(usern,passwd)
    try:
        a = loginmodel.objects.get(username=usern, password=passwd, type=ty)
        return render(request, "adminhome.html", {"name": usern})
    except loginmodel.DoesNotExist:
        messages.error(request, "not valid")
        return redirect("adminlogin")


def allstudentdetails(request):
    stu = studentmodel.objects.all()
    return render(request,"allstudentdetails.html",{"data":stu})


def allstudentdetails_delete(request):
    d1=request.POST.get("d1")
    studentmodel.objects.filter(username=d1).delete()
    loginmodel.objects.filter(username=d1).delete()
    stu = studentmodel.objects.all()
    return render(request,"allstudentdetails.html",{"data":stu})


def logout_admin(request):
    return render(request,"home.html")