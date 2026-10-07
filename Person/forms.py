
from django.contrib.auth.forms import UserCreationForm
from .models import Person
class FormRegistration(UserCreationForm):
    class Meta(UserCreationForm):
        model=Person
        #fields="__all__"
        fields=('cin','email','first_name','last_name','username')
    