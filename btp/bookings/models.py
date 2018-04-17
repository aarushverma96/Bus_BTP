from django.db import models



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
	booked_seats = models.IntegerField(default=0)
	available_seats = models.IntegerField(default=40)
	
	def __str__(self):
		return str(self.bus_id)

class Customer(models.Model):

	ticket_id=models.IntegerField(default=0)
	ticket_booked=models.IntegerField(null=True)
	customer_name=models.CharField(max_length=30,null=True)

	def __str__(self):
		return str(self.ticket_id)
