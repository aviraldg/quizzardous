from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	'''Represents a question asked by a user.'''

	content = models.TextField()
	author = models.ForeignKey('auth.User', related_name='questions')
	when = models.DateTimeField(auto_now=True)
	hearters = models.ManyToManyField('auth.User', related_name='hearted_questions')
	correct_answers = models.TextField()
	
	# TODO: Tags - custom implementation or django-tagging?

	@property
	def hearts(self):
		return self.hearters.count()

	def __unicode__(self):
		return unicode(self.content)

class Answer(models.Model):
	'''Represents an answer to a question (submitted by a user)'''

	question = models.ForeignKey('Question', related_name='answers')
	answer = models.TextField()
	author = models.ForeignKey('auth.User', related_name='answers')
