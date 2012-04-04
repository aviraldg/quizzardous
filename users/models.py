from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):

    user = models.OneToOneField(User)

    # Placeholder
    def get_rank(self):
        return 1

    # Placeholder
    def get_score(self):
        return 1

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
