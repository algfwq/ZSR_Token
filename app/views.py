from django.shortcuts import render
from django.http import JsonResponse
from .models import UserToken
from datetime import timedelta
from django.utils import timezone
import random
import string

# Create your views here.

#生成随机token函数
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def add_token(request):
    if request.method == 'POST':
        #获得可用时间
        use_time = request.POST.get('use_time')
        #生成token
        random_string = generate_random_string(40)
        print(random_string)
        try:
            #保存到数据库中
            UserToken.objects.create(token=random_string,use_time=use_time)
            #返回数据
            message = {'mode':'succeed','token':random_string}
            return JsonResponse(message)
        except:
            message = {'mode':'fail','error':'database error'}
            return JsonResponse(message)

    if request.method == 'GET':
        return render(request, 'app/FUCK.html')

def find_token(request):
    if request.method == 'POST':
        #获取查询的token值
        token = request.POST.get('token')
        #搜索数据库
        try:
            #查询成功
            UserToken.objects.get(token=token)
            message = {'mode':'succeed'}
            return JsonResponse(message)
        except:
            #查询失败
            message = {'mode':'fail'}
            return JsonResponse(message)

    if request.method == 'GET':
        return render(request, 'app/FUCK.html')

def token_delete(request):
    if request.method == 'POST':
        token_list = UserToken.objects.all()
        for data in token_list:
            use_time = dict(eval(data.use_time))
            if use_time['mode'] == 'day':
                use_time_number = int(use_time['number'])
                #计算过期时间
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

        message = {'mode':'succeed'}
        return JsonResponse(message)

    if request.method == 'GET':
        return render(request, 'app/FUCK.html')