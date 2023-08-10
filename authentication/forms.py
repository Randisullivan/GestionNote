from django import forms

CLASSES_CHOICES = [
    ('6eme', '6eme'),
    ('5eme', '5eme'),
    ('4eme', '4eme'),
    ('3eme', '3eme'),
]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    classe = forms.ChoiceField(choices=CLASSES_CHOICES,  label="Votre classe")
    Numero = forms.IntegerField()
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label="Mot de passe")

MATIERES_CHOICES = [
    ('PC', 'PC'),
    ('SVT', 'SVT'),
    ('MATH', 'MATH'),
    ('FRS', 'FRS'),
    ('MLG', 'MLG'),
    ('ANG', 'ANG'),
    ('ALL', 'ALL'),
    ('HG', 'HG'),
    ('EPS', 'EPS'),
]
class teachForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom de professeur")
    matricule = forms.CharField(max_length=63, label="Matricule")
    matiere = forms.ChoiceField(choices=MATIERES_CHOICES, label="Matière enseigné")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label="Mot de passe")

