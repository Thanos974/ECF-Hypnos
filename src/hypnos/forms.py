from django import forms


MOTIFS = (
  ("1", "Je souhaite poser une réclamation"),
  ("2", "Je souhaite commander un service supplémentaire"),
  ("3", "Je souhaite en savoir plus sur une suite"),
  ("4", "J'ai un souci avec cette application"),
)


class SignupForm(forms.Form):
  last_name = forms.CharField(max_length=10, required=False)
  first_name = forms.CharField(max_length=50)
  email = forms.EmailField()
  password = forms.CharField(min_length=8)
  motif = forms.ChoiceField(choices=MOTIFS)