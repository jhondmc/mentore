from django.db import models
from django.contrib.auth.models import User


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    bio = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=120, blank=True, verbose_name='Materia principal')
    phone = models.CharField(max_length=30, blank=True, verbose_name='Teléfono')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Foto de perfil')
    school_name = models.CharField(max_length=150, blank=True, verbose_name='Nombre del colegio')
    city = models.CharField(max_length=100, blank=True, verbose_name='Ciudad')
    # Director de grupo
    is_homeroom_teacher = models.BooleanField(default=False, verbose_name='¿Es director(a) de grupo?')
    homeroom_group = models.CharField(max_length=100, blank=True, verbose_name='Grupo a cargo (dirección)')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Perfil de {self.user.get_full_name() or self.user.username}"
