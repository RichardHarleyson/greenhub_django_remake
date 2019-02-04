from django.urls import path, include
from . import views

app_name = 'clients'
urlpatterns = [
	path('testdrive_form', views.testdrive_form, name='testdrive_form'),
	path('callme_form', views.callme_form, name='callme_form'),
]
