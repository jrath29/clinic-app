from django import forms
from .models import Appointment, Patient, Doctor, Product

class FormAppointment(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            'title',
            'doctor',
            'start',
            'end'
        ]

class FormPatient(forms.ModelForm):

    class Meta:
        model = Patient
    
        fields = [
            'name',
            'birth_date'
        ]

class FormDoctor(forms.ModelForm):

    class Meta:
        model = Doctor
        
        fields = [
            'name',
            'birth_date',
            'specialty'
        ]

class FormProduct(forms.ModelForm):

    class Meta:
        model = Product
    
        fields = [
            'name',
            'expiration',
            'product_type'
        ]