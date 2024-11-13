import requests 
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    if r.status_code == 200:
        try:
            data = r.json()  # Only attempt to decode JSON if the response is OK
            print(data)
        except requests.exceptions.JSONDecodeError:
            print("Error: Response is not valid JSON")
    else:
        print(f"Error: Server responded with status code {r.status_code}")
get_data(1)
get_data()
