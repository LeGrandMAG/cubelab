from pyexpat import model
from django.forms import ModelForm
from accounts.models import Product, Profile, EarlyUser
from django import forms 


class UserForm(ModelForm):

   class Meta:
      model = Product
      fields = ['nom', 'price', 'cat', 'image', 'battery', 'model', 'imei','fissure1', 'fissure2', 'memory']




class RegisterProfile(ModelForm):

   class Meta:
      model = Profile
      fields = ['prenom', 'nom', 'username', 'email', 'commune', 'phone_number']

class LoginForm(ModelForm):
   class Meta:
      model = Profile
      fields = ['email', 'password']

class EarlyUserForm(ModelForm):

   class Meta:
      model: EarlyUser
      fields = ['nom', 'phone']