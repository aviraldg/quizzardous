from django.shortcuts import render_to_response
from .models import Question

def questions(request):
	'''Displays the list of questions.'''

	context = {
		'questions': Question.objects.all(),
	}

	return render_to_response('index.html', context)
