from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Question

def questions(request):
    """Displays the list of questions."""

    context = {
            'questions': Question.objects.all(),
    }

    return render_to_response('questions.html',
        context,
        RequestContext(request))
