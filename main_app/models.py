from django.db import models


class Clients(models.Model):
    client_first_name = models.CharField(max_length=100)
    client_second_name = models.CharField(max_length=100)
    client_phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.client_first_name}{self.client_second_name}'


class Master(models.Model):
    master_first_name = models.CharField(max_length=50)
    master_second_name = models.CharField(max_length=50)
    master_phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.master_first_name}{self.master_second_name}'


class Services(models.Model):
    service_name = models.CharField(max_length=150)
    service_description = models.TextField(max_length=500)
    service_cost = models.PositiveIntegerField()
    service_duration = models.PositiveIntegerField()
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='master')
    client = models.ManyToManyField(Clients)

    def __str__(self):
        return self.service_name


class Sessions(models.Model):
    datetime = models.DateTimeField()
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    def __str__(self):
        return self.datetime
