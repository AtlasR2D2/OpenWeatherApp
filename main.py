import requests
import send_sms

API_KEY = "002ff92ad9cc3a5704511f7c92519aea"
CITY_NAME = "Edinburgh"
URL_ENDPOINT = f"https://api.openweathermap.org/data/2.5/onecall"


parameters = {
    "lat": 48.3069,
    "lon": 14.2858,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(url=URL_ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()

next_12_hours = weather_data["hourly"][0:12]

blnBringBrolly = False
for i_x in range(len(next_12_hours)):
     id_x = int(next_12_hours[i_x]["weather"][0]["id"])
     print(id_x)
     if id_x < 700:
         blnBringBrolly = True
         break

if blnBringBrolly:
    print("You may need a Brolly today!")
    send_sms.send_sms("You may need a Brolly!")
else:
    print("Doesn't look like you'll need a Brolly today.")
