from django.db import models

# Create your models here.
class UserToken(models.Model):
    token = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    use_time = models.CharField(max_length=100)