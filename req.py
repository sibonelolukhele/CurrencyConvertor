import requests

#base url 
# https://ifconfig.co

# endpoint
# /city


url = "https://ifconfig.co/city"
req = requests
response = req.get(url)

print(response.status_code)
print(response.text)
print(type(response))
print(response)

