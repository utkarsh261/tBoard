from django.db import models

# Create your models here.

class Info(models.Model):
    user = models.CharField(max_length=15)
    name = models.CharField(max_length=50, default = 'Dummy_User')
    def __str__(self):
        return self.user

class Data(models.Model):
    user_link = models.ForeignKey(Info, on_delete=models.CASCADE)
    data_text = models.CharField(max_length=199999)

    def __str__(self):
        return self.data_text