from django.contrib import admin
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'customer_name', 'status', 'created_at', 'updated_at')  # Ensure these fields exist in the model
    list_filter = ('status',)  # Only filter by status if it exists as a model field

admin.site.register(ServiceRequest, ServiceRequestAdmin)
