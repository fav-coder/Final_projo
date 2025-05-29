from django.urls import path
from . import views

urlpatterns = [
path('about_us/',views.about_us, name="about_us"),
path('allergy_filter/',views.allergy_filter, name="allergy_filter"),
path('meal_station/',views.meal_station, name="meal_station"),
path('ingredients_map/',views.ingredients_map, name="ingredients_map"),
path('meal_planner/',views.meal_planner, name="meal_planner"),
path('utensil_hub/',views.utensil_hub, name="utensil_hub"),
path('login/',views.login, name="login"),

]


