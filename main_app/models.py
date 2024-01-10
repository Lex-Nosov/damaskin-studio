from django.db import models


class Master(models.Model):
    master_first_name = models.CharField(max_length=50)
    master_second_name = models.CharField(max_length=50)
    master_phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.master_first_name}{self.master_second_name}'


class Clients(models.Model):
    client_first_name = models.CharField(max_length=100)
    client_second_name = models.CharField(max_length=100)
    client_phone_number = models.CharField(max_length=20)
    profile_image = models.ImageField(blank=True, null=True)
    master = models.ForeignKey(Master, related_name='master', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.client_first_name}+' '+{self.client_second_name}"


class Sessions(models.Model):
    datetime = models.DateTimeField()
    client = models.ForeignKey(Clients, related_name='session_client', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.datetime


class Services(models.Model):
    service_name = models.CharField(max_length=150)
    service_description = models.TextField(max_length=500)
    service_cost = models.PositiveIntegerField()
    service_duration = models.PositiveIntegerField()
    client = models.ForeignKey(Clients, related_name='service_client', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.service_name
