from  fastapi import FastAPI
from models import hotel_mgnt_models as structure
import sqlalchemy
import psycopg2
import requests 
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/room")
def main_get():
    return 'get room info'


@app.post("/room")
def main_post():
    return 'create room'


@app.put("/room")
def main_post():
    return 'put room'


@app.delete("/room")
def main_post():
    return 'delete room'














