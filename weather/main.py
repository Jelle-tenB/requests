import requests
from twilio.rest import Client

api_key = "b7d2eb5ec3940ff25c1e8cee025d0498"
# forecast for 5 days, every 3 hours
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": 52.304999,
    "lon": 4.668723,
    "appid": api_key,
    "units": "metric",
    "cnt": 4,
}

account_sid = "AC2bc5726229b561ebbb2316c9ad087f2d"
auth_token = "a098023576b6e3ffcd9a3c0e18b9263e"

# current weather:
# https://api.openweathermap.org/data/2.5/weather?lat=52.304999&lon=4.668723&appid=b7d2eb5ec3940ff25c1e8cee025d0498
# https://api.openweathermap.org/data/2.5/weather?q=haarlem,NL&appid=b7d2eb5ec3940ff25c1e8cee025d0498

# forecast for 5 days, every 3 hours
response = print(requests.get(endpoint, params=weather_params))
response.raise_for_status()
weather_data = response.json()

# forecast_codes = []
# repeat = 0
will_rain = False

# while repeat < 4:
#     forecast_codes.append(weather_data['list'][repeat]['weather'][0]['id'])
#     repeat += 1
# print(forecast_codes)

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# for i in forecast_codes:
#     if i < 700:
#         rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Remember to bring an umbrella",
        from_="+12055193852",
        to="+31652593317",
    )
    print(message.status)
