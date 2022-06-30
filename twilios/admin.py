
# Register your models here.

#main/admin.py
from django.contrib import admin
from .models import Customer
from twilio.rest import Client
from django.conf import settings
def send_text(modeladmin, request, queryset):
  client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN )
  for customer in queryset:
    message = client.messages.create(
      to= str(customer.phone_number), 
      from_="+13156403238", # insert trial number 
      body="Hey I hope you received this message") # insert message
send_text.short_description = "Send text campaign"
class CustomerAdmin(admin.ModelAdmin):
  fields = ('name', 'phone_number' )
  actions = [send_text]
admin.site.register(Customer, CustomerAdmin)