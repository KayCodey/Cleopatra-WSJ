from django.urls import path
from . import views
from home.views import signup 


urlpatterns = [
    path('', views.index, name='index'),
    path("signup/",signup, name="signup"),

]