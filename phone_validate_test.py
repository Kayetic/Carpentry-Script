import requests

request_url = "http://apilayer.net/api/validate?access_key=1dOpGNMPbZmia6cCWrknvWy0IXdeuTfM"
response = requests.get(request_url)
print(response.json())
