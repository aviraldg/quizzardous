from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator
from django.conf import settings
from .models import Question

def questions(request, page=1):
    '''Displays the list of questions.'''

    # TODO: This can't be hardcoded, has to be an option on the
    # sorting/filtering toolbar.
    results = Question.objects.all().order_by('-when').select_related('author')
    paginator = Paginator(results, settings.QUESTIONS_PER_PAGE)

    context = {
        'questions': paginator.page(page),
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