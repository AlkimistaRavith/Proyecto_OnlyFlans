from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto

# Create your views here.

def home(request):
    flanes_publicos = Producto.objects.filter(is_private=False)
    return render(request, "web/home.html", {"flanes_publicos": flanes_publicos})


@login_required
def home_premium(request):
    flanes_publicos = Producto.objects.filter(is_private=False)
    flanes_premium = Producto.objects.filter(is_private=True)
    return render(request, "web/home.html", {"flanes_premium": flanes_premium, "flanes_publicos": flanes_publicos})
