from django.db import models


class Clients(models.Model):
    client_first_name = models.CharField(max_length=100)
    client_second_name = models.CharField(max_length=100)
    client_phone_number = models.CharField(max_length=20)
    avatar = models.ImageField()

    def __str__(self):
        return f'{self.client_first_name}+' '+{self.client_second_name}'


class Master(models.Model):
    master_first_name = models.CharField(max_length=50)
    master_second_name = models.CharField(max_length=50)
    master_phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.master_first_name}{self.master_second_name}'


class Sessions(models.Model):
    datetime = models.DateTimeField()

    def __str__(self):
        return self.datetime


class Services(models.Model):
    service_name = models.CharField(max_length=150)
    service_description = models.TextField(max_length=500)
    service_cost = models.PositiveIntegerField()
    service_duration = models.PositiveIntegerField()
    master = models.ManyToManyField(Master, related_name='master')
    client = models.ManyToManyField(Clients, related_name='client')
    session = models.ManyToManyField(Sessions, related_name='session')

    def __str__(self):
        return self.service_name


class Review(models.Model):
    person = models.ForeignKey(Clients, related_name='client', on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
