from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def index(request):
    """主页"""
    return render(request, 'login/index.html')


def login(request):
    """登录"""
    return render(request, 'login/login.html')


def register(request):
    """注册"""
    return render(request, 'login/register.html')


def logout(request):
    """登出"""
    return redirect('/login/')