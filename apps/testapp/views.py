from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	content = {'header' : 'Question', 'lable1' : 'This is a form', 'btn_text' : 'Button?', 'id' : 3}
	return render(request, 'testapp/base_testapp.html', context={'content' : content})

def testapp_method(request):
	return HttpResponse('Got it!')
