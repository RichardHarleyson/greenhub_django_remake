from django.db import models

class Clients_main(models.Model):
	client_name = models.charfield(maxlength=50, null=True, blank=True)
	client_phone = models.charfield(maxlenght=20)
	client_stage = models.charfield(maxlength=20, null=True, blank=True)
	client_status = models.booleanfield()
	client_join_date = models.DateTimeField()
