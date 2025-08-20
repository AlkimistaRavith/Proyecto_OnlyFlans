from django import forms
from .models import Producto

class ContactDataForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')


class CompraForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=64)
    correo = forms.EmailField(label="Correo")
    producto = forms.ModelChoiceField(queryset=Producto.objects.none(), label="Producto")
    cantidad = forms.ChoiceField(label="Cantidad")
    fecha_entrega = forms.DateField(
        label="Fecha de entrega",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    direccion = forms.CharField(
        label="Dirección de entrega",
        widget=forms.Textarea(attrs={"rows": 2})
    )

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)

        # Autocompletar si hay usuario
        if usuario and usuario.is_authenticated:
            self.fields['nombre'].initial = usuario.get_full_name() or usuario.username
            self.fields['correo'].initial = usuario.email
            # Mostrar todos los productos
            self.fields['producto'].queryset = Producto.objects.all()
        else:
            # Mostrar solo no premium
            self.fields['producto'].queryset = Producto.objects.filter(is_private=False)

        # Cantidades por defecto para no premium
        self.fields['cantidad'].choices = [(10, "10"), (20, "20")]