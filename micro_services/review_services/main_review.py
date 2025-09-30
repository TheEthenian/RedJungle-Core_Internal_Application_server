from  fastapi import FastAPI
from models import review_models as structure
import sqlalchemy
import psycopg2
import requests 
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/review/{param_a}")
def main_get(param_a):
    if param_a ==  'user':
        return 'get user review'

    if param_a ==  'public':
        return 'get public review'


@app.post("/review/user")
def main_post():
    return 'post user review'


@app.put("/review/user")
def main_put():
    return 'put user review'


@app.delete("/review/{param_a}")
def main_delete(param_a):
    if param_a ==  'user':
        return 'delete user review'

    if param_a ==  'public':
        return 'delete public review'







