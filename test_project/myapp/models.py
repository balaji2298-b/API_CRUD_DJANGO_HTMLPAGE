from django.db import models

class Employee(models.Model):
	mobilenumber = models.CharField(max_length=200)
	otp = models.CharField(max_length=200)
