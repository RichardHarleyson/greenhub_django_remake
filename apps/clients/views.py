from django.shortcuts import render
from django.http import HttpResponse
from djan.core.mail import send_mail


def testdrive_form(request):
	print(request.POST)
	send_mail(
	'Запись на тест драйв',
	'Имя: %s. Тел: %s'%(request.POST.get('name'), request.POST.get('phone')),
	'greenhub@greenhub.pro',
	['richard.harleyson@gmail.com'],
	fail_silently=False,
	)
	return HttpResponse(True)

def callme_form(request):
	send_mail(
	'Перезвонить',
	'Имя: %s. Тел: %s'%(request.POST.get('name'), request.POST.get('phone')),
	'greenhub@greenhub.pro',
	['richard.harleyson@gmail.com'],
	fail_silently=False,
	)
	return HttpResponse(True)
