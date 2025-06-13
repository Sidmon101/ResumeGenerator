from django import forms
from django.core import validators
class UserRegistrationForm(forms.Form):
    GENDER=[('male','MALE'),('female','FEMALE')]
    firstName=forms.CharField(validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(20)])
    lastName= forms.CharField()
    email=forms.EmailField()
    gender=forms.CharField(widget=forms.Select(choices=GENDER))
    password=forms.CharField(widget=forms.PasswordInput)
    ssn=forms.IntegerField()

"""
    def clean(self):
        user_clean_data=super().clean()
        inputFirstName=user_clean_data['firstName']
        if len(inputFirstName) > 20:
          raise forms.ValidationError('The max length is 20 characters')
        inputEmail = user_clean_data['email']
        if (inputEmail.find('@') == -1):
            raise forms.ValidationError('email should contain @')

    def clean_firstName(self):
        inputFirstname=self.cleaned_data['firstName']
        if len(inputFirstname)>20:
            raise forms.ValidationError('The max length is 20 characters')
        return inputFirstname

    def clean_email(self):
        inputEmail=self.cleaned_data['email']
        if(inputEmail.find('@')==-1):
            raise forms.ValidationError('email should contain @')
        return inputEmail
"""