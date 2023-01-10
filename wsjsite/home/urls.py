from django.urls import path
from . import views


urlpatterns = [
    path('', views.review, name='index'),
    path('service/', views.services, name='list-service'),
    path('products/', views.products, name='list-product'),
    path('team/', views.employees, name='our-team'),
    path("signup/",views.signup, name="signup"),
    path("signin/",views.signin, name="signin"),
    path("logout/",views.logoutUser, name="logout"),

]