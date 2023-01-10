from django.db import models

from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Service(models.Model):
    
    service_name = models.CharField(max_length= 100, verbose_name= "Usługa")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name= "Cena")
    approx_time = models.DurationField("Przewidywany czas")
    class Meta:
        verbose_name_plural = "Usługi"

    def __str__(self):
        return f"{self.service_name}"


class Employee(models.Model):
    first_name = models.CharField(max_length=100,verbose_name= "Imię")
    last_name = models.CharField(max_length=100, verbose_name= "Nazwisko")
    phone_number = models.CharField(validators=[MinLengthValidator(9)], unique=True, max_length=20,verbose_name= "Numer telefonu")
    email = models.EmailField(unique=True,verbose_name= "E-mail")
    login = models.CharField(validators = [MinLengthValidator(5)], max_length=20, unique=True, verbose_name= "Login")
    password = models.CharField(validators=[MinLengthValidator(8)], max_length=20, verbose_name= "Hasło")
    image = models.ImageField(upload_to="photos", null=True,verbose_name= "Zdjęcie")
    class Meta:
        verbose_name_plural = "Fryzjerzy"

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
    product_name = models.CharField(max_length=100, verbose_name= "Nazwa produktu")
    product_type = models.CharField(max_length=100, verbose_name= "Typ")
    manufacturer = models.CharField(max_length=100, verbose_name= "Producent")
    amount = models.IntegerField("Ilość")
    class Meta:
        verbose_name_plural = "Produkty"


class Comment(models.Model):
    user_name = models.CharField(max_length=120,verbose_name= "Username")
    user_email = models.EmailField("E-mail klienta")
    service_name = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True,verbose_name= "Usługa")
    worker_name = models.ForeignKey(Employee,on_delete=models.SET_NULL, null=True, verbose_name= "Fryzjer")
    text = models.TextField(max_length=400,verbose_name= "Treść")
    class Meta:
        verbose_name_plural = "Komentarze"


class Unavailability(models.Model):
    worker = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, verbose_name= "Fryzjer")
    start_date = models.DateTimeField('Początek')
    end_date = models.DateTimeField('Koniec')
    class Meta:
        verbose_name = 'Niedostępność'
        verbose_name_plural = 'Niedostępność'

    def __str__(self):
        return f"{self.worker}"



class Appointment(models.Model):
    class AppointmanetStatus(models.TextChoices):
        ZREALIZOWANA = 'Zrealizowana'
        ZAPLANOWANA =  'Zaplanowana'
        ODWOŁANA= 'Odwołana'
    client = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,verbose_name= "Klient")
    employee = models.ForeignKey(Employee,on_delete=models.SET_NULL, null=True,verbose_name= "Fryzjer")
    status= models.CharField(max_length=100, choices=AppointmanetStatus.choices, default=AppointmanetStatus.ZAPLANOWANA)
    service = models.ManyToManyField(Service, verbose_name= "Usługa")
    date = models.DateTimeField("Data")
    class Meta:
        verbose_name_plural = "Wizyta"
    def __str__(self):
        return f"Wizyta"