import requests
import json

url = "http://localhost:8000/api/chat"
data = {
    "query": "What is the prepayment penalty for a personal loan?",
    "session_id": "test_session_123"
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print("Response JSON:")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {e}")
