from django import forms


MOTIFS = (
  ("1", "Je souhaite poser une réclamation"),
  ("2", "Je souhaite commander un service supplémentaire"),
  ("3", "Je souhaite en savoir plus sur une suite"),
  ("4", "J'ai un souci avec cette application"),
)


class ContactForm(forms.Form):
  last_name = forms.CharField(max_length=100, required=False)
  first_name = forms.CharField(max_length=50)
  email = forms.EmailField()
  motif = forms.ChoiceField(choices=MOTIFS)
  message= forms.CharField(widget=forms.Textarea)