from django.shortcuts import render


def index(request):
	return render(request, 'contacts/base_contacts.html')
