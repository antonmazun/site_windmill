from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime




class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    date  = forms.DateTimeField(initial=datetime.date.today)
    people  = forms.IntegerField(max_value= 100)


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True , widget = forms.TextInput(attrs= {'placegolder' : 'Введіть емейл'}))
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required= True)
#
#
#     class Meta:
#         model = User
#         fields = ('first_name' , 'last_name' , 'email' , 'username' , 'password1' , 'password2')
#
#         def clean_mail(self):
#             email = self.cleaned_data['email']
#             try:
#                 User._default_manager.get(email = email)
#             except User.DoesNotExist:
#                 return email
#             raise forms.ValidationError('Такий емайл вже зареэстрований')
#
#         def save(self , commit = True):
#             user = super(RegistrationForm , self).save(commit = False)
#             if commit:
#                 user.is_active = False
#                 user.save()
#                 return user
#
#
#
#
#
