from django.db import models

# Create your models here.
class Destination(models.Model):

    name = models.CharField(max_length=200,default=None)
    img = models.ImageField(upload_to='pics', blank=True, null=True)
    desc = models.TextField(blank=True)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
