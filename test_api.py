import requests
import random

url = "http://127.0.0.1:5000/add-delivery"

data = {
    "order_name": f"Order_{random.randint(1,100)}",
    "source": random.randint(1,10),
    "destination": random.randint(1,10)
}

response = requests.post(url, json=data)

print(response.json())