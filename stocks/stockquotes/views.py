from django.shortcuts import render

def home(request):
	import requests
	import json
	#pk_31c5bc7830ff4ea688629886d9b90cf5#
	api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_31c5bc7830ff4ea688629886d9b90cf5")
	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api ="Error.."

	return render(request, 'home.html', {'api': api})

def about(request):
	return render(request, 'about.html', {})	
# Create your views here.
