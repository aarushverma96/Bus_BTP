from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from bookings.models import *
from bookings.serializers import *
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

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
	prevAvail=book.available_seats
	prevBooked=book.booked_seats

	if request.method=='GET':
		
		return render(request, 'bookings/booking.html',{'book':book})
	else:
		selected_seats=request.POST.get("seats")
		book.available_seats=prevAvail-int(selected_seats)
		book.booked_seats=prevBooked+int(selected_seats)

		book.save()

		#return redirect(customer, seats=selected_seats)
		return render(request,'bookings/sucess.html')


