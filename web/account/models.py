from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PUserManager(models.Manager):
	def create_puser(self):
		return self.create()

class PUser(models.Model):
	user = models.OneToOneField(User)
	key = models.AutoField(primary_key=True)
	objects = PUserManager()
