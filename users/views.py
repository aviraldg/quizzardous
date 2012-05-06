from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User
from .forms import UserCreationForm

def register(request,template_name='users/register.html'):
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

    return render_to_response(template_name,
        context,
        RequestContext(request))

def user_profile(request, pk, username, template_name='users/user_profile.html'):
    '''Displays a User's profile.'''

    target_user = get_object_or_404(User, pk=pk, username=username)

    context = {
        'target_user': target_user,
    }

    return render_to_response(template_name,
        context,
        RequestContext(request))
