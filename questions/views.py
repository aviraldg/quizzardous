from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Question
from .forms import QuestionForm

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

@login_required
def ask(request):
    '''
    Displays a form to ask a question and creates a new question if validated.
    '''

    form = None

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect(question.get_absolute_url())
    else:
        form = QuestionForm()

    return render_to_response('questions/ask.html',
        {'form': form},
        RequestContext(request))