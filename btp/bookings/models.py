from django.db import models

from django.core.validators import validate_comma_separated_integer_list

# Create your models here.

class BusInfo(models.Model):
	
	bus_id=models.IntegerField()
	source=models.CharField(max_length=10)
	destination=models.CharField(max_length=10)	
	arrival=models.TimeField()
	departure=models.TimeField()

	def __str__(self):
		return str(self.bus_id)

class Status(models.Model):
	
	bus_id=models.IntegerField(default=123)
	seats=models.CharField(validators=[validate_comma_separated_integer_list],max_length=200,default='a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a')
	
	def __str__(self):
		return str(self.bus_id)

class Customer(models.Model):

	ticket_id=models.IntegerField(default=0)
	ticket_booked=models.IntegerField(null=True)
	customer_name=models.CharField(max_length=30,null=True)

	def __str__(self):
		return str(self.ticket_id)
