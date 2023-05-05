import store
<<<<<<< HEAD
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app=FastAPI() #instanciamos la aplicacion
@app.get("/") #decorador o la ruta por la que pueden accedera a la web

def get_list():
    return [1,2,3]
@app.get("/contact",response_class=HTMLResponse)

def get_list():
    return """
           <h1> Hola soy una pagina</h1>
           <p>soy un parrafo</p>
           """



"""""""""
def get_list():
    return{"name":"Platzi"}
    """""""""
=======

>>>>>>> 3ad7cb4f88a90ecfff57d8740e7cf2658b5516a7
def run():
    store.categories()

if __name__ == "__main__":
    run()
    