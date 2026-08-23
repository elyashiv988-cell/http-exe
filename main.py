import requests
import os
import json
from dotenv import load_dotenv
from datetime import datetime

def get_key():
    load_dotenv(".env")
    key = os.getenv("KEY")
    return key

def get_wether_uml():
    return "http://api.weatherapi.com/v1"

def load_cache():
    try:
        with open("wether.json","r") as file:
            data_wether=json.load(file)
            return data_wether
        
    except:
        return {}
    
    
def save_cache(cache_data):

    with open("wether.json","w") as file:
        last_updated=datetime.now().hour
        cache_data["last_updated"]=last_updated
        json.dump(cache_data,file,indent=4)
   
def get_corrent_wether(base_uml,key, city):
    
    response = requests.get(f"{base_uml}/current.json?key={key}&q={city}")
    data_wether=response.json()
    return data_wether

def display_wether(data_wether):

    try:
        state = data_wether['location']['country']
        city = data_wether['location']["name"]
        status = data_wether['current']['temp_c']
        humidity = data_wether['current']["humidity"]
        print (f"State: {state} | City: {city} | Corrent temp: {status} | Humidity: {humidity}")
    except:
        print("Location not found! try again. ")

def get_weather(city):
    try:
        stored_data = load_cache()
        corrent_time = datetime.now().hour
        last_update_time = stored_data["last_updated"]
        last_update_city = stored_data ['location']["name"]
        if corrent_time - last_update_time < 5 and city.upper() == last_update_city.upper():
            data_wether = stored_data
            
        else:
            
            data_wether = get_corrent_wether(get_wether_uml(), get_key(), city)
            save_cache(data_wether)
            

    except KeyError:
        data_wether = get_corrent_wether(get_wether_uml(), get_key(), city)
        save_cache(data_wether)

    return data_wether

def main():

    city= input ("Enter city name: ")
    data_wether=get_weather(city)
    display_wether(data_wether)

main()




    


