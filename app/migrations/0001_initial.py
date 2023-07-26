# Generated by Django 4.2.3 on 2023-07-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('token', models.CharField(max_length=100)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
