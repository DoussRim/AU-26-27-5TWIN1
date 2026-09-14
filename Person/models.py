from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.
def valideCin(value):
    if len(value)!=8:
        raise ValidationError("cin must have 8 characters!")
def valideEmail(value):
    if str(value).endswith('@esprit.tn')== False:
        raise ValidationError(f"Your email {value} must ends with @esprit.tn")
class Person(AbstractUser):
    #cin=models.CharField(primary_key=True,max_length=8,validators=[valideCin])
    cin=models.CharField(primary_key=True,max_length=8)
    email=models.EmailField('Email',max_length=50,unique=True,validators=[valideEmail])
    username=models.EmailField(max_length=20,unique=True)