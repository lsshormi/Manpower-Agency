from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Apply(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nid = models.IntegerField()
    skills_have = models.TextField()
    skill_want = models.TextField()
    email = models.CharField(primary_key=True, max_length=122)
    password = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    city = models.CharField(max_length=30)
    zip = models.CharField(max_length=50)
    resume = models.FileField()
    date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Applies'

    def __str__(self):
        return self.email

class Hire(models.Model):
    company_name = models.CharField(max_length=122) 
    company_type = models.CharField(max_length=122) 
    trade_license = models.FileField() 
    email = models.CharField(primary_key=True, max_length=122)
    password = models.CharField( max_length=122)
    address = models.CharField(max_length=122)
    employee_recuirement = models.TextField()
    city = models.CharField(max_length=30)
    zip = models.CharField(max_length=50)
    cc_name = models.CharField(max_length=122) 
    cc_number = models.BigIntegerField()
    cc_expiration = models.DateField()
    cc_cvv = models.BigIntegerField()
    date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Hires'

    def __str__(self):
        return self.email



class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
