from django.contrib import admin
from .models import Service, Requests, Worker

admin.site.register(Service)
admin.site.register(Worker)