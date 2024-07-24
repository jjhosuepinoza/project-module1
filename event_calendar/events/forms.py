from django import forms
from django.forms import ModelForm
from .models import Venue

#Create a venue form

class VenueForm(ModelForm):
    class Meta:
        model = Venue 
        fields = ('name', 'address', 'zip_code', 'phone', 'email_address', 'web' )
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name' }), 
            'address': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Address'}), 
            'zip_code': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Zip Code'}), 
            'phone': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Phone'}), 
            'email_address': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Email'}), 
            'web': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Web Url'})
            }
        
        labels =  {
        'name': '', 
        'address': '', 
        'zip_code': '', 
        'phone': '', 
        'email_address': '', 
        'web': ''
    }



