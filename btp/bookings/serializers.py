from rest_framework import serializers
from bookings.models import *

class BusInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = BusInfo
		fields = '__all__'



class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = '__all__'