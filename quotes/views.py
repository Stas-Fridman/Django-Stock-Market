from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages


def home(request):
	import requests
	import json

	if request.method=='POST':
		# name of the input form in base.html 
		ticker = request.POST['ticker']
		# the api key : pk_aec1d3d5b81d4099890650585f1bbcb0	
		# the url that we take from - conect the api  + ticker symbol 
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_aec1d3d5b81d4099890650585f1bbcb0")
		try:
			api = json.loads(api_request.content) 
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api': api})

	else:
		return render(request, 'home.html', {'ticker': "Enter A Ticker Symbol Above.."})
	



def about(request):
	return render(request, 'about.html', {})

def chart(request):
	return render(request, 'Chart.html', {})


def add_stock(request):
	import requests
	import json

	if request.method=='POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock Has Been Added!"))
			return redirect('add_stock')

	else:
		# all the data base 
		ticker = Stock.objects.all()
		# empty list
		output = []
		# we do for loop because the ticker represent all objects and we want to do it one-by-one
		# it will loop for each object in objects and make an api call 
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_aec1d3d5b81d4099890650585f1bbcb0")
			try:
				# decode json file 
				api = json.loads(api_request.content) 
				# add to the list , because we need to save the data somehow
				output.append(api)
			except Exception as e:
				api = "Error..."
		return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

# stock_id is passed through urls.py
def delete_stock(request, stock_id):
	# primry key = id number
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock Has Been Deleted !!"))
	return redirect(add_stock)

	