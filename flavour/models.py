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



