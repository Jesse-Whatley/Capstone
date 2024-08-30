from django import forms 

class OrderForm(forms.Form):
    name = forms.CharField(max_length=225, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField(max_length=225, widget=forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email'}))
    street = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Street'}))
    street_2 = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Street 2'}))
    city = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    state = forms.CharField(max_length=24, widget=forms.TextInput(attrs={'placeholder': 'State'}))
    zip_code = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Zip Code'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))