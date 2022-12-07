from django.db import models


class Cafes(models.Model):
	name = models.CharField(max_length=500, unique=True)
	map_url = models.CharField(max_length=500)
	img_url = models.CharField(max_length=500)
	location = models.CharField(max_length=250)
	has_sockets = models.BooleanField(default=False)
	has_toilet = models.BooleanField(default=False)
	has_wifi = models.BooleanField(default=False)
	can_take_calls = models.BooleanField(default=False)
	seats = models.CharField(max_length=250)
	coffee_price = models.CharField(max_length=250)

	def __str__(self):
		return self.name
