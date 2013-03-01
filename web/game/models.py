from django.db import models

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Cards(models.Model):
	card_name = models.CharField(max_length=64)
	card_effect = models.CharField(max_length=64)

class Cards_to_Users(models.Model):
	uid = models.IntegerField(primary_key=True)
	card_id = models.IntegerField()

class Decks(models.Model):
	uid = models.IntegerField(primary_key=True)
	deck_id = models.IntegerField()
	card_ids = models.CharField(max_length=400)

	class Meta:
		unique_together = ('uid','deck_id')
