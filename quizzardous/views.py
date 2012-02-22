from django.shortcuts import render_to_response

def homepage(request):
	'''The homepage view.

	note: This is not static because it also handles logins.
	'''

	return render_to_response('homepage.html', {})