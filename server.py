import asyncio
import json
import logging
from ssl import AlertDescription
from urllib import request
from fastapi import FastAPI
import uvicorn
from fastapi import Request
# from player_stats import Player_stats
import requests
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from backend.database import ingredient_queries

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# app.include_router(routes.router)


@app.get('/sanity')
def root():
    return {"message": "OK"}


def prepare_data(data):
    res = [
        {
            "title": result["title"],
            "thumbnail": result["thumbnail"],
            "href": result["href"],
            "ingredients": result["ingredients"]
        }
        for result in data["results"]
    ]
    return res


def filter_recipe_by_dairy(recipe):
    print("here")

    alergan = ingredient_queries.get_dairy_ing()
    for ing in recipe["ingredients"]:
        if ing in alergan:
            return False
    return True


def filter_recipe_by_gluten(recipe):
    alergan = ingredient_queries.get_gluten_ing()
    for ing in recipe["ingredients"]:
        if ing in alergan:
            return False
    return True


@app.get('/recipes/{ingredient}', status_code=200)
async def get_recipes_by_ingredient(ingredient, filter_dairy="false", filter_gluten="false"):
    try:
        filter_dairy = json.loads(filter_dairy.lower())
        filter_gluten = json.loads(filter_gluten.lower())

        res = requests.get(
            f"https://recipes-goodness.herokuapp.com/recipes/{ingredient}")

        res = prepare_data(res.json())

        if filter_gluten:
            gluten = filter(filter_recipe_by_gluten, res)
            res = list(gluten)
        if filter_dairy:
            dairy = filter(filter_recipe_by_dairy, res)
            res = list(dairy)
        return res
    except Exception as e:
        print(e)
        return e


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
