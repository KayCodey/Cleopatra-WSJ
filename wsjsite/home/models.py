from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Service(models.Model):
    service_name = models.CharField(max_length= 100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    approx_time = models.DurationField()

    def __str__(self):
        return f"{self.service_name}"


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(validators=[MinLengthValidator(9)], unique=True, max_length=20)
    email = models.EmailField(unique=True)
    login = models.CharField(validators = [MinLengthValidator(5)], max_length=20, unique=True)
    password = models.CharField(validators=[MinLengthValidator(8)], max_length=20)
    image = models.ImageField(upload_to="photos", null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(validators=[MinLengthValidator(9)], unique=True, max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(validators=[MinLengthValidator(8)], max_length=20)
    


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    service_name = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    worker_name = models.ForeignKey(Employee,on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=400)