from django import forms
from .models import FormularioModel


class FormularioModelForm(forms.ModelForm):
    class Meta:
        model = FormularioModel
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'required': True, 'class': 'custom-date-input'}),
            'turno': forms.Select(attrs={'required': True}),
            'conferente': forms.TextInput(attrs={'placeholder': 'Nome do conferente', 'required': True}),
            'cliente': forms.TextInput(attrs={'placeholder': 'Nome do cliente', 'required': True}),
            'transportadora': forms.TextInput(attrs={'placeholder': 'Nome da transportadora', 'required': True}),
            'num_nota': forms.TextInput(attrs={'placeholder': 'Ex: 000.000.000', 'required': True}),
            'quantidade_cx': forms.NumberInput(attrs={'min': 1, 'max': 4000, 'required': True}),
            'quantidade_recebidas': forms.NumberInput(attrs={'min': 1, 'max': 4000, 'required': True}),
            'motivo': forms.Select(attrs={'required': True}),
            'setor': forms.Select(attrs={'required': True}),
            'valor': forms.NumberInput(attrs={'step': '0.01', 'required': True}),
        }

    