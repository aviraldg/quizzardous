from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rankings.models import ScoreCounter
from quizzardous.utils import get_current_month_datetime

class UserProfile(models.Model):

    user = models.OneToOneField(User, related_name='profile')

    def can_edit(self, question):
        return self.user.is_staff or question.author == self.user

    def add_monthly_score(self, value):
        counter = ScoreCounter.objects.get_or_create(user=self.user,
            when=get_current_month_datetime())[0]

        counter.score += value
        counter.save()

    def get_monthly_score(self):
        '''
        Gets the score from this month's ScoreCounter, or creates it if it
        doesn't already exist.
        '''
        
        counter = ScoreCounter.objects.get_or_create(user=self.user,
            when=get_current_month_datetime())[0]
        
        return counter.score

    def get_monthly_rank(self):
        '''
        Gets the score from this month's ScoreCounter, or creates it if it
        doesn't already exist.
        '''

        now_month = get_current_month_datetime()

        counter = ScoreCounter.objects.get_or_create(user=self.user,
            when=now_month)[0]

        # a User's rank is also essentially a count of how many Users have a
        # score greater than the current user + 1

        return ScoreCounter.objects.order_by('-score').filter(when__gte=now_month,
            score__gt=counter.score).count() + 1


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
