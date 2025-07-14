from django.db import models


class TransportModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PackageType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DeliveryStatus(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#000000')  # hex для фронта

    def __str__(self):
        return self.name


class Delivery(models.Model):
    number = models.CharField(max_length=20)
    model = models.ForeignKey(TransportModel, on_delete=models.SET_NULL, null=True)
    license_plate = models.CharField(max_length=20)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    distance_km = models.PositiveIntegerField()
    media = models.FileField(upload_to='uploads/', null=True, blank=True)
    services = models.ManyToManyField(Service)
    status = models.ForeignKey(DeliveryStatus, on_delete=models.SET_NULL, null=True)
    package = models.ForeignKey(PackageType, on_delete=models.SET_NULL, null=True)
    is_working = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number
