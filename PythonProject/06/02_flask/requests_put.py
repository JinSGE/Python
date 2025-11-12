import requests

# PUT Method 요청
url = "https://jsonplaceholder.typicode.com/users/1"
data = {"name": "Alice"}

resp = requests.get(url, json=data)
print(resp.headers)
print(resp.text)

