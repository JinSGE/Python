import requests

# POST Method 요청
url = "https://jsonplaceholder.typicode.com/users"
data = {"name": "Alice", "email": "alice@example.com"}

resp = requests.get(url, json=data)
print(resp.headers)
print(resp.text)

