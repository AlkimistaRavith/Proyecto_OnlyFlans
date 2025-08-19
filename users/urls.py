from django.urls import path
from .views import Registro, Login, Logout

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("registro/", Registro.as_view(), name="registro"),
    path("logout/", Logout.as_view(), name="logout"),
]