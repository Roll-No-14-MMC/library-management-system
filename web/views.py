from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

def index(request):
    return render(request,'auth\login.html')

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user and user.is_superuser:
            login(request,user)
            return redirect('/dashboard/')
        else:
            return render(request,"auth/login.html")
    else:
        return render(request,'auth/login.html')

def dashboard(request):
    if request.user.is_authenticated == True:
        return render(request, 'dashboard/index.html')
    else:
        return redirect('/login/')
    
def category(request):
    if request.user.is_authenticated == True:
        return render(request,'dashboard/category/index.html')
    else:
        return redirect('/login/')
def books(request):
    return render(request,'dashboard/books/index.html')
def borrow(request):
    return render(request,'dashboard/borrow/index.html')
def student(request):
    return render(request,'dashboard/student/index.html')

