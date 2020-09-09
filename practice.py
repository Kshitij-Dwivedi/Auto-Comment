import requests

url = "https://www.youtube.com/oembed?format=json&url=http://www.youtube.com/watch?v=2L6gsn7rGqI"

req = requests.get(url)
print(req.status_code)