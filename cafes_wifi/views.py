from django.shortcuts import render
from .models import Cafes


def home(request):
	cafes = Cafes.objects.all()
	context = {'cafes': cafes}
	return render(request, 'index.html', context)


def city_details(request, cafe_id):
	cafes = Cafes.objects.get(id=cafe_id)
	context = {'cafes': cafes}
	return render(request, 'cities.html', context)
