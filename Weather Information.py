# Getting Weather Information
import requests
from pprint import pprint

API_Key = 'VJ2CR7NESMLW3QTSNPXB58KDZ'
city = input("Enter a city: ")
base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/[location]/[date1]/[date2]?key="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()
pprint(weather_data)
