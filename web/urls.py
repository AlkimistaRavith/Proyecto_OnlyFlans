from django.urls import path
from .views import home, home_premium, contacto, exito

urlpatterns = [
    path("", home, name="home"),
    path("premium/", home_premium, name="home_premium"),
    path("contacto/", contacto, name="contacto"),
    path("exito/", exito, name="exito"),
]