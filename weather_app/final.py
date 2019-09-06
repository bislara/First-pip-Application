#!/usr/bin/env python

import requests                             #getting data from weather.com using the weather api
from datetime import date                   #getting the current date
from lxml import html                       # import only html class

# url to scrape data from
url = 'https://weather.com/en-IN/'

# path to particular element
path = '/html/body/script[6]/text()'

# get response object
response = requests.get(url)

# get byte string
byte_data = response.content

# get filtered source code
source_code = html.fromstring(byte_data)

# jump to preferred html element
tree = source_code.xpath(path)

# # print texts in first element in list
# print(tree[0])
api_key=""
for i in range(32,64):
    api_key=api_key+tree[0][i]
print(api_key)


place="Rourkela Odisha"                     #default place
today = date.today()                        #default date
type_of_forecast="today"                    #default type of forecast

p=input("Enter place in details ie place and state :")         #user place input
d=input("Enter date in yyyy-mm-dd :")                          #user date input
print("Enter type of forecast you want :")                     #options for type of forecast
print("1.Today")
# print("2.Hourly")
print("2.5-day")
print("3.10-day")
print("4.Weekend")
# print("5.Monthly")
t=input("Enter the type:")                                     #user input for type of forecast

if p!="":
    place=p
if d!="":
    today=d
if t=="Today" or t=="today":
    type_of_forecast=t
elif t=="Hourly" or t=="hourly":
    type_of_forecast=t
elif t=="5-day" or t=="5 day":
    type_of_forecast=t
elif t=="10-day" or t=="10 day":
    type_of_forecast=t
elif t=="Weekend" or t=="weekend":
    type_of_forecast=t
elif t=="Monthly" or t=="monthly":
    type_of_forecast=t

#get the coordinates of the place
request1= requests.get("https://api.weather.com/v3/location/search?query="+ str(p)+"&locationType=city&language=en-IN&format=json&apiKey="+api_key)
place_data=request1.json()
# print(place_data["location"]["latitude"][0])
# print(place_data["location"]["longitude"][0])


def today_data(data1):
    print("The current weather of " + str(place_data["location"]["address"][0]) + " is :-")
    print("  Co-ordinate - latitude :" + str(place_data["location"]["latitude"][0])+ " longitude :" + str(place_data["location"]["longitude"][0]))
    print("  Temperature :" + str(data1["vt1observation"]["temperature"])+" deg C " +str(data1["vt1observation"]["phrase"])+ " as of "+str(data1["vt1observation"]["observationTime"]))
    print("  Feels like "+str(data1["vt1observation"]["feelsLike"]) + " deg C" )
    print("  Dew point :"+str(data1["vt1observation"]["dewPoint"])+ " deg")
    print("  Humidity :" +str(data1["vt1observation"]["humidity"])+" %")
    print("  UV Index " +str(data1["vt1observation"]["uvIndex"]) +" out of 10 which is "+str(data1["vt1observation"]["uvDescription"]))
    print("  Wind :"+ str(data1["vt1observation"]["windDirCompass"])+" " + str(data1["vt1observation"]["windSpeed"])+ " km/hr")
    print("  Visibility :"+str(data1["vt1observation"]["visibility"])+ " km")
    print("  Pressure: "+str(data1["vt1observation"]["altimeter"])+"mb "+ str(data1["vt1observation"]["barometerTrend"]))


