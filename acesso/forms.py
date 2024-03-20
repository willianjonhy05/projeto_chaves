from .models import Funcionario, Predio
from django.forms import EmailField, CharField, ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



class PredioForm(ModelForm):
    class Meta:
        model = Predio
        fields = '__all__'


class RegistrationForm(UserCreationForm):

    first_name = CharField(max_length=150, label="Nome")
    last_name = CharField(max_length=150, label="Sobrenome")
    email = EmailField(max_length=200, label="Email")
    
    class Meta:
        model = get_user_model()
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ]