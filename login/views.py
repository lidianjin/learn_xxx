from django.shortcuts import render
from django.shortcuts import redirect

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
            return redirect('/index/')
    return render(request, 'login/login.html')


def register(request):
    """注册"""
    return render(request, 'login/register.html')


def logout(request):
    """登出"""
    return redirect('/login/')