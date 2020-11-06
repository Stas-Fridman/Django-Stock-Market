from django import forms
from .models import Stock


class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		# put all of the fiels that we put in the database
		fields = ["ticker"]