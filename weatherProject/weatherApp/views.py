from django.shortcuts import render, HttpResponse
import requests
import datetime
from django.contrib import messages
from requests.exceptions import RequestException


# Create your views here.

def home(request):
    return HttpResponse("hey this is my django server")

def home2 (request) :
    if 'city' in request.POST :
        city =request.POST['city']
    else :
        city = 'Tunis'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=45e80778880ca791836345a2f4ca0e39'
    PARAMS = {'units': 'metric'}

    try :
        data = requests.get(url,PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = round(data['main']['temp'], 1)
        day = datetime.date.today()
        return render (request, 'index.html', { 'description': description, 'icon': icon, 'temp': temp, 'city': city, 'day': day, 'exception_occured' : False })
    except KeyError:
        exception_occurrred = True
        message.error (request, 'data entrée est non valide pour API')
        day = datetime.date.today()
        return render (request, 'index.html', {'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'indore' , 'exception_occurred':exception_occurred } )
               
