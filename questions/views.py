from django.shortcuts import *
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.conf import settings
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

def questions(request, page=None):
    '''Displays the list of questions.'''

    page = 1 if page is None else page

    order_dict = {
        'newest': '-when',
        'oldest': 'when'
    }

    # TODO: This can't be hardcoded, has to be an option on the
    # sorting/filtering toolbar.
    results = Question.objects.all().order_by(order_dict.get(
        request.GET.get('order', 'newest'))).select_related(
        'author').prefetch_related('category', 'reporters', 'hearters')
    paginator = Paginator(results, settings.QUESTIONS_PER_PAGE)

    # TODO: IMPORTANT: The _count bits below *need* to be cached.
    context = {
        'questions_list': paginator.page(page),
        'question_count': Question.objects.count(),
        'answer_count': Answer.objects.count(),
        'user_count': User.objects.count(),
        'order': request.GET.get('order', 'newest'),
        'page': page,
    }

    return render_to_response('questions/questions.html',
        context,
        RequestContext(request))

def question(request, pk, slug):
    '''Displays a specific question. Also allows user to answer a question.'''

    answer_form = None
    question = get_object_or_404(Question, pk=pk, slug=slug)

    if request.method == 'POST':
        if not request.user.is_authenticated():
            return redirect(reverse('login'))
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = Question.objects.get(pk=pk, slug=slug)
            answer.author = request.user
            answer.save()
    else:
        answer_form = AnswerForm()

    context = {
        'question': question,
        'answer_form': answer_form,
        'hide_answer_link': True,
        'answered': question.is_answered(request.user),
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

@csrf_protect
def report_question(request, pk, slug):
    '''
    Report a question. Only for internal use, the API has another method.
    It's assumed that the user has already confirmed this action. If the user
    has already reported this question, then it is "un-reported"
    '''

    if request.method != 'POST':
        # We should probably show an error message or something here, but
        # this really isn't a view that might be accessed manually by a user.
        return redirect(reverse('questions'))

    question = get_object_or_404(Question, pk=pk, slug=slug)
    user = request.user

    if user.is_authenticated() and question.author != user:
        question.toggle_report(user)
    else:
        return render(request, 'questions/report_error.html', status=401)
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

@login_required
def reviews(request):

    # Ugly and counterintuitive, but possibly the best (+fastest) way to do it
    # Basically: "Give me a list of all answers for questions whose author is
    # the current user and which are not reviewed. Now, give me a list of all
    # distinct questions whose answers are in the first list."
    # We're interested in the latter.

    if request.method == 'POST':

        answer = Answer.objects.get(pk=request.POST.get('answer-pk'))
        if not request.user.get_profile().can_edit(answer.question):
            context = {
                'error_message': '''It looks like you tried to review an answer
                on someone else's question.'''
            }

            return render(request, '401.html', status=401, dictionary=context)
        
        correct = None
        if 'mark-correct' in request.POST:
            correct = True
            answer.author.get_profile().add_monthly_score(settings.POINTS_PER_ANSWER)
        elif 'mark-incorrect' in request.POST:
            correct = False

        # If correct is None, then the answer will be assumed as 'not reviewed'
        answer.correct = correct
        answer.save()
    
    answers_list = Answer.objects.filter(question__author = request.user,
        correct=None)
    questions_list = Question.objects.filter(answers__in=answers_list).distinct()

    context = {
        'questions_list': questions_list,
    }

    return render_to_response('questions/reviews.html',
        context,
        RequestContext(request))
