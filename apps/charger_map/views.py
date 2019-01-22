from django.shortcuts import render


def index(request):
	return render(request, 'charger_map/base_charger_map.html')
