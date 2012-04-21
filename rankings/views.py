from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
from django.conf import settings
from quizzardous.utils import get_current_month_datetime
from .models import ScoreCounter

def rankings(request):

    rankings = ScoreCounter.objects.filter(
        when=get_current_month_datetime()).select_related(
        'user').order_by('-score')

    paginator = Paginator(rankings, settings.USERS_PER_PAGE)

    # TODO: Allow rankings other than the top "N" to be seen?
    context = dict(rankings=paginator.page(1))

    return render_to_response('rankings/rankings.html', context,
        RequestContext(request))
