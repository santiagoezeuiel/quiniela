from django import forms
from .models import *


class FormularioRendicion(forms.ModelForm):

    agencia = forms.CharField(
        label = "Numero de agencia",
        widget = forms.TextInput(attrs= {
            'class' : '''
            w-full h-12 px-4 py-2 border-2 border-gray-300 rounded-xl focus:outline-none
            focus:ring-2 focus:ring-blue-500 focus:border-blue-500 appeatace-none text-lg font-semibold''',
            'placeholder' : 'Introduzca en numero de agencia',
        }) 
    )


    monto = forms.CharField(
        label = "Monto de la transferencia",
        widget = forms.NumberInput( attrs= {
            'class' : '''
            w-full h-12 px-4 py-2 border-2 border-gray-300 rounded-xl focus:outline-none
            focus:ring-2 focus:ring-blue-500 focus:border-blue-500 appeatace-none''',
            'placeholder' : 'Introduzca el monto',
        })
    )

    n_comprobante = forms.CharField(
        label = "Numero de Comprobante",
        help_text= "Introduzca el numero de comprobante",
        widget = forms.NumberInput( attrs= {
            'class' : '''
            w-full h-12 px-4 py-2 border-2 border-gray-300 rounded-xl focus:outline-none
            focus:ring-2 focus:ring-blue-500 focus:border-blue-500 appeatace-none''',
            'placeholder' : 'Introduzca el numero del comprobante',
        })
    )

    class Meta:

        model = Rendicion
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'created': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'updated': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }