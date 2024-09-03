from rest_framework import serializers
from myapp.models import Employee
from django.db.models import fields


class Page(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = ('id','mobilenumber','otp')