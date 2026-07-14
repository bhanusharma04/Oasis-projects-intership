import requests

def get_weather_no_api(city_name):
    # wttr.in format '?format=j1' returns a clean JSON structure
    url = f"https://wttr.in/{city_name}?format=j1"
    
    try:
        print("🔄 Fetching live data...")
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Extracting specific details from the wttr.in JSON structure
            current_condition = data['current_condition'][0]
            nearest_area = data['nearest_area'][0]
            
            temp_c = current_condition['temp_C']
            feels_like = current_condition['FeelsLikeC']
            humidity = current_condition['humidity']
            wind_speed = current_condition['windspeedKmph']
            weather_desc = current_condition['weatherDesc'][0]['value']
            
            region = nearest_area['region'][0]['value']
            country = nearest_area['country'][0]['value']
            
            # Printing the clean dashboard report
            print(f"\n🌍 Weather Report for {city_name.title()} ({region}, {country}) 🌍")
            print("-" * 50)
            print(f"Condition     : {weather_desc}")
            print(f"Temperature   : {temp_c}°C")
            print(f"Feels Like    : {feels_like}°C")
            print(f"Humidity      : {humidity}%")
            print(f"Wind Speed    : {wind_speed} Km/h")
            print("-" * 50)
            
        else:
            print(f"\n❌ Could not find weather data for '{city_name}'.")
            
    except requests.exceptions.ConnectionError:
        print("\n❌ Network Error: Please check your internet connection.")
    except (KeyError, IndexError):
        print("\n❌ Parsing Error: The location structure could not be processed.")

if __name__ == "__main__":
    print("🌤️ Welcome to the Permanent Python Weather App 🌤️")
    print("(No API Key Required)")
    
    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()
        
        if city.lower() == 'exit':
            print("Goodbye!")
            break
            
        if city == "":
            print("Please type a location name.")
            continue
            
        get_weather_no_api(city)
