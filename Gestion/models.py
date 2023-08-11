from django.db import models
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

    def __str__(self):
        return f'{self.name}'

class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

    def __str__(self):
        return f'{self.name}'

class AuthenticationUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    profile_photo = models.CharField(max_length=100)
    role = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'authentication_user'

    def __str__(self):
        return f'{self.username}'

class AuthenticationUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthenticationUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authentication_user_groups'
        unique_together = (('user', 'group'),)

    def __str__(self):
        return f'{self.user}'

class AuthenticationUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthenticationUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authentication_user_user_permissions'
        unique_together = (('user', 'permission'),)



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthenticationUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Classe(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'classe'

    def __str__(self):
        return f'{self.nom}'


class Eleve(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'eleve'

    def __str__(self):
        return self.nom



class Matiere(models.Model):
    id_matiere = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, blank=True, null=True)
    coefficient = models.IntegerField(blank=True, null=True)
    id_prof = models.ForeignKey('Professeur', models.DO_NOTHING, db_column='id_prof', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matiere'

    def __str__(self):
        return f'{self.nom}'

class Notes(models.Model):
    id_notes = models.AutoField(primary_key=True)
    id_eleve = models.ForeignKey(Eleve, models.DO_NOTHING, db_column='id_eleve', blank=True, null=True)
    valeurs_notes = models.DecimalField(max_digits=10, decimal_places=2)
    id_matiere = models.ForeignKey(Matiere, models.DO_NOTHING, db_column='id_matiere', blank=True, null=True)
    classe = models.ForeignKey(Classe, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notes'



class Professeur(models.Model):
    id_prof = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professeur'

    def __str__(self):
        return f'{self.nom}'


class AjouterNotes(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True  # Allow Django to manage this table
        db_table = 'ajouter_notes'

    def __str__(self):
        return f'Note de {self.eleve} en {self.matiere} ({self.classe}) : {self.note}'






class Note(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True
    def __str__(self):
        return f'{self.eleve}'


class NoteClasse3eme(Note):
    class Meta:
        managed = True
        db_table = 'note_classe_3eme'

class NoteClasse4eme(Note):
    class Meta:
        managed = True
        db_table = 'note_classe_4eme'

# Ajoutez des modèles similaires pour les autres classes...

class NoteClasse5eme(Note):
    class Meta:
        managed = True
        db_table = 'note_classe_'

class NoteClasse6eme(Note):
    class Meta:
        managed = True
        db_table = 'note_classe'




class NotesEleve(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'notes_eleve'

    def __str__(self):
        return f'Note de {self.eleve} en {self.matiere} : {self.note}'

