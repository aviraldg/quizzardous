from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from quizzardous.utils import slugify
from .utils import *

def _get_default_category():
    return Category.objects.get_or_create(name='uncategorised')[0]


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return unicode(self.name)

class Question(models.Model):
    '''Represents a question asked by a user.'''

    class Meta:
        ordering = ['-when']

    question = RichTextField()
    # A slug is actually required, but if it's empty, then it'll automatically
    # be converted from question (see above)
    slug = models.SlugField(default='', blank=True)
    author = models.ForeignKey('auth.User', related_name='questions')
    when = models.DateTimeField(auto_now=True, db_index=True)
    correct_answer = models.TextField()
    category = models.ForeignKey(Category, related_name='questions', default=_get_default_category)
    hearters = models.ManyToManyField('auth.User', related_name='hearted_questions')
    reporters = models.ManyToManyField('auth.User', related_name='reported_questions')

    def toggle_report(self, user):
        if self.reporters.filter(pk=user.pk).exists():
            self.reporters.remove(user)
        else:
            self.reporters.add(user)

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.question)

    def save(self):
        self.full_clean()
        super(self.__class__, self).save(self)

    @models.permalink
    def get_absolute_url(self):
        return ('question', (self.pk, self.slug))

    def __unicode__(self):
        return unicode(self.question)

class Answer(models.Model):
    '''Represents an answer to a question (submitted by a user)'''

    question = models.ForeignKey('Question', related_name='answers')
    answer = models.TextField()
    authors = models.ForeignKey('auth.User', related_name='answers')
    # A 'null' value here represents that the answer has not been reviewed yet
    correct = models.NullBooleanField()

    def __unicode__(self):
        return unicode(self.answer)
