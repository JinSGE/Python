import requests

# Delete Method 요청
url = "https://jsonplaceholder.typicode.com/users/1"
data = {"name": "Alice"}

resp = requests.delete(url)
print(resp.headers)
print(resp.text)

