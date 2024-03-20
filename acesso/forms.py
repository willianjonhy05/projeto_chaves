from .models import Funcionario
from django.forms import EmailField, CharField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class RegistrationForm(UserCreationForm):

    first_name = CharField(max_length=150, label="Nome")
    last_name = CharField(max_length=150, label="Sobrenome")
    email = EmailField(max_length=200, label="Email")
    
    class Meta:
        model = get_user_model()
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ]