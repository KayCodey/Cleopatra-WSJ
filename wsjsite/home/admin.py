from django.contrib import admin
from .models import Service, Employee, Comment, Products, Unavailability, Appointment
from .forms import CreateUserForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service_name",)
    list_filter = ("service_name","price","approx_time",)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name",)
    list_filter = ("first_name","last_name",)


class CommentAdmin(admin.ModelAdmin):
     list_display = ("user_name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name","amount",)
    list_filter = ("manufacturer", "product_type",)

class UnavailAdmin(admin.ModelAdmin):
    list_display =("worker",)
    list_filter = ("worker","start_date","end_date",)


#class AppointmentAdmin(admin.ModelAdmin):
    #list_display = ("client", "status",)
    #list_filter = ("client", "status",)

'''class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_number')
    list_select_related = ('profile', )

    def get_number(self, instance):
        return instance.profile.phone_number
    get_number.short_description = 'Phone number'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)'''




admin.site.register(Service, ServiceAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Products, ProductAdmin)
admin.site.register(Unavailability, UnavailAdmin)
admin.site.register(Appointment)