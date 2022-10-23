from multiprocessing import reduction
from unittest import result
from urllib import request
from fastapi import APIRouter
import requests
from .database import ingredient_queries
import json


# def prepare_data(ingredient, data):
#     res = [{
#         "title": result["title"],
#         "thumbnail": result["thumbnail"],
#         "href": result["href"],
#         "ingredients": result["ingredients"],
#         # "dairy":filter_recipe_by_alergan(result, dairy_alergan),
#         # "gluten":filter_recipe_by_alergan(result, gluten_alergan)
#     }
#         for result in data["results"]

#     ]
#     return res


# def filter_recipe_by_dairy(recipe):
#     alergan = ingredient_queries.get_dairy_ing()
#     for ing in recipe["ingredients"]:
#         if ing in alergan:
#             return False
#     return True


# def filter_recipe_by_gluten(recipe):
#     alergan = ingredient_queries.get_gluten_ing()
#     for ing in recipe["ingredients"]:
#         if ing in alergan:
#             return False
#     return True

#     # for result['ingredients'] for item in data if item == ingredient]


# @router.get("/{ingredient}")
# async def get_recipes_by_ingredient(ingredient, filter_dairy="false", filter_gluten="false"):
#     print("here")
#     filter_dairy = json.loads(filter_dairy.lower())
#     filter_gluten = json.loads(filter_gluten.lower())
#     res = requests.get(
#         f"https://recipes-goodness.herokuapp.com/recipes/{ingredient}")

#     if filter_gluten:
#         res = filter(filter_recipe_by_dairy, res)
#     if filter_dairy:
#         res = filter(filter_recipe_by_gluten, res)
#     return res
