from django.db import models

# Create your models here.
class Customer(models.Model):
	genderClass = {
		'M': 'Male',
		'F': 'Female'
	}
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	age = models.IntegerField()
	email = models.EmailField(max_length=100, unique=True)
	phone = models.CharField(max_length=15, unique=True)
	location = models.CharField(max_length=100)
	gender = models.CharField(max_length=1, choices=genderClass)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class MealStation(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	ingredients = models.TextField()
	steps = models.TextField()
	preparation_time = models.IntegerField()
	cooking_time = models.IntegerField()
	total_time = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class ingredientsMap(models.Model):
	#meal_station = models.ForeignKey(MealStation, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.TextField()
	calories_per_unit = models.FloatField(null=True, blank=True)
	protein_per_unit = models.FloatField(null=True, blank=True)
	fat_per_unit = models.FloatField(null=True, blank=True)
	carbohydrates_per_unit = models.FloatField(null=True, blank=True)
	fibre_per_unit = models.FloatField(null=True, blank=True)
	sodium_per_unit = models.FloatField(null=True, blank=True)
	iron_per_unit = models.FloatField(null=True, blank=True)
	calcium_per_unit = models.FloatField(null=True, blank=True)
	vitamin_a_per_unit = models.FloatField(null=True, blank=True)
	vitamin_c_per_unit = models.FloatField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



	def __str__(self):
		return self.name	

class mealPlanner(models.Model):
	MEAL_TIMES = [
		('Breakfast', 'Breakfast'),
		('Lunch', 'Lunch'),
		('Dinner', 'Dinner'),
		('Snack', 'Snack'),
	]
	
	meal = models.ForeignKey(MealStation, on_delete=models.CASCADE)
	date = models.DateField()
	meal_time = models.CharField(max_length=10, choices=MEAL_TIMES)
	reminder = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.meal.name} on {self.date} for ({self.meal_time})"

