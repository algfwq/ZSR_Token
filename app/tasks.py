from celery import shared_task
from .models import UserToken
from datetime import timedelta
from django.utils import timezone


# shared_task重要参数name
@shared_task(name="ZSR_Token.tasks.delete_expired_data")
def delete_expired_data():
    token_list = UserToken.objects.all()
    for data in token_list:
        use_time = dict(eval(data.use_time))
        if use_time['mode'] == 'day':
            use_time_number = int(use_time['number'])
            # 计算过期时间
            expiration_time = timezone.now() - timedelta(days=use_time_number)
            if data.data <= expiration_time:
                data.delete()
                print(data.token + '已过期并删除')
            else:
                print(data.token + '暂未过期')

        elif use_time['mode'] == 'hour':
            use_time_number = int(use_time['number'])
            # 计算过期时间
            expiration_time = timezone.now() - timedelta(hours=use_time_number)
            if data.data <= expiration_time:
                data.delete()
                print(data.token + '已过期并删除')
            else:
                print(data.token + '暂未过期')

        elif use_time['mode'] == 'minute':
            use_time_number = int(use_time['number'])
            # 计算过期时间
            expiration_time = timezone.now() - timedelta(minutes=use_time_number)
            if data.data <= expiration_time:
                data.delete()
                print(data.token + '已过期并删除')
            else:
                print(data.token + '暂未过期')

    print('Token检查任务已经完成！')
