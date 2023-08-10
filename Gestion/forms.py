from django import forms
from Gestion.models import Notes, NoteClasse3eme, NoteClasse4eme, NoteClasse5eme, NoteClasse6eme

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'


class NoteClasse3emeForm(forms.ModelForm):
    class Meta:
        model = NoteClasse3eme
        fields = '__all__'


class NoteClasse4emeForm(forms.ModelForm):
    class Meta:
        model = NoteClasse4eme
        fields = '__all__'


class NoteClasse5emeForm(forms.ModelForm):
    class Meta:
        model = NoteClasse5eme
        fields = '__all__'


class NoteClasse6emeForm(forms.ModelForm):
    class Meta:
        model = NoteClasse6eme
        fields = '__all__'

