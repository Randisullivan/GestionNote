"""
URL configuration for GestionNotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentication.views
from django.contrib.auth.views import LoginView
import Gestion.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.home_page, name='homePage'),
    path('studentLogin/', authentication.views.login_page, name="studentLogin"),
    path('teacherLogin/', authentication.views.teacher_page, name="teacherLogin"),
    path('logoutS/', authentication.views.logout_student, name='logoutStudent'),
    path('logoutT/', authentication.views.logout_teacher, name='logoutTeacher'),
    path('student/', Gestion.views.student, name='studentPage'),
    path('teacher/', Gestion.views.teacher, name='teacherPage'),
   # path('notes/', Gestion.views.notes_list, name="notes"),
    path('teacherPc/', authentication.views.pc_teacher_page, name="pc_teacher_page"),
    path('teacherSvt/', authentication.views.svt_teacher_page, name="svt_teacher_page"),
    path('teacherMath/', authentication.views.math_teacher_page, name="math_teacher_page"),
    path('teacherEps/', authentication.views.eps_teacher_page, name="eps_teacher_page"),
    path('teacherFrs/', authentication.views.frs_teacher_page, name="frs_teacher_page"),
    path('teacherAng/', authentication.views.ang_teacher_page, name="ang_teacher_page"),
    path('teacherAll/', authentication.views.all_teacher_page, name="all_teacher_page"),
    path('teacherHg/', authentication.views.hg_teacher_page, name="hg_teacher_page"),
    path('teacherMlg/', authentication.views.mlg_teacher_page, name="mlg_teacher_page"),
   # path('listeClasse/', Gestion.views.liste_classes, name="liste_classe"),
   # path('eleveClasse/', Gestion.views.eleves_par_classe, name="eleves_par_classe"),
    path('classes/', Gestion.views.liste_classes, name='liste_classes'),
    path('eleves/<int:classe_id>/',Gestion.views.eleves_par_classe, name='eleves_par_classe'),





]
