from django.shortcuts import render

# Create your views here.


def allergy_filter(request):
	return render(request,'flavour/allergy_filter.html')


def meal_station(request):
	return render(request,'flavour/meal_station.html')


def ingredients_map(request):
	return render(request,'flavour/ingredients_map.html')


def about_us(request):
	return render(request,'flavour/about_us.html')


def meal_planner(request):
	return render(request,'flavour/meal_planner.html')

def utensil_hub(request):
	return render(request,'flavour/utensil_hub.html')	

def login(request):
	return render(request,'flavour/login.html')

