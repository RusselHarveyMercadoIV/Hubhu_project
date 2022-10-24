from django.forms import ModelForm
from django import forms

from registration.models import User


class RegistrationForm(ModelForm):
    type = 'D'
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        exclude = ['type', 'profile_pic']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type