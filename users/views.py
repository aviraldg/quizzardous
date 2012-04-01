from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User

# NOTE: This code may change *significantly* once we start using user profiles
# from django-socialregistration. For now, this mainly serves as a placeholder
# while things get sorted out.

def user_profile(request, pk, username):
    '''Displays a User's profile.'''

    target_user = get_object_or_404(User, pk=pk, username=username)

    context = {
        'target_user': target_user,
    }

    return render_to_response('user_profile.html', context)
