from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    """Represents a question asked by a user."""

    class Meta:
        ordering = ['-when']

    question = models.TextField()
    author = models.ForeignKey('auth.User', related_name='questions')
    when = models.DateTimeField(auto_now=True)
    hearters = models.ManyToManyField('auth.User', related_name='hearted_questions')
    correct_answers = models.TextField()

    # TODO: Tags - custom implementation or django-tagging?

    @property
    def hearts(self):
        try:
            return self.hearters.count()
        except ValueError:
            return 0

    def __unicode__(self):
        return unicode(self.question)

class Answer(models.Model):
    """Represents an answer to a question (submitted by a user)"""

    question = models.ForeignKey('Question', related_name='answers')
    answer = models.TextField()
    author = models.ForeignKey('auth.User', related_name='answers')
