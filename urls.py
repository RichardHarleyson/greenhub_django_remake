"""greenhub_remake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
import greenhub_remake.apps.clients.views as clients_views
import greenhub_remake.apps.core.views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),

	path('', views.index, name='index'),
	# path('', include('greenhub_remake.apps.core.urls')),
	path('contacts/', views.contacts, name='contacts'),
	path('charger_map/', views.charger_map, name='charger_map'),

	path('electrocars/', include('greenhub_remake.apps.electrocars.urls')),
	path('electromoto/', include('greenhub_remake.apps.electromoto.urls')),
	path('testapp/', include('greenhub_remake.apps.testapp.urls')),
	path('testdrive_form', clients_views.testdrive_form, name='testdrive_form'),
	path('callme_form', clients_views.callme_form, name='callme_form'),
]
