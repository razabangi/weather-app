import requests
import json

try:
    while (1):
        city = input("Enter your city name \n")
        url = f"https://api.weatherapi.com/v1/current.json?key=7cce2306c28e4452988160524230408&q={city}"

        result = requests.get(url)
        result = json.loads(result.text)
        print(f"The temperature is in your typed city is {result['current']['temp_c']}")
        if (city == "q"):
            break
except Exception as e:
    print(f"some error occured {e}")
