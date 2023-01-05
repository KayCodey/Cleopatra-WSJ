from django.contrib import admin
from .models import Service, Employee, Comment, Client, Products, Unavailability, Appointment
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service_name",)
    list_filter = ("service_name","price","approx_time",)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name",)
    list_filter = ("first_name","last_name",)


class CommentAdmin(admin.ModelAdmin):
     list_display = ("user_name",)

class ClientAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","phone_number",)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name","amount",)

class UnavailAdmin(admin.ModelAdmin):
    list_display =("worker",)
    list_filter = ("worker","start_date","end_date",)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("client", "status",)
    list_filter = ("client", "status",)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Products, ProductAdmin)
admin.site.register(Unavailability, UnavailAdmin)
admin.site.register(Appointment)