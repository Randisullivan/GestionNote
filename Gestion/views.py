from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Classe, Eleve, Note, NoteClasse3eme, NoteClasse4eme, NoteClasse5eme, NoteClasse6eme
from Gestion.forms import NotesForm, NoteClasse3emeForm, NoteClasse4emeForm, NoteClasse5emeForm, NoteClasse6emeForm
from django.shortcuts import render, get_object_or_404


def is_student(user):
    return user.role == 'STUDENT'

def is_teacher(user):
    return user.role == 'TEACHER'


@login_required(login_url='studentLogin')
@user_passes_test(is_student, login_url='studentPage')
def student(request):
    return render(request, 'Gestion/student.html')

@login_required(login_url='teacherLogin')
@user_passes_test(is_teacher, login_url='teacherPage')
def teacher(request):
    return render(request, 'Gestion/teacher.html')


def liste_classes(request):
    classes = Classe.objects.all()
    return render(request, 'Gestion/liste_classe.html', {'classes': classes})

def eleves_par_classe(request, classe_id):
    eleves = Eleve.objects.filter(classe_id=classe_id)
    classe_nom = Classe.objects.get(id=classe_id).nom
    return render(request, 'Gestion/eleves_par_classe.html', {'eleves': eleves, 'classe_nom': classe_nom})

def ajout_notes3(request):
    notes = NoteClasse3eme.objects.all()
    return render(request, 'Gestion/ajout_notes.html', {'notes': notes})


def create_note3(request):
    if request.method == 'POST':
        form = NoteClasse3emeForm(request.POST)
        if form.is_valid():
            eleve = form.cleaned_data['eleve']
            matiere = form.cleaned_data['matiere']
            note = form.cleaned_data['note']

            # Créer une nouvelle instance du modèle NotesEleve avec les données du formulaire
            notes = NoteClasse3eme(
                eleve=eleve,
                matiere=matiere,
                note=note,

            )

            # Sauvegarder la note dans la base de données
            notes.save()

            return redirect('ajout_notes')
    else:
        form = NoteClasse3emeForm()

    return render(request, 'Gestion/create_note3.html', {'form': form})



def ajout_notes4(request):
    notes = NoteClasse4eme.objects.all()
    return render(request, 'Gestion/ajout_notes4.html', {'notes': notes})


def create_note4(request):
    if request.method == 'POST':
        form = NoteClasse4emeForm(request.POST)
        if form.is_valid():
            eleve = form.cleaned_data['eleve']
            matiere = form.cleaned_data['matiere']
            note = form.cleaned_data['note']

            # Créer une nouvelle instance du modèle NotesEleve avec les données du formulaire
            notes = NoteClasse4eme(
                eleve=eleve,
                matiere=matiere,
                note=note,

            )

            # Sauvegarder la note dans la base de données
            notes.save()

            return redirect('ajout_notes4')
    else:
        form = NoteClasse4emeForm()

    return render(request, 'Gestion/create_note4.html', {'form': form})




def ajout_notes5(request):
    notes = NoteClasse5eme.objects.all()
    return render(request, 'Gestion/ajout_notes5.html', {'notes': notes})


def create_note5(request):
    if request.method == 'POST':
        form = NoteClasse5emeForm(request.POST)
        if form.is_valid():
            eleve = form.cleaned_data['eleve']
            matiere = form.cleaned_data['matiere']
            note = form.cleaned_data['note']

            # Créer une nouvelle instance du modèle NotesEleve avec les données du formulaire
            notes = NoteClasse5eme(
                eleve=eleve,
                matiere=matiere,
                note=note,

            )

            # Sauvegarder la note dans la base de données
            notes.save()

            return redirect('ajout_notes5')
    else:
        form = NoteClasse5emeForm()

    return render(request, 'Gestion/create_note5.html', {'form': form})



def ajout_notes6(request):
    notes = NoteClasse6eme.objects.all()
    return render(request, 'Gestion/ajout_notes6.html', {'notes': notes})


def create_note6(request):
    if request.method == 'POST':
        form = NoteClasse6emeForm(request.POST)
        if form.is_valid():
            eleve = form.cleaned_data['eleve']
            matiere = form.cleaned_data['matiere']
            note = form.cleaned_data['note']

            # Créer une nouvelle instance du modèle NotesEleve avec les données du formulaire
            notes = NoteClasse6eme(
                eleve=eleve,
                matiere=matiere,
                note=note,

            )

            # Sauvegarder la note dans la base de données
            notes.save()

            return redirect('ajout_notes6')
    else:
        form = NoteClasse4emeForm()

    return render(request, 'Gestion/create_note6.html', {'form': form})


from django.shortcuts import render
from .models import Eleve, NoteClasse3eme, NoteClasse4eme, NoteClasse5eme, NoteClasse6eme

from django.shortcuts import render, get_object_or_404
from .models import Eleve, NoteClasse3eme, NoteClasse4eme, NoteClasse5eme, NoteClasse6eme

