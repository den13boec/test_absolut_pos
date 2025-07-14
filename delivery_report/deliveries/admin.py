from django.contrib import admin
from .models import *

admin.site.register(TransportModel)
admin.site.register(PackageType)
admin.site.register(Service)
admin.site.register(DeliveryStatus)
admin.site.register(Delivery)
