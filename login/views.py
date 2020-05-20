import hashlib
import datetime

from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from . import models
from . import forms

# Create your views here.
def hash_code(password, salt='Friday'):
    """hash加密密码"""
    # 加点盐
    password += salt
    # 注意加密后的密码长度
    h = hashlib.sha256()
    # 只接受bytes类型
    h.update(password.encode())
    return h.hexdigest()


def make_confirm_string(user):
    """生成确认码"""
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user)
    return code


def send_mail(email, code):
    """发送邮件"""
    subject = '用户注册测试邮件'
    text_content = '欢迎访问李典金的个人网站https://blog.lidianjin.cn/'
    html_content = '''
        <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>李典金的个人网站</a></p>
        <P>请点击链接完成注册确认</p>
        <p>此链接有效期为{}天</p>
    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)
    message = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    message.attach_alternative(html_content, 'text/html')
    message.send()


def index(request):
    """主页"""
    return render(request, 'login/index.html')


def login(request):
    """登录"""
    # 不允许用户重复登录
    if request.session.get('is_login', None):
        # 重定向到首页，即选择采集网址页面
        return redirect('/ecommerce/index/')
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

            if not user.has_confirmed:
                message = '用户还未经过邮件确认'
                return  render(request, 'login/login.html', locals())

            if user.password == hash_code(password):
                # 保存用户信息
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = username
                return redirect('/ecommerce/index/')
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
    # 不允许已登录用户注册
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = '请检查填写的内容'
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同'
                return render(request, 'login/register.html', locals())
            else:
                some_name_user = models.User.objects.filter(name=username)
                if some_name_user:
                    message = '用户名已存在'
                    return render(request, 'login/register.html', locals())
                some_email_user = models.User.objects.filter(email=email)
                if some_email_user:
                    message = '邮箱已被注册'
                    return render(request, 'login/register.html', locals())

            # 保存新注册用户信息
            new_user = models.User()
            new_user.name = username
            new_user.password = hash_code(password1)
            new_user.email = email
            new_user.sex = sex
            new_user.save()

            # 邮箱确认
            code = make_confirm_string(new_user)
            send_mail(email, code)
            message = '请前往邮箱进行确认'
            return render(request, 'login/confirm.html', locals())
        else:
            # 表单无效，请检查填写的内容
            return render(request, 'login/register.html', locals())

    # 对于非POST方法发送数据时，比如GET方法请求页面，返回空的表单，让用户可以填入数据
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


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


def user_confirm(request):
    """用户邮箱验证"""
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求'
        return  render(request, 'login/confirm.html', locals())

    create_time = confirm.create_time
    now = datetime.datetime.now()
    if now > create_time + datetime.timedelta(days=settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已过期,请重新注册'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认,请使用账户登录'
        return  render(request, 'login/confirm.html', locals())
