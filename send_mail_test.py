import os

from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    subject = '来自新浪的测试邮件'
    from_email = 'dianjinli@sina.com'
    to_email = '2284631918@qq.com'
    text_content = '欢迎访问李典金的个人网站https://blog.lidianjin.cn/'
    html_content = '<p>欢迎访问<a href="https://blog.lidianjin.cn/" target=blank>李典金的个人网站</a></p>'
    message = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    message.attach_alternative(html_content, 'text/html')
    message.send()