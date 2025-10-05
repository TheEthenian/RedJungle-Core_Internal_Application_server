from  fastapi import FastAPI
from models.review_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/review/{param_a}")
def main_get(param_a, data: Incoming_Data):
    if param_a ==  'user':
        return 'get user review'

    if param_a ==  'public':
        return 'get public review'


@app.post("/review/user")
def main_post(data: Incoming_Data):
    return 'post user review'


@app.put("/review/user")
def main_put(data: Incoming_Data):
    return 'put user review'


@app.delete("/review/{param_a}")
def main_delete(param_a, data: Incoming_Data):
    if param_a ==  'user':
        return 'delete user review'

    if param_a ==  'public':
        return 'delete public review'







