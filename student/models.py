from django.db import models

class Sms(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    message = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return self.name
