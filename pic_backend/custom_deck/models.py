from django.db import models

# Create your models here.
class Card(models.Model):
	present = models.TextField()
	uses_names = models.BooleanField(default=False)

	def __str__(self):
		return self.present

class Deck(models.Model):
	title = models.CharField(max_length=21, unique=True, primary_key=True)
	cards = models.ManyToManyField(Card, blank=True, related_name="cards")

	def __str__(self):
		return self.title