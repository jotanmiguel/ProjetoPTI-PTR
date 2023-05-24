from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class PasswordChangingForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangingForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = "Password Antiga"
        self.fields['new_password1'].label = "Password Nova"
        self.fields['new_password2'].label = "Repita a Password"

        
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    

    class Meta:
        model = User
        labels = {
        "old_password":  "Palavra-Passe antiga",
        "new_password1": "Nova Palavra-Passe",
        "new_password2": "Repita a Palavra-Passe",
        }
        fields = ('old_password', 'new_password1', 'new_password2')
    
