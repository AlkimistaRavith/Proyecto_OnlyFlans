from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        help_texts = {
            'username': 'Ingrese un nombre de usuario único. Solo letras, números y @/./+/-/_',
            'password1': 'La contraseña debe tener al menos 8 caracteres y no ser muy común.',
            'password2': 'Repita la misma contraseña para confirmarla.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Quitar mensajes por defecto de Django
        self.fields['password1'].help_text = 'Debe tener al menos 8 caracteres y no ser muy común.'
        self.fields['password2'].help_text = 'Repita la contraseña para confirmarla.'
        
        # Estilo Bootstrap
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})