from django.contrib import admin
from .models import UserToken
# Register your models here.

class Token(admin.ModelAdmin):
    # 配置要在后台显示的字段
    list_display = ['token','data','use_time']

admin.site.register(UserToken, Token)