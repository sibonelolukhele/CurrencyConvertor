import requests

print("Pokemon color check:")
#base url = https://pokeapi.co/api 
#version = v2
#endpoint = pokemon/charmander


pname = input("\nEnter a pokemon name: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pname}"
req = requests
response = req.get(url)

rc = response.status_code

if rc == 404:
    print("Pokemon does not exist")
else:    
    #parse
    data = response.json()

    name = data["name"]
    somedata = data["sprites"]
    species = data["species"]

    sp = req.get(species["url"])

    color = sp.json()["shape"]["name"]

    # print(response.status_code)
    print(f"The name of the pokemon is {name} and the color is {color}")
        
# print(somedata["front_default"])
# print(sp.json()["name"]["color"])


# print(response.status_code)
# print(response.text)
# print(type(response))
# print(response)
