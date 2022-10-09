import requests
from datetime import datetime
import os

NUTRITION_API_KEY = 'e33c8d682835ba3b6639519cca2b7513'
NUTRITION_APP_ID = '8d692209'
SHEET_BEARER = "Bearer fsfkjlwkejklfjslkwqmfds"


user_workout = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
}
nutrition_param = {
    "query": user_workout,
    "gender": "male",
    "weight_kg": 75,
    "age": 27,
}

nutrition_response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise',json=nutrition_param,headers=headers)
today = datetime.now()
exercise = nutrition_response.json()['exercises']

sheet_headers = {
    "Authorization": SHEET_BEARER
}
for ex in exercise:
    sheet_parameter = {
        "workout":{
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": ex['name'].title(),
            "duration": ex['duration_min'],
            "calories": ex['nf_calories'],
        }
    }
    sheet_response = requests.post(url='https://api.sheety.co/522dcb0493698871159d9ab4cd20f4f1/euiHyunWorkouts/workouts', json=sheet_parameter,headers=sheet_headers)
    print(sheet_response.text)