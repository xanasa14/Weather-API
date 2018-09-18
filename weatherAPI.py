import requests
from pprint import pprint
def main():
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=New%20Jersey&appid=cf387195d4b97836eaf354d24051b5c4&units=imperial")
    weather = response.json()
    print("The weather for ", weather['name'])
    print(weather['main']['temp'])
    print("Its gonna be",weather['weather'][0]['description'])


if (__name__ == '__main__'):
    main()

#create a web services
