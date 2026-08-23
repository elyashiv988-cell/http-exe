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

def get_stored_wether():
    with open("wether.json","r") as file:
        data_wether=json.load(file)
        return data_wether

def write_wether(data_wether):

    with open("wether.json","w") as file:
        last_updated=datetime.now().hour
        data_wether["last_updated"]=last_updated
        json.dump(data_wether,file,indent=4)

def get_wether(base_uml,key, city):
    
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
    except KeyError:
        raise "Location not found! try again. "

def main():

    corrent_time = datetime.now().hour
    last_update_time = get_stored_wether()["last_updated"]
    last_update_city = get_stored_wether()['location']["name"]
    city= input ("Enter city name: ")

    if corrent_time - last_update_time < 5 and city.upper() == last_update_city.upper():
        data_wether = get_stored_wether()

    else:
        
        data_wether = get_wether(get_wether_uml(), get_key(), city)
        write_wether(data_wether)


    display_wether(data_wether)

main()




    


