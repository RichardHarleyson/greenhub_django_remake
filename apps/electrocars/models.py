from django.db import models

# veh_title
# veh_comp
# veh_vin
# veh_year
# veh_mileage
# veh_color_in
# veh_color
# veh_price
# veh_photo
# veh_battery

class Vehicle(models.Model):
	veh_title = models.CharField(max_length=100)
	veh_comp = models.CharField(max_length=10, blank=True)
	veh_vin = models.CharField(max_length=30, unique=True)
	veh_year = models.CharField(max_length=12, blank=True)
	veh_mileage = models.CharField(max_length=20, blank=True)
	veh_color_in = models.CharField(max_length=30, blank=True)
	veh_color = models.CharField(max_length=30)
	veh_price = models.CharField(max_length=10)
	veh_photo = models.CharField(max_length=250, blank=True)
	veh_battery = models.CharField(max_length=10, blank=True)
	veh_info = models.CharField(max_length=100, blank=True)
	veh_type = models.CharField(max_length=10)
	veh_status = models.PositiveSmallIntegerField(default=0)
	add_date = models.DateTimeField(auto_now_add=True)
