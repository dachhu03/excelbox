from django.urls import path, include
from .views import authView, home , totalsolutions


urlpatterns = [
 path("", home, name="home"),
 path("signup/", authView, name="authView"),
 path("totalsales/",totalsolutions, name="totalsolutions"),
 path("accounts/", include("django.contrib.auth.urls")),
 
 
]
