from django.shortcuts import render, redirect
import requests
import json
from .models import Stocks
from .forms import StockForm
from django.contrib import messages
import quotes.config_api 

# Create your views here.

def home(request):
    # pk_940d7b4687ce49b985469f99c1f3b460

    

    if request.method == 'POST':

        ticker = request.POST['ticker']

        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker +"/quote?token="+ quotes.config_api.api_key)

        try:

            api = json.loads(api_request.content)

        except Exception as e:
            api = "error"
        
        return render(request, 'home.html', {"api": api})


    else:
        return render(request, 'home.html', {"ticker": "Enter a Ticker Symbol Above..."})


    
def about(request):
    return render(request, 'about.html')

def add_stock(request):

    if request.method == 'POST':
        form = StockForm(request.POST or None)
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ request.POST['ticker'] +"/quote?token=" + quotes.config_api.api_key)
        


        try:
            
            api = json.loads(api_request.content)
            if form.is_valid():
                print("lol")
                form.save()
                messages.success(request, ("Stock has been added"))
                return redirect('add_stock')
        
        except Exception as e:
            messages.success(request, ("Can't find requested ticker"))


        
    ticker = Stocks.objects.all()
    output = []
    for ticker_item in ticker:
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ str(ticker_item) +"/quote?token=" + quotes.config_api.api_key)

        try:

            api = json.loads(api_request.content)
            output.append(api)

        except Exception as e:
            api = "error"
        
    return render(request, 'add_stock.html', {"ticker": ticker, "output":output})

def delete_stock(request, stock_id):

    item = Stocks.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ('Stock has been Deleted'))
    return redirect(add_stock)