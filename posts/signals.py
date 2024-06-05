from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario, Filme, Serie

@receiver(post_save, sender=Usuario)
def update_usuario_signal(sender, instance, created, **kwargs):
    if created:
        instance.email = 'email_atualizado@example.com'
        instance.save(update_fields=['email'])