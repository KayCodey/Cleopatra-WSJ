from django.db import models

from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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

'''class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[MinLengthValidator(9)], unique=True, max_length=20)
    def __str__(self):
        return f"{self.user.username}"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()'''

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    amount = models.IntegerField()
    class Meta:
        verbose_name_plural = "Products"


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    service_name = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    worker_name = models.ForeignKey(Employee,on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=400)


class Unavailability(models.Model):
    worker = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField('Start Date')
    end_date = models.DateTimeField('End Date')
    class Meta:
        verbose_name = 'Unavailability'
        verbose_name_plural = 'Unavailability'

    def __str__(self):
        return f"{self.worker}"



class Appointment(models.Model):
    class AppointmanetStatus(models.TextChoices):
        COMPLETED = 'Completed'
        SCHEDULED =  'Scheduled'
        CANCELLED = 'Cancelled'
    client = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee,on_delete=models.SET_NULL, null=True)
    status= models.CharField(max_length=100, choices=AppointmanetStatus.choices, default=AppointmanetStatus.SCHEDULED)
    service = models.ManyToManyField(Service)
    date = models.DateTimeField()
    def __str__(self):
        return f"Appointment"