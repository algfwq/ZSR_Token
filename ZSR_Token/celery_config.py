import os
from celery import Celery

# eventlet非常重要，Windows特有
# celery -A ZSR_Token worker -l INFO -P eventlet
# 周期任务：celery -A ZSR_Token beat -l info

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZSR_Token.settings')  # 设置django环境

app = Celery('ZSR_Token')  # 实例化一个app对象

app.config_from_object('django.conf:settings', namespace='CELERY')  # 使用CELERY_ 作为前缀，在settings中写配置

app.autodiscover_tasks(['app'])  # 发现任务文件每个app下的tasks.py文件
