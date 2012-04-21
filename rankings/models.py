from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from quizzardous import utils

class ScoreCounter(models.Model):
    '''Stores a User's score history (usually month-to-month)'''

    user = models.ForeignKey('auth.User', related_name='score_counters')
    score = models.IntegerField(default=0, db_index=True)
    # when is set to the first of the current month by default, by calling
    # the get_current_month_datetime function from quizzardous.utils
    when = models.DateTimeField(default=utils.get_current_month_datetime,
        db_index=True)

    def __unicode__(self):
        return u'{0} ({1})'.format(self.user.username, self.score)


def _create_scorecounter(sender, instance, created, **kwargs):
    if created:
        counter = ScoreCounter(user=instance)
        counter.save()

signals.post_save.connect(_create_scorecounter, sender=User)
