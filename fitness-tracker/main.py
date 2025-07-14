import requests
from datetime import datetime

APP_ID = "1d044b18"
API_KEY = "503238ae49569f1e91306921283cf9b9"
nutrix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_post_endpoint = "https://api.sheety.co/ea31ee1ae79ebcbb30879676130a9d51/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

exercise_text = input("Tell me which exercise you did: ")

nutrix_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 185,
    "age": 32,
}

sheety_auth = {
    "Authorization": "Bearer ahglagpaegiphagiha"
}

response = requests.post(url=nutrix_endpoint, headers=headers, json=nutrix_params)
response.raise_for_status()
result = response.json()

now = str(datetime.now())
date = now.split()[0]
time = now.split()[1][:8]

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(sheety_post_endpoint, json=sheet_inputs, headers=sheety_auth)
print(sheet_response.text)
