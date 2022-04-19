from django import forms

class SignupForm(forms.Form):
    nom = forms.CharField(max_length=12, required=True)
    prenom = forms.CharField(max_length=12, required=True)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    confirm = forms.CharField(max_length=6, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())


MOTIFS = (
    ("Je souhaite poser une réclamation"),
    ("Je souhaite commander un service supplémentaire"),
    ("Je souhaite en savoir plus sur une suite"),
    ("J'ai un souci avec cette application"),
)

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=12, required=True)
    prenom = forms.CharField(max_length=12, required=True)
    email = forms.EmailField()
    motif = forms.ChoiceField(choices=MOTIFS)
    message = forms.Textarea()
