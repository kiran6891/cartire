from django import forms

class TireForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    phone_no = forms.CharField(label="Phone No", max_length=100)
    city = forms.CharField(label="City", max_length=100)
    state = forms.CharField(label="State", max_length=100)
    car_manufacturer = forms.CharField(label="Car Manufacturer", max_length=100)
    car_year = forms.CharField(label="Car Year", max_length=4)
    car_model = forms.CharField(label="Car Model", max_length=100)
