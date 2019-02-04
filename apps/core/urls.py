from django.urls import path, include
from . import views
import greenhub_remake.apps.clients.views as c_views
# import greenhub_remake.apps.clients

app_name = 'core'
urlpatterns = [
	path('', views.index, name='index'),
	path('testdrive_form', c_views.testdrive_form, name='testdrive_form'),
]
