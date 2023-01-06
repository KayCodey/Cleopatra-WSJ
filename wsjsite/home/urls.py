from django.urls import path
from . import views
from home.views import signup,signin, logoutUser


urlpatterns = [
    path('', views.index, name='index'),
    path("signup/",signup, name="signup"),
    path("signin/",signin, name="signin"),
    path("logout/",logoutUser, name="logout"),

]