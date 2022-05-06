from django import forms

class SignupForm(forms.Form):
    nom = forms.CharField(max_length=12, required=True)
    prenom = forms.CharField(max_length=12, required=True)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    


