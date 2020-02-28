from django.shortcuts import render
from django.shortcuts import redirect

from . import models
from . import forms

# Create your views here.

def index(request):
    """主页"""
    return render(request, 'login/index.html')


def login(request):
    """登录"""
    # 不允许用户重复登录
    if request.session.get('is_login', None):
        return redirect('index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = models.User.objects.get(name=username)
            except:
                message = '用户不存在'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                # 保存用户信息
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = username
                return redirect('/index/')
            else:
                message = '密码不正确'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    # 对于非POST方法发送数据时，比如GET方法请求页面，返回空的表单，让用户可以填入数据
    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    """注册"""
    return render(request, 'login/register.html')


def logout(request):
    """登出"""
    # 本来没有登录，没有登出一说
    if not request.session.get('is_login', None):
        return redirect('/login/')
    # 清空session
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['username']
    return redirect('/login/')