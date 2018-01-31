from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=200)
	bid = models.AutoField(primary_key=True)


class Author(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
