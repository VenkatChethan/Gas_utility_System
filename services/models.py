from django.db import models

class ServiceRequest(models.Model):
    email = models.EmailField()
    customer_name = models.CharField(max_length=100)
    attachment = models.FileField(upload_to='uploads/')
    request_type = models.CharField(max_length=50)
    
    # Add status, created_at, and updated_at if they are missing
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name