from  fastapi import FastAPI
from models import auth_models as structure
import sqlalchemy
import psycopg2
import requests 
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/auth")
def main_get():
    return 'get auth'


@app.post("/auth")
def main_post(something):
    return 'post auth'


@app.put("/auth")
def main_put(new_instance):
    return 'put auth'


@app.delete("/auth")
def main_delete(uuid):
    return 'delete auth'








