from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Classe, Eleve
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