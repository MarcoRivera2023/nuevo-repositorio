import requests
#vamos a hacer un request a un servicio web para utilizar el ambiente virtual de python
def categories():
    r=requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code) #obtenemos el estado del ip 
    print(r.text) #que informacion recibimos
    categories= r.json() #por este metodo podemos iterar una lista de diccioanrios
    for category in categories:
        print(category["name"])