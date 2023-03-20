from django.db import models

# Create your models here.
class Produto(models.Model):
	name = models.CharField('Nome do produto', max_length=1000)
	price = models.CharField('Preço do produto', max_length=10)
	#code = models.TextField()
	#img = models.ImageField(upload_to = "images/")
	#file = models.FileField(upload_to = "files/")
	#slug = models.SlugField(max_length=1000)
	#category = models.CharField(max_length=500)
	#Author = models.CharField(max_length=500)
	date = models.DateTimeField('Data de produção')

	def __str__(self):
		return self.name