def day5_data(data):
        print("Co-ordinate - latitude :" + str(place_data["location"]["latitude"][0])+ " longitude :" + str(place_data["location"]["longitude"][0]))
        print("Weather of "+str(place_data["location"]["address"][0])+" for the next 5 days are :-")
        for i in range(0,5):
            print(str(i+1)+"- "+data["vt1dailyForecast"]["dayOfWeek"][i])
            print("   Description : Day- "+str(data["vt1dailyForecast"]["day"]["phrase"][i])+" ,Night- "+str(data["vt1dailyForecast"]["night"]["phrase"][i]))
            print("   Temperature : Max- "+str(data["vt1dailyForecast"]["day"]["temperature"][i])+" deg C, Min- "+str(data["vt1dailyForecast"]["night"]["temperature"][i])+ " deg C")
            print("   Precipitation : Day- "+str(data["vt1dailyForecast"]["day"]["precipPct"][i])+"% " +str(data["vt1dailyForecast"]["day"]["precipType"][i]) + " Night- "+str(data["vt1dailyForecast"]["night"]["precipPct"][i])+"% "+str(data["vt1dailyForecast"]["day"]["precipType"][i]))
            print("   Wind : Day- "+ str(data["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(data["vt1dailyForecast"]["day"]["windSpeed"][i])+" km/hr ,Night- "+ str(data["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(data["vt1dailyForecast"]["night"]["windSpeed"][i])+" km/hr")
            print("   Humidity : Day- "+str(data["vt1dailyForecast"]["day"]["humidityPct"][i])+" % ,Night- "+str(data["vt1dailyForecast"]["night"]["humidityPct"][i])+" %")
            print("   UV Index : Day- "+str(data["vt1dailyForecast"]["day"]["uvIndex"][i])+" out of 10 ,Night- "+str(data["vt1dailyForecast"]["night"]["uvIndex"][i])+" out of 10")
            print("   Sunrise : "+str(data["vt1dailyForecast"]["sunrise"][i]))
            print("   SunSet : "+str(data["vt1dailyForecast"]["sunset"][i]))
            print("   Moon Phase : "+str(data["vt1dailyForecast"]["moonPhrase"][i]))
            print("   Moonrise : "+str(data["vt1dailyForecast"]["moonrise"][i]))
            print("   MoonSet : "+str(data["vt1dailyForecast"]["moonset"][i]))
            print(" ")
    
def day10_data(data):
        print("Co-ordinate - latitude :" + str(place_data["location"]["latitude"][0])+ " longitude :" + str(place_data["location"]["longitude"][0]))
        print("Weather of "+str(place_data["location"]["address"][0])+" for the next 10 days are :-")
        for i in range(0,10):
            print(str(i+1)+"- "+data["vt1dailyForecast"]["dayOfWeek"][i])
            print("   Description : Day- "+str(data["vt1dailyForecast"]["day"]["phrase"][i])+" ,Night- "+str(data["vt1dailyForecast"]["night"]["phrase"][i]))
            print("   Temperature : Max- "+str(data["vt1dailyForecast"]["day"]["temperature"][i])+" deg C, Min- "+str(data["vt1dailyForecast"]["night"]["temperature"][i])+ " deg C")
            print("   Precipitation : Day- "+str(data["vt1dailyForecast"]["day"]["precipPct"][i])+"% " +str(data["vt1dailyForecast"]["day"]["precipType"][i]) + " Night- "+str(data["vt1dailyForecast"]["night"]["precipPct"][i])+"% "+str(data["vt1dailyForecast"]["day"]["precipType"][i]))
            print("   Wind : Day- "+ str(data["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(data["vt1dailyForecast"]["day"]["windSpeed"][i])+" km/hr ,Night- "+ str(data["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(data["vt1dailyForecast"]["night"]["windSpeed"][i])+" km/hr")
            print("   Humidity : Day- "+str(data["vt1dailyForecast"]["day"]["humidityPct"][i])+" % ,Night- "+str(data["vt1dailyForecast"]["night"]["humidityPct"][i])+" %")
            print("   UV Index : Day- "+str(data["vt1dailyForecast"]["day"]["uvIndex"][i])+" out of 10 ,Night- "+str(data["vt1dailyForecast"]["night"]["uvIndex"][i])+" out of 10")
            print("   Sunrise : "+str(data["vt1dailyForecast"]["sunrise"][i]))
            print("   SunSet : "+str(data["vt1dailyForecast"]["sunset"][i]))
            print("   Moon Phase : "+str(data["vt1dailyForecast"]["moonPhrase"][i]))
            print("   Moonrise : "+str(data["vt1dailyForecast"]["moonrise"][i]))
            print("   MoonSet : "+str(data["vt1dailyForecast"]["moonset"][i]))
            print(" ")


def weekend_data(data):
        print("Co-ordinate - latitude :" + str(place_data["location"]["latitude"][0])+ " longitude :" + str(place_data["location"]["longitude"][0]))
        print("Weather of "+str(place_data["location"]["address"][0])+" for the next 2 weekends are :-")
        j=0
        for i in range(0,15):
            if data["vt1dailyForecast"]["dayOfWeek"][i]=="Saturday":
                j+=1
                print(str(j)+"- "+ data["vt1dailyForecast"]["dayOfWeek"][i])
                print("   Description : Day- "+str(data["vt1dailyForecast"]["day"]["phrase"][i])+" ,Night- "+str(data["vt1dailyForecast"]["night"]["phrase"][i]))
                print("   Temperature : Max- "+str(data["vt1dailyForecast"]["day"]["temperature"][i])+" deg C, Min- "+str(data["vt1dailyForecast"]["night"]["temperature"][i])+ " deg C")
                print("   Precipitation : Day- "+str(data["vt1dailyForecast"]["day"]["precipPct"][i])+"% " +str(data["vt1dailyForecast"]["day"]["precipType"][i]) + " Night- "+str(data["vt1dailyForecast"]["night"]["precipPct"][i])+"% "+str(data["vt1dailyForecast"]["day"]["precipType"][i]))
                print("   Wind : Day- "+ str(data["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(data["vt1dailyForecast"]["day"]["windSpeed"][i])+" km/hr ,Night- "+ str(data["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(data["vt1dailyForecast"]["night"]["windSpeed"][i])+" km/hr")
                print("   Humidity : Day- "+str(data["vt1dailyForecast"]["day"]["humidityPct"][i])+" % ,Night- "+str(data["vt1dailyForecast"]["night"]["humidityPct"][i])+" %")
                print("   UV Index : Day- "+str(data["vt1dailyForecast"]["day"]["uvIndex"][i])+" out of 10 ,Night- "+str(data["vt1dailyForecast"]["night"]["uvIndex"][i])+" out of 10")
                print("   Sunrise : "+str(data["vt1dailyForecast"]["sunrise"][i]))
                print("   SunSet : "+str(data["vt1dailyForecast"]["sunset"][i]))
                print("   Moon Phase : "+str(data["vt1dailyForecast"]["moonPhrase"][i]))
                print("   Moonrise : "+str(data["vt1dailyForecast"]["moonrise"][i]))
                print("   MoonSet : "+str(data["vt1dailyForecast"]["moonset"][i]))
                print(" ")
            elif data["vt1dailyForecast"]["dayOfWeek"][i]=="Sunday":
                j+=1
                print(str(j)+"- "+ data["vt1dailyForecast"]["dayOfWeek"][i])
                print("   Description : Day- "+str(data["vt1dailyForecast"]["day"]["phrase"][i])+" ,Night- "+str(data["vt1dailyForecast"]["night"]["phrase"][i]))
                print("   Temperature : Max- "+str(data["vt1dailyForecast"]["day"]["temperature"][i])+" deg C, Min- "+str(data["vt1dailyForecast"]["night"]["temperature"][i])+ " deg C")
                print("   Precipitation : Day- "+str(data["vt1dailyForecast"]["day"]["precipPct"][i])+"% " +str(data["vt1dailyForecast"]["day"]["precipType"][i]) + " Night- "+str(data["vt1dailyForecast"]["night"]["precipPct"][i])+"% "+str(data["vt1dailyForecast"]["day"]["precipType"][i]))
                print("   Wind : Day- "+ str(data["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(data["vt1dailyForecast"]["day"]["windSpeed"][i])+" km/hr ,Night- "+ str(data["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(data["vt1dailyForecast"]["night"]["windSpeed"][i])+" km/hr")
                print("   Humidity : Day- "+str(data["vt1dailyForecast"]["day"]["humidityPct"][i])+" % ,Night- "+str(data["vt1dailyForecast"]["night"]["humidityPct"][i])+" %")
                print("   UV Index : Day- "+str(data["vt1dailyForecast"]["day"]["uvIndex"][i])+" out of 10 ,Night- "+str(data["vt1dailyForecast"]["night"]["uvIndex"][i])+" out of 10")
                print("   Sunrise : "+str(data["vt1dailyForecast"]["sunrise"][i]))
                print("   SunSet : "+str(data["vt1dailyForecast"]["sunset"][i]))
                print("   Moon Phase : "+str(data["vt1dailyForecast"]["moonPhrase"][i]))
                print("   Moonrise : "+str(data["vt1dailyForecast"]["moonrise"][i]))
                print("   MoonSet : "+str(data["vt1dailyForecast"]["moonset"][i]))
                print(" ")



#current data of the place
if type_of_forecast=="Today" or type_of_forecast=="today":
    resp= requests.get("https://api.weather.com/v2/turbo/vt1observation?apiKey="+api_key+"&format=json&geocode=" +str(place_data["location"]["latitude"][0]) + "," + str(place_data["location"]["longitude"][0]) + "&language=en-IN&units=m")
    data1=resp.json()
    today_data(data1)
    
else :
    response=requests.get("https://api.weather.com/v2/turbo/vt1dailyForecast?apiKey="+api_key+"&format=json&geocode=" +str(place_data["location"]["latitude"][0]) + "," + str(place_data["location"]["longitude"][0]) + "&language=en-IN&units=m")
    data=response.json()

    #get the 5 day weather details of the given place
    if type_of_forecast=="5-day" or type_of_forecast=="5 day":
        day5_data(data)

    #get the 10 day weather details of the given place
    elif type_of_forecast=="10-day" or type_of_forecast=="10 day":
        day10_data(data)
    
    #get the weekend weather details of the given place
    elif type_of_forecast=="weekend" or type_of_forecast=="Weekend":
        weekend_data(data)


