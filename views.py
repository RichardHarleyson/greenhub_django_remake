from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	# return HttpResponse('Hello there')
	data = {'data': 'Sir Annoy-0'}
	return render(request, 'index.html', context=data)
