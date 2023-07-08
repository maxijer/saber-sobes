import requests
import json

data_1 = {"build": "forward_interest"}
data_json = json.dumps(data_1)
print(requests.post("http://127.0.0.1:8000/get_tasks", data=data_json).json())
