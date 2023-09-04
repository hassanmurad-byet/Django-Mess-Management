from django import forms
from mess_app import models
from django.contrib.auth.models import User
from mess_app.models import UserInfo


class MemberForm(forms.ModelForm):
    class Meta:
        model = models.Member
        fields ="__all__"
        
class MealForm(forms.ModelForm):
    MealDate = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))

    class Meta:
        model = models.Meal
        fields = "__all__"



class UserForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput() )
    username = forms.CharField(widget=None)

    class Meta():
        model = User
        fields = {'username', 'password', 'email'}
      
        
       