# Weather App

A simple Python CLI tool to check current weather conditions for any city using WeatherAPI.

## Requirements
- Python 3.x
- Dependencies listed in `requirements.txt`
- Free API key from weatherapi.com

## Setup
1. Install required packages:
   pip install -r requirements.txt

2. Create a .env file in the project directory:
   KEY=your_weatherapi_key

## How to Run
Run the script from your terminal:
python main.py

When prompted, type a city name (e.g., London, Tel Aviv, New York).

## Caching
The application saves the last fetched weather result in wether.json. If you query the same city within 5 hours, it loads the data from the local cache instead of making a new API request.

## Common Issues & Troubleshooting
- Location not found / invalid city: Ensure the city name is spelled correctly in English.
- Missing API key: Make sure your .env file exists in the same directory as main.py and contains the variable KEY.
- Invalid API key / 401 / 403 errors: Verify that your API key is active on weatherapi.com.
- Corrupted cache file (JSONDecodeError): If wether.json becomes empty or malformed, delete wether.json or reset its content to {} and run the script again.
- Connection errors: Check your internet connection if the program cannot reach api.weatherapi.com.