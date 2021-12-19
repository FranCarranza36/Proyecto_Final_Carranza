from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class FutbolistasFormulario(forms.Form):
    nombre = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, ,]+', 'title':'Solo se permiten letras'}))
    apellido = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, , ]+', 'title':'Solo se permiten letras'}))
    edad = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'type':'number','max':99,'class':'form-control' , 'autocomplete': 'off'}))
    
class BasquetbolistasFormulario(forms.Form):
    nombre = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, ,]+', 'title':'Solo se permiten letras'}))
    apellido = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, ,]+', 'title':'Solo se permiten letras'}))
    triples = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9 ]+', 'title':'Solo se permiten números'}))
    
class TenistasFormulario(forms.Form):
    nombre = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, ,]+', 'title':'Solo se permiten letras'}))
    apellido = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, ,]+', 'title':'Solo se permiten letras'}))
    titulos = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'type':'number','max':103,'class':'form-control' , 'autocomplete': 'off'}))

class LoginAuthenticationForm(AuthenticationForm):
    username = forms.CharField(required=True, label= 'Usuario')
    password = forms.CharField(required=True, label= 'Contraseña', widget=forms.PasswordInput)
    
    error_messages = {
        'invalid_login': 'Credenciales erróneas. Por favor, inténtalo de nuevo.',
        'inactive': 'El usuario se encuentra bloqueado. Por favor, entre en contacto con el Administrador.'
    }
      
class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField(required=True, label= 'Usuario')
    email = forms.EmailField(required=True, label= 'E-mail')
    password1 = forms.CharField(required=True, label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, label= '', widget=forms.PasswordInput)
    
    error_messages = {
        'password_mismatch': 'Las contraseñas introducidas no coinciden.',
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Se permiten letras, dígitos y los símbolos @/./+/-/_'
        self.fields['password1'].help_text = 'No se permite similitud con información personal. Debe tener al menos 8 caracteres y no se permiten números únicamente'
        self.fields['password2'].help_text = 'Repite la contraseña.'
    
    class Meta:
         model = User
         fields = ['username', 'email', 'password1', 'password2']

class EditarUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label= 'Nuevo E-mail')
    password1 = forms.CharField(required=True, label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, label= '', widget=forms.PasswordInput)
    
    error_messages = {
        'password_mismatch': 'Las contraseñas introducidas no coinciden.',
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'No se permite similitud con información personal. Debe tener al menos 8 caracteres y no se permiten números únicamente'
        self.fields['password2'].help_text = 'Repita la contraseña.'
    
    class Meta:
         model = User
         fields = ['email', 'password1', 'password2']

class AvatarForm(forms.Form):
    avatar = forms.ImageField()