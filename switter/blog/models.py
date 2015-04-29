# libraries
from datetime import datetime
# django libraries
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

	category = models.CharField(max_length=200)

	def __str__(self):
		return self.category

class Blog(models.Model):

	title = models.CharField(max_length=200)
	description = models.TextField()
	body = models.TextField()
	category = models.ForeignKey('Category')
	created = models.DateTimeField(default=datetime.now)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.title

class Coment(models.Model):
	blog = models.ForeignKey('Blog')
	coment = models.TextField()
	created = models.DateTimeField(default=datetime.now)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.coment

