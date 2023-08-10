from django.contrib import admin

# Register your models here.

from django.contrib import admin

from Gestion.models import AuthenticationUser, Classe, Eleve, Matiere, Notes, Professeur, DjangoSession, DjangoAdminLog, AuthGroupPermissions


admin.site.register(AuthenticationUser)



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
