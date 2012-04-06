from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User
from .forms import UserCreationForm

def register(request):
    '''Renders the registration form and allows a user to register.'''

    form = None

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('homepage'))
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }

    return render_to_response('users/register.html',
        context,
        RequestContext(request))

def user_profile(request, pk, username):
    '''Displays a User's profile.'''

    target_user = get_object_or_404(User, pk=pk, username=username)

    context = {
        'target_user': target_user,
    }

    return render_to_response('users/user_profile.html',
        context,
        RequestContext(request))
