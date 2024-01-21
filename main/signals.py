from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from main.models import UserProfile

@receiver(post_save, sender=User)
def create_profile(created, sender, instance , *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)
