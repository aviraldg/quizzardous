from django import forms
from django.contrib.auth.forms import UserCreationForm as DjUserCreationForm

class UserCreationForm(DjUserCreationForm):
    '''
    A customized version of Django's default UserCreationForm that adds
    fields that we want, like first_name, last_name etc.
    '''

    class Meta(DjUserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'username', 'email',)
