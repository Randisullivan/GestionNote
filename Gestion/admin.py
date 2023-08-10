from django.contrib import admin

# Register your models here.

from django.contrib import admin

from Gestion.models import AuthenticationUser,NotesEleve, NoteClasse4eme, NoteClasse3eme, NoteClasse5eme, NoteClasse6eme, AjouterNotes, Classe, Eleve, Matiere, Notes, Professeur, DjangoSession, DjangoAdminLog, AuthGroupPermissions

admin.site.register(AuthenticationUser)
class NoteClasse3emeAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'matiere', 'note')

admin.site.register(NoteClasse3eme, NoteClasse3emeAdmin)


class NoteClasse4emeAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'matiere', 'note')
admin.site.register(NoteClasse4eme,NoteClasse4emeAdmin)

class NoteClasse5emeAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'matiere', 'note')

admin.site.register(NoteClasse5eme, NoteClasse5emeAdmin)


class NoteClasse6emeAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'matiere', 'note')

admin.site.register(NoteClasse6eme, NoteClasse6emeAdmin)

admin.site.register(NotesEleve)






admin.site.register(AjouterNotes)


admin.site.register(Professeur)
admin.site.register(DjangoSession)
admin.site.register(DjangoAdminLog)
admin.site.register(AuthGroupPermissions)

class EleveAdmin(admin.ModelAdmin):
  list_display = ('nom', 'classe')

admin.site.register(Eleve, EleveAdmin)






class MatiereAdmin(admin.ModelAdmin):
  list_display = ('nom', 'coefficient', 'id_prof')

admin.site.register(Matiere, MatiereAdmin)




class EleveInline(admin.TabularInline):
  model = Eleve
  extra = 0  # Pour afficher exactement les élèves associés à la classe, sans formulaire vide

class ClasseAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom']
    inlines = [EleveInline]  # Ajoute l'inline des élèves à la page d'admin de la classe


admin.site.register(Classe, ClasseAdmin)


class NotesAdmin(admin.ModelAdmin):
    list_display = ('valeurs_notes', 'id_eleve', 'id_matiere', 'classe')

admin.site.register(Notes, NotesAdmin)


class AjouterNotes(admin.ModelAdmin):
    list_display = ('classe', 'eleve', 'matiere', 'note')