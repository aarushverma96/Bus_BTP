from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from bookings.models import *
from bookings.serializers import *
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.core.mail import send_mail
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def jsonallbuses(request,gsource,gdestination):
	if request.method == 'GET':
		bus = BusInfo.objects.filter(source=gsource,destination=gdestination)
		serializer = BusInfoSerializer(bus, many=True)
		return JsonResponse(serializer.data, safe=False)


def jsonstatus(request,gbusId):
	if request.method == 'GET':
		st = Status.objects.filter(bus_id=gbusId)
		serializer = StatusSerializer(st, many=True)
		return JsonResponse(serializer.data, safe=False)

def buses(request,gsource,gdestination):
	if request.method == 'GET':
		bus = BusInfo.objects.filter(source=gsource,destination=gdestination)

		return render(request, 'bookings/index.html', {'buses': bus})
	
def search(request):
	if request.method== 'GET':
		return render(request,'bookings/search.html')
	else:
		source=request.POST.get("source")
		destination=request.POST.get("destination")
		return redirect(buses, gsource=source , gdestination=destination)

		#print (rt)

def customer(request,seats):
	if request.method=='GET':
		return render(request,'bookings/customer.html')
	elif request.method=='POST':
		tckt_id=request.POST.get("ticket_id")
		name=request.POST.get("customer_name")
		cust=Customer(ticket_id=tckt_id,ticket_booked=seats,customer_name=name )
		cust.save()

		return render(request,'bookings/sucess.html')
		
	

def booking(request,gbusId):
	book=Status.objects.get(bus_id=gbusId)
	prevStatus=book.seats

	if request.method=='GET':
		
		return render(request, 'bookings/booking.html',{'book':book})
	else:
		selected_seats=request.POST.get("seats")
		print(selected_seats)
		temp1=list(selected_seats.split(','))
		print(temp1)
		temp2=list(prevStatus.split(','))
		print(temp2)

		for i in temp1:
			temp2[int(i)-1]='b'

		#print(temp2)
		prevStatus=','.join(temp2)
		#print(prevStatus)
		book.seats=prevStatus

		#book.seats
		#print (prevStatus)
		book.save()

		#return redirect(customer, seats=selected_seats)
		return render(request,'bookings/sucess.html')

@csrf_exempt
@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def test(request,gbusId):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	if request.method=='PUT':
		book=Status(bus_id=gbusId)
		st=StatusSerializer(book, data=request.data)
		if st.is_valid():
			st.save()
			return Response(st.data)
		return Response(st.errors,status=status.HTTP_400_BAD_REQUEST)


def mail(request,gticket_id,gbus_id):

	cust=Customer(ticket_id=gticket_id)
	bus=BusInfo(bus_id=gbus_id)

	send_mail(
	'Booking Details',
	'Hello your booking is confirmed',
	'aarushverma96@gmail.com',
	['15ucs003@lnmiit.ac.in'],
	
	)

	return render(request,'bookings/sucess.html')


@csrf_exempt
@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def delete(request,gbusId):
	if request.method=='PUT':
		st=Status.objects.get(bus_id=gbusId)
		prevStatus=st.seats
		tempo=prevStatus.split(',')
		data=request.data
		
		temp=data['seats'].split(',')
		
		for i in temp:
			tempo[int(i)-1]='a'


		updatedStatus=','.join(tempo)
		st.seats=updatedStatus
		
		st.save()
		return Response(st.seats)
		#return Response(st.errors,status=status.HTTP_400_BAD_REQUEST)
