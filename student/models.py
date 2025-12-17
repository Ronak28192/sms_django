from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

class Sms(models.Model):
    name = models.CharField(max_length=100,validators=[MinLengthValidator(3)])
    mobile = models.CharField(max_length=15, validators=[
            RegexValidator(
                regex=r'^[0-9]+\d{9}$',
                message='Enter valid Indian mobile number'
            )
        ])
    message = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return self.name
