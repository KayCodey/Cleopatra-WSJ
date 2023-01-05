from django.contrib import admin
from .models import Service, Employee, Comment, Client
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


admin.site.register(Service, ServiceAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Client)