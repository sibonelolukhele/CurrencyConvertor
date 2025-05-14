import requests 


def conlibrary():

    url = "https://v6.exchangerate-api.com/v6/f78e7e33e4ac22a7c91ae402/pair/USD/ZAR"
    req = requests
    res = req.get(url)
    data = res.json()
    return data["conversion_rate"]