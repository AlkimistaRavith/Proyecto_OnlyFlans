from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, ContactData
from .forms import ContactDataForm
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    flanes_publicos = Producto.objects.filter(is_private=False)
    return render(request, "web/home.html", {"flanes_publicos": flanes_publicos})


@login_required
def home_premium(request):
    flanes_publicos = Producto.objects.filter(is_private=False)
    flanes_premium = Producto.objects.filter(is_private=True)
    return render(request, "web/home_premium.html", {"flanes_premium": flanes_premium, "flanes_publicos": flanes_publicos})

def contacto(request):
    if request.method == 'POST':

        form = ContactDataForm(request.POST)
        if form.is_valid():
            contact_form = ContactData.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
        
    else:
        form = ContactDataForm()
    
    return render(request, 'web/contacto.html', {'form': form})

def exito(request):
    return render(request, "web/exito.html", {})

def about(request):
    return render(request, "web/about.html", {})

def detalle_producto(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    return render(request, 'web/detalle_producto.html', {'producto': producto})
