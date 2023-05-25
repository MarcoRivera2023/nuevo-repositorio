from fastapi import FastAPI,Body
from fastapi.responses import HTMLResponse
import requests
app = FastAPI()
app.title="Mi aplicacion FastAPI"
app.version="0.0.1"

@app.get("/",tags=["home"])
def message():
    return HTMLResponse("<h1>Hello World</h1>")

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Accion'    
    } ,
     {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Accion'    
    } 
]



@app.get("/movies/{id}",tags=["Movies"])
def get_movies(id:int):
     for item in movies:
         if item["id"]==id:
            return item
     return "Eror: Pelicula no encontrada"
 
@app.get("/movies/", tags=["Movies"])
def get_movies_by_categories(category:str, year:int):
    return list(filter(lambda item: item["category"]==category,movies))

@app.post("/movies/testing",tags=["movies"])
def create_movies(id:int=Body(),title:str=Body(),overview:str=Body(),year:int=Body(),rating:float=Body(),category:str=Body()):
    movies.append({
                    "id":id,
                    "title":title,
                    "overview":overview,
                    "year":year,
                    "rating":rating,
                    "category":category
                })
    return movies

@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id:int, title:str=Body(),overview:str=Body(),year:int=Body(),rating:float=Body(),category:str=Body()):
    for item in movies:
        if item["id"]== id:
            item["title"]=title
            item["overview"]=overview
            item["year"]=year
            item["rating"]=rating
            item["category"]=category
            return movies
            
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    movie = [movie for movie in movies if id == movie['id']]
    movies.remove(movie[0])
    return movies           
            
