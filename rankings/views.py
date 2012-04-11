from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import ScoreCounter
from quizzardous.utils import get_current_month_datetime

def rankings(request):

    rankings = ScoreCounter.objects.filter(
        when=get_current_month_datetime()).select_related(
        'user').order_by('-score')

    context = dict(rankings=rankings)

    return render_to_response('rankings/rankings.html', context,
        RequestContext(request))
