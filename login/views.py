from django.shortcuts import render
from django.shortcuts import redirect

from . import models

# Create your views here.

def index(request):
    """主页"""
    return render(request, 'login/index.html')


def login(request):
    """登录"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 用户名和密码都不为空
        if username.strip() and password:
            # 用户名字符合法性验证
            # 密码长度验证
            # 其他验证...
            try:
                user = models.User.objects.get(name=username)
            except:
                return render(request, 'login/login.html')

            if user.password == password:
                return redirect('/index/')
    return render(request, 'login/login.html')


def register(request):
    """注册"""
    return render(request, 'login/register.html')


def logout(request):
    """登出"""
    return redirect('/login/')