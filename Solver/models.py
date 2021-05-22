from django.db import models

# Create your models here.
# class Sum(models.Model):
#     img=models.FileField(upload_to='sums')

class Sum(models.Model):
    topic = models.CharField("Problem Topic",max_length=50)
    sum_img = models.ImageField("Problem Image",upload_to='images/',)


