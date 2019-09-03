from tkinter import *  
from functools import partial  
import requests                             #getting data from weather.com using the weather api
from geopy.geocoders import Nominatim       #getting the coordinates and other data of the place
from datetime import date                   #getting the current date
from geopy.exc import GeocoderTimedOut      #getting the coordinates and other data of the place

top = Tk()  
top.title("Weather Application")
top.geometry("500x500")  

 
def call_result(p, d,t):
    top2 = Toplevel() 
    top2.title('Results') 
    
    scrollbar = Scrollbar(top2) 
    scrollbar.pack( side = RIGHT, fill = Y ) 
    mylist = Listbox(top2, yscrollcommand = scrollbar.set ) 
    
    place="Rourkela Odisha"                     #default place
    today = date.today()                        #default date
    type_of_forecast="today"                    #default type of forecast

    if p!="":
        place=p.get()
    if d!="":
        today=d.get()
    if t=="Today" or t=="today":
        type_of_forecast=t.get()
    elif t=="Hourly" or t=="hourly":
        type_of_forecast=t.get()
    elif t=="5-day" or t=="5 day":
        type_of_forecast=t.get()
    elif t=="10-day" or t=="10 day":
        type_of_forecast=t.get()
    elif t=="Weekend" or t=="weekend":
        type_of_forecast=t.get()
    elif t=="Monthly" or t=="monthly":
        type_of_forecast=t.get()

    geolocator = Nominatim(user_agent="LARA_Sahoo")       #Nominatim (from the Latin, 'by name') is a tool to search OSM data by name and address (geocoding) and to generate synthetic addresses of OSM points (reverse geocoding). It can be found at nominatim.openstreetmap.org

    #get the coordinates of the place
    location = geolocator.geocode(place,timeout=None)
    mylist.insert(END, str(location) )              #shows the complete details of the place entered
    mylist.insert(END, " ("+str(location.latitude)+","+str(location.longitue)+")" )          #shows the lat and lon of the place
    if type_of_forecast=="Today" or type_of_forecast=="today":
        resp= requests.get("https://api.weather.com/v2/turbo/vt1observation?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&geocode=" +str(location.latitude) + "," + str(location.longitude) + "&language=en-IN&units=m")
        data1=resp.json()
        # print(data1)
        print("The current weather of " + str(location.address) + " is :-")
        print("  Co-ordinate - latitude :" + str(location.latitude)+ " longitude :" + str(location.longitude))
        print("  Temperature :" + str(data1["vt1observation"]["temperature"])+" deg C " +str(data1["vt1observation"]["phrase"])+ " as of "+str(data1["vt1observation"]["observationTime"]))
        print("  Feels like "+str(data1["vt1observation"]["feelsLike"]) + " deg C" )
        print("  Dew point :"+str(data1["vt1observation"]["dewPoint"])+ " deg")
        print("  Humidity :" +str(data1["vt1observation"]["humidity"])+" %")
        print("  UV Index " +str(data1["vt1observation"]["uvIndex"]) +" out of 10 which is "+str(data1["vt1observation"]["uvDescription"]))
        print("  Wind :"+ str(data1["vt1observation"]["windDirCompass"])+" " + str(data1["vt1observation"]["windSpeed"])+ " km/hr")
        print("  Visibility :"+str(data1["vt1observation"]["visibility"])+ " km")
        print("  Pressure: "+str(data1["vt1observation"]["altimeter"])+"mb "+ str(data1["vt1observation"]["barometerTrend"]))

    else :
        response=requests.get("https://api.weather.com/v2/turbo/vt1dailyForecast?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&geocode=" +str(location.latitude) + "," + str(location.longitude) + "&language=en-IN&units=m")
        data=response.json()

        #get the 5 day weather details of the given place
        if type_of_forecast=="5-day" or type_of_forecast=="5 day":
            print("Co-ordinate - latitude :" + str(location.latitude)+ " longitude :" + str(location.longitude))
            print("Weather of "+str(location.address)+" for the next 5 days are :-")
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

        #get the 10 day weather details of the given place
        elif type_of_forecast=="10-day" or type_of_forecast=="10 day":
            print("Co-ordinate - latitude :" + str(location.latitude)+ " longitude :" + str(location.longitude))
            print("Weather of "+str(location.address)+" for the next 10 days are :-")
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
        
        #get the weekend weather details of the given place
        elif type_of_forecast=="weekend" or type_of_forecast=="Weekend":
            print("Co-ordinate - latitude :" + str(location.latitude)+ " longitude :" + str(location.longitude))
            print("Weather of "+str(location.address)+" for the next 2 weekends are :-")
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



    mylist.pack( side = LEFT, fill = BOTH ) 
    scrollbar.config( command = mylist.yview ) 

    top2.mainloop()


place =StringVar()  
date1 = StringVar()  
type_of_forecast = StringVar()  

p = Label(top, text = "Enter place in details ie place and state :").place(x = 30,y = 50)  

d = Label(top, text = "Enter date in yyyy-mm-dd :").place(x = 30, y = 90)

type_of = Label(top, text = "Enter type of forecast you want :\n 1.Today \n 2.5-day \n 3.10-day \n 4.Weekend").place(x = 30, y = 130)  


e1 = Entry(top,textvariable=place).place(x = 300, y = 50)    
e2 = Entry(top,textvariable=date1).place(x = 300, y = 90)  
e3 = Entry(top,textvariable=type_of_forecast).place(x = 300, y = 130)  

call_result = partial(call_result,place, date1,type_of_forecast)  

sbmitbtn = Button(top, text = "Submit",activebackground = "pink", activeforeground = "blue",command=call_result).place(x = 200, y = 250)  

top.mainloop()