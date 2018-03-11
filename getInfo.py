import requests

response = requests.get("http://localhost:6001/api/player")

print(response.status_code)
print(response.json())
