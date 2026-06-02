import requests
import random

for i in range(100):
    payload = {
        "order_name": f"Order_{1000+i}",
        "source": random.randint(1, 10),
        "destination": random.randint(1, 10)
    }

    response = requests.post(
        "http://127.0.0.1:5000/add-delivery",
        json=payload
    )

    print(response.json())