from django.shortcuts import *
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from .models import Question
from .forms import QuestionForm

def questions(request, page=None):
    '''Displays the list of questions.'''

    if not page:
        page = 1

    # TODO: This can't be hardcoded, has to be an option on the
    # sorting/filtering toolbar.
    results = Question.objects.all().order_by('-when').select_related('author')
    paginator = Paginator(results, settings.QUESTIONS_PER_PAGE)

    context = {
        'questions_list': paginator.page(page),
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

@csrf_protect
def delete_question(request, pk, slug):
    '''
    Delete a question. Only for internal use, the API has another method.
    It's assumed that the user has already confirmed this action.
    '''

    if request.method != 'POST':
        # We should probably show an error message or something here, but
        # this really isn't a view that might be accessed manually by a user.
        return redirect(reverse('questions'))

    question = get_object_or_404(Question, pk=pk, slug=slug)
    user = request.user

    if user.is_authenticated() and user.get_profile().can_edit(question):
        question.delete()
    else:
        context = {
            'error_message': '''It looks like you tried to delete someone else\'s
            question (which you obviously can\'t do.) If you\'re sure this is
            your question, try clearing your browser\'s cookies and logging
            in again.'''
        }

        return render(request, '401.html', status=401, dictionary=context)

    return redirect(request.GET.get('next', reverse('questions')))

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