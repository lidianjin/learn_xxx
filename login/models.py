from django.db import models

# Create your models here.

class User(models.Model):
    """用户"""
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    # 注意: 这里和教程不同
    create_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        """返回用户姓名"""
        return self.name


    class Meta:
        """按创建日期降序排序,别名"""
        ordering = ['-create_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class ConfirmString(models.Model):
    """确认码"""
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回用户名和确认码"""
        return self.user.name + ': ' + self.code


    class Meta:
        """按创建日期降序排序,别名"""
        ordering = ['-create_time']
        verbose_name = '确认码'
        verbose_name_plural = '确认码'