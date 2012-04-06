from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .models import Question

def questions(request):
    """Displays the list of questions."""

    context = {
            'questions': Question.objects.all(),
    }

    return render_to_response('questions/questions.html',
        context,
        RequestContext(request))

def question(request, pk, slug):
    '''Displays a specific question. (mainly for search engines)'''

    context = {
        'question': get_object_or_404(Question, pk=pk, slug=slug)
    }

    return render_to_response('questions/question.html',
        context,
        RequestContext(request))