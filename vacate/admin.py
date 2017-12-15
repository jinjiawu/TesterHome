from django.contrib import admin
from vacate.models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'realname', 'reason','days','start_time','end_time']

# class GuestAdmin(admin.ModelAdmin):
#     list_display = ['realname', 'reason','days','start_time','end_time','event']

admin.site.register(Event,EventAdmin)
#admin.site.register(Guest,GuestAdmin)