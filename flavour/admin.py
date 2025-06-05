from django.contrib import admin
from .models import Customer, MealStation, mealPlanner,ingredientsMap

# Register your models here.
admin.site.register(Customer)
admin.site.register(MealStation)
admin.site.register(ingredientsMap)
admin.site.register(mealPlanner)
