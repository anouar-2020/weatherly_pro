import requests
from django.shortcuts import render, HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import os
import time
import sys
import pandas as pd
import numpy as np


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn import metrics
# proceed with city


#dataset = pd.read_csv(r'C:\Users\anouar\Desktop\weatherly_pro\weatherly\home\weather_update.csv')
#dataset = dataset.fillna(method='ffill')
#X = dataset[['pressure', 'max_temp', 'min_temp', 'meanhum', 'meancloud',
#             'wind_direction', 'wind_speed']]
#y = dataset['mean_temp']
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
#knn = KNeighborsRegressor(n_neighbors=3)
#knn.fit(X_train, y_train)


def home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    g = GeoIP2()
    location = g.city("1.178.209.3")
    location_country = location["country_name"]
    location_city = location["city"]

    context = {
        "ip": ip,

        "location_country": location_country,
        "location_city": location_city
    }
    """
    url_2="https://countriesnow.space/api/v0.1/countries/population/cities"
    r2=requests.get(url_2).json()
    """
    #df1 = pd.read_json("https://countriesnow.space/api/v0.1/countries/population/cities")



    url ="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1269d0bb1e193b3687dc716729cbc3b1"
    r= requests.get(url.format(location_city)).json()
    #estimated_temp = knn.predict([[float(r['main']['pressure']),float(r['main']['temp_max']),float(r['main']['temp_min']),float(r['main']['humidity']),float(r['clouds']['all']),float(r['wind']['deg']),float(r['wind']['speed'])]])

    city_weather ={
      'city': location_city ,
      'country':location_country,
      'temp':r['main']['temp'],
      'description': r['weather'][0]['description'],
      'icon': r['weather'][0]['icon'] ,

    }
    context={'city_weather':city_weather}

    return render(request,'home/index.html',context)
