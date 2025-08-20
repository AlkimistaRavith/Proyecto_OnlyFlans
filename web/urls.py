from django.urls import path
from .views import home, home_premium, contacto, exito, about, detalle_producto

urlpatterns = [
    path("", home, name="home"),
    path("premium/", home_premium, name="home_premium"),
    path("contacto/", contacto, name="contacto"),
    path("exito/", exito, name="exito"),
    path("about/", about, name="about"),
    path('detalle_flan/<slug:slug>/', detalle_producto, name='detalle_producto'),
]