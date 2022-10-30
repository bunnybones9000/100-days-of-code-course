import requests
from datetime import datetime
NUTRI_APP_ID = "967f182d"
NUTRI_APP_KEY = "3483d767d1f029ff647fcf276339f14f"

GENDER = "male"
WEIGHT = 68
HEIGHT = 186
AGE = 18

HEADERS = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_APP_KEY,
    "x-remote-user-id": "josef_sho"
}


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("what exercise did you do today: ")


parameter = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": AGE
}

response = requests.post(url=exercise_endpoint, headers=HEADERS, json=parameter)
response = response.json()


add_row_endpoint = "https://api.sheety.co/9595023b8abf54e7f2e3aeb0091976ec/copyOfMyWorkouts/workouts"


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in response["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(add_row_endpoint, json=sheet_inputs)

    print(sheet_response.text)
