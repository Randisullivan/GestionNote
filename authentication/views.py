from . import forms
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from Gestion.models import Matiere



# Create your views here.
'''
class LoginPage(View):
    form_class = forms.LoginForm
    template_name = 'authentication/login.html'
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(
            request, self.template_name, {'form': form, 'message': message}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                    username=form.cleaned_data['username'],
                    classe=form.cleaned_data['classe'],
                    Numero=form.cleaned_data['Numero'],
                    password=form.cleaned_data['password'],
                )
            if user is not None:
                    login(request, user)
                    return redirect('home')
            else:
                    message = 'Identifiants invalides.'

        return render(
            request, self.template_name, {'form': form, 'message': message}
        )'''



def home_page(request):
    return render(request, 'authentication/homePage.html')


def logout_student(request):
    logout(request)
    return redirect('studentLogin')


def logout_teacher(request):
    logout(request)
    return redirect('teacherLogin')




def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                classe=form.cleaned_data['classe'],
                Numero=form.cleaned_data['Numero'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('studentPage')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'authentication/stuDlogin.html', {'form': form, 'message': message}
    )

def teacher_page(request):
    form = forms.teachForm()
    message = ''
    if request.method == 'POST':
        form = forms.teachForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                matricule=form.cleaned_data['matricule'],
                matiere=form.cleaned_data['matiere'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                matiere = form.cleaned_data['matiere']
                if matiere == 'PC':
                    return redirect('pc_teacher_page')
                elif matiere == 'SVT':
                    return redirect('svt_teacher_page')
                elif matiere == 'MATH':
                    return redirect('math_teacher_page')
                elif matiere == 'EPS':
                    return redirect('eps_teacher_page')
                elif matiere == 'FRS':
                    return redirect('frs_teacher_page')
                elif matiere == 'ANG':
                    return redirect('ang_teacher_page')
                elif matiere == 'ALL':
                    return redirect('all_teacher_page')
                elif matiere == 'HG':
                    return redirect('hg_teacher_page')
                elif matiere == 'MLG':
                    return redirect('mlg_teacher_page')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'authentication/teacHlogin.html', {'form': form, 'message': message}
    )




def pc_teacher_page(request):

    return render(request, 'Gestion/pc_teacher_page.html')

def svt_teacher_page(request):
    return render(request, 'Gestion/svt_teacher_page.html')


def math_teacher_page(request):
    return render(request, 'Gestion/math_teacher_page.html')


def eps_teacher_page(request):
    return render(request, 'Gestion/eps_teacher_page.html')


def frs_teacher_page(request):
    return render(request, 'Gestion/frs_teacher_page.html')


def ang_teacher_page(request):
    return render(request, 'Gestion/ang_teacher_page.html')


def all_teacher_page(request):
    return render(request, 'Gestion/all_teacher_page.html')


def hg_teacher_page(request):
    return render(request, 'Gestion/hg_teacher_page.html')


def mlg_teacher_page(request):
    return render(request, 'Gestion/mlg_teacher_page.html')

