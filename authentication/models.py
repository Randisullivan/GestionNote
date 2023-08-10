
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    STUDENT = 'STUDENT'
    TEACHER = 'TEACHER'

    ROLE_CHOICES = (
        (STUDENT, 'étudiant'),
        (TEACHER, 'professeur'),
    )
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

    # Ajoutez le related_name pour résoudre les conflits
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='Groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',  # Nom personnalisé pour éviter le conflit
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='User permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',  # Nom personnalisé pour éviter le conflit
        related_query_name='custom_user',
    )
