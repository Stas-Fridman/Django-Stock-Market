from django.db import models

class Stock(models.Model):
	# for the symbol of the stock until 10 letters , our database named ticker
	ticker = models.CharField(max_length=10)

	def __str__(self):
		return self.ticker

