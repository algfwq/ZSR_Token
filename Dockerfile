FROM ubuntu:latest
FROM python:3.10-slim
LABEL authors="ALG"

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . /app/

# 设置环境变量
ENV PYTHONUNBUFFERED=1

#配置安装依赖
RUN python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

#暴露8000端口
EXPOSE 8000

#运行项目
CMD python manage.py runserver 0.0.0.0:8000
