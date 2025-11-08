from django.shortcuts import render , HttpResponse
import requests
import datetime

# Create your views here.

def home (request) :
    return HttpResponse ("hey this is my django server")

def home2 (request) :
    if 'city' in request.POST :
        city =request.POST['city']
    else :
        city = 'Tunis'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=45e80778880ca791836345a2f4ca0e39'
    PARAMS = {'unitd': 'metric'}

    data = requests.get(url,PARAMS).json()
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp'] - 273.15
    day = datetime.date.today
    
    return render (request, 'index.html', { 'description': description, 'icon': icon, 'temp': temp, 'city': city, 'day': day })
