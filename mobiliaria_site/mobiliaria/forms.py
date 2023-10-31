from django import forms
from .models import Imoveis




class Mensagem(forms.Form):
    name=forms.CharField(
        label='Full name', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }
        )
    )

    email=forms.EmailField(
        label='Email Address',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }
        )
    )

    subject=forms.CharField(
        label='Subject', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
            }
        )
    )

    message=forms.CharField(
        label='Message', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mensage',
            }
        )
    )




class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imoveis
        fields = [
            'address', 'status', 'area', 'bedrooms', 'bathrooms',
            'floor', 'parking', 'value', 'type', 'path'
        ]
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Textarea(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'bedrooms': forms.TextInput(attrs={'class': 'form-control'}),
            'bathrooms': forms.TextInput(attrs={'class': 'form-control'}),
            'floor': forms.TextInput(attrs={'class': 'form-control'}),
            'parking': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}), 
            'path': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


