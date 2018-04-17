from django.contrib import admin
from bookings.models import *
# Register your models here.

class BusInfoAdmin(admin.ModelAdmin):
    pass
admin.site.register(BusInfo, BusInfoAdmin)


class StatusAdmin(admin.ModelAdmin):
	pass
admin.site.register(Status,StatusAdmin)