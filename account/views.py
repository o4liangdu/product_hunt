from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method=="POST":
        user_name=request.POST.get("用户名",None)
        ps1=request.POST.get("密码",None)
        ps2=request.POST.get("确认密码",None)
        try:
            User.objects.get(username=user_name)
            return render(request,'signup.html',{'用户名重复':'该用户已存在'})
        except User.DoesNotExist:
            if ps1==ps2:
                User.objects.create(username=user_name,password=ps1)
                return redirect('主页')
            else:
                return render(request,'signup.html',{'密码错误':'两次输入的密码不一致'})
    elif request.method == "GET":
        return render(request,'signup.html')

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method=='POST':
        user_name = request.POST.get("用户名", None)
        ps = request.POST.get("密码", None)
        user=auth.authenticate(username=user_name,password=ps)
        if user is None:
            return render(request,'login.html',{'错误':'用户名或密码错误'})
        else:
            auth.login(request,user)
            return redirect('主页')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('主页')