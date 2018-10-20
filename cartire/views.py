from django.shortcuts import render
from django.http import HttpResponse
from .forms import TireForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = TireForm(request.POST)
        if form.is_valid():
            car_manufacturer = form.cleaned_data["car_manufacturer"]
            car_year = form.cleaned_data["car_year"]
            car_model = form.cleaned_data["car_model"]
            print(car_manufacturer + car_model + car_year)
    else:
        form = TireForm()
    return render(request, "cartire/index.html", {"form": form})