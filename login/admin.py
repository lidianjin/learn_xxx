from django.contrib import admin

# Register your models here.

from . import models

# 注册User模型
admin.site.register(models.User)
admin.site.register(models.ConfirmString)