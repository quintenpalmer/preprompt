from django.db import models

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name
