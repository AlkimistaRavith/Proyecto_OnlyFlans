from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "web/home.html", {})


@login_required
def home_premium(request):
    return render(request, "web/home_premium.html", {})
