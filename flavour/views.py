from django.shortcuts import render
from .models import Customer, MealStation

# Create your views here.


def allergy_filter(request):
	return render(request,'flavour/allergy_filter.html')


def meal_station(request):
	# Fetch all meal stations from the database
	meal_stations = MealStation.objects.all()
	# Pass the meal stations to the template context
	context = {'meal_stations': meal_stations}
	return render(request,'flavour/meal_station.html',context)

def meal_station(request, pk):
	# Fetch a specific meal station by its primary key
	meal_station = MealStation.objects.get(id=pk)
	# Pass the meal station to the template context
	context = {'meal_station': meal_station}
	return render(request,'flavour/meal_station_detail.html',context)


def ingredients_map(request):
	context = {'ingredients_map': ingredients_map}
	return render(request,'flavour/ingredients_map.html',context)

def ingredients_map(request,pk):
	ingredients_map = MealStation.objects.get(id=pk)
	context = {'ingredients_map': ingredients_map}
	return render(request,'flavour/ingredients_map.html',context)
 


def about_us(request):	# This view renders the 'about us' page
	# You can add any context data you want to pass to the template here
	return render(request,'flavour/about_us.html')


def meal_planner(request):
	context = {'meal_planner': meal_planner}
	return render(request,'flavour/meal_planner.html',context)

def utensil_hub(request):
	context = {'utensil_hub': utensil_hub}
	return render(request,'flavour/utensil_hub.html',context)

def utensil_hub(request, pk):
	utensil_hub = MealStation.objects.get(id=pk)
	context = {'utensil_hub': utensil_hub}
	return render(request,'flavour/utensil_hub.html',context)	

def login(request):
	return render(request,'flavour/login.html')

